(venv) a@as-MacBook-Pro visualisasi nilai pyhton p arifin % "/Users/a/Documents/visualisasi nilai pyhton p arifin/venv/bin/python" "/Users/a/Documents/visualisasi nilai pyhton p arifin/projek_visualisasi/analisisdata.py"

=== Informasi Dataset ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Nama    22 non-null     object
 1   Matpel  22 non-null     object
 2   Nilai   22 non-null     int64 
dtypes: int64(1), object(2)
memory usage: 660.0+ bytes

=== 5 Data Pertama ===
     Nama            Matpel  Nilai
0     Ade  Bahasa Indonesia     87
1    Aira  Bahasa Indonesia     88
2    Badi    Bahasa Inggris     78
3    Cyla    Bahasa Inggris     90
4  Khansa        Matematika     98

=== Statistik Deskriptif ===
           Nilai
count  22.000000
mean   86.318182
std     6.066193
min    75.000000
25%    85.000000
50%    86.500000
75%    90.000000
max    98.000000

=== Statistik Nilai ===
Rata-rata: 86.31818181818181
Median: 86.5
Modus: 85

=== Nilai per Mata Pelajaran ===

--- Bahasa Indonesia ---
     Nama            Matpel  Nilai
0     Ade  Bahasa Indonesia     87
1    Aira  Bahasa Indonesia     88
11   Agus  Bahasa Indonesia     87
12  Gilam  Bahasa Indonesia     75

--- Bahasa Inggris ---
   Nama          Matpel  Nilai
2  Badi  Bahasa Inggris     78
3  Cyla  Bahasa Inggris     90
5  Maya  Bahasa Inggris     85

--- Matematika ---
     Nama      Matpel  Nilai
4  Khansa  Matematika     98
6     Dwi  Matematika     85

--- Fisika ---
      Nama  Matpel  Nilai
7     Raka  Fisika     95
8    Rasya  Fisika     90
10   Sania  Fisika     86
13    Rudi  Fisika     75
18  Evelyn  Fisika     90
19   Raina  Fisika     95
20     Ade  Fisika     90
21   Rasya  Fisika     85

--- Produktif ---
      Nama     Matpel  Nilai
9     Mala  Produktif     80
14  Faizal  Produktif     80
15   Hanif  Produktif     90
16  Danish  Produktif     85
17  Darian  Produktif     85

=== Nilai Maksimum dan Minimum per Mapel ===
                  max  min
Matpel                    
Bahasa Indonesia   88   75
Bahasa Inggris     90   78
Fisika             95   75
Matematika         98   85
Produktif          90   80

=== Grafik Rata-Rata Nilai per Mapel ===

=== Boxplot Sebaran Nilai per Mata Pelajaran ===
/Users/a/Documents/visualisasi nilai pyhton p arifin/projek_visualisasi/analisisdata.py:53: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

  sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')

=== Peringkat Rata-Rata Nilai per Mapel ===
             Matpel  Rata-Rata
0        Matematika  91.500000
1            Fisika  88.250000
2    Bahasa Inggris  84.333333
3  Bahasa Indonesia  84.250000
4         Produktif  84.000000

=== Kesimpulan ===
• Grafik batang menunjukkan perbandingan rata-rata nilai antar mata pelajaran (diurutkan dari tertinggi).
• Boxplot memperlihatkan sebaran nilai dan kemungkinan outlier di tiap mapel.
• Dari grafik dan data, kamu bisa lihat mata pelajaran dengan nilai tertinggi dan terendah.
(venv) a@as-MacBook-Pro visualisasi nilai pyhton p arifin % 
(venv) a@as-MacBook-Pro visualisasi nilai pyhton p arifin % 
