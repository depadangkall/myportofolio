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

### Tugas 3
1. Saya pakai `ModelForm` karena fieldnya otomatis kebuat dari model, jadi saya gak perlu nulis satu satu tag `<input>` dan validasinya juga ikut model, gak perlu dicek manual lagi. Kalau field di model berubah, formnya otomatis nyesuain. `{% csrf_token %}` wajib ada biar form saya gak bisa disalahgunain website lain buat ngirim request atas nama saya diam diam token ini yang jadi bukti kalau request-nya beneran dari form saya sendiri.

2. JSON lebih ringkas dari XML karena gak perlu closing tag di tiap elemen, jadi lebih kecil dan lebih cepat diproses. Formatnya juga udah mirip struktur object/array JavaScript, jadi gampang langsung dipakai di frontend tanpa parsing ribet, dan hampir semua bahasa pemrograman udah support baca/tulis JSON.

3. Waktu ada request ke `/api/education/`, viewnya ambil data dari database (`Education.objects.all()`), hasilnya berupa objek Python, bukan teks. Karena HTTP cuma bisa kirim teks, saya perlu ubah dulu objek itu jadi string JSON lewat `serializers.serialize` (serialization) sebelum dikirim sebagai response. Buat nampilin lagi di halaman Django, saya baca balik JSON-nya pakai `serializers.deserialize` biar jadi objek Python lagi yang bisa dipakai di template.

### AI Disclosure
Saya minta bantuan Claude Code dalam merancang fitur Create, Update, Delete, dan JSON data delivery untuk bagian Education, mulai dari struktur `EducationForm` di `forms.py`, alur fungsi-fungsi view di `views.py`, routing di `urls.py`, sampai template form dan modal delete-nya, dengan mengikuti pola yang sudah ada di bagian Experience. Selain itu saya juga minta saran soal tampilan, seperti ukuran tombol Edit/Delete di halaman Education biar gak kebesaran. Setelah itu saya cek ulang hasilnya dengan jalanin `python manage.py check` dan `runserver`, buka tiap halaman (list, form create, form update, tombol delete) satu-satu, serta cek endpoint `/api/education/` buat mastiin datanya beneran muncul dalam format JSON dan gak ada error.

### Tugas 4

### AI Disclosure
Saya minta bantuan Claude Code untuk membaca PDF Tutorial 04 dan menjelaskan langkah-langkahnya step by step, lalu menyesuaikannya ke proyek saya karena tutorialnya pakai model `Project` sedangkan proyek saya pakai `Experience`. Setelah itu saya juga minta bantuan dalam membuat pembatasan akses di bagian Education, mulai dari `@login_required` dan pengecekan superuser di `views.py`, peran Editor lewat Django Group dan permission `change_education` yang cuma boleh edit data, sampai nyembunyiin tombol Add/Edit/Delete di template sesuai peran. Selain itu saya minta bantuan untuk nerjemahin teks halaman login, register, dan profil ke bahasa Inggris, ngehapus security key karena udah digantiin sistem login, ngatur `DEBUG` biar mati di PWS, benerin warning `DEFAULT_AUTO_FIELD` dari feedback Tugas 2, dan minta saran pembagian commit, branch, serta cara deploy ke PWS. Setelah itu saya cek ulang hasilnya dengan jalanin `python manage.py check` dan `runserver`, bikin grup Editor dan akun lewat Django Admin, lalu nyoba login pakai akun user biasa, editor, dan superuser satu-satu buat mastiin tombol dan aksesnya sesuai, serta cek cookie `last_login` dan endpoint `/api/experience/` buat mastiin datanya muncul dan gak ada error.

### Tugas 5

1. Debouncing itu cara buat nunda sebuah fungsi sampai user berhenti ngelakuin sesuatu selama beberapa saat. Di halaman Skills, pencarian langsung jalan waktu saya ngetik. Masalahnya, kalau setiap huruf langsung ngirim request, ngetik "JavaScript" aja udah 10 request ke server, padahal yang saya butuhin cuma hasil akhirnya. Jadi saya pakai debouncing: tiap ada huruf baru, timer-nya diulang lagi dari awal, dan request baru dikirim kalau saya udah berhenti ngetik sekitar 300 milidetik. Hasilnya cukup satu request aja, server gak kerja percuma, dan hasil pencarian lama gak nimpa hasil yang baru.

2. `fetch()` itu gak langsung ngasih data, dia ngasih `Promise` dulu, semacam "janji" kalau datanya bakal datang nanti. `await` gunanya buat nunggu janji itu selesai, jadi baris di bawahnya baru jalan setelah balasan dari server beneran sampai. Kalau gak pakai `await`, kodenya bakal jalan duluan padahal datanya belum ada. Misalnya `response.ok` jadi `undefined` dan `response.json()` malah error, jadi daftar skill saya bakal kosong atau langsung masuk ke tampilan error.

3. XSS itu serangan di mana orang nyisipin kode JavaScript ke dalam data, terus kode itu ikut kejalan di browser orang lain yang buka halaman tersebut. Contohnya kalau ada yang nambahin skill dengan nama `<img src="x" onerror="alert('XSS!')">`. Kalau datanya ditampilin lewat template Django, ini aman karena Django otomatis ngubah `<` dan `>` jadi teks biasa. Tapi kalau lewat AJAX, datanya saya masukin ke halaman pakai `innerHTML`, dan di situ gak ada yang ngebersihin, jadi browser bakal nganggap tag itu sebagai HTML beneran dan kodenya kejalan. Makanya semua data saya lewatin `escapeHtml` dulu sebelum ditampilin, dan di server inputnya juga saya bersihin pakai `strip_tags`.

### AI Disclosure
Di tugas ini saya bikin bagian baru, yaitu Skills, yang saya bagi jadi Hard Skills dan Soft Skills, plus logo yang boleh diisi khusus buat hard skill. Saya dibantu Claude Code buat ngerti materi Tutorial 05 dan nerapin polanya ke Skills, mulai dari model, form, data JSON, pembatasan akses tiap role, sampai halaman yang datanya dimuat pakai `fetch()`. Claude Code juga bantu di bagian pencarian dengan debouncing, modal buat nambah skill, notifikasi toast, dan perlindungan XSS, sekalian ngasih saran buat naruh fungsi `getCookie` sama `escapeHtml` di satu file biar bisa dipakai bareng. Beberapa hal saya putusin sendiri, kayak ngehapus star di Education karena menurut saya kurang cocok, bikin pembagian Hard Skills dan Soft Skills, sama nyembunyiin kolom logo kalau yang dipilih soft skill. Setelah itu saya cek sendiri hasilnya: jalanin test dan `runserver`, nambahin permission "Can change skill" ke grup Editor di Django Admin, terus nyoba halaman Skills pakai akun pengunjung, user biasa, editor, dan superuser. Saya juga nyoba nambah skill, nyari, filter, kasih star, dan nyoba masukin `<img src="x" onerror="alert('XSS!')">` buat mastiin alert-nya gak muncul.
