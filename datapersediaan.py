import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("datapersediaan.csv")

# Menampilkan distribusi stok (Histogram)
plt.figure(figsize=(8, 6))
sns.histplot(df['stok'], bins=20, kde=True, color='skyblue')
plt.title('Distribusi Stok Produk')
plt.xlabel('Stok')
plt.ylabel('Frekuensi')
plt.show()

# Barplot kategori produk
plt.figure(figsize=(8, 6))
sns.countplot(x='kategori_produk', data=df, palette='muted')
plt.title('Distribusi Kategori Produk')
plt.xlabel('Kategori Produk')
plt.ylabel('Frekuensi')
plt.show()

# Kluster menggunakan KMeans
# Menggunakan hanya stok dan penjualan untuk klasterisasi
X = df[['stok', 'penjualan']]

# Menentukan jumlah kluster
num_clusters = 3

# Membuat model KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Melakukan klasterisasi
kmeans.fit(X)

# Mendapatkan label kluster untuk setiap data point
df['cluster'] = kmeans.labels_

# Plot kluster
plt.figure(figsize=(8, 6))
sns.scatterplot(x='stok', y='penjualan', hue='cluster', data=df, palette='Set1', legend='full')
plt.title('Plot Kluster dengan KMeans')
plt.xlabel('Stok')
plt.ylabel('Penjualan')
plt.show()

# Scatterplot untuk hubungan antara stok dan penjualan
plt.figure(figsize=(8, 6))
sns.scatterplot(x='stok', y='penjualan', data=df, color='orange')
plt.title('Scatterplot Stok vs Penjualan')
plt.xlabel('Stok')
plt.ylabel('Penjualan')
plt.show()

# Boxplot untuk distribusi penjualan dalam setiap kluster
plt.figure(figsize=(8, 6))
sns.boxplot(x='cluster', y='penjualan', data=df, palette='Set2')
plt.title('Distribusi Penjualan dalam Setiap Kluster')
plt.xlabel('Kluster')
plt.ylabel('Penjualan')
plt.show()
