# OpenShop RESTful API

RESTful API sederhana untuk platform e-commerce OpenShop, dibangun sebagai
proyek akhir kelas **Belajar Back-End Pemula dengan Python** di Dicoding.
API ini menangani pengelolaan data produk: menambahkan, menampilkan,
mencari, mengubah, dan menghapus (soft delete) produk.

## ✨ Fitur

- **CRUD Produk** — Create, Read, Update, Delete data produk
- **Pencarian Produk** — filter berdasarkan nama dan lokasi
- **Soft Delete** — produk yang dihapus tidak benar-benar hilang dari database
- **HATEOAS** — setiap response menyertakan tautan aksi yang tersedia
- **Validasi Data** — menggunakan serializer Django REST Framework

## 🛠️ Tech Stack

- Python 3.10
- Django 4.2 (LTS)
- Django REST Framework
- SQLite (database default)
- Pipenv (dependency management)

## 📁 Struktur Proyek

\`\`\`
openshop-api-final/
├── openshop/          # Konfigurasi utama proyek Django
│   ├── settings.py
│   └── urls.py
├── products/          # App untuk resource produk
│   ├── models.py      # Definisi model Product
│   ├── serializers.py # Serializer + HATEOAS
│   ├── views.py       # Logic endpoint CRUD
│   └── urls.py        # Routing endpoint produk
├── manage.py
├── Pipfile
└── Pipfile.lock
\`\`\`

## 🚀 Cara Menjalankan

1. Clone repository ini
   \`\`\`bash
   git clone <url-repo-kamu>
   cd openshop-api-final
   \`\`\`

2. Install dependencies menggunakan pipenv
   \`\`\`bash
   pipenv install
   pipenv shell
   \`\`\`

3. Jalankan migrasi database
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

4. Jalankan server
   \`\`\`bash
   python manage.py runserver
   \`\`\`

   API akan berjalan di `http://127.0.0.1:8000/`

## 📌 Endpoint API

| Method | Endpoint              | Deskripsi                          |
|--------|-----------------------|-------------------------------------|
| POST   | `/products/`           | Menambahkan produk baru            |
| GET    | `/products/`           | Menampilkan semua produk           |
| GET    | `/products/?name=`     | Mencari produk berdasarkan nama    |
| GET    | `/products/?location=` | Mencari produk berdasarkan lokasi  |
| GET    | `/products/<id>/`      | Menampilkan detail satu produk     |
| PUT    | `/products/<id>/`      | Memperbarui data produk            |
| DELETE | `/products/<id>/`      | Menghapus produk (soft delete)     |

### Contoh Request — Menambahkan Produk

\`\`\`json
POST /products/
{
    "name": "Kelas Belajar Python",
    "sku": "DCD01",
    "description": "Kelas dasar pemrograman Python.",
    "shop": "Dicoding",
    "location": "Bandung",
    "price": 1500000,
    "discount": 0,
    "category": "Course",
    "stock": 1000,
    "is_available": true,
    "picture": "https://example.com/image.jpg"
}
\`\`\`

## 🧪 Pengujian

Pengujian dilakukan menggunakan Postman Collection & Environment resmi
dari Dicoding, mencakup skenario data valid, data tidak lengkap,
pencarian, dan penghapusan (soft delete).

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran pada program Dicoding.
