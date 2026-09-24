import streamlit as st
# Pembuatan title halaman
st.set_page_config(page_title="CV App", page_icon="🎓", layout="wide")

# Pembuatan sidebar
st.sidebar.title("⚙️Pengaturan Profile")
st.sidebar.write("Masukan data diri anda di bawah ini:")

# Komponen Inputan 
nama = st.sidebar.text_input("Nama:", "")
nim = st.sidebar.text_input("NIM:", "")
jurusan = st.sidebar.text_input("Jurusan:", "")

deskripsi = st.sidebar.text_area("Deskripsi:", "")

# Area Utama
st.title("Curiculum Vitae")
st.markdown("--------------")

kolom_kiri, kolom_kanan = st.columns([1, 2])
with kolom_kiri:
    st.header(nama)
    st.image("foto.jpeg", width=150)
    st.markdown(f"{jurusan} | NIM: {nim}  ")

with kolom_kanan:
    st.write(f"🙌 Tentang saya:{deskripsi}")



