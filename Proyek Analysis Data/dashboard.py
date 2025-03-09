import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

# Load Data
def load_data():
    # Dapatkan path absolut berdasarkan lokasi file script
    file_path = os.path.join(os.path.dirname(__file__), "all_data.csv")
    df = pd.read_csv(file_path)
    df = df.loc[:, ~df.columns.duplicated()]
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

# Memanggil fungsi untuk load data
df = load_data()  
min_date = df["dteday"].min()  
max_date = df["dteday"].max()  

with st.sidebar:
    # Menambahkan logo perusahaan 
    st.image(os.path.abspath("logo bike rental.jpg"))

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Sidebar Filters
st.sidebar.header("Filter")
season = st.sidebar.selectbox("Pilih Musim:", df['season_x'].unique())
weather = st.sidebar.selectbox("Pilih Cuaca:", df['weathersit_x'].unique())
# day_of_week = st.sidebar.selectbox("Pilih Hari:", df['weekday_x'].unique())

# Filter Data
df_filtered = df[(df['season_x'] == season) & (df['weathersit_x'] == weather)]

total_rides = df_filtered['cnt_x'].sum()
st.metric(label="Total Peminjaman Sepeda", value=total_rides)
st.write("Hasil peningkatan penyewaan sepeda bisa dilihat dari filter yang dipilih")

# Menghitung rata-rata penyewaan sepeda berdasarkan cuaca dan musim 
weather_avg = df.groupby("weathersit_x")["cnt_x"].mean()
season_avg = df.groupby("season_x")["cnt_x"].mean()

# Visualisasi penyewaan sepeda berdasarkan musim
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_avg.index, y=season_avg.values, palette="coolwarm", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim", fontsize=14)
ax.set_xlabel("Musim", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Kesimpulan 
st.write("Berdasarkan visualisasi di atas, dapat dilihat grafik ini menunjukkan bahwa permintaan penyewaan sepeda tertinggi terjadi di musim gugur, diikuti oleh musim panas dan musim dingin, sedangkan musim semi memiliki permintaan terendah.")

# Visualisasi penyewaan sepeda berdasarkan cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_avg.index, y=weather_avg.values, palette="viridis", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca", fontsize=14)
ax.set_xlabel("Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Kesimpulan
st.write("Berdasarkan visualisasi di atas, dapat dilihat grafik ini menunjukkan bahwa penyewaan sepeda paling tinggi saat cuaca cerah, diikuti oleh cuaca berawan, sementara penyewaan menurun drastis saat hujan.")

# Visualisasi penyewaan sepeda berdasarkan JAM
hour_avg = df.groupby("hr")["cnt_x"].mean()
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hour_avg.index, y=hour_avg.values, marker="o", color="blue", ax=ax)
ax.set_xticks(range(0, 24))
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam", fontsize=14)
ax.set_xlabel("Jam", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Kesimpulan
st.write("Berdasarkan visualisasi di atas, dapat dilihat grafik ini menunjukkan bahwa penyewaan sepeda memuncak pada pukul 08.00 dan 17.00-18.00, yang kemungkinan besar terjadi saat jam sibuk berangkat dan pulang kerja. Sementara itu, pada dini hari (00.00-05.00), jumlah penyewaan sangat rendah.")

# Visualisasi penyewaan sepeda berdasarkan HARI dalam seminggu
day_avg = df.groupby("weekday_x")["cnt_x"].mean()
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Hari")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=day_avg.index, y=day_avg.values, palette="muted", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Hari", fontsize=14)
ax.set_xlabel("Hari dalam Minggu", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Kesimpulan
st.write("Berdasarkan visualisasi di atas, dapat dilihat grafik ini menunjukkan bahwa Penyewaan sepeda cenderung stabil sepanjang minggu, dengan sedikit peningkatan pada hari Jumat dan Sabtu.")


#ANALISIS LANJUTAN
# Rule-Based Clustering
def categorize_hour(hour):
    if 7 <= hour <= 9:
        return "Morning Hour"
    elif 10 <= hour <= 15:
        return "Regular Hours"
    elif 16 <= hour <= 21:
        return "Evening Hour"
    else:
        return "Off-Peak Hours"

df['time_category'] = df['hr'].apply(categorize_hour)

time_avg = df.groupby("time_category")["cnt_x"].mean().sort_values(ascending=False)

# Menampilkan hasil dalam metric cards
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Kategori Waktu")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Evening Hour", value=f"{time_avg['Evening Hour']:.1f}")
col2.metric(label="Morning Hour", value=f"{time_avg['Morning Hour']:.1f}")
col3.metric(label="Regular Hours", value=f"{time_avg['Regular Hours']:.1f}")
col4.metric(label="Off-Peak Hours", value=f"{time_avg['Off-Peak Hours']:.1f}")
