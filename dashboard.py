import streamlit as st
import sqlite3
import pandas as pd

from main import process_complaint

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="AI Civic Command Center",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (UI Styling)
# -----------------------------

st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.metric-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

.big-title {
    font-size:40px;
    font-weight:bold;
}

.section {
    background-color:#1e293b;
    padding:20px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATABASE
# -----------------------------

conn = sqlite3.connect("complaints.db")

data = pd.read_sql("SELECT * FROM complaints", conn)

# -----------------------------
# TITLE
# -----------------------------

st.markdown(
    "<div class='big-title'>🚨 AI Civic Command Center</div>",
    unsafe_allow_html=True
)

st.write("AI-powered civic complaint intelligence platform")

st.divider()

# -----------------------------
# COMPLAINT INPUT
# -----------------------------

st.subheader("📞 Register Complaint")

with st.container():

    complaint = st.text_input(
        "Describe the issue",
        placeholder="Example: Garbage everywhere in sector 9"
    )

    if st.button("Submit Complaint"):

        if complaint != "":

            issue, location, priority, department = process_complaint(complaint)

            st.success("Complaint Registered")

            col1, col2, col3, col4 = st.columns(4)

            col1.info(f"Issue: {issue}")
            col2.info(f"Location: {location}")
            col3.info(f"Priority: {priority}")
            col4.info(f"Department: {department}")

st.divider()

# -----------------------------
# METRICS
# -----------------------------

st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

total = len(data)

critical = 0
departments = 0

if len(data) > 0:

    critical = len(data[data["priority"] == "Critical"])

    departments = data["department"].nunique()

col1.metric("Total Complaints", total)

col2.metric("Critical Alerts", critical)

col3.metric("Departments Active", departments)

st.divider()

# -----------------------------
# CHARTS
# -----------------------------

col4, col5 = st.columns(2)

if len(data) > 0:

    with col4:

        st.subheader("Issue Distribution")

        st.bar_chart(data["issue_type"].value_counts())

    with col5:

        st.subheader("Priority Distribution")

        st.bar_chart(data["priority"].value_counts())

st.divider()

# -----------------------------
# ALERT SECTION
# -----------------------------

st.subheader("🚨 Critical Alerts")

if len(data) > 0:

    critical_cases = data[data["priority"] == "Critical"]

    if len(critical_cases) > 0:

        st.warning("Critical complaints detected!")

        st.dataframe(critical_cases)

    else:

        st.success("No critical emergencies")

st.divider()

# -----------------------------
# DATABASE TABLE
# -----------------------------

st.subheader("📋 Complaint Database")

st.dataframe(data, use_container_width=True)