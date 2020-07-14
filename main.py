import csv
import json
import pandas as pd
from matplotlib import pyplot as plt

# # DATA COVID-19 (POSITIF, NEGATIF, MENINGGAL)
col_list = ["date", "new_tested", "acc_tested", "new_confirmed", "acc_confirmed", "acc_negative",
            "being_checked", "isolated", "new_released", "acc_released", "new_deceased", "acc_deceased",
            "positive_rate", "negative_rate", "decease_rate", "release_rate", "dailypositive_rate"]
kasus = pd.read_csv('./indonesia-coronavirus-cases/cases.csv', usecols=col_list)
# print(kasus)
data = kasus.drop(["new_tested", "acc_tested", "new_confirmed", "being_checked",
                  "isolated", "new_released", "new_deceased",
                  "positive_rate", "negative_rate", "decease_rate", "release_rate", "dailypositive_rate"], axis=1)

date        = data["date"]
positif     = data["acc_confirmed"]
negatif     = data["acc_negative"]
recovery    = data["acc_released"]
death       = data["acc_deceased"]

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

# CREATE PIE CHART
# labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
# sizes = [38.4, 40.6, 20.7, 10.3]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.show()

labels = 'Positif', 'Negatif', 'Recovery', 'Death'
sizes = [22.55, 77.45, 5.30, 8.90]

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)

ax1.pie(sizes, autopct='%1.1f%%', textprops={'fontsize': 8}, startangle=90)
ax1.set_title("COVID-19 31-Mar-2020")
ax1.legend(labels, loc=5, prop={'size': 6})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


ax2.pie(sizes, autopct='%1.1f%%', startangle=90)
ax2.set_title("COVID-19 31-Mar-2020")
ax2.legend(labels, loc=4, prop={'size': 6} )
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# END CREATE PIE CHART

# SHOW PIE CHART
plt.show()
# END SHOW PIE CHART

# # END OF DATA COVID-19 (POSITIF, NEGATIF, MENINGGAL)

# # PARSE DATA CSV TO JSON
csvFilePath = './indonesia-coronavirus-cases/cases.csv'
jsonFilePath = './data-JSON/cases.json'

dataObject = {}
dataObject['cases'] = data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['date']
        data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(dataObject, indent=4))
# # END PARSE DATA CSV TO JSON