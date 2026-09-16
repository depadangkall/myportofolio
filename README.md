Nama : I Gede Devadatta Arsha Darmaputra
NPM : 2506622481
Kelas : PBP A

### Tugas 1

1. Iya, saya pakai beberapa elemen semantik kayak `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`. Menurut saya ini membantu karena struktur halamannya jadi lebih jelas, bukan cuma numpuk `<div>` semua. Saya belum pakai `<article>` sama `<aside>` karena menurut saya belum terlalu kepakai untuk halaman sesederhana ini.

2. Tantangan yang saya temui itu foto-fotonya suka jadi gepeng/aneh pas layarnya diperbesar-kecilin. Awalnya saya kasih tinggi tetap ke gambarnya, eh ternyata itu penyebab masalahnya. Setelah coba-coba, saya pakai `aspect-ratio` biar bentuk fotonya tetap proporsional walau ukuran layar berubah-ubah. Untuk versi mobile, saya lihat dulu mana yang lebih penting buat dibaca, baru foto sama layout-nya saya sesuaikan ikutan mengecil/bertumpuk.

3. Karena masih static web, semua data (pengalaman, pendidikan, foto kegiatan) saya tulis manual langsung di HTML. Jadi kalau mau nambah atau ubah sesuatu, saya harus edit kodenya sendiri, belum ada cara yang lebih gampang. Form kontaknya juga belum beneran jalan, masih pakai link email biasa. Ke depannya saya pengen coba pakai database biar datanya bisa diatur lebih gampang tanpa harus bolak-balik edit HTML.

#dalam proses pengerjaan tugas ini saya menggunakan bantuan ai terutama pada css nya untuk membantu saya dalam menentukan dan memberi saran untuk warna, ukuran, dan tampilan dari website saya.

### Tugas 2

1. Jadi alurnya kira-kira gini: pas saya buka halaman Education, browser ngirim request ke URL `/education/`. Yang pertama nangkep itu `urls.py` punya proyek (`portofolio/urls.py`), tapi dia sendiri gak ngurusin, cuma nge-lempar ke `main.urls` pakai `include()`. Nah di `main/urls.py` punya aplikasi `main` inilah baru dicocokin path `education/`-nya ke fungsi view `show_education` di `views.py`. Fungsi ini yang kerja beneran: dia ambil semua data Education dari model lewat `Education.objects.all()`, masukin ke context, terus di-render ke template `education.html`. Template-nya tinggal loop pakai `{% for %}` buat nampilin satu-satu, hasil akhirnya (HTML jadi) itu yang dikirim balik ke browser dan muncul di layar saya.

2. Karena kalau ditulis langsung di HTML, tiap kali saya mau nambah atau ganti data pendidikan, saya harus bongkar file template-nya satu-satu. Ribet, dan gampang salah/kelupaan. Kalau datanya di model, saya cukup ubah sekali di database (lewat admin atau shell), terus otomatis kepakai di manapun data itu ditampilin. Jadi bagian "tampilan" sama "isi data" itu kepisah, bikin ke depannya lebih gampang di-maintain atau dikembangin lagi tanpa harus ngoprek HTML.

3. Bedanya, `makemigrations` itu cuma bikin "rencana" perubahan dalam bentuk file migrasi berdasarkan apa yang berubah di model, belum benar-benar nyentuh database-nya. Baru pas `migrate` dijalanin, perubahan itu beneran diterapin ke database. Contoh nyatanya pas saya bikin model `Education` (field `institution`, `thumbnail`, `start_year`, `end_year`), saya jalanin `makemigrations` dulu buat generate file migrasinya, baru habis itu `migrate` biar tabelnya beneran kebuat di database.

### AI Disclosure

Saya menggunakan bantuan Claude (Claude Code) untuk beberapa hal di tugas ini, seperti minta saran styling CSS untuk halaman Education dan bantuan debug pas field `thumbnail` gagal disave lewat Django admin.