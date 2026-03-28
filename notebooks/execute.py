import papermill as pm
import sys
import argparse

import os
import shutil

# https://docs.python.org/3/library/filesys.html

# Define notebook sequence, the order actually matters. Each notebook continues where the previous
# left off, so we can't just run them in parallel or out of order because of file dependencies.
# This sequence will be looped through in the run_pipeline function.
notebook_pipeline = [
    "./00_pipeline_refresh.ipynb",
    "./01_ucs_cleanup.ipynb",
    "./02_satcat_cleanup.ipynb",
    "./03_kinetic_master_synthesis.ipynb",
    "./04_orbital_debris_synthesis.ipynb",
    "./05_orbital_debris_exploration.ipynb",
    "./06_orbital_debris_queries.ipynb",
    "./07_orbital_debris_visualizations.ipynb"
]

def purge_outputs():
    
    print("\n⚠️  Purging all exported/cleaned outputs...")
    
    # Purge datasets in the clean folder but skip the results folder.
    # This is where we save any exported datasets or cleaned versions of the original data that we want to keep separate from the raw downloads in the clean folder. We want to purge these on demand because they can be large and we don't want to accidentally delete them every time we run the pipeline, but we also want to give the option to start fresh if needed.
    
    clean_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/clean'))
    if os.path.exists(clean_dir):
        for fname in os.listdir(clean_dir):
            fpath = os.path.join(clean_dir, fname)
            
            # Skip the results folder
            if fname == 'results' and os.path.isdir(fpath):
                continue
            if os.path.isfile(fpath):
                os.remove(fpath)
                
    # Explicitly remove the database file if it exists still.
    # The previous loop should have removed it, but if it was open or locked
    # for some reason it might still be there, so we do this as a final cleanup step to ensure a fresh start.
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/clean/orbital_debris.db'))
    if os.path.exists(db_path):
        os.remove(db_path)
        
    # Purge images in charts directory but leave the folder structure intact.
    charts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../charts'))
    if os.path.exists(charts_dir):
        for root, dirs, files in os.walk(charts_dir):
            for file in files:
                if file.endswith(('.png', '.svg')):
                    os.remove(os.path.join(root, file))
                    
    # Purge items inside results but leave the folder structure intact.
    results_dir = os.path.abspath(os.path.join(clean_dir, 'results'))
    
    if os.path.exists(results_dir):
        for fname in os.listdir(results_dir):
            fpath = os.path.join(results_dir, fname)
            try:
                if os.path.isfile(fpath) or os.path.islink(fpath):
                    os.remove(fpath)
                    
            except Exception as e:
                print(f"Warning: Could not delete {fpath}: {e}")
        
    print("✅ Purge complete.\n")
    
def run_pipeline(download_originals=False, purge=False):
    if purge:
        purge_outputs()
        
    for nb in notebook_pipeline:
        if nb == "./00_pipeline_refresh.ipynb" and not download_originals:
            print(f"Skipping {nb} (original data refresh) per download_originals parameter.")
            continue
                
        try:
            print(f"Running: {nb}...")
            pm.execute_notebook(
                input_path=nb,
                output_path=nb
            )
            print("✅ Success")
            
        except Exception as e:
            print("❌ FAILED")
            print("-" * 30)
            print(f"CRITICAL ERROR in {nb}:")
            print(e)
            print("-" * 30)
            print("Stopping pipeline to prevent data corruption.")
            sys.exit(1)

    print("\n🎉 Pipeline finished successfully!")

if __name__ == "__main__":
    
    # Setup command line arguments
    parser = argparse.ArgumentParser(description="Run the orbital debris pipeline.")
    
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
    
    # Parse arguments and execute accordingly
    # If --purge-only is set, we purge outputs and exit immediately. Otherwise, we run the pipeline with the specified options.
    args = parser.parse_args()
    if args.purge_only:
        purge_outputs()
        sys.exit(0)
        
    run_pipeline(download_originals=args.refresh, purge=args.purge)