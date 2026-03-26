import papermill as pm
import sys
import argparse

# 1. Define your sequence (Order matters!)
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