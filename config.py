import os
from pathlib import Path
from dotenv import  load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# --------------------------------------------------
# 1. Path Configuration
# --------------------------------------------------
# Since config.py is in the root directory, .parent gives us the root path.
BASE_DIR = Path(__file__).resolve().parent

# Define the  main data directory
DATA_DIR = BASE_DIR / "data"

# Define the subdirectories for raw and processed data
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Create these directories if they don't exist yet
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

