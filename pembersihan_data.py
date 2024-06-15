import pandas as pd

def pembersihan_data(filepath):
    # Load data
    df = pd.read_csv(filepath)
    
    # Menghapus baris dengan nilai yang hilang
    df = df.dropna()
    
    # Menghapus duplikasi
    df = df.drop_duplicates()
    
    # Mengubah tipe data jika diperlukan (misalnya stok dan penjualan ke integer)
    df['stok'] = df['stok'].astype(int)
    df['penjualan'] = df['penjualan'].astype(int)
    
    return df
