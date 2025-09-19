import os
from pathlib import Path

PROJECT_NAME = "hotel-cancellation-prediction"

def create_project_structure():
    """
    Generates a standard, scalable end-to-end ML project structure.
    """
    # List of files and directories to create
    list_of_files = [
        f"src/{PROJECT_NAME}/__init__.py",
        f"src/{PROJECT_NAME}/components/__init__.py",
        f"src/{PROJECT_NAME}/components/data_ingestion.py",
        f"src/{PROJECT_NAME}/components/data_transformation.py",
        f"src/{PROJECT_NAME}/components/model_trainer.py",
        f"src/{PROJECT_NAME}/pipeline/__init__.py",
        f"src/{PROJECT_NAME}/pipeline/train_pipeline.py",
        f"src/{PROJECT_NAME}/pipeline/predict_pipeline.py",
        f"src/{PROJECT_NAME}/exception.py",
        f"src/{PROJECT_NAME}/logger.py",
        f"src/{PROJECT_NAME}/utils.py",
        "notebooks/1-eda.ipynb",
        "data/raw/.gitkeep", # .gitkeep to ensure the folder is tracked by git
        "app.py",
        "requirements.txt",
        "setup.py",
        "README.md",
        ".gitignore"
    ]

    print(f"--- Setting up project: {PROJECT_NAME} ---")

    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        # Create directory if it doesn't exist
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            print(f"Creating directory: {filedir} for the file {filename}")

        # Create empty file if it doesn't exist or is empty
        if (not filepath.exists()) or (filepath.stat().st_size == 0):
            with open(filepath, "w") as f:
                print(f"Creating empty file: {filepath}")
                pass  # Create an empty file
        else:
            print(f"{filename} already exists.")

    # --- Create boilerplate content for key files ---

    # requirements.txt
    with open("requirements.txt", "w") as f:
        f.write("pandas\n")
        f.write("numpy\n")
        f.write("scikit-learn\n")
        f.write("streamlit\n")
        f.write("dill\n") # Used for saving pipeline objects

    # setup.py
    with open("setup.py", "w") as f:
        f.write("from setuptools import find_packages, setup\n\n")
        f.write("setup(\n")
        f.write(f"    name='{PROJECT_NAME}',\n")
        f.write("    version='0.0.1',\n")
        f.write("    author='Your Name',\n")
        f.write("    author_email='your.email@example.com',\n")
        f.write("    packages=find_packages(),\n")
        f.write(")\n")

    # app.py (Streamlit app)
    with open("app.py", "w") as f:
        f.write("import streamlit as st\n\n")
        f.write("st.title('Hotel Booking Cancellation Prediction')\n\n")
        f.write("# Add your input fields here\n")
        f.write("# e.g., lead_time = st.number_input('Lead Time')\n\n")
        f.write("if st.button('Predict Cancellation'):\n")
        f.write("    # Code to load model and make prediction\n")
        f.write("    st.success('Prediction: [Result]')\n")

    # .gitignore
    with open(".gitignore", "w") as f:
        f.write("*.pyc\n")
        f.write("__pycache__/\n")
        f.write(".DS_Store\n")
        f.write("*.env\n")
        f.write(".venv/\n")
        f.write("env/\n")
        f.write("venv/\n")
        f.write("artifacts/\n")
        f.write("data/\n")

    print("\n--- Project structure created successfully! ---")
    print(f"Next steps:")
    print(f"1. Move your 'hotel_booking.csv' into the 'data/raw/' directory.")
    print(f"2. Run 'pip install -r requirements.txt' to install dependencies.")
    print(f"3. Run 'pip install -e .' to install your 'src' directory as a local package.")

if __name__ == "__main__":
    # This script should be run from the root of your project folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    create_project_structure()