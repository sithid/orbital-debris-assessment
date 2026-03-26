import papermill as pm
import sys
import argparse

# Define note sequence, the order actually matters. Each notebook continues where the previous
# left off, so we can't just run them in parallel or out of order because of file dependencies.
# This sequence will be looped through in the run_pipeline function.
notebook_pipeline = [
    "./00_pipeline_refresh.ipynb",
    "./01_ucs_cleanup.ipynb",
    "./02_satcat_cleanup.ipynb",
    "./03_kinetic_master_synthesis.ipynb",
    "./04_orbital_debris_synthesis.ipynb",
    "./05_orbital_debris_queries.ipynb",
    "./06_visualizations.ipynb"
]

def run_pipeline(download_originals=False):
    print(f"🔔 Starting execution of {len(notebook_pipeline)} notebooks...\n")
    
    for nb in notebook_pipeline:
        if nb == "./00_pipeline_refresh.ipynb" and not download_originals:
            print(f"Skipping {nb} (original data refresh) per download_originals parameter.")
            continue
                
        try:
            # papermill makes executing notebooks trivial.
            # it will run the notebook and save the output back to the same file, or
            # you can specify a different output path if you want to keep the original clean
            # without output cells. Here we overwrite the original for simplicity but I may
            # decide to change this later if I want to keep the original notebooks as templates
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
    
    # This adds the --refresh flag. If you don't include it, it defaults to False.
    parser.add_argument(
        "--refresh", 
        action="store_true", 
        help="Run the first notebook to download fresh data."
    )
    
    args = parser.parse_args()
    
    run_pipeline(download_originals=args.refresh)