import streamlit as st


def create_ui():
    st.markdown(
        '<h2 class="section-title" style="text-align:center;justify-content:center;">📋 Shipment Information</h2>'
        '<p class="section-subtitle" style="text-align:center;">'
        "Enter the shipment details below to predict whether it will arrive on time.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            '<div class="form-card">'
            '<div class="form-card-title">📍 Route & Shipment</div>',
            unsafe_allow_html=True,
        )
        warehouse = st.selectbox("Warehouse Block", ["A", "B", "C", "D", "F"])
        shipment = st.selectbox("Mode of Shipment", ["Flight", "Road", "Ship"])
        importance = st.selectbox("Product Importance", ["high", "medium", "low"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="form-card">'
            '<div class="form-card-title">👤 Customer Profile</div>',
            unsafe_allow_html=True,
        )
        gender = st.selectbox("Customer Gender", ["F", "M"])
        customer_care_calls = st.number_input(
            "Customer Care Calls", min_value=0, value=0
        )
        customer_rating = st.number_input(
            "Customer Rating", min_value=1, max_value=5, value=3
        )
        prior_purchases = st.number_input(
            "Prior Purchases", min_value=0, value=0
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            '<div class="form-card">'
            '<div class="form-card-title">💰 Product Details</div>',
            unsafe_allow_html=True,
        )
        cost = st.number_input("Cost of Product ($)", min_value=1.0, value=100.0)
        discount = st.number_input("Discount Offered (%)", min_value=0.0, value=0.0)
        weight = st.number_input("Weight in Grams", min_value=1.0, value=1000.0)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="form-card">'
            '<div class="form-card-title">📊 Quick Stats</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='display:flex;justify-content:space-between;padding:0.25rem 0;'>"
            "<span style='color:#9090b0;font-size:0.75rem;'>Product Cost</span>"
            f"<span style='color:#e8e8f0;font-weight:600;font-size:0.85rem;'>${cost:.2f}</span>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='display:flex;justify-content:space-between;padding:0.25rem 0;'>"
            "<span style='color:#9090b0;font-size:0.75rem;'>Discount Applied</span>"
            f"<span style='color:#e8e8f0;font-weight:600;font-size:0.85rem;'>{discount:.1f}%</span>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='display:flex;justify-content:space-between;padding:0.25rem 0;'>"
            "<span style='color:#9090b0;font-size:0.75rem;'>Package Weight</span>"
            f"<span style='color:#e8e8f0;font-weight:600;font-size:0.85rem;'>{weight:.1f}g</span>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)


    return (
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