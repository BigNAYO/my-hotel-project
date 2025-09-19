import os
import sys
import pandas as pd
import joblib

# Add components folder to sys.path for direct imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "components")))
import data_transformation


class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.transformer_path = os.path.join("artifacts", "transformer.pkl")

        try:
            self.model = joblib.load(self.model_path)
            self.transformer = joblib.load(self.transformer_path)

            if not hasattr(self.transformer, "feature_columns") or self.transformer.feature_columns is None:
                raise RuntimeError(
                    "Loaded transformer has no feature_columns. Make sure you trained the model first."
                )

            print("✅ Model and transformer loaded successfully for prediction.")
        except Exception as e:
            raise RuntimeError(f"Error loading artifacts: {e}")

    def predict(self, data: pd.DataFrame):
        try:
            # Transform input in prediction mode
            X, _ = self.transformer.initiate_data_transformation(data, training=False)

            # Predict
            preds = self.model.predict(X)
            return preds
        except Exception as e:
            raise RuntimeError(f"Prediction failed: {e}")


class CustomData:
    """
    Convert user inputs into a DataFrame for prediction.
    """
    def __init__(self,
                 hotel: str,
                 lead_time: int,
                 arrival_date_year: int,
                 arrival_date_week_number: int,
                 arrival_date_month: str,
                 stays_in_weekend_nights: int,
                 stays_in_week_nights: int,
                 adults: int,
                 children: int,
                 babies: int,
                 meal: str,
                 market_segment: str,
                 distribution_channel: str,
                 reserved_room_type: str,
                 assigned_room_type: str,
                 deposit_type: str,
                 agent: int,
                 customer_type: str,
                 adr: float,
                 required_car_parking_spaces: int,
                 total_of_special_requests: int,
                 reservation_status: str,
                 credit_card: str):

        self.data = {
            "hotel": [hotel],
            "lead_time": [lead_time],
            "arrival_date_year": [arrival_date_year],
            "arrival_date_week_number": [arrival_date_week_number],
            "arrival_date_month": [arrival_date_month],
            "stays_in_weekend_nights": [stays_in_weekend_nights],
            "stays_in_week_nights": [stays_in_week_nights],
            "adults": [adults],
            "children": [children],
            "babies": [babies],
            "meal": [meal],
            "market_segment": [market_segment],
            "distribution_channel": [distribution_channel],
            "reserved_room_type": [reserved_room_type],
            "assigned_room_type": [assigned_room_type],
            "deposit_type": [deposit_type],
            "agent": [agent],
            "customer_type": [customer_type],
            "adr": [adr],
            "required_car_parking_spaces": [required_car_parking_spaces],
            "total_of_special_requests": [total_of_special_requests],
            "reservation_status": [reservation_status],
            "credit_card": [credit_card],
        }

    def get_data_as_dataframe(self):
        return pd.DataFrame(self.data)
