# Smart Restroom

Repositori ini berisi aplikasi Streamlit untuk monitoring smart restroom.

Langkah cepat untuk deploy ke Streamlit Cloud:

1. Buat repository di GitHub dan push seluruh folder (termasuk `app.py` dan `smart_restroom_data.csv`).

Contoh perintah (jalankan di folder proyek):

```bash
git init
git add .
git commit -m "Initial commit"
# jika pakai GitHub CLI: gh repo create <your-repo> --public --source=. --remote=origin --push
# atau buat repo di github.com lalu:
# git remote add origin git@github.com:yourusername/your-repo.git
git branch -M main
git push -u origin main
```

2. Deploy di Streamlit Cloud:

- Buka https://share.streamlit.io dan login dengan GitHub.
- Klik "New app" → pilih repository → branch `main` → file path `app.py` → Deploy.
- Setelah deploy selesai, klik link aplikasi untuk mengakses URL publik (contoh: `https://share.streamlit.io/username/repo/main`).

Catatan:
- Pastikan `requirements.txt` ada di repo (file ini sudah disertakan).
- Pastikan `smart_restroom_data.csv` juga ikut di-commit supaya aplikasi dapat membaca data lokal.

Jika mau, saya bisa menjalankan `git init` + commit lokal untuk Anda — beri tahu kalau mau saya jalankan.
