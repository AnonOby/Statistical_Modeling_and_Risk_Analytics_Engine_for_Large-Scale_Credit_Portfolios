import pandas as pd
import sys
import os

from fontTools.merge.util import first

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# import our previously built extractor and config
from src.etl.extractor import DataExtractor
import config

def main():
    print("Initializing Data Exploration...")
    print("-" * 50)

    # 1. Initialize Extractor
    extractor = DataExtractor(config.RAW_LOAN_DATA_FILE)

    try:
        # 2. Read only the first small chunk (e.g. 10,000 rows) to peek
        print("reading the first 10,000 rows from the CSV...")

        # Get just the first yield
        first_chunk = next(extractor.get_chunks(chunksize=10000))

        print(f"Successfully loaded {first_chunk.shape[0]} rows.")
        print(f"Total Columns in Dataset: {first_chunk.shape[1]}")
