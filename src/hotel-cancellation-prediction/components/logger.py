import logging
import os

# Create artifacts directory for logs
LOG_FILE = os.path.join("artifacts", "app.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
