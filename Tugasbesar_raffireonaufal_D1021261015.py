import streamlit as st

# Judul aplikasi
st.title("Aplikasi Biaya Laundry Kiloan")
st.write("Program Menghitung Biaya Laundry Berdasarkan NIM")

col1, col2 = st.columns([3, 1])

with col2:
    st.image(".devcontainer/miku_chibi.png", width=180)

if "nim" not in st.session_state:
    st.session_state.nim = ""

if "nim" not in st.session_state:
    st.session_state.nim = ""

if "berat" not in st.session_state:
    st.session_state.berat = 1

if "hasil" not in st.session_state:
    st.session_state.hasil = None

def reset_data():
    st.session_state.nim = ""
    st.session_state.berat = 1
    st.session_state.hasil = None

st.subheader("Data Pelanggan")

nim = st.text_input(
    "Masukkan NIM (10 digit angka)",
    key="nim"
)

berat = st.number_input(
    "Berat Cucian (kg)",
    min_value=0,
    step=1,
    key="berat"
)

col1, col2 = st.columns(2)

with col1:
    tombol_hitung = st.button("Hitung Biaya", use_container_width=True)

with col2:
    st.button(
        "Reset",
        on_click=reset_data,
        use_container_width=True
    )


if tombol_hitung:

    if len(nim) != 10 or not nim.isdigit():
        st.session_state.hasil = None
        st.error("NIM harus terdiri dari tepat 10 digit angka!")

    elif berat <= 0:
        st.session_state.hasil = None
        st.error("Berat cucian harus lebih dari 0 kg!")

    else:

        digit_terakhir = int(nim[-1])

        tarif = 5000 + (digit_terakhir * 500)

        jumlah_genap = 0

        for angka in nim:
            if int(angka) % 2 == 0:
                jumlah_genap = jumlah_genap + 1

        diskon = jumlah_genap * 1
 
        biaya_normal = berat * tarif

        potongan = biaya_normal * diskon / 100

        total_bayar = biaya_normal - potongan

        st.session_state.hasil = {
            "tarif": tarif,
            "jumlah_genap": jumlah_genap,
            "diskon": diskon,
            "biaya_normal": biaya_normal,
            "potongan": potongan,
            "total_bayar": total_bayar
        }


    hasil = st.session_state.hasil

    st.divider()
    st.subheader("Hasil Perhitungan")

    # Menampilkan informasi
    st.write("NIM:", nim)
    st.write("Berat Cucian:", berat, "kg")
    st.write("Tarif per kg: Rp", f"{hasil['tarif']:,.0f}".replace(",", "."))
    st.write("Jumlah Digit Genap:", hasil["jumlah_genap"])
    st.write("Diskon:", hasil["diskon"], "%")

    st.divider()

    # Menampilkan biaya
    st.write(
        "Biaya Normal: Rp",
        f"{hasil['biaya_normal']:,.0f}".replace(",", ".")
    )
                                          
    st.write(
        "Potongan Harga: Rp",
        f"{hasil['potongan']:,.0f}".replace(",", ".")
    )

    st.success(
        "Total Bayar: Rp "
        + f"{hasil['total_bayar']:,.0f}".replace(",", ".")
    )
