# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIG HALAMAN ---
st.set_page_config(
    page_title="🍓 Cute Profitability Dashboard",
    page_icon="🍰",
    layout="wide"
)

# --- CSS AESTHETIC ---
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #5e2a5e;
    }
    .title {
        text-align: center;
        font-size: 50px;
        color: #ff69b4;
    }
    .stButton>button {
        background-color: #ffb6c1;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ff69b4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1 class='title'>🍓 Menu Profitability Dashboard 🍓</h1>", unsafe_allow_html=True)
st.write("Halo bestie! 💖 Yuk kita lihat data menu restoran yang paling cuan ✨")

# --- UPLOAD FILE ---
uploaded_file = st.file_uploader("📂 Upload dataset CSV kamu", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Data Awal")
    st.dataframe(df.head())

    # --- HEATMAP CORRELATION ---
    st.subheader("💖 Korelasi Variabel")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(df.corr(), annot=True, cmap="pink", ax=ax)
    st.pyplot(fig)

    # --- PROFITABILITY COUNT ---
    st.subheader("🍰 Distribusi Profitability")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="Profitability", data=df, palette="pastel", ax=ax2)
    st.pyplot(fig2)

    # --- FILTER MENU ---
    st.subheader("🔍 Filter Berdasarkan Harga")
    min_price, max_price = st.slider(
        "Pilih range harga menu",
        float(df["Price"].min()),
        float(df["Price"].max()),
        (float(df["Price"].min()), float(df["Price"].max()))
    )
    filtered_df = df[(df["Price"] >= min_price) & (df["Price"] <= max_price)]
    st.dataframe(filtered_df)

    st.success("🎀 Data berhasil difilter! Lanjutkan eksplorasi 💖")

else:
    st.info("Silakan upload dataset CSV dulu ya bestie 🍓")

