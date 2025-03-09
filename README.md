# Bike Sharing Data Analysis & Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset peminjaman sepeda (Bike Sharing Dataset) dan menyajikan dashboard interaktif menggunakan **Streamlit**. Dashboard ini memungkinkan pengguna untuk mengeksplorasi pola peminjaman sepeda berdasarkan berbagai variabel seperti cuaca, musim, jam, dan hari dalam seminggu.

## Struktur Proyek
```
|-- Proyek Analysis Data/
|   |-- dashboard.py         # File utama untuk menjalankan dashboard Streamlit
|   |-- all_data.csv         # Dataset peminjaman sepeda
|
|-- Bike sharing dataset/
|   |-- README.md            # Dokumentasi dataset
|   |-- day.csv              # Dataset dari tabel day
|   |-- hour.csv             # Dataset dari tabel hour
|
|-- notebook.ipynb           # Analisis eksploratif dalam Jupyter Notebook
|-- requirements.txt         # Daftar library yang dibutuhkan
|-- README.md                # Dokumentasi proyek
|-- url.txt                  # link streamlit
```

## Instalasi dan Menjalankan Program
### **1. Clone Repository**
Jalankan perintah berikut di terminal:
```bash
git clone https://github.com/aauliadwi/proyek-analysis-data.git
cd proyek-analysis-data
```
### **2. Setup Environment - Anaconda**
```bash
conda create --name dashboard-ds python=3.13.2
conda activate dashboard-ds
pip install -r requirements.txt
```
### **3. Setup Environment - Shell/Terminal**
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
### **4. Jalankan Dashboard Streamlit**
```bash
streamlit run dashboard.py
```
Dashboard akan terbuka di browser secara otomatis.

## Deployment
Dashboard ini dapat dideploy menggunakan **Streamlit Community Cloud**.

### **Deploy dengan Streamlit Community Cloud**
1. **Upload proyek ke GitHub**.
2. **Buka** [Streamlit Community Cloud](https://share.streamlit.io/).
3. **Hubungkan dengan repository GitHub**.
4. **Pilih file `dashboard.py` sebagai entry point**.
5. **Klik deploy**.

Setelah deployment berhasil, kamu akan mendapatkan link dashboard yang bisa dibagikan.

## Dataset
Dataset yang digunakan berasal dari Bike Sharing Dataset dan telah diproses untuk keperluan analisis dan visualisasi.

