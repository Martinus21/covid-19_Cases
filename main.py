# KELOMPOK DPPL (COVID19)
# 1. MARTINUS RICHARD TICOALU (20180801055)
# 2. NABILLA (20180801107)
# 3. ASHAHRA VINDY ARIESTA (20180801001)
# SEBELUM MENJALANKAN PROGRAM, PASTIKAN INSTALL PACKAGE ATAU LIBRARY DITERMINAL DENGAN CARA :
# PIP INSTALL PANDAS
# PIP INSTALL MATPLOTLIB
# PIP INSTALL TKINTER
# PIP INSTALL PILLOW
# INSTALL DENGAN TEXT LOWER CASE ATAU HURUF KECIL
# UNTUK CEK PACKAGE ATAU LIBRARY : PIP FREEZE

# IMPORT
# import csv untuk memanggil folder yang berextend .csv
# import json untuk membuat data berupa object
# import pandas untuk melakukan scraping/cleaning data
# form matplotlib import pylot untuk membuat visualisasi chart
# form tkinter import * untuk membuat visualisasi Homepage
# from PIL import ImageTk,Image untuk menampilkan gambar pada frame

import csv
import json
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
from PIL import ImageTk,Image

# DEKLARASI FRAME PADA ROOT
root = Tk()

# # PARSE DATA CSV TO JSON

# GET FILE CSV
csvFilePath = './indonesia-coronavirus-cases/cases.csv'
# EXPORT FILE JSON
jsonFilePath = './data-JSON/cases.json'

# DEKLARASI OBJECT
dataObject = {}
dataObject['cases'] = data = {}

# OPEN FILE CSV
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['date']
        data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(dataObject, indent=4))
# # END PARSE DATA CSV TO JSON

# # FUNCTION UNTUK CLICK GRAFIK CHART
def onClickGChart():
    # # DATA COVID-19 (POSITIF, NEGATIF, MENINGGAL)

    # DEKLARASI ARRAY COL_LIST UNTUK GRAFIK CHART
    col_list = ["date", "new_tested", "acc_tested", "new_confirmed", "acc_confirmed", "acc_negative",
                "being_checked", "isolated", "new_released", "acc_released", "new_deceased", "acc_deceased",
                "positive_rate", "negative_rate", "decease_rate", "release_rate", "dailypositive_rate"]

    # PD.READ_CSV UNTUK GET DATA CSV PADA FILE CSV UNTUK GRAFIK CHART
    kasus = pd.read_csv('./indonesia-coronavirus-cases/cases.csv', usecols=col_list)

    # KASUS.DROP UNTUK MENDROP DATA COLUMN PADA DATA CSV UNTUK GRAFIK CHART
    data = kasus.drop(["new_tested", "acc_tested", "new_confirmed", "being_checked",
                       "isolated", "new_released", "new_deceased",
                       "positive_rate", "negative_rate", "decease_rate", "release_rate", "dailypositive_rate"], axis=1)

    # DATA YANG SUDAH DISCRAPING DIMASUKAN PADA DEKLARASI DATE,POSITIF,NEGATIF,RECOVERY,DEATH UNTUK GRAFIK CHART
    date = data["date"]
    positif = data["acc_confirmed"]
    negatif = data["acc_negative"]
    recovery = data["acc_released"]
    death = data["acc_deceased"]

    # CREATE GRAFIK CHART
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(date, positif, label='Positive')
    ax.plot(date, negatif, label='Negative')
    ax.plot(date, recovery, label='Recovery')
    ax.plot(date, death, label='Death')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title("COVID-19")
    for tick in ax.get_xticklabels():
        tick.set_rotation(55)
    fig.align_labels()
    ax.legend()  # Add a legend.
    # END CREATE GRAFIK CHART

    # SHOW GRAFIK CHART
    plt.show()
    # END SHOW GRAFIK CHART

    # # END OF DATA COVID-19 (POSITIF, NEGATIF, MENINGGAL)
# # END FUNCTION UNTUK CLICK GRAFIK CHART

# # FUNCTION UNTUK CLICK PIE CHART
def onClickPChart():
    # # CREATE PIE CHART

    # DEKLARASI ARRAY COL_LIST UNTUK PIE CHART
    col_list = ["date", "new_tested", "acc_tested", "new_confirmed", "acc_confirmed", "acc_negative",
                "being_checked", "isolated", "new_released", "acc_released", "new_deceased", "acc_deceased",
                "positive_rate", "negative_rate", "decease_rate", "release_rate", "dailypositive_rate"]

    # PD.READ_CSV UNTUK GET DATA CSV PADA FILE CSV UNTUK PIE CHART
    kasus = pd.read_csv('./indonesia-coronavirus-cases/cases.csv', usecols=col_list)

    # KASUS.DROP UNTUK MENDROP DATA COLUMN PADA DATA CSV UNTUK GRAFIK CHART
    data = kasus.drop(["new_tested", "acc_tested", "new_confirmed", "being_checked",
                       "isolated", "new_released", "new_deceased",
                       "acc_confirmed", "acc_negative", "acc_released", "acc_deceased", "dailypositive_rate"], axis=1)

    # DATA YANG SUDAH DISCRAPING DIMASUKAN PADA DEKLARASI DATE,POSITIF,NEGATIF,RECOVERY,DEATH UNTUK PIE CHART
    positif = data["positive_rate"]
    negatif = data["negative_rate"]
    recovery = data["release_rate"]
    death = data["decease_rate"]

    labels = 'Positif', 'Negatif', 'Recovery', 'Death'
    sizes_ax1 = [positif[0], negatif[0], recovery[0], death[0]]
    sizes_ax2 = [positif[10], negatif[10], recovery[10], death[10]]
    sizes_ax3 = [positif[19], negatif[19], recovery[19], death[19]]
    sizes_ax4 = [positif[29], negatif[29], recovery[29], death[29]]

    # UNTUK MENAMBAH SUBPLOT GRAFIK PIE AGAR BERADA PADA 1 FRAME
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    ax1.pie(sizes_ax1, autopct='%1.1f%%', textprops={'fontsize': 8}, startangle=90)
    ax1.set_title("COVID-19 2-Mar-2020")
    ax1.legend(labels, loc=4, prop={'size': 6})
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.pie(sizes_ax2, autopct='%1.1f%%', textprops={'fontsize': 8}, startangle=90)
    ax2.set_title("COVID-19 12-Mar-2020")
    ax2.legend(labels, loc=4, prop={'size': 6})
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax3.pie(sizes_ax3, autopct='%1.1f%%', textprops={'fontsize': 8}, startangle=90)
    ax3.set_title("COVID-19 21-Mar-2020")
    ax3.legend(labels, loc=4, prop={'size': 6})
    ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax4.pie(sizes_ax4, autopct='%1.1f%%', textprops={'fontsize': 8}, startangle=90)
    ax4.set_title("COVID-19 31-Mar-2020")
    ax4.legend(labels, loc=4, prop={'size': 6})
    ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # # END CREATE PIE CHART

    # # SHOW PIE CHART
    plt.show()
    # # END SHOW PIE CHART
# # END FUNCTION UNTUK CLICK PIE CHART

# TITLE PADA GUI
title = Label(root, text="COVID-19")
title_kel = Label(root, text="Kelompok DPPL")

# IMAGE PADA GUI
# IMAGETK.PHOTOIMAGE UNTUK MENGAMBIL IMAGE PADA FOLDER ASSETS
my_img = ImageTk.PhotoImage(Image.open("assets/chart_DPPL.png"))
my_images = Label(image=my_img)

# BUTTON PADA GUI
btnGrafikChart = Button(root, text="Grafik Chart", command=onClickGChart, fg="white", bg="#448C40", padx=100)
btnPieChart = Button(root, text="Pie Chart", command=onClickPChart, fg="white", bg="#448C40", padx=100)
btnExit = Button(root, text="Exit", command=root.quit, fg="white", bg="#448C40", padx=100)

# UNTUK MENGATUR POSISI TITLE, BUTTON, DAN IMAGE PADA FRAME
title.grid(row=0, column=0, columnspan=3)
title_kel.grid(row=1, column=0, columnspan=3)
my_images.grid(row=2, column=0, columnspan=3)
btnGrafikChart.grid(row=3, column=0)
btnPieChart.grid(row=3, column=1)
btnExit.grid(row=3, column=2)

# UNTUK MENJALANKAN FRAME
root.mainloop()