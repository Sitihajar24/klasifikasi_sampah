import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('naive_bayes_sampah.pkl')

# Custom CSS untuk styling
st.markdown("""
    <style>
    .title {
        font-size: 50px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 30px;
        color: #333;
        text-align: center;
    }
    .description {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-top: -20px;
    }
    .container {
        text-align: center;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        font-size: 20px;
        border-radius: 5px;
        margin-top: 30px;
    }
    .header {
        text-align: center;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Halaman Depan: Judul, Deskripsi, dan Gambar
st.markdown('<div class="title">Sistem Klasifikasi Sampah Organik dan Non-Organik</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplikasi Pengelolaan Sampah Berdasarkan Klasifikasi</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Masukkan data sampah untuk mengetahui apakah itu organik atau non-organik. Sistem ini membantu memisahkan sampah untuk pengelolaan yang lebih baik, seperti pembuatan kompos dan daur ulang.</div>', unsafe_allow_html=True)

# Gambar ilustrasi
st.image("https://www.example.com/sampah_image.png", use_column_width=True)  # Ganti dengan link gambar sampah atau upload gambar lokal

# Button untuk menuju form input
st.markdown('<div class="container"><a href="#form" class="button">Mulai Prediksi Sampah</a></div>', unsafe_allow_html=True)

# Input form untuk prediksi (disembunyikan di bawah)
st.markdown('<div id="form"></div>', unsafe_allow_html=True)

# Form Input
st.title('Klasifikasi Sampah: Organik atau Non-Organik')

# Input user
keterangan = st.text_input('Keterangan Sampah (misal: Kulit Pisang)')
bentuk = st.selectbox('Bentuk', ['Bulat', 'Pipih', 'Tak Beraturan', 'Silinder'])
tekstur = st.selectbox('Tekstur', ['Kasar', 'Halus', 'Berlendir', 'Keras'])
warna = st.selectbox('Warna Dominan', ['Coklat', 'Hijau', 'Putih', 'Hitam', 'Abu-Abu', 'Merah', 'Kuning'])
kondisi = st.selectbox('Kondisi', ['Basah', 'Kering'])
berat = st.slider('Berat Sampah (gram)', 1, 5000, 100)
sumber = st.selectbox('Sumber', ['Rumah Tangga', 'Pasar', 'Industri', 'Perkantoran', 'Sekolah'])
bahaya = st.selectbox('Tingkat Bahaya', ['Rendah', 'Sedang', 'Tinggi'])
pengolahan = st.selectbox('Pengolahan', ['Kompos', 'Daur Ulang', 'Kerajinan', 'Dibakar', 'Dibuang'])

# Button prediksi
if st.button('Prediksi'):
    # Preprocessing input user - HARUS encode sama seperti training
    input_data = {
        'Keterangan': 0,  # misal, abaikan karena keterangan teks
        'Bentuk': 0,
        'Tekstur': 0,
        'Warna Dominan': 0,
        'Kondisi': 0,
        'Berat (gram)': berat,
        'Sumber': 0,
        'Tingkat Bahaya': 0,
        'Pengolahan': 0,
    }
    
    # Manual encode sesuai model training
    bentuk_map = {'Bulat': 0, 'Pipih': 1, 'Tak Beraturan': 2, 'Silinder': 3}
    tekstur_map = {'Kasar': 0, 'Halus': 1, 'Berlendir': 2, 'Keras': 3}
    warna_map = {'Coklat': 0, 'Hijau': 1, 'Putih': 2, 'Hitam': 3, 'Abu-Abu': 4, 'Merah': 5, 'Kuning': 6}
    kondisi_map = {'Basah': 0, 'Kering': 1}
    sumber_map = {'Rumah Tangga': 0, 'Pasar': 1, 'Industri': 2, 'Perkantoran': 3, 'Sekolah': 4}
    bahaya_map = {'Rendah': 0, 'Sedang': 1, 'Tinggi': 2}
    pengolahan_map = {'Kompos': 0, 'Daur Ulang': 1, 'Kerajinan': 2, 'Dibakar': 3, 'Dibuang': 4}
    
    input_data['Bentuk'] = bentuk_map[bentuk]
    input_data['Tekstur'] = tekstur_map[tekstur]
    input_data['Warna Dominan'] = warna_map[warna]
    input_data['Kondisi'] = kondisi_map[kondisi]
    input_data['Sumber'] = sumber_map[sumber]
    input_data['Tingkat Bahaya'] = bahaya_map[bahaya]
    input_data['Pengolahan'] = pengolahan_map[pengolahan]
    
    # Konversi ke DataFrame 1 baris
    input_df = pd.DataFrame([input_data])
    
    # Prediksi
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.success('Prediksi: SAMPAH ORGANIK 🍃')
    else:
        st.success('Prediksi: SAMPAH NON-ORGANIK 🛠️')
