# Pembuat Option untuk Apache Echarts

### Deskripsi:
API ini dapat digunakan untuk membuat bar plot, line plot, area plot, scatter plot, bubble plot, pie chart, histogram, boxplot.

### Struktur JSON secara umum:
```
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
        "y_axis_end": (Batas maksimum sumbu Y pada grafik),
        "symbol_size_min": (Ukuran terkecil titik pada grafik bubble plot),
        "symbol_size_max": (Ukuran terkecil titik pada grafik bubble plot),
        "orientation": (Orientasi grafik),
        "show_legend": (Nilai true/false untuk menunjukkan legend pada grafik),
        "enable_zoom": (Aktif atau tidaknya tombol zoom),
        "enable_save": (Aktif atau tidaknya tombol simpan gambar)
    }
}
```

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
- orientation: Diisi dengan 'horizontal' atau 'vertical' untuk orientasi grafik. Secaa default bernilai 'vertical'.
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
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
        "y_axis_start": 20,
        "y_axis_end": 75,
        "orientation": "vertical",
        "show_legend": false,
        "enable_zoom": false,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Bar Plot](https://user-images.githubusercontent.com/64583473/158557225-d3e46ebd-a0e1-4f41-ac26-96303d3a035d.png)

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
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
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
        "y_axis_start": 200,
        "y_axis_end": 400,
        "show_legend": true,
        "enable_zoom": true,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Line Plot](https://user-images.githubusercontent.com/64583473/158557011-55d2417b-415d-493b-8152-d1f5856ffc7a.png)

## Area Plot
### Endpoint:
{url}/api/visualize/area

### Deskripsi:
Grafik ini dapat menampilkan banyak area plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk bar plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik area plot.
- subtitle: Diisi dengan sub judul grafik area plot.
- categories: Diisi dengan kategori (nilai-nilai pada sumbu X) sesuai dengan jumlah data dalam area plot.
- data_names: Diisi dengan nama kelompok-kelompok data dalam grafik area plot.
- x_axis_name: Diisi dengan nama sumbu X grafik area plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik area plot.
- y_axis_start: Diisi dengan nilai batas minimum sumbu Y grafik area plot.
- y_axis_end: Diisi dengan nilai batas maksimum sumbu Y grafik area plot.
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
{
    "data": {
        "title": "Laba Total Franchise Z",
        "subtitle": "Periode 2017-2021",
        "values": [[124, 211, 259, 347, 381], [165, 175, 222, 293, 317], [182, 215, 276, 279, 303]],
        "categories": ["2017", "2018", "2019", "2020", "2021"],
        "data_names": ["Toko E", "Toko F", "Toko G"],
        "x_axis_name": "Tahun",
        "y_axis_name": "Laba (dalam juta Rupiah)"
    },
    "custom_settings": {
        "y_axis_start": 0,
        "y_axis_end": 400,
        "show_legend": true,
        "enable_zoom": true,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Area Plot](https://user-images.githubusercontent.com/64583473/158557212-b834b10f-1f1b-446d-92fa-e668de91391b.png)

## Scatter Plot
### Endpoint:
{url}/api/visualize/scatter

### Deskripsi:
Grafik ini dapat menampilkan banyak scatter plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 3D berisi nilai-nilai untuk scatter plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris. Nilai yang dimasukkan berbentuk array berisi nilai X dan nilai Y.

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
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
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
        "y_axis_end": 10,
        "show_legend": true,
        "enable_zoom": false,
        "enable_save": false
    }
}
```

### Keluaran dari Contoh:

![Contoh Scatter Plot](https://user-images.githubusercontent.com/64583473/158557024-11cfcde8-768d-47a8-8328-3e9fb6ca61ba.png)

## Bubble Plot
### Endpoint:
{url}/api/visualize/bubble

### Deskripsi:
Grafik ini dapat menampilkan banyak bubble plot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 3D berisi nilai-nilai untuk bubble plot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris. Nilai yang dimasukkan berbentuk array berisi nilai X, nilai Y, dan nilai yang akan menentukan ukuran titik.

#### Opsional:
- title: Diisi dengan judul grafik bubble plot.
- subtitle: Diisi dengan sub judul grafik bubble plot.
- data_names: Diisi dengan nama kelompok-kelompok data dalam grafik bubble plot
- x_axis_name: Diisi dengan nama sumbu X grafik bubble plot.
- y_axis_name: Diisi dengan nama sumbu Y grafik bubble plot.
- x_axis_start: Diisi dengan nilai batas minimum sumbu X grafik bubble plot.
- x_axis_end: Diisi dengan nilai batas maksimum sumbu X grafik bubble plot.
- y_axis_start: Diisi dengan nilai batas minimum sumbu Y grafik bubble plot.
- y_axis_end: Diisi dengan nilai batas maksimum sumbu Y grafik bubble plot.
- symbol_size_min: Diisi dengan ukuran terkecil titik pada grafik. Secara default bernilai 10.
- symbol_size_max: Diisi dengan ukuran terbesar titik pada grafik. Secara default bernilai 100.
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
{
    "data": {
        "title": "Rating dan Harga terhadap Laba Penjualan Produk Toko A",
        "subtitle": "Januari 2022 - Maret 2022",
        "values": [[[40000.0, 5.0, 19500000.0], [5000.0, 4.0, 82500000.0], [30000.0, 5.0, 85500000.0], [5000.0, 4.5, 85000000.0], [10000.0, 3.0, 94500000.0]], [[25000.0, 4.0, 91000000.0], [5000.0, 5.0, 52000000.0], [45000.0, 3.5, 39000000.0], [20000.0, 4.5, 37500000.0], [20000.0, 4.5, 93500000.0]], [[25000.0, 4.0, 28000000.0], [5000.0, 5.0, 46500000.0], [35000.0, 5.0, 86500000.0], [25000.0, 4.0, 93500000.0], [25000.0, 3.5, 38000000.0]]],
        "data_names": ["Kue Kering", "Roti", "Kue Ulang Tahun"],
        "x_axis_name": "Harga",
        "y_axis_name": "Rating"
    },
    "custom_settings": {
        "x_axis_start": 0,
        "x_axis_end": 60000,
        "y_axis_start": 2,
        "y_axis_end": 6,
        "symbol_size_min": 20,
        "symbol_size_max": 100,
        "show_legend": true,
        "enable_zoom": false,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Bubble Plot](https://user-images.githubusercontent.com/64583473/158557273-ed080be0-17a4-42fc-a042-9b04f0288eb9.png)

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
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
{
    "data": {
        "title": "Hasil Penjualan Minuman Kafe A (Tahun 2021)",
        "subtitle": "Data dalam juta Rupiah",
        "values": [390, 241, 133, 190, 85],
        "data_names": ["Kopi", "Coklat", "Jus", "Teh", "Lainnya"]
    },
    "custom_settings": {
        "show_legend": true,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Pie Chart](https://user-images.githubusercontent.com/64583473/158557016-a3a60bed-cba8-40ef-987c-310276996c52.png)

## Histogram
### Endpoint:
{url}/api/visualize/histogram

### Deskripsi:
Grafik ini dapat menampilkan grafik histogram dari kumpulan data yang diberikan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 1D berisi nilai-nilai untuk histogram.

#### Opsional:
- title: Diisi dengan judul grafik histogram.
- subtitle: Diisi dengan sub judul grafik histogram.
- x_axis_name: Diisi dengan nama sumbu X grafik histogram.
- y_axis_name: Diisi dengan nama sumbu Y grafik histogram.
- start: Diisi dengan titik awal kalkulasi grafik histogram. Tidak bisa lebih besar atau sama dengan "end" atau nilai "start" dan "end" akan diabaikan.
- end: Diisi dengan titik akhir kalkulasi grafik histogram.
- orientation: Diisi dengan 'horizontal' atau 'vertical' untuk orientasi grafik. Secaa default bernilai 'vertical'.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
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
        "bins" :2500,
        "orientation": "vertical",
        "enable_zoom": false,
        "enable_save": false
    }
}
```

### Keluaran dari Contoh:

![Contoh Histogram](https://user-images.githubusercontent.com/64583473/158557007-79ff671f-0176-440d-a7ff-8fbf401e63b5.png)

## Boxplot
### Endpoint:
{url}/api/visualize/boxplot

### Deskripsi:
Grafik ini dapat menampilkan banyak boxplot pada saat yang bersamaan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk boxplot dengan nilai dalam kelompok yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik boxplot.
- subtitle: Diisi dengan sub judul grafik boxplot.
- categories: Diisi dengan kategori (nilai-nilai pada sumbu Y) sesuai dengan jumlah data dalam boxplot.
- x_axis_name: Diisi dengan nama sumbu X grafik boxplot.
- y_axis_name: Diisi dengan nama sumbu Y grafik boxplot.
- orientation: Diisi dengan 'horizontal' atau 'vertical' untuk orientasi grafik. Secaa default bernilai 'vertical'.
- show_legend: Diisi dengan nilai true atau false untuk penampilan legend pada grafik. Secara default bernilai true.
- enable_zoom: Diisi dengan nilai true atau false untuk penampilan tombol zoom pada grafik. Secara default bernilai true.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
{
    "data": {
        "title": "Pengeluaran Pelanggan per Pesanan",
        "subtitle": "Data diambil pada tanggal 15 Januari 2022",
        "values": [[15000, 17000, 15000, 13000, 17000, 15000, 14000, 17000, 6000, 13000, 17000, 9000, 19000, 16000, 11000, 14000, 19000, 16000, 9000, 17000, 11000, 9000, 19000, 16000, 19000, 17000, 23000, 19000, 23000, 12000],[10000, 14000, 13000, 15000, 9000, 19000, 19000, 16000, 12000, 7000, 7000, 5000, 14000, 16000, 5000, 11000, 5000, 4000, 11000, 13000, 15000, 16000, 20000, 22000, 7000, 7000, 21000, 22000, 13000, 16000]],
        "categories": ["Makanan", "Minuman"],
        "x_axis_name": "Pengeluaran",
        "y_axis_name": "Jenis Barang"
    },
    "custom_settings" : {
        "orientation": "horizontal",
        "show_legend": false,
        "enable_zoom": false,
        "enable_save": true
    }
}
```

### Keluaran dari Contoh:

![Contoh Boxplot](https://user-images.githubusercontent.com/64583473/158557368-981d7480-0761-40d5-a303-0d2cb32a423c.png)

## Heatmap
### Endpoint:
{url}/api/visualize/heatmap

### Deskripsi:
Grafik ini dapat menampilkan heatmap sesuai data yang diberikan.

### Pengisian JSON:
#### Harus diisi:
- values: Diisi dengan array 2D berisi nilai-nilai untuk heatmap dengan nilai dalam satu kategori sumbu Y yang sama dimasukkan menjadi 1 baris.

#### Opsional:
- title: Diisi dengan judul grafik heatmap.
- subtitle: Diisi dengan sub judul grafik heatmap.
- categories: Diisi dengan kategori-kategori (nilai-nilai pada sumbu X dan Y) sesuai dengan data yang dimasukkan. Kategori dibuat dalam bentuk 2D dengan baris pertama diisi dengan kategori untuk sumbu X dan baris kedua diisi dengan kategori untuk sumbu Y.
- x_axis_name: Diisi dengan nama sumbu X grafik heatmap.
- y_axis_name: Diisi dengan nama sumbu Y grafik heatmap.
- enable_save: Diisi dengan nilai true atau false untuk penampilan tombol simpan gambar pada grafik. Secara default bernilai true.

### Contoh JSON:
```
{
    "data": {
        "title": "Petugas Aktif Shift Malam Toko A",
        "subtitle": "1 Maret 2022",
        "values": [[1, 3, 3, 0, 0, 0, 2, 2, 3, 0, 1, 2], [1, 1, 3, 3, 3, 3, 3, 0, 2, 3, 0, 1], [0, 2, 2, 1, 1, 0, 3, 2, 2, 1, 3, 1]],
        "categories": [["19.00", "20.00", "21.00", "22.00", "23.00", "00.00", "01.00", "02.00", "03.00", "04.00", "05.00", "06.00"],["Pos Jaga", "Counter", "Kebersihan"]],
        "x_axis_name": "Jam",
        "y_axis_name": "Posisi"
    },
    "custom_settings" : {
        "enable_save": false
    }
}
```

### Keluaran dari Contoh:

![Contoh Heatmap](https://user-images.githubusercontent.com/64583473/158557390-073a82bf-dcf2-47f8-9a79-13136695ef34.png)
