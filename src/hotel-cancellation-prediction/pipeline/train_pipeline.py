import sys
import os

# Add components folder to sys.path for direct imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "components")))

import data_ingestion
import data_transformation
import model_trainer

def main():
    print("===== Starting Training Pipeline =====")

    # Step 1: Data Ingestion
    ingestion = data_ingestion.DataIngestion()
    df = ingestion.initiate_data_ingestion()
    print(f"Data Ingestion completed. Shape: {df.shape}")

    # Step 2: Data Transformation
    transformer = data_transformation.DataTransformation()
    X, y = transformer.initiate_data_transformation(df, training=True)
    print(f"Data Transformation completed. X shape: {X.shape}, y shape: {y.shape}")
    print(f"Stored feature columns: {len(transformer.feature_columns)} features")

    # Step 3: Model Training
    trainer = model_trainer.ModelTrainer()
    report = trainer.initiate_model_training(X, y, transformer=transformer)
    print(f"Model Training completed. Report: {report}")

    print("===== Training Pipeline Completed Successfully =====")

if __name__ == "__main__":
    main()
