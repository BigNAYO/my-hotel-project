import pandas as pd
import numpy as np

class DataTransformation:
    def __init__(self):
        # Will be set during training
        self.feature_columns = None

    def frequency_encode_column(self, df, col_name):
        freq_map = df[col_name].value_counts().to_dict()
        df[col_name] = df[col_name].map(freq_map)
        return df

    def add_date_features(self, df):
        if "arrival_date_year" in df.columns:
            df["arrival_date_year"] = df["arrival_date_year"].astype(int)

        if "arrival_date_week_number" in df.columns:
            week = df["arrival_date_week_number"]
            week_sin = np.sin(2 * np.pi * week / 52)
            week_cos = np.cos(2 * np.pi * week / 52)
            df["week_sin"] = (week_sin + 1) / 2
            df["week_cos"] = (week_cos + 1) / 2
            df.drop(columns=["arrival_date_week_number"], inplace=True)
        return df

    def initiate_data_transformation(self, df, training=True):
        df = df.drop(columns=[
            'country','company','name','email',
            'phone-number','reservation_status_date'
        ], errors="ignore")

        df = df.dropna()

        if training:
            X = df.drop(['is_canceled'], axis=1)
            y = df['is_canceled']
        else:
            X = df.copy()
            y = None

        X = pd.get_dummies(
            X,
            columns=['hotel','arrival_date_month','meal','market_segment',
                     'distribution_channel','reserved_room_type',
                     'assigned_room_type','deposit_type','customer_type',
                     'reservation_status'],
            drop_first=True,
            dtype=float
        )

        if "credit_card" in X.columns:
            X = self.frequency_encode_column(X, "credit_card")

        X = self.add_date_features(X)

        if training:
            # Save the training feature order
            self.feature_columns = X.columns
        else:
            # Align prediction data with training features
            for col in self.feature_columns:
                if col not in X.columns:
                    X[col] = 0
            # Drop any extras and reorder
            X = X[self.feature_columns]

        return X, y
