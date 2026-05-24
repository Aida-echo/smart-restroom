import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Restroom Dashboard",
    page_icon="🚻",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("smart_restroom_data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()
latest = df.iloc[-1]

st.title("🚻 Smart Restroom Monitoring")
st.caption("Dashboard pemantauan kondisi toilet berbasis data sensor")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Suhu", f"{latest['suhu_c']} °C")
col2.metric("Kelembapan", f"{latest['kelembapan_pct']} %")
col3.metric("Amonia", f"{latest['amonia_ppm']} ppm")
col4.metric("Status", latest["status"])

st.divider()

# Status alert
if latest["status"] == "Aman":
    st.success("Kondisi toilet aman dan normal.")
elif latest["status"] == "Digunakan":
    st.info("Toilet sedang digunakan.")
else:
    st.warning("Kualitas udara perlu diperhatikan. Aktifkan ventilasi atau lakukan pengecekan.")

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Tren Suhu & Kelembapan")
    chart_df = df.set_index("timestamp")[["suhu_c", "kelembapan_pct"]]
    st.line_chart(chart_df)

with right:
    st.subheader("Tren Amonia")
    ammonia_df = df.set_index("timestamp")[["amonia_ppm"]]
    st.line_chart(ammonia_df)

st.subheader("Riwayat Data Sensor")

status_filter = st.multiselect(
    "Filter status",
    options=sorted(df["status"].unique()),
    default=sorted(df["status"].unique())
)

filtered_df = df[df["status"].isin(status_filter)]
st.dataframe(filtered_df, use_container_width=True)

st.caption("Catatan: Data ini menggunakan CSV lokal sebagai alternatif Firebase Realtime Database.")
