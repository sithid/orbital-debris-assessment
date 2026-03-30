import papermill as pm
import sys
import argparse
import os

# https://docs.python.org/3/library/filesys.html

# Set the root directory path (project root, one level up from this file)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define notebook sequence, the order actually matters. Each notebook continues where the previous
# left off, so we can't just run them in parallel or out of order because of file dependencies.
# This sequence will be looped through in the run_pipeline function.
notebook_pipeline_complete = [
    os.path.join(ROOT_DIR, "notebooks/00_pipeline_refresh.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/01_ucs_cleanup.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/02_satcat_cleanup.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/03_kinetic_master_synthesis.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/04_orbital_debris_synthesis.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/05_orbital_debris_exploration.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/06_orbital_debris_story_queries.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/07_orbital_debris_story_visualizations.ipynb")
]
# notebook_pipeline_data_only should contain 01 - 04
notebook_pipeline_data_only = notebook_pipeline_complete[1:5]  # Only the first 4 notebooks which are for data processing and synthesis
notebook_pipeline_vis_only = notebook_pipeline_complete[-3:]  # Only the last 3 notebooks which are for exploration and visualization

def purge_outputs():
    print("\n⚠️  Purging all exported/cleaned outputs...")
    
    # Purge datasets in the clean folder but skip the results folder.
    # This is where we save any exported datasets or cleaned versions of the original data that 
    # we want to keep separate from the raw downloads in the clean folder.
    # We want to purge these on demand because they can be large and we don't want to 
    # accidentally delete them every time we run the pipeline, but we also want to give the
    # option to start fresh if needed.
    
    clean_dir = os.path.join(ROOT_DIR, 'data/clean')
    
    if os.path.exists(clean_dir):
        for fname in os.listdir(clean_dir):
            fpath = os.path.join(clean_dir, fname)
            if fname == 'results' and os.path.isdir(fpath):
                continue
            if os.path.isfile(fpath):
                os.remove(fpath)
    
    # Explicitly remove the database file if it exists still.
    # The previous loop should have removed it, but if it was open or thread-locked for some
    # reason it might still be there, so we do this as a final cleanup step to ensure a fresh start.            
    db_path = os.path.join(clean_dir, 'orbital_debris.db')
    
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Purge images in charts directory but leave the folder structure intact.
    charts_dir = os.path.join(ROOT_DIR, 'charts')
    
    if os.path.exists(charts_dir):
        for root, dirs, files in os.walk(charts_dir):
            for file in files:
                if file.endswith(('.png', '.svg')):
                    os.remove(os.path.join(root, file))
    
    # Purge items inside results but leave the folder structure intact.
    results_dir = os.path.join(clean_dir, 'results')
    
    if os.path.exists(results_dir):
        for fname in os.listdir(results_dir):
            fpath = os.path.join(results_dir, fname)
            try:
                if os.path.isfile(fpath) or os.path.islink(fpath):
                    os.remove(fpath)
            except Exception as e:
                print(f"Warning: Could not delete {fpath}: {e}")
    
    # Purge executed notebooks in the output folder (if it exists)
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    if os.path.exists(output_dir):
        for fname in os.listdir(output_dir):
            fpath = os.path.join(output_dir, fname)
            if os.path.isfile(fpath) and fname.endswith('.ipynb'):
                os.remove(fpath)
                
    print("✅ Purge complete.\n")

def run_pipeline(
    refresh=False, 
    purge=False, 
    first_run=False, 
    vis_only=False, 
    data_only=False ):
    
    notebooks = None
    
    if first_run:
        print("🚀 First run mode enabled.")
        
        print("✅ Enabling purge to ensure a clean slate and prevent issues from any existing outputs.")
        purge = True
        
        print("✅ Enabling refresh of original data to ensure pipeline has necessary inputs.")
        refresh = True
        
        print("✅ Disabling vis-only and data-only modes to ensure the full pipeline runs end-to-end and all outputs are generated.")
        vis_only = False
        data_only = False

    # Select which pipeline to run
    if data_only:
        print("⚠️ Data-only mode enabled. Only running data processing and synthesis notebooks, skipping exploration and visualization.")
        print("⚠️ At some point you will need to re-run the exploration and visualization notebooks to generate the updated outputs for visualization.")
                
        if refresh:
            print("🔄 Running refresh and data processing/synthesis notebooks.")
            notebooks = [notebook_pipeline_complete[0]] + notebook_pipeline_data_only
        else:
            print("🔄 Running data processing/synthesis notebooks without refresh.")
            notebooks = notebook_pipeline_data_only
    elif vis_only:
        print("⚠️ Vis-only mode enabled. Only running exploration and visualization notebooks, skipping data processing and synthesis.")
        print("⚠️ Make sure you have already run the data processing notebooks at least once to generate the necessary outputs for visualization, otherwise the visualization notebooks may fail due to missing data.")
        print("⚠️ Purge is disabled in vis-only mode to prevent accidental deletion of data outputs needed for visualizations.")
        purge = False
        
        if refresh:
            print("🔄 Refresh is enabled")
            notebooks = [notebook_pipeline_complete[0]] + notebook_pipeline_vis_only
        else:
            print("🔄 Refresh is disabled")
            notebooks = notebook_pipeline_vis_only  
    elif (not vis_only and not data_only) or (vis_only and data_only):
        if refresh:
            print("🔄 Running full pipeline with refresh of original data.")
            notebooks = notebook_pipeline_complete
        else:
            print("🔄 Running full pipeline without refresh of original data.")
            notebooks = notebook_pipeline_complete[1:]

    if purge:
        print("⚠️ Purge is enabled. All outputs from data processing, synthesis, exploration, and visualization will be deleted.")
        purge_outputs()

    for nb in notebooks:
        nb_name = os.path.basename(nb)

        try:
            print(f"Running: {nb_name}...")
            pm.execute_notebook(
                input_path=nb,
                
                # save executed notebooks to the outputs folder
                output_path= 'output/' + nb_name.replace('.ipynb', '_executed.ipynb'),
            )
            print("✅ Success")
        except Exception as e:
            print("❌ FAILED")
            print("-" * 30)
            print(f"CRITICAL ERROR in {nb_name}:")
            print(e)
            print("-" * 30)
            print("Stopping pipeline to prevent data corruption.")
            sys.exit(1)

    print("\n🥂 Pipeline finished successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the orbital debris pipeline.")
    
    parser.add_argument(
        "--first-run",
        action="store_true",
        help="Indicates this is the first time running the pipeline. This will trigger an automatic purge to ensure a clean slate, and will also enable downloading original data if not already specified."
    )
    
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Run the first notebook to download fresh data."
    )
    
    parser.add_argument(
        "--purge",
        action="store_true",
        help="Purge all exported/cleaned outputs before running the pipeline."
    )
    
    parser.add_argument(
        "--purge-only",
        action="store_true",
        help="Only purge outputs and do not run the pipeline."
    )
    
    parser.add_argument(
        "--vis-only",
        action="store_true",
        help="Only run the pipeline notebooks needed for exploration and visualization, skipping the data processing and synthesis steps."
    )
    
    parser.add_argument(
        "--data-only",
        action="store_true",
        help="Only run the pipeline notebooks needed to process and synthesize data, skipping the visualization steps."
    )
    
    # Parse arguments and execute accordingly
    args = parser.parse_args()

    # If --purge-only is set, we purge outputs and exit immediately. Otherwise, we run the pipeline with the specified options.    
    if args.purge_only:
        purge_outputs()
        sys.exit(0)
        
    # Add support for --data-only argument if needed in the future
    run_pipeline(
        refresh=args.refresh,
        purge=args.purge,
        first_run=args.first_run,
        vis_only=args.vis_only,
        data_only=args.data_only
    )
