# Bike Sharing Data Analysis & Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset peminjaman sepeda (Bike Sharing Dataset) dan menyajikan dashboard interaktif menggunakan **Streamlit**. Dashboard ini memungkinkan pengguna untuk mengeksplorasi pola peminjaman sepeda berdasarkan berbagai variabel seperti cuaca, musim, jam, dan hari dalam seminggu.

## Struktur Proyek
```
|-- dashboard/
|   |-- dashboard.py         # File utama untuk menjalankan dashboard Streamlit
|   |-- all_data.csv         # Dataset peminjaman sepeda
|
|-- data/
|   |-- README.md            # Dokumentasi dataset
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
git clone https://github.com/username/repo-name.git
cd repo-name
```

### **2. Install Dependencies**
Gunakan perintah berikut untuk menginstal library yang diperlukan:
```bash
pip install -r requirements.txt
```

### **3. Jalankan Dashboard Streamlit**
Untuk menjalankan dashboard, gunakan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
```
Dashboard akan terbuka di browser secara otomatis.

## Fitur Dashboard
- **Filter Data**: Pengguna dapat memfilter data berdasarkan musim, cuaca, jam, dan hari dalam seminggu.
- **Visualisasi Data**: Grafik interaktif untuk menampilkan pola peminjaman sepeda berdasarkan berbagai variabel.
- **Statistik Utama**: Menampilkan total peminjaman dan rata-rata peminjaman berdasarkan kategori waktu.

## Deployment
Dashboard ini dapat dideploy menggunakan **Streamlit Community Cloud** atau platform lain seperti **Render** dan **Heroku**.

### **Deploy dengan Streamlit Community Cloud**
1. **Upload proyek ke GitHub**.
2. **Buka** [Streamlit Community Cloud](https://share.streamlit.io/).
3. **Hubungkan dengan repository GitHub**.
4. **Pilih file `dashboard.py` sebagai entry point**.
5. **Klik deploy**.

Setelah deployment berhasil, kamu akan mendapatkan link dashboard yang bisa dibagikan.

## Dataset
Dataset yang digunakan berasal dari Bike Sharing Dataset dan telah diproses untuk keperluan analisis dan visualisasi.

