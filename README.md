# Pembuat Option untuk Apache Echarts

### Deskripsi:
API ini dapat digunakan untuk membuat bar plot, line plot, scatter plot, pie chart, histogram, dan boxplot.

### Struktur JSON secara umum:
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
        "category_amount": (Jumlah kategori pada grafik histogram),
        "x_axis_start": (Batas minimum sumbu X pada grafik),
        "x_axis_end": (Batas maksimum sumbu X pada grafik),
        "y_axis_start": (Batas minimum sumbu Y pada grafik),
        "y_axis_end": (Batas maksimum sumbu Y pada grafik)
    }
    
}

### Keluaran:
Payload berisi option yang dapat digunakan dalam Apache Echarts.

# Cara Menggunakan:

## Bar Plot
### Endpoint:
{url}/api/visualize/bar

### Deskripsi:
Grafik ini dapat menampilkan banyak bar plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk bar plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik bar plot.
- subtitle: Diisi dengan sub judul grafik bar plot.
- categories: Diisi dengan kategori (nilai-nilai pada sumbu X) sesuai dengan jumlah data dalam bar plot.
- data_names: Diisi dengan nama kelompok-kelompok data dalam grafik bar plot.
- x_axis_name: Diisi dengan nama sumbu X grafik bar plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik bar plot.
- y_axis_start: Diisi dengan nilai batas minimum sumbu Y grafik bar plot.
- y_axis_end: Diisi dengan nilai batas maksimum sumbu Y grafik bar plot.

### Contoh JSON:
{

    "data": {
        "title": "Laba Penjualan Kue",
        "subtitle": "Per 31 Januari 2022",
        "values": [[33, 50, 44, 25], [47, 62, 33, 29], [40, 48, 49, 30]],
        "categories": ["Toko A", "Toko B", "Toko C", "Toko D"],
        "data_names": ["Kue X", "Kue Y", "Kue Z"],
        "x_axis_name": "Lokasi",
        "y_axis_name": "Laba Bersih (jt)"
    },
    "custom_settings": {
        "y_axis_start": 0,
        "y_axis_end": 75
    }
    
}

### Keluaran dari Contoh:

![Contoh Bar Plot](https://user-images.githubusercontent.com/64583473/151127988-26c2aba3-2103-4a8a-a037-0646b5e1f387.png)

## Line Plot
### Endpoint:
{url}/api/visualize/line

### Deskripsi:
Grafik ini dapat menampilkan banyak line plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk bar plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik line plot.
- subtitle: Diisi dengan sub judul grafik line plot.
- categories: Diisi dengan kategori (nilai-nilai pada sumbu X) sesuai dengan jumlah data dalam line plot.
- data_names: Diisi dengan nama kelompok-kelompok data dalam grafik line plot.
- x_axis_name: Diisi dengan nama sumbu X grafik line plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik line plot.
- y_axis_start: Diisi dengan nilai batas minimum sumbu Y grafik line plot.
- y_axis_end: Diisi dengan nilai batas maksimum sumbu Y grafik line plot.

### Contoh JSON:
{

    "data": {
        "title": "Pemasukan dari Penjualan Kopi",
        "subtitle": "Periode 2017-2021",
        "values": [[223, 217, 224, 234, 350], [220, 222, 228, 253, 248], [229, 223, 253, 284, 283], [217, 217, 231, 232, 251]],
        "categories": ["2017", "2018", "2019", "2020", "2021"],
        "data_names": ["Toko A", "Toko B", "Toko C", "Toko D"],
        "x_axis_name": "Tahun",
        "y_axis_name": "Pemasukan (dalam juta Rupiah)"
    },
    "custom_settings": {
        "y_axis_start": 0,
        "y_axis_end": 400
    }
    
}

### Keluaran dari Contoh:

![Contoh Line Plot](https://user-images.githubusercontent.com/64583473/151128000-45fbc8e7-c3f2-460f-ab47-36411f7862ec.png)

## Scatter Plot
### Endpoint:
{url}/api/visualize/scatter

### Deskripsi:
Grafik ini dapat menampilkan banyak scatter plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 3D berisi nilai-nilai untuk bar plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris. Nilai titik yang dimasukkan berbentuk array 2D berisi nilai X dan nilai Y.

#### Opsional:
- title: Diisi dengan judul grafik scatter plot.
- subtitle: Diisi dengan sub judul grafik scatter plot.
- data_names: Diisi dengan nama kelompok-kelompok data dalam grafik scatter plot
- x_axis_name: Diisi dengan nama sumbu X grafik scatter plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik scatter plot.
- x_axis_start: Diisi dengan nilai batas minimum sumbu X grafik scatter plot.
- x_axis_end: Diisi dengan nilai batas maksimum sumbu X grafik scatter plot.
- y_axis_start: Diisi dengan nilai batas minimum sumbu Y grafik scatter plot.
- y_axis_end: Diisi dengan nilai batas maksimum sumbu Y grafik scatter plot.

### Contoh JSON:
{

    "data": {
        "title": "Feedback Pembeli (Harga terhadap Kepuasan)",
        "values": [[[9, 6], [7, 7], [9, 7], [9, 6], [8, 5]],[[8, 8], [8, 7], [7, 10], [7, 8], [6, 7]],[[9, 9], [8, 9], [8, 8], [9, 8], [9, 7]]],
        "data_names": ["Kue X", "Kue Y", "Kue Z"],
        "x_axis_name": "Skor Harga",
        "y_axis_name": "Skor Kepuasan"
    },
    "custom_settings": {
        "x_axis_start": 0,
        "x_axis_end": 10,
        "y_axis_start": 0,
        "y_axis_end": 10
    }
    
}

### Keluaran dari Contoh:

![Contoh Scatter Plot](https://user-images.githubusercontent.com/64583473/151128006-e5a8febe-0ad1-4d88-a0b2-56bcf0edfd19.png)

## Pie Chart
### Endpoint:
{url}/api/visualize/pie

### Deskripsi:
Grafik ini dapat menampilkan grafik pie chart.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 1D berisi nilai-nilai untuk pie chart.

#### Opsional:
- title: Diisi dengan judul grafik pie chart.
- subtitle: Diisi dengan sub judul grafik pie chart.
- data_names: Diisi dengan nama tiap data dalam grafik pie chart.

### Contoh JSON:
{

    "data": {
        "title": "Hasil Penjualan Minuman Kafe A (Tahun 2021)",
        "subtitle": "Data dalam juta Rupiah",
        "values": [390, 241, 133, 190, 85],
        "data_names": ["Kopi", "Coklat", "Jus", "Teh", "Lainnya"]
    }

}

### Keluaran dari Contoh:

![Contoh Pie Chart](https://user-images.githubusercontent.com/64583473/151292359-300705d8-d919-44d9-a55a-9831996df145.png)

## Histogram
### Endpoint:
{url}/api/visualize/histogram

### Deskripsi:
Grafik ini dapat menampilkan grafik histogram dari kumpulan data yang diberikan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 1D berisi nilai-nilai untuk histogram.

#### Opsional:
- title: Diisi dengan judul grafik scatter plot.
- subtitle: Diisi dengan sub judul grafik scatter plot.
- x_axis_name: Diisi dengan nama sumbu X grafik histogram.
- y_axis_name: Diisi dengan nama sumbu Y grafik histogram.
- start: Diisi dengan titik awal kalkulasi grafik histogram. Tidak bisa lebih besar atau sama dengan "end" atau nilai "start" dan "end" akan diabaikan.
- end: Diisi dengan titik akhir kalkulasi grafik histogram.

### Contoh JSON:
{

    "data": {
        "title": "Pengeluaran Pelanggan per Pesanan",
        "subtitle": "Data diambil pada tanggal 31 Desember 2021",
        "values": [28000, 22000, 20000, 25000, 33000, 20000, 24000, 30000, 21000, 30000, 33000, 20000, 32000, 18000, 29000, 22000, 17000, 20000, 10000, 14000, 30000, 18000, 25000, 22000, 24000, 18000, 24000, 33000, 25000, 15000],
        "x_axis_name": "Pengeluaran",
        "y_axis_name": "Frekuensi"
    },
    "custom_settings" : {
        "start": 0,
        "end": 40000,
        "bins": 2500
    }

}

### Keluaran dari Contoh:

![Contoh Histogram](https://user-images.githubusercontent.com/64583473/151127999-0c0eb5f0-23fa-4201-a1a1-ee9a9a2741fb.png)

## Boxplot
### Endpoint:
{url}/api/visualize/boxplot

### Deskripsi:
Grafik ini dapat menampilkan banyak boxplot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk bar plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik scatter plot.
- subtitle: Diisi dengan sub judul grafik scatter plot.
- categories: Diisi dengan kategori (nilai-nilai pada sumbu Y) sesuai dengan jumlah data dalam boxplot.
- x_axis_name: Diisi dengan nama sumbu X grafik scatter plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik scatter plot.

### Contoh JSON:
{

    "data": {
        "title": "Pengeluaran Pelanggan per Pesanan",
        "subtitle": "Data diambil pada tanggal 15 Januari 2022",
        "values": [[15000, 17000, 15000, 13000, 17000, 15000, 14000, 17000, 6000, 13000, 17000, 9000, 19000, 16000, 11000, 14000, 19000, 16000, 9000, 17000, 11000, 9000, 19000, 16000, 19000, 17000, 23000, 19000, 23000, 12000],[10000, 14000, 13000, 15000, 9000, 19000, 19000, 16000, 12000, 7000, 7000, 5000, 14000, 16000, 5000, 11000, 5000, 4000, 11000, 13000, 15000, 16000, 20000, 22000, 7000, 7000, 21000, 22000, 13000, 16000]],
        "categories": ["Makanan", "Minuman"],
        "x_axis_name": "Pengeluaran",
        "y_axis_name": "Jenis Barang"
    }

}

### Keluaran dari Contoh:

![Contoh Boxplot](https://user-images.githubusercontent.com/64583473/151127994-1a9c7996-125c-4c28-9105-b55793aa4552.png)
