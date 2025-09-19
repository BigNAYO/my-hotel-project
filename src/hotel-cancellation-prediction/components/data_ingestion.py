import os
import sys
import pandas as pd

# Direct imports (same-folder or sibling-folder style)
import logger
import exception

class DataIngestion:
    """
    Handles the data ingestion process.
    Reads the raw data and saves it into a DataFrame.
    """
    def __init__(self):
        self.raw_data_path = os.path.join("data", "raw", "hotel_booking.csv")

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(self.raw_data_path)
            logger.logging.info("Data read successfully.")
            return df
        except Exception as e:
            raise exception.CustomException(e, sys)
