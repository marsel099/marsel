import streamlit as st
from core import Blockchain

st.set_page_config(page_title="Blockchain Ezplorer", page_icon="🔗", layout="wide")

st.title(" 🍵Blockchain for Halal Supply chain")

# Mebuat session state untuk menyimpan transaksi
if 'my_blockchain' not in st.session_state:
    st.session_state['my_blockchain'] = Blockchain()

# Membuat sidebar inputan
st.sidebar.header("➕Tambah data")
petani = st.sidebar.text_input("Nama Petani/Aktor:")
jumlah_kopi = st.sidebar.number_input("Jumlah Kopi(Kg):", min_value=0, step=1)
lokasi = st.sidebar.text_input("Lokasi:")

if st.sidebar.button("Tambah Data"):
    if petani and lokasi and jumlah_kopi > 0:
        data_transaksi = f"Petani: {petani}, Jumlah Kopi: {jumlah_kopi} Kg, Lokasi: {lokasi}"
        st.session_state['my_blockchain'].add_block(data_transaksi)
        st.success("Data berhasil ditambahkan!")
    else:
        st.warning("Semua field harus diisi dan jumlah kopi harus lebih besar dari 0.")

st.subheader("Blockchain Ledger / Buku besar")

is_valid = st.session_state['my_blockchain'].is_chain_valid()
if is_valid:
    st.success("✅Blockchain valid!")
else:
    st.error(" ❌Blockchain tidak valid! (rantai dimanipulasi)")

for block in st.session_state.my_blockchain.chain:
    with st.expander(f"Block # {block.index} | Hash: {block.hash}"):
        col1, col2 = st.columns(2)

        with col1:
            st.write("Data Payload")
            st.info(block.data)
            st.write(f"Timestamp: {block.timestamp_readable}")

        with col2:
            st.write("Kriptografi")
            st.write(f"Hash saat ini")
            st.write(block.hash)
            st.write(f"Hash sebelumnya")
            st.write(block.previous_hash)