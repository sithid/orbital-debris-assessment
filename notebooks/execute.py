import papermill as pm
import sys
import argparse
import os
import shutil

# https://docs.python.org/3/library/filesys.html
# https://docs.python.org/3/library/shutil.html

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
    os.path.join(ROOT_DIR, "notebooks/07_orbital_debris_story_visualizations.ipynb"),
    os.path.join(ROOT_DIR, "notebooks/08_orbital_debris_assessment_presentation.ipynb")
]
notebook_pipeline_data_only = notebook_pipeline_complete[1:5]  # Only the first 4 notebooks which are for data processing and synthesis
notebook_pipeline_vis_only = notebook_pipeline_complete[-4:]  # Only the last 4 notebooks which are for exploration, queries, visualization and presentation.

def purge_outputs():
    print("\n⚠️  Purging all exported/cleaned outputs...")
    
    # Remove output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        
    # Remove charts directory
    charts_dir = os.path.join(ROOT_DIR, 'charts')
    if os.path.exists(charts_dir):
        shutil.rmtree(charts_dir)
        
    # Remove data/clean directory (all cleaned/intermediate files, CSVs, DBs, and results)
    # db sometimes locks, handle the exception
    clean_dir = os.path.join(ROOT_DIR, 'data/clean')
    if os.path.exists(clean_dir):
        try:
            shutil.rmtree(clean_dir)
        except Exception as e:
            print(f"⚠️  Failed to remove clean directory: {e}")
            
    print("✅ Output, charts, and clean directories removed.")

    print("💨 Reinitializing directory structure...")
    build_directory_structure(True)
    print("✅ Purge and reinitialization complete.\n")

def build_directory_structure(silent=False):
    if not silent:
        print("💨 Initializing pipeline directory structure...")
        
    # Create the output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
            
    # Create the clean/results directory if it doesn't exist
    clean_results_dir = os.path.join(ROOT_DIR, 'data/clean/results')
    if not os.path.exists(clean_results_dir):
        os.makedirs(clean_results_dir)
        
    # Create the charts directory and subdirectories if they don't exist.
    charts_dir = os.path.join(ROOT_DIR, 'charts')
    if not os.path.exists(charts_dir):
        if not silent:
            print("✅ Creating charts directory at: ", charts_dir)
        os.makedirs(charts_dir)
        
    questions_dir = os.path.join(charts_dir, 'questions')
    if not os.path.exists(questions_dir):
        if not silent:
            print("✅ Creating questions directory at: ", questions_dir)
        os.makedirs(questions_dir)

    # Create initial subdirectories for exploratory, primary, and secondary.
    sub_questions_dirs = ['exploratory', 'primary', 'secondary']
    for subdir in sub_questions_dirs:
        subdir_path = os.path.join(questions_dir, subdir)
        if not os.path.exists(subdir_path):
            if not silent:
                print("✅ Creating subdirectory for question type: ", subdir_path)
            os.makedirs(subdir_path)
                
        # Create subdirectories for the two image types inside each question type folder.
        if subdir in sub_questions_dirs:
            for img_type in ['png', 'svg']:
                img_subdir_path = os.path.join(subdir_path, img_type)
                if not os.path.exists(img_subdir_path):
                    if not silent:
                        print("✅ Creating subdirectory for image type: ", img_subdir_path)
                    os.makedirs(img_subdir_path)
        
    if not silent:
        print("✅ Directory structure initialized.") 
        
def run_pipeline(
    refresh=False, 
    purge=False, 
    first_run=False, 
    vis_only=False, 
    data_only=False ):
    
    notebooks = None
    
    if first_run:
        print("🚀 First run mode enabled. 🚀")
        
        # Build initial directory structure to ensure all necessary folders are created before running any notebooks.
        # silent=false for verbose output since this is the first run and we want to see the initialization steps.
        build_directory_structure(False)
        
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
