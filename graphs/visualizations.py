import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.size'] = 11

df = pd.read_csv('temperature_data.csv')
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

annual = df.groupby('Year').agg({
    'Global_Anomaly': 'mean',
    'NH_Anomaly': 'mean',
    'SH_Anomaly': 'mean',
    'Land_Anomaly': 'mean',
    'Ocean_Anomaly': 'mean'
}).reset_index()

annual['10yr_MA'] = annual['Global_Anomaly'].rolling(window=10, center=True).mean()
annual['Decade'] = (annual['Year'] // 10) * 10

fig, ax = plt.subplots(figsize=(14, 7))
ax.scatter(annual['Year'], annual['Global_Anomaly'], alpha=0.4, s=20, color='#2E86AB', label='Annual Anomaly')
ax.plot(annual['Year'], annual['10yr_MA'], linewidth=2.5, color='#C73E1D', label='10-Year Moving Average')
z = np.polyfit(annual['Year'], annual['Global_Anomaly'], 1)
p = np.poly1d(z)
ax.plot(annual['Year'], p(annual['Year']), "--", linewidth=2, color='#F18F01', alpha=0.7, label='Linear Trend')
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3)
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=13, fontweight='bold')
ax.set_title('Global Temperature Anomalies (1880-2025)\nRelative to 1901-2000 Average', fontsize=15, fontweight='bold', pad=20)
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3, linestyle='--')
slope = z[0] * 10
ax.text(0.02, 0.98, f'Warming rate: {slope:.3f}°C per decade', transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.tight_layout()
plt.savefig('figure1_time_series.png', dpi=300, bbox_inches='tight')
plt.close()

heatmap_data = df.pivot_table(values='Global_Anomaly', index='Year', columns='Month', aggfunc='mean')
years_to_show = heatmap_data.index[::5]
heatmap_data_subset = heatmap_data.loc[years_to_show]

fig, ax = plt.subplots(figsize=(14, 10))
sns.heatmap(heatmap_data_subset, cmap='RdYlBu_r', center=0, vmin=-1.5, vmax=1.5,
            cbar_kws={'label': 'Temperature Anomaly (°C)'}, linewidths=0.1, ax=ax)
ax.set_xlabel('Month', fontsize=13, fontweight='bold')
ax.set_ylabel('Year', fontsize=13, fontweight='bold')
ax.set_title('Monthly Temperature Anomalies Heatmap (1880-2025)\nSelected Years (Every 5th Year)', 
             fontsize=15, fontweight='bold', pad=20)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(month_labels, rotation=0)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
plt.tight_layout()
plt.savefig('figure2_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

decadal_stats = annual.groupby('Decade')['Global_Anomaly'].agg(['mean', 'std']).reset_index()
fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.bar(decadal_stats['Decade'], decadal_stats['mean'], width=8, color='#2E86AB', 
              alpha=0.8, edgecolor='black', linewidth=1.2)
ax.errorbar(decadal_stats['Decade'], decadal_stats['mean'], yerr=decadal_stats['std'],
            fmt='none', color='black', capsize=5, capthick=1.5, linewidth=1.5)
for i, (bar, mean_val) in enumerate(zip(bars, decadal_stats['mean'])):
    if mean_val < 0:
        bar.set_color('#6C9BD2')
    elif mean_val < 0.5:
        bar.set_color('#2E86AB')
    else:
        bar.set_color('#C73E1D')
ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.5)
ax.set_xlabel('Decade', fontsize=13, fontweight='bold')
ax.set_ylabel('Average Temperature Anomaly (°C)', fontsize=13, fontweight='bold')
ax.set_title('Decadal Average Temperature Anomalies (1880-2025)\nError bars show standard deviation', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figure3_decadal.png', dpi=300, bbox_inches='tight')
plt.close()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
ax1.plot(annual['Year'], annual['NH_Anomaly'], linewidth=2, color='#C73E1D', label='Northern Hemisphere', alpha=0.8)
ax1.plot(annual['Year'], annual['SH_Anomaly'], linewidth=2, color='#6C9BD2', label='Southern Hemisphere', alpha=0.8)
ax1.fill_between(annual['Year'], annual['NH_Anomaly'], annual['SH_Anomaly'], alpha=0.2, color='#6C757D')
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Temperature Anomaly (°C)', fontsize=12, fontweight='bold')
ax1.set_title('Hemispheric Temperature Anomalies Comparison', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax1.grid(True, alpha=0.3, linestyle='--')

ax2.plot(annual['Year'], annual['Land_Anomaly'], linewidth=2, color='#A23B72', label='Land Surfaces', alpha=0.8)
ax2.plot(annual['Year'], annual['Ocean_Anomaly'], linewidth=2, color='#2E86AB', label='Ocean Surfaces', alpha=0.8)
ax2.fill_between(annual['Year'], annual['Land_Anomaly'], annual['Ocean_Anomaly'], alpha=0.2, color='#6C757D')
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Temperature Anomaly (°C)', fontsize=12, fontweight='bold')
ax2.set_title('Land vs Ocean Temperature Anomalies Comparison', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax2.grid(True, alpha=0.3, linestyle='--')
plt.suptitle('Regional Temperature Variations (1880-2025)', fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('figure4_regional.png', dpi=300, bbox_inches='tight')
plt.close()

annual_sorted = annual.sort_values('Year')
annual_sorted['Cumulative_Max'] = annual_sorted['Global_Anomaly'].cummax()
annual_sorted['Is_Record'] = annual_sorted['Global_Anomaly'] >= annual_sorted['Cumulative_Max']
record_years = annual_sorted[annual_sorted['Is_Record']].copy()

fig, ax = plt.subplots(figsize=(14, 7))
ax.scatter(annual_sorted['Year'], annual_sorted['Global_Anomaly'], alpha=0.3, s=30, 
           color='#2E86AB', label='All Years')
ax.scatter(record_years['Year'], record_years['Global_Anomaly'], s=150, color='#C73E1D', 
           marker='*', edgecolors='black', linewidths=1.5, zorder=5, label='Record Warm Years')
z = np.polyfit(annual_sorted['Year'], annual_sorted['Global_Anomaly'], 1)
p = np.poly1d(z)
ax.plot(annual_sorted['Year'], p(annual_sorted['Year']), "--", linewidth=2, 
        color='#F18F01', alpha=0.7, label='Linear Trend')
recent_records = record_years[record_years['Year'] >= 2000]
for _, row in recent_records.iterrows():
    ax.annotate(f"{int(row['Year'])}\n{row['Global_Anomaly']:.2f}°C",
               xy=(row['Year'], row['Global_Anomaly']), xytext=(10, 10), textcoords='offset points',
               fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
               arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3)
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=13, fontweight='bold')
ax.set_title('Record-Breaking Warm Years (1880-2025)', fontsize=15, fontweight='bold', pad=20)
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('figure5_extreme_years.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations generated successfully.")
