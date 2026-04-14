import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("📊 Dashboard Analisis E-Commerce")

# ======================
# DEBUG PATH
# ======================
st.write("Current Path:", os.getcwd())

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    base_path = "../Data/"

    customers = pd.read_csv(base_path + "customers_dataset.csv")
    orders = pd.read_csv(base_path + "orders_dataset.csv")
    order_items = pd.read_csv(base_path + "order_items_dataset.csv")
    order_payments = pd.read_csv(base_path + "order_payments_dataset.csv")
    order_reviews = pd.read_csv(base_path + "order_reviews_dataset.csv")
    products = pd.read_csv(base_path + "products_dataset.csv")
    category = pd.read_csv(base_path + "product_category_name_translation.csv")

    return customers, orders, order_items, order_payments, order_reviews, products, category

customers, orders, order_items, order_payments, order_reviews, products, category = load_data()

# ======================
# SIDEBAR
# ======================
st.sidebar.header("Menu")
menu = st.sidebar.selectbox("Pilih Analisis", [
    "Produk",
    "Metode Pembayaran",
    "Penjualan 2018",
    "Kepuasan Pelanggan"
])

# ======================
# 1. PRODUK
# ======================
if menu == "Produk":
    st.header("📦 Analisis Produk")

    df_product = order_items.merge(products, on='product_id', how='left')
    df_product = df_product.merge(category, on='product_category_name', how='left')

    category_counts = df_product['product_category_name_english'].value_counts()

    top_category = category_counts.head(10)
    low_category = category_counts.tail(10)

    st.subheader("Top 10 Kategori Terlaris")
    fig1, ax1 = plt.subplots()
    top_category.plot(kind='bar', ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.subheader("10 Kategori Paling Sedikit Terjual")
    fig2, ax2 = plt.subplots()
    low_category.plot(kind='bar', ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# ======================
# 2. PAYMENT
# ======================
elif menu == "Metode Pembayaran":
    st.header("💳 Metode Pembayaran")

    payment_counts = order_payments['payment_type'].value_counts()

    fig, ax = plt.subplots()
    payment_counts.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ======================
# 3. PENJUALAN 2018
# ======================
elif menu == "Penjualan 2018":
    st.header("📈 Tren Penjualan Tahun 2018")

    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders_2018 = orders[orders['order_purchase_timestamp'].dt.year == 2018]

    sales_2018 = orders_2018.groupby(
        orders_2018['order_purchase_timestamp'].dt.month
    ).size()

    fig, ax = plt.subplots()
    sales_2018.plot(kind='line', marker='o', ax=ax)
    plt.xticks(range(1,13))
    plt.grid()
    st.pyplot(fig)

# ======================
# 4. REVIEW
# ======================
elif menu == "Kepuasan Pelanggan":
    st.header("⭐ Kepuasan Pelanggan")

    review_dist = order_reviews['review_score'].value_counts().sort_index()

    fig, ax = plt.subplots()
    review_dist.plot(kind='bar', ax=ax)
    st.pyplot(fig)

    avg_review = order_reviews['review_score'].mean()
    st.metric("Rata-rata Review", round(avg_review, 2))