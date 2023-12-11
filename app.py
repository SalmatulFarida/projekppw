# generate_label.py
import joblib

def get_label(news_text):
    try:
        # Pastikan path file model benar
        model_path = 'model/svm_model'
        model = joblib.load(model_path)
        # ...
        # Proses klasifikasi dan pengembalian label
        # ...
        return label
    except FileNotFoundError as e:
        # Tangani kesalahan file tidak ditemukan
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Tangani kesalahan umum
        print(f"Error: {e}")
        return None
# main.py
import streamlit as st
from generate_label import get_label

def main():
    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita AntaraNews", page_icon="📺")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("News Classification: Aplikasi Kategori Berita Online (AntaraNews)")
        st.caption("Berita online akan dikategorikan menjadi beberapa kategori seperti hukum, hiburan, lifestyle. Dengan melakukan klasifikasi pada berita, kita dapat mengetahui kategori berita online yang sesuai.")

    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            result_placeholder = st.empty()  # Placeholder untuk hasil klasifikasi
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                if text:
                    result_placeholder.write(f'Berita yang Anda masukkan termasuk dalam kategori: {text}')
                    url = ""

                    if text == "hukum":
                        st.info(text, icon="🧑‍🏫")
                        url = "https://www.antaranews.com/search?q=hukum+hari+ini"
                    elif text == "hiburan":
                        st.info(text, icon="🚣")
                        url = "https://www.antaranews.com/search?q=hiburan+hari+ini"
                    elif text == "lifestyle":
                        st.info(text, icon="💸")
                        url = "https://www.antaranews.com/search?q=lifestyle+hari+ini"

                    st.write(f'Baca juga berita terbaru terkait {text} 🔎 [Berita {text} hari ini]({url})')
                else:
                    st.warning('Klasifikasi tidak berhasil. Silakan coba lagi atau periksa teks berita Anda.')
        else:
            st.warning('Masukkan teks terlebih dahulu')

if __name__ == "__main__":
    main()
