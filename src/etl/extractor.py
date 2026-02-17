import pandas as pd
import sys
import os
from tqdm import tqdm

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import config

class DataExtractor:
    """
    Handles extractions of large datasets using chunking to optimize memory usage.
    Implements a Generator to yield pieces of data on demand.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def validate_file(self):
        """
        Check if the raw data file exists in the designated directory.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Data not found at: {self.file_path}\n"
                f"Please download the 'accepted_2007_to_2018Q4.csv' from Lending Club Kaggle,\n"
                f"rename it to 'lending_club_loan.csv' and place it in the '{config.RAW_DATA_DIR} folder.'"
            )
        print(f"File found: {self.file_path.name} ({self.file_path.stat().st_size / 1024 / 1024:.2f} MB)")

    def get_chunks(self, chunksize = 50000):
        """
        Generator that yields pandas DataFrames in chunks.


        """