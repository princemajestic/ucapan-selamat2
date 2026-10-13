import streamlit as str
import streamlit.components.v1 as components

# Mengatur judul halaman web
str.set_page_config(page_title="Pesan Semangat", page_icon="✨")

str.title("✨ Kotak Semangat untukmu ✨")
str.write("Tulis namamu di bawah ini untuk mengambil energi positif hari ini!")

# Menu input nama
nama = str.text_input("Masukkan nama Anda:", placeholder="Ketik nama di sini...")

# Ketika pembaca mulai memasukkan nama, musik tersembunyi akan dipicu untuk berputar
if nama:
    str.markdown("---")
    str.success(f"### Halo {nama}, tetap semangat ya menjalani hari ini!")
    str.info("💡 **Ingat:** Jangan menyerah, setiap langkah kecil membawamu lebih dekat ke impianmu!")
    str.markdown("---")
    link_mp3 = "https://jumpshare.com/s/em1fj9sBQq4dWDTbrSML"
    
    komponen_audio = f"""
    <audio id="bg-audio" src="{link_mp3}" loop></audio>
    <script>
        var audio = document.getElementById("bg-audio");
        audio.volume = 0.5; // Mengatur volume (0.0 sampai 1.0)
        
        // Memaksa browser memutar audio setelah interaksi input nama selesai
        audio.play().catch(function(error) {{
            console.log("Autoplay diblokir oleh browser, butuh klik manual tambahan.");
        }});
    </script>
    """

    components.html(komponen_audio, height=0, width=0)
