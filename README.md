# Quiz Docker FastAPI

Repository ini berisi dokumentasi tugas integrasi Docker dengan MariaDB serta implementasi API sederhana menggunakan FastAPI.

## Tujuan

- Menjalankan MariaDB menggunakan Docker.
- Membuat dan menggunakan Docker network.
- Mengimplementasikan API sederhana menggunakan FastAPI.
- Menampilkan endpoint Hello World dan endpoint nama.

## Teknologi yang Digunakan

- Docker Desktop
- Docker Engine
- Docker Compose
- WSL 2
- Ubuntu 24.04
- MariaDB 11.2
- Python 3.12
- FastAPI

## Struktur Folder

```text
quiz-docker-fastapi/
├── db-book/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── .env
├── app-book/
│   ├── main.py
└── README.md
```

> Catatan: File konfigurasi yang berisi kredensial pribadi tidak disertakan dalam repository publik.

## 1. Membuat Docker Network

Docker network digunakan agar container dapat saling terhubung.

```bash
docker network create oop-net
```

Untuk memeriksa network:

```bash
docker network ls
```

## 2. Menjalankan MariaDB dengan Docker

Masuk ke folder database:

```bash
cd db-book
```

Build dan jalankan container:

```bash
docker compose up -d --build
```
## 5. Menjalankan FastAPI

Jalankan aplikasi dari folder `app-book`:

```bash
fastapi dev main.py
```

Aplikasi akan berjalan pada alamat lokal yang ditampilkan oleh terminal.

## 6. Endpoint API

| Endpoint | Fungsi | Contoh Respons |
|---|---|---|
| `/` | Menampilkan Hello World | `{"message": "Hello World"}` |
| `/name/{nama}` | Menampilkan nama berdasarkan parameter | `{"name": "Ars"}` |

Contoh akses endpoint:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/name/Ars
```

## 7. Dokumentasi API

FastAPI menyediakan dokumentasi API interaktif melalui Swagger UI.

Buka:

```text
http://127.0.0.1:8000/docs
```

## 8. Menghentikan Aplikasi

Untuk menghentikan server FastAPI, tekan:

```text
Ctrl + C
```
