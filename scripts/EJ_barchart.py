import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('summary_table_PM25.csv')

plt.figure(figsize=(6,4))
colors = ['#b3cde0', '#6497b1', '#005b96']
bars = plt.bar(df['Income_Gro'], df['MEAN_PM25'],
               color=colors, edgecolor='black')

plt.title('Average Modeled PM₂.₅ by Income Group – Massachusetts (2022)', fontsize=12)
plt.ylabel('PM₂.₅ (µg/m³)')
plt.ylim(6.75, 6.85)
plt.grid(axis='y', alpha=0.3)

for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.002,
             f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('outputs/correlation_plot.png', dpi=300)
plt.show()