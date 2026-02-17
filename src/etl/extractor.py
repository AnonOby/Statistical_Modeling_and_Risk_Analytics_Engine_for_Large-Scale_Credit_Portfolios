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
