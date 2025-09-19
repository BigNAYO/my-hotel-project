import os
import sys
import streamlit as st
import pandas as pd

# Add components folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "hotel-cancellation-prediction", "pipeline")))

from predict_pipeline import PredictPipeline, CustomData

st.title("🏨 Hotel Booking Cancellation Prediction")

st.markdown("Fill in the booking details below to predict if it will be cancelled.")

# --- Input fields ---
hotel = st.selectbox("Hotel Type", ["Resort Hotel", "City Hotel"])
lead_time = st.number_input("Lead Time (days)", min_value=0, max_value=1000, value=50)
arrival_date_year = st.selectbox("Arrival Year", [2017, 2018, 2019])
arrival_date_week_number = st.slider("Arrival Week Number", 1, 52, 25)
arrival_date_month = st.selectbox("Arrival Month", 
                                  ["January","February","March","April","May","June",
                                   "July","August","September","October","November","December"])
stays_in_weekend_nights = st.number_input("Weekend Nights", min_value=0, max_value=30, value=1)
stays_in_week_nights = st.number_input("Week Nights", min_value=0, max_value=30, value=2)
adults = st.number_input("Adults", min_value=1, max_value=10, value=2)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
babies = st.number_input("Babies", min_value=0, max_value=5, value=0)
meal = st.selectbox("Meal", ["BB","HB","FB","SC"])
market_segment = st.selectbox("Market Segment", ["Direct","Corporate","Online TA","Offline TA/TO"])
distribution_channel = st.selectbox("Distribution Channel", ["Direct","Corporate","TA/TO","GDS"])
reserved_room_type = st.text_input("Reserved Room Type", "A")
assigned_room_type = st.text_input("Assigned Room Type", "A")
deposit_type = st.selectbox("Deposit Type", ["No Deposit","Non Refund","Refundable"])
agent = st.number_input("Agent ID", min_value=0, max_value=500, value=1)
customer_type = st.selectbox("Customer Type", ["Transient","Contract","Group","Transient-Party"])
adr = st.number_input("Average Daily Rate", min_value=0.0, max_value=1000.0, value=100.0)
required_car_parking_spaces = st.number_input("Parking Spaces", min_value=0, max_value=10, value=0)
total_of_special_requests = st.number_input("Special Requests", min_value=0, max_value=5, value=0)
reservation_status = st.selectbox("Reservation Status", ["Check-Out","Canceled","No-Show"])
credit_card = st.text_input("Credit Card Number", "1234")

# --- Prediction button ---
if st.button("Predict Cancellation"):
    try:
        # Convert user input into DataFrame
        input_data = CustomData(
            hotel=hotel,
            lead_time=lead_time,
            arrival_date_year=arrival_date_year,
            arrival_date_week_number=arrival_date_week_number,
            arrival_date_month=arrival_date_month,
            stays_in_weekend_nights=stays_in_weekend_nights,
            stays_in_week_nights=stays_in_week_nights,
            adults=adults,
            children=children,
            babies=babies,
            meal=meal,
            market_segment=market_segment,
            distribution_channel=distribution_channel,
            reserved_room_type=reserved_room_type,
            assigned_room_type=assigned_room_type,
            deposit_type=deposit_type,
            agent=agent,
            customer_type=customer_type,
            adr=adr,
            required_car_parking_spaces=required_car_parking_spaces,
            total_of_special_requests=total_of_special_requests,
            reservation_status=reservation_status,
            credit_card=credit_card,
        )

        df = input_data.get_data_as_dataframe()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)

        result = "❌ Cancelled" if prediction[0] == 1 else "✅ Not Cancelled"
        st.success(f"Prediction: {result}")

    except Exception as e:
        st.error(f"Error making prediction: {e}")

