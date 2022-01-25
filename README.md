# Pembuat Option untuk Apache Echarts

### Deskripsi:
API ini dapat digunakan untuk membuat bar plot, histogram, scatter plot, line plot, boxplot, dan pie chart.

### Struktur JSON :
{
    "data": 
    {
        "title": (Judul grafik),
        "subtitle": (Sub judul grafik),
        "values": (Nilai-nilai pada grafik),
        "categories": (Kategori pada grafik),
        "data_names": (Nama untuk kumpulan nilai pada grafik),
        "x_axis_name": (Nama sumbu X pada grafik),
        "y_axis_name": (Nama sumbu Y pada grafik)
    },
    "custom_settings" : 
    {
        "start": (Nilai awal grafik histogram),
        "end": (Nilai akhir grafik histogram),
        "bins": (Jarak pada grafik histogram),
        "category_amount": (Jumlah kategori pada grafik histogram)
    }
}

### Keluaran:
Option yang dapat digunakan dalam Apache Echarts

# Cara menggunakan:

## Barplot
### Endpoint:
{url}/api/visualize/bar

### Deskripsi:
Grafik ini dapat menampilkan barplot beberapa data pada saat yang bersamaan.

### Contoh JSON:

