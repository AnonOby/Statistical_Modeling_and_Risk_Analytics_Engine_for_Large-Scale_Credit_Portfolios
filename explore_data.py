import pandas as pd
import sys
import os

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

    # 3. Inspect the "emp_title" column specifically
    if "emp_title" in first_chunk.columns:
        print("\n" + "="*50)
        print("TOP 20 MOST COMMON JOB TITLES (Raw Data):")
        print("="*50)

        # Count frequency and show top 20
        job_counts = first_chunk["emp_title"].value_counts().head(20)

        for title, count in job_counts.items():
            bar = "🧊" * int(count / 20) # Simple visual bar
            print(f"{title:<25} | {count:<5} {bar}")

