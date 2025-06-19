# script to extract team box and player box scores from .csv.gv files and save them as .csv files
import os
import pandas as pd
import gzip

def extract_csv_from_gz(directory):
    """ 
    Extract CSV files from .csv.gz files in the specified directory.
    """
    for filename in os.listdir(directory):
        print(f"Processing file: {filename}")
        if filename.endswith(".csv.gz"):
            input_path = os.path.join(directory, filename)
            output_filename = filename.replace(".csv.gz", ".csv")
            output_path = os.path.join(directory, output_filename)

            try:
                with gzip.open(input_path, 'rt') as f:
                    df = pd.read_csv(f)
                df.to_csv(output_path, index=False)
                print(f"Extracted: {output_filename}")
            except Exception as e:
                print(f"Failed to extract {filename}: {e}")
        else:
            print(f"Skipping non-gzipped file: {filename}")

dir = "/path/to/your/directory"
extract_csv_from_gz(dir)