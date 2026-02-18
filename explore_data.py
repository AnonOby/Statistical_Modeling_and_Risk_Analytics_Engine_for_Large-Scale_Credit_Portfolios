import pandas as pd
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# import our previously built extractor and config
from src.etl.extractor import DataExtractor
import config

