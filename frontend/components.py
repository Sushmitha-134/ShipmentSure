import streamlit as st
import pickle
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
plt.style.use("dark_background")

FEATURE_NAMES = [
    "Customer Care Calls", "Customer Rating", "Cost of Product",
    "Prior Purchases", "Discount Offered", "Weight (gms)",
    "Cost/Weight Ratio", "Discount/Cost Ratio", "Calls/Purchase",
    "Warehouse B", "Warehouse C", "Warehouse D", "Warehouse F",
    "Ship by Road", "Ship by Sea", "Low Importance",
    "Medium Importance", "Gender Male",
]


def load_feature_importances():
    with open("models/ShipmentSure_Model.pkl", "rb") as f:
        model = pickle.load(f)
    importances = model.feature_importances_
    df = pd.DataFrame({"Feature": FEATURE_NAMES, "Importance": importances})
    return df.sort_values("Importance", ascending=True).reset_index(drop=True)


def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-logo">
                <div class="sidebar-logo-icon">📦</div>
                <div class="sidebar-logo-text">
                    <span class="sidebar-logo-title">ShipmentSure</span>
                    <span class="sidebar-logo-subtitle">Logistics Analytics</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<hr>", unsafe_allow_html=True)

        st.markdown(
            '<div class="sidebar-section-label">Navigation</div>',
            unsafe_allow_html=True,
        )

        nav_items = [
            ("📊", "Dashboard", True),
            ("📋", "Predictions", False),
            ("📈", "Analytics", False),
            ("ℹ️", "About", False),
        ]
        for icon, label, active in nav_items:
            cls = "sidebar-nav-item active" if active else "sidebar-nav-item"
            st.markdown(
                f'<div class="{cls}">'
                f'<span class="sidebar-nav-icon">{icon}</span>'
                f"<span>{label}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<hr>", unsafe_allow_html=True)

        st.markdown(
            '<div class="sidebar-section-label">System Status</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="sidebar-stats">'
            '<div class="sidebar-stat">'
            '<span class="sidebar-stat-label">Model</span>'
            '<span class="sidebar-stat-value">XGBoost</span>'
            "</div>"
            '<div class="sidebar-stat">'
            '<span class="sidebar-stat-label">Version</span>'
            '<span class="sidebar-stat-value">v2.1</span>'
            "</div>"
            '<div class="sidebar-stat">'
            '<span class="sidebar-stat-label">Accuracy</span>'
            '<span class="sidebar-stat-value">68%</span>'
            "</div>"
            '<div class="sidebar-stat">'
            '<span class="sidebar-stat-label">Features</span>'
            '<span class="sidebar-stat-value">18</span>'
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="sidebar-status">'
            '<span class="sidebar-status-dot"></span>'
            "<span>All systems operational</span>"
            "</div>",
            unsafe_allow_html=True,
        )


def render_hero():
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-badge">
                ⚡ AI-Powered Analytics
            </div>
            <h1 class="hero-title">🚚 ShipmentSure</h1>
            <div class="hero-tagline">AI-Powered Shipment Delay Prediction</div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <span class="hero-stat-value">68%</span>
                    <span class="hero-stat-label">Model Accuracy</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-value">18</span>
                    <span class="hero-stat-label">Features</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-value">10,999</span>
                    <span class="hero-stat-label">Dataset Records</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpi_cards():
    st.markdown(
        '<h2 class="section-title">📊 Key Metrics</h2>',
        unsafe_allow_html=True,
    )

    kpis = [
        {
            "icon": "🎯",
            "value": "68%",
            "label": "Model Accuracy",
            "change": "+2.5%",
            "change_class": "positive",
            "desc": "Cross-validated XGBoost score",
        },
        {
            "icon": "🧩",
            "value": "18",
            "label": "Input Features",
            "change": "Engineered",
            "change_class": "neutral",
            "desc": "Raw + derived attributes",
        },
        {
            "icon": "📦",
            "value": "10,999",
            "label": "Dataset Records",
            "change": "Analyzed",
            "change_class": "neutral",
            "desc": "Historical shipment records",
        },
    ]

    cols = st.columns(3)
    for col, kpi in zip(cols, kpis):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-card-header">
                        <div class="kpi-card-icon">{kpi["icon"]}</div>
                        <span class="kpi-card-change {kpi['change_class']}">
                            {kpi["change"]}
                        </span>
                    </div>
                    <div class="kpi-card-value">{kpi["value"]}</div>
                    <div class="kpi-card-label">{kpi["label"]}</div>
                    <div class="kpi-card-desc">{kpi["desc"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def get_risk_level(delay_prob):
    if delay_prob < 40:
        return "🟢", "Low Risk"
    elif delay_prob < 70:
        return "🟡", "Medium Risk"
    else:
        return "🔴", "High Risk"


def render_prediction_result(prediction, probability):
    delay_prob = probability[1] * 100
    ontime_prob = probability[0] * 100
    confidence = max(probability) * 100

    is_delayed = prediction == 1
    status_text = "Delayed" if is_delayed else "On Time"
    status_class = "result-delayed" if is_delayed else "result-ontime"
    status_icon = "🚨" if is_delayed else "✅"
    risk_icon, risk_label = get_risk_level(delay_prob)

    st.markdown(
        f"""
        <div class="result-card {status_class}">
            <div class="result-header">
                <div class="result-icon">{status_icon}</div>
                <div>
                    <div class="result-title">Shipment Likely {status_text}</div>
                    <div class="result-subtitle">Based on trained XGBoost model analysis</div>
                </div>
            </div>
            <div class="result-risk-badge">
                {risk_icon} {risk_label}
            </div>
            <div class="result-probabilities">
                <div class="result-prob-item">
                    <div class="result-prob-label">On-Time Probability</div>
                    <div class="result-prob-value ontime">{ontime_prob:.1f}%</div>
                </div>
                <div class="result-prob-item">
                    <div class="result-prob-label">Delay Probability</div>
                    <div class="result-prob-value delay">{delay_prob:.1f}%</div>
                </div>
                <div class="result-prob-item">
                    <div class="result-prob-label">Confidence Score</div>
                    <div class="result-prob-value confidence">{confidence:.1f}%</div>
                </div>
            </div>
            <div class="result-progress-container">
                <div class="result-progress-row">
                    <span class="result-progress-label">On Time</span>
                    <div class="result-progress-bar-bg">
                        <div class="result-progress-bar-fill ontime"
                             style="width: {ontime_prob:.1f}%"></div>
                    </div>
                    <span class="result-progress-value">{ontime_prob:.1f}%</span>
                </div>
                <div class="result-progress-row">
                    <span class="result-progress-label">Delayed</span>
                    <div class="result-progress-bar-bg">
                        <div class="result-progress-bar-fill delay"
                             style="width: {delay_prob:.1f}%"></div>
                    </div>
                    <span class="result-progress-value">{delay_prob:.1f}%</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_importance():
    st.markdown(
        '<h2 class="section-title">📈 Feature Importance</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-subtitle">'
        "How each input feature influences the delay prediction.</p>",
        unsafe_allow_html=True,
    )

    df = load_feature_importances()

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("none")
    ax.set_facecolor("none")

    colors = plt.cm.Greens(np.linspace(0.3, 0.9, len(df)))
    colors = colors[::-1]

    bars = ax.barh(df["Feature"], df["Importance"], color=colors, height=0.65, edgecolor="none")

    for bar, val in zip(bars, df["Importance"]):
        ax.text(
            val + 0.002,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.3f}",
            va="center",
            fontsize=8,
            fontfamily="monospace",
            color="#9090b0",
        )

    ax.set_xlabel("Importance Score", fontsize=9, color="#606080", fontfamily="sans-serif")
    ax.tick_params(axis="y", labelsize=9, colors="#9090b0")
    ax.tick_params(axis="x", labelsize=8, colors="#606080")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#1e1e3a")
    ax.spines["bottom"].set_color("#1e1e3a")
    ax.set_xlim(0, max(df["Importance"]) * 1.25)

    st.markdown(
        '<div class="feature-importance-container">',
        unsafe_allow_html=True,
    )
    st.pyplot(fig, width='stretch')
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)


def render_prediction_history():
    if not st.session_state.get("prediction_history"):
        return

    history = st.session_state.prediction_history[:10]
    st.markdown(
        '<h2 class="section-title">⭐ Prediction History</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-subtitle">Last 10 predictions made.</p>',
        unsafe_allow_html=True,
    )

    cols = st.columns([2, 1.5, 1.5, 1.2, 1.2, 0.8])
    headers = ["Date", "Warehouse", "Shipment Mode", "Prediction", "Delay Prob", ""]
    for col, header in zip(cols, headers):
        col.markdown(
            f"<div style='font-size:0.65rem;font-weight:600;color:#606080;"
            f"text-transform:uppercase;letter-spacing:0.06em;padding:0.4rem 0.5rem;'>"
            f"{header}</div>",
            unsafe_allow_html=True,
        )

    for i, record in enumerate(history):
        pred = record["Prediction"]
        is_delayed = pred == "Delayed"
        icon = "🚨" if is_delayed else "✅"
        color = "#ef4444" if is_delayed else "#22c55e"

        vals = [
            record["Date"],
            f"Block {record['Warehouse']}",
            record["Shipment Mode"],
            pred,
            record["Probability"],
            icon,
        ]
        bg = "#111122" if i % 2 == 0 else "#0c0c18"
        for col, val in zip(cols, vals):
            style = (
                f"font-size:0.78rem;color:{color};font-weight:600;padding:0.4rem 0.5rem;"
                if val in ("Delayed", "On Time") and col == cols[3]
                else f"font-size:0.78rem;color:#9090b0;padding:0.4rem 0.5rem;"
            )
            col.markdown(
                f"<div style='background:{bg};border-radius:4px;{style}'>{val}</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)


def render_about():
    st.markdown(
        '<h2 class="section-title">ℹ️ About Project</h2>',
        unsafe_allow_html=True,
    )

    features_list = [
        ("🏭", "Warehouse Block"),
        ("🚚", "Mode of Shipment"),
        ("📊", "Product Importance"),
        ("👤", "Customer Gender"),
        ("📞", "Customer Care Calls"),
        ("⭐", "Customer Rating"),
        ("💰", "Cost of Product"),
        ("🛒", "Prior Purchases"),
        ("🎁", "Discount Offered"),
        ("⚖️", "Weight in Grams"),
    ]

    tech_tags = ["Python", "Streamlit", "scikit-learn", "XGBoost", "Pandas", "Matplotlib"]

    left_col, right_col = st.columns([3, 2])

    with left_col:
        st.markdown(
            '<div class="about-section">',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="about-header">
                <div class="about-icon">📦</div>
                <div class="about-title">ShipmentSure AI</div>
            </div>
            <div class="about-description">
                ShipmentSure is an AI-powered logistics analytics platform that predicts
                shipment delays using machine learning. By analyzing historical shipment
                data and key logistics factors, the system provides real-time predictions
                to help logistics teams make proactive decisions and improve delivery
                performance.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='font-size:0.8rem;font-weight:600;color:#9090b0;margin-bottom:0.5rem;'>"
            "Input Features</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="about-grid">',
            unsafe_allow_html=True,
        )
        for icon, name in features_list:
            st.markdown(
                f'<div class="about-feature">'
                f'<span class="about-feature-icon">{icon}</span>'
                f"<span>{name}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown(
            '<div class="about-section">',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="about-header">
                <div class="about-icon">🛠️</div>
                <div class="about-title">Technology Stack</div>
            </div>
            <div class="about-description">
                Built with modern Python data science tools and deployed as an
                interactive web application.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="about-tech-stack">',
            unsafe_allow_html=True,
        )
        for tag in tech_tags:
            st.markdown(
                f'<span class="about-tech-tag">{tag}</span>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


def render_footer():
    st.markdown(
        """
        <div class="footer">
            <div class="footer-brand">
                <span>ShipmentSure</span>
            </div>
            <div class="footer-text">
                ShipmentSure &copy; 2026
            </div>
            <div class="footer-subtext">
                Built using Streamlit, XGBoost and Scikit-Learn
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
