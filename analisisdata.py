# 8–10. Impor library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 11. Baca dataset nilai_siswa.csv (pakai pemisah ;)
data = pd.read_csv('nilai_siswa.csv', sep=';')

# 16–17. Tampilkan Informasi Dataset
print("=== Informasi Dataset ===")
data.info()

# 18–19. Tampilkan 5 data pertama
print("\n=== 5 Data Pertama ===")
print(data.head())

# 20–21. Statistik deskriptif
print("\n=== Statistik Deskriptif ===")
print(data.describe())

# 22–25. Rata-rata, median, modus nilai
print("\n=== Statistik Nilai ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# 26–29. Nilai per mata pelajaran
print("\n=== Nilai per Mata Pelajaran ===")
for mapel in data['Matpel'].unique():
    print(f"\n--- {mapel} ---")
    print(data[data['Matpel'] == mapel])

# 30–31. Nilai maksimum dan minimum per mapel
print("\n=== Nilai Maksimum dan Minimum per Mapel ===")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))

# 32–38. Grafik batang rata-rata nilai per mapel (urut dari tertinggi ke terendah)
print("\n=== Grafik Rata-Rata Nilai per Mapel ===")
rata = data.groupby('Matpel')['Nilai'].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran', fontsize=14, fontweight='bold')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 39–42. Boxplot sebaran nilai
print("\n=== Boxplot Sebaran Nilai per Mata Pelajaran ===")
plt.figure(figsize=(8, 5))
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 43–46. Peringkat rata-rata nilai per mapel
print("\n=== Peringkat Rata-Rata Nilai per Mapel ===")
ranking = rata.reset_index().rename(columns={'Nilai': 'Rata-Rata'})
print(ranking)

# 47–50. Kesimpulan sederhana
print("\n=== Kesimpulan ===")
print("• Grafik batang menunjukkan perbandingan rata-rata nilai antar mata pelajaran (diurutkan dari tertinggi).")
print("• Boxplot memperlihatkan sebaran nilai dan kemungkinan outlier di tiap mapel.")
print("• Dari grafik dan data, kamu bisa lihat mata pelajaran dengan nilai tertinggi dan terendah.")
