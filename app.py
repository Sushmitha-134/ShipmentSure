import streamlit as st
import pandas as pd

from frontend.ui import create_ui
from frontend.components import (
    render_sidebar,
    render_hero,
    render_prediction_result,
    render_feature_importance,
    render_prediction_history,
    render_about,
    render_footer,
)
from backend.preprocess import create_features
from backend.predictor import predict

st.set_page_config(
    page_title="ShipmentSure — Logistics Analytics Platform",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

with open("frontend/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

render_sidebar()
render_hero()

left, right = st.columns([2, 1], gap="large")

with left:
    form_data = create_ui()
    (
        warehouse,
        shipment,
        importance,
        gender,
        customer_care_calls,
        customer_rating,
        cost,
        prior_purchases,
        discount,
        weight,
    ) = form_data

    predict_clicked = st.button("🚀 Predict Shipment Status", use_container_width=True)

with right:
    if predict_clicked:
        data = create_features(
            warehouse,
            shipment,
            importance,
            gender,
            customer_care_calls,
            customer_rating,
            cost,
            prior_purchases,
            discount,
            weight,
        )

        prediction, probability = predict(data)
        st.session_state.last_prediction = (prediction, probability)
        render_prediction_result(prediction, probability)

        delay_prob = probability[1] * 100
        st.session_state.prediction_history.insert(0, {
            "Date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
            "Warehouse": warehouse,
            "Shipment Mode": shipment,
            "Prediction": "Delayed" if prediction == 1 else "On Time",
            "Probability": f"{delay_prob:.1f}%",
        })

    elif "last_prediction" in st.session_state:
        render_prediction_result(*st.session_state.last_prediction)

    if st.session_state.get("prediction_history"):
        with st.expander("📈 Feature Importance", expanded=False):
            render_feature_importance()

if st.session_state.get("prediction_history"):
    c1, c2 = st.columns([6, 1])
    with c1:
        render_prediction_history()
    with c2:
        if st.button("🗑 Clear", use_container_width=True):
            st.session_state.prediction_history = []
            st.rerun()

with st.expander("ℹ️ About ShipmentSure", expanded=False):
    render_about()

render_footer()
