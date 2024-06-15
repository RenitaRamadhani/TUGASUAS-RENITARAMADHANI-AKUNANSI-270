# Nama : Renita Ramadhani #
# NIM : 12030122140270 #
# Kelas : Pengkodean dan Pemrograman/D #

# Soal #
1. Buatlah visualisasi histogram distribusi stok produk dari sistem persediaan dalam sebuah perusahaan serta interpretasikan dari hasil visualisasi tersebut!
2. Buatlah visualisasi barplot distribusi kategori produk serta interpretasikan dari hasil visualisasi tersebut!
3. Buatlah visualisasi scatterplot yang menampilkan kluster hasil dari algoritma KMeans serta interpretasikan hasil visualisasi tersebut!
4. Buatlah visualisasi serta interpretasikan hasil visualisasi tersebut!
5. Buatlah visualisasi serta interpretasikan hasil visualisasi tersebut!

# Cara Pengerjaan #
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

# Data #
![image](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/d78ada03-149a-4ea0-8c9e-2a1f2bc03b34)

# Hasil #
![Screenshot 2024-06-15 163326](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/221de07e-6085-4d37-99ee-5a2476f6f818)
# Interpretasi #
Berdasarkan histogram yang ditampilkan pada gambar di atas, berikut adalah beberapa interpretasi mengenai distribusi stok produk:

1. **Distribusi Stok Produk**:
   - Distribusi stok produk menunjukkan jumlah frekuensi produk dengan berbagai tingkat stok.
   - Histogram menunjukkan bahwa stok produk terdistribusi secara cukup merata dalam beberapa rentang stok tertentu.

2. **Puncak Distribusi**:
   - Terdapat beberapa puncak dalam distribusi stok, yang menunjukkan bahwa ada beberapa rentang stok di mana frekuensi produk yang ada lebih tinggi dibandingkan rentang stok lainnya.
   - Puncak tertinggi terjadi pada rentang stok sekitar 40-50 dan 90-100 dengan frekuensi mencapai 3 produk.

3. **Rentang Stok**:
   - Rentang stok bervariasi dari sekitar 40 hingga 200.
   - Frekuensi produk menurun pada stok di atas 100, dengan beberapa pengecualian pada stok sekitar 140 dan 200 yang juga memiliki frekuensi lebih tinggi dibandingkan rentang stok lainnya.

4. **Kepadatan Inti (KDE)**:
   - Garis biru halus yang mengalir di atas histogram adalah Kernel Density Estimate (KDE), yang memberikan gambaran mengenai distribusi probabilitas dari data stok.
   - KDE menunjukkan bahwa meskipun terdapat beberapa puncak pada histogram, secara umum distribusi stok menurun secara bertahap setelah mencapai puncak di sekitar stok 60.

5. **Interpretasi Umum**:
   - Produk dengan stok sekitar 40-50 dan 90-100 lebih sering terjadi dibandingkan dengan rentang stok lainnya.
   - Produk dengan stok di atas 100 lebih jarang terjadi, kecuali pada stok tertentu seperti 140 dan 200.

Informasi ini dapat digunakan untuk menganalisis pola stok produk dan mengidentifikasi rentang stok yang paling umum, yang dapat berguna untuk perencanaan inventaris dan strategi penjualan.

# Hasil #
![Screenshot 2024-06-15 163345](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/6b0cf94b-0d5f-4c7e-85c4-401ecac5e2e1)
# Interpretasi #
Berikut adalah interpretasi dari gambar yang menampilkan barplot distribusi kategori produk:

1. **Distribusi Kategori Produk**:
   - Gambar menunjukkan distribusi frekuensi produk berdasarkan kategori. Kategori yang ditampilkan adalah Elektronik, Pakaian, dan Makanan.
   - Barplot memperlihatkan bahwa setiap kategori memiliki jumlah produk yang berbeda dalam dataset.

2. **Kategori Elektronik**:
   - Kategori Elektronik memiliki frekuensi produk sekitar 9.
   - Ini menunjukkan bahwa ada sekitar 9 produk yang termasuk dalam kategori Elektronik di dalam dataset.

3. **Kategori Pakaian**:
   - Kategori Pakaian memiliki frekuensi produk yang sama dengan kategori Elektronik, yaitu sekitar 9.
   - Ini menunjukkan bahwa kategori Pakaian memiliki jumlah produk yang sama dengan kategori Elektronik dalam dataset.

4. **Kategori Makanan**:
   - Kategori Makanan memiliki frekuensi produk sekitar 7.
   - Ini menunjukkan bahwa ada sedikit lebih sedikit produk dalam kategori Makanan dibandingkan dengan Elektronik dan Pakaian dalam dataset.

5. **Interpretasi Umum**:
   - Kategori Elektronik dan Pakaian memiliki jumlah produk yang sama dalam dataset ini, dengan frekuensi yang lebih tinggi dibandingkan kategori Makanan.
   - Perbedaan frekuensi antara kategori-kategori tersebut tidak terlalu besar, yang menunjukkan bahwa distribusi produk cukup merata di antara ketiga kategori tersebut.

Informasi ini dapat digunakan untuk memahami komposisi kategori produk dalam dataset, yang bisa berguna untuk analisis lebih lanjut terkait penjualan, persediaan, dan strategi pemasaran.

# Hasil #
![Screenshot 2024-06-15 163401](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/299ff063-9be2-480a-b9db-fb74a744ce0a)
# Interpretasi #
Berdasarkan scatterplot yang menampilkan kluster hasil dari algoritma KMeans, berikut adalah beberapa interpretasi:

1. **Distribusi Kluster**:
   - Terdapat tiga kluster yang berbeda, ditunjukkan dengan warna yang berbeda: kluster 0 (merah), kluster 1 (biru), dan kluster 2 (hijau).
   - Setiap titik pada scatterplot mewakili data produk dengan atribut stok dan penjualan.

2. **Karakteristik Kluster**:
   - **Kluster 0 (Merah)**:
     - Produk dengan stok tinggi (sekitar 180 hingga 200) dan penjualan tinggi (sekitar 250 hingga 300).
     - Produk dalam kluster ini memiliki stok dan penjualan yang paling tinggi dibandingkan dengan kluster lainnya.
   - **Kluster 1 (Biru)**:
     - Produk dengan stok rendah (sekitar 40 hingga 80) dan penjualan rendah (sekitar 80 hingga 150).
     - Produk dalam kluster ini memiliki stok dan penjualan yang relatif rendah.
   - **Kluster 2 (Hijau)**:
     - Produk dengan stok menengah (sekitar 100 hingga 160) dan penjualan menengah hingga tinggi (sekitar 150 hingga 200).
     - Produk dalam kluster ini memiliki stok dan penjualan yang berada di antara kluster 0 dan kluster 1.

3. **Hubungan Antara Stok dan Penjualan**:
   - Scatterplot menunjukkan adanya pola peningkatan penjualan seiring dengan peningkatan stok, meskipun terdapat beberapa variasi.
   - Produk dengan stok yang lebih tinggi cenderung memiliki penjualan yang lebih tinggi juga, seperti yang terlihat pada kluster 0.

4. **Kegunaan Klustering**:
   - Klustering membantu dalam mengidentifikasi pola di antara data produk yang dapat digunakan untuk strategi inventarisasi dan penjualan.
   - Dengan mengetahui kluster mana produk-produk tersebut termasuk, perusahaan dapat merencanakan strategi pemasaran dan persediaan yang lebih baik.

Informasi ini sangat berguna untuk analisis lebih lanjut terkait bagaimana stok produk mempengaruhi penjualan dan bagaimana perusahaan dapat mengelompokkan produk mereka berdasarkan karakteristik tersebut.

# Hasil #
![Screenshot 2024-06-15 163414](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/45c84254-93ed-4c69-a68f-75fbfe9e2101)
# Interpretasi #


# Hasil #
![Screenshot 2024-06-15 163433](https://github.com/RenitaRamadhani/TUGASUAS-RENITARAMADHANI-AKUNANSI-270/assets/153142982/774a9675-eefb-45ad-a00a-e94306d261d4)
# Interpretasi #



