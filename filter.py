import pandas as pd

# CSV dosyasını yükle
df = pd.read_csv('rapor.csv')

# Koşullara göre filtrele
filtrelenmis_df = df[(df['PR Durumu'].isin(['Strong', 'PR Quality: Very Strong', 'PR Quality: Strong', 'PR Quality: Weak', 'PR Quality: Moderate'])) & (df['Spam Skoru'].isin(['Spam Score: 0 / 18', 'Spam Score: 1 / 18']))]

# Filtrelenmiş verileri yeni bir CSV dosyasına kaydet
filtrelenmis_df.to_csv('temizrapor.csv', index=False)
