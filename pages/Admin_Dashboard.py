import streamlit as st
import sqlite3
import pandas as pd

DB_NAME = "healthcare.db"

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Admin Dashboard")

# ---------------- AUTH GUARD ----------------
if "user" not in st.session_state or not st.session_state.user.get("is_admin"):
    st.error("⛔ Access denied. Admins only.")
    st.stop()

# ---------------- DB CONNECTION ----------------
conn = sqlite3.connect(DB_NAME)

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(
    ["👨‍⚕️ Manage Doctors", "📅 View Appointments", "👥 Manage Users"]
)

# =====================================================
# 👨‍⚕️ DOCTORS TAB
# =====================================================
with tab1:
    st.subheader("Doctors List")

    doctors_df = pd.read_sql_query("""
        SELECT
            name AS Doctor,
            specialty AS Specialty,
            hospital AS Hospital,
            location AS Location,
            working_days AS Working_Days,
            timings AS Timings
        FROM doctors
        ORDER BY name
    """, conn)

    # ✅ REMOVE DUPLICATES + FIX SERIAL NUMBERS
    doctors_df = doctors_df.drop_duplicates(subset=["Doctor"]).reset_index(drop=True)

    st.dataframe(doctors_df, use_container_width=True)

# =====================================================
# 📅 APPOINTMENTS TAB
# =====================================================
with tab2:
    st.subheader("All Appointments")

    appointments_df = pd.read_sql_query("""
        SELECT
            u.username AS patient_name,
            d.name AS doctor_name,
            a.appointment_datetime,
            a.status
        FROM appointments a
        JOIN users u ON a.user_id = u.id
        JOIN doctors d ON a.doctor_id = d.id
        ORDER BY a.appointment_datetime DESC
    """, conn)

    if appointments_df.empty:
        st.info("No appointments found.")
    else:
        st.dataframe(appointments_df, use_container_width=True)

# =====================================================
# 👥 USERS TAB
# =====================================================
with tab3:
    st.subheader("Users")

    users_df = pd.read_sql_query("""
        SELECT
            id,
            username,
            CASE
                WHEN is_admin = 1 THEN 'Admin'
                ELSE 'User'
            END AS role
        FROM users
        ORDER BY id
    """, conn)

    st.dataframe(users_df, use_container_width=True)

# ---------------- CLOSE DB ----------------
conn.close()
