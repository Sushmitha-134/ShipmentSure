import streamlit as st
import pandas as pd

from frontend.ui import create_ui
from frontend.components import (
    render_sidebar,
    render_hero,
    render_kpi_cards,
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
render_kpi_cards()

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
) = create_ui()

if st.button("🚀 Predict Shipment Status", width='stretch'):
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
    render_prediction_result(prediction, probability)
    with st.expander("📈 Feature Importance"):
        render_feature_importance()

    delay_prob = probability[1] * 100
    st.session_state.prediction_history.insert(0, {
        "Date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
        "Warehouse": warehouse,
        "Shipment Mode": shipment,
        "Prediction": "Delayed" if prediction == 1 else "On Time",
        "Probability": f"{delay_prob:.1f}%",
    })

render_prediction_history()

render_about()
render_footer()
