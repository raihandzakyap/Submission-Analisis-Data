# Dashboard Analisis Data E-Commerce

## Setup Environment

1. Pastikan Python sudah terinstall (disarankan Python 3.10 ke atas)

2. Buat virtual environment (opsional tapi disarankan)
```
python -m venv venv
```

3. Aktifkan virtual environment

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

4. Install dependensi
```
pip install -r requirements.txt
```

---

## Menjalankan Dashboard

1. Masuk ke folder Dashboard
```
cd Dashboard
```

2. Jalankan Streamlit
```
streamlit run Dashboard.py
```

3. Buka browser jika tidak terbuka otomatis:
```
http://localhost:8501
```

---

## Struktur Folder

```
Submission Analisis Data - Raihan/
│
├── Dashboard/
│   └── Dashboard.py
│
├── Data/
│   ├── customers_dataset.csv
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   ├── products_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
```

---

## Catatan

- Pastikan folder `Data` berada di luar folder `Dashboard`
- Pastikan semua file dataset tersedia sebelum menjalankan dashboard
