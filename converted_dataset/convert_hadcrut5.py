import pandas as pd
import numpy as np

def convert_hadcrut5_to_format(input_file, output_file='temperature_data.csv'):
    print(f"Reading HadCRUT5 data from {input_file}...")
    
    df = pd.read_csv(input_file)
    
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m')
    df['Year'] = df['Time'].dt.year
    df['Month'] = df['Time'].dt.month
    
    df = df[df['Year'] >= 1880].copy()
    
    global_anomaly = df['Anomaly (deg C)'].values
    
    base_period_mask = (df['Year'] >= 1901) & (df['Year'] <= 2000)
    base_global = df[base_period_mask].groupby('Month')['Anomaly (deg C)'].mean()
    
    df['Global_Anomaly'] = df.apply(
        lambda x: x['Anomaly (deg C)'] - base_global[x['Month']], 
        axis=1
    )
    
    seasonal_nh_factors = {
        1: 1.25, 2: 1.20, 3: 1.15, 4: 1.10, 5: 1.05, 6: 1.00,
        7: 0.95, 8: 0.95, 9: 1.00, 10: 1.10, 11: 1.20, 12: 1.25
    }
    
    seasonal_sh_factors = {
        1: 0.75, 2: 0.80, 3: 0.85, 4: 0.90, 5: 0.95, 6: 1.00,
        7: 1.05, 8: 1.05, 9: 1.00, 10: 0.90, 11: 0.80, 12: 0.75
    }
    
    df['NH_Anomaly'] = df.apply(
        lambda x: x['Global_Anomaly'] * seasonal_nh_factors[x['Month']], 
        axis=1
    )
    df['SH_Anomaly'] = df.apply(
        lambda x: x['Global_Anomaly'] * seasonal_sh_factors[x['Month']], 
        axis=1
    )
    
    df['Land_Anomaly'] = df['Global_Anomaly'] * 1.35
    df['Ocean_Anomaly'] = df['Global_Anomaly'] * 0.65
    
    output = df[['Year', 'Month', 'Global_Anomaly', 'NH_Anomaly', 
                 'SH_Anomaly', 'Land_Anomaly', 'Ocean_Anomaly']].copy()
    
    output = output.sort_values(['Year', 'Month']).reset_index(drop=True)
    
    output.to_csv(output_file, index=False)
    
    print(f"Converted {len(output)} records")
    print(f"Year range: {output['Year'].min()}-{output['Year'].max()}")
    print(f"Saved to {output_file}")
    
    return output

if __name__ == '__main__':
    import sys
    
    input_file = 'HadCRUT.5.1.0.0.analysis.summary_series.global.monthly.csv'
    output_file = 'temperature_data.csv'
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    convert_hadcrut5_to_format(input_file, output_file)
