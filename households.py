import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df = pd.read_csv('households_raw.csv', delimiter=";", encoding="ISO-8859-1", parse_dates=['years'])
print(df.head())

fig, ax = plt.subplots()
plt.tick_params(labelsize=8)
plt.title('Haushalte mit Kindern unter 18 Jahren')
ax.plot(df['years'], df['1 child'], '--', label="1 Kind")
ax.plot(df['years'], df['2 children'], ':', label="2 Kinder")
ax.plot(df['years'], df['3 children'], label="3 Kinder")
ax.plot(df['years'], df['4 or more children'], label="4 Kinder und mehr")
ax.xaxis.set_major_locator(MaxNLocator(10))
ax.set_xlabel('Jahr')
ax.set_ylabel('Anzahl in 1000')
ax.legend(loc='upper left', fontsize='small')

plt.show()