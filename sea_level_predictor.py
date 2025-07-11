import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # First line of best fit (1880–2050)
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, result.slope * years_extended + result.intercept,
             'r', label='Best Fit Line: 1880–2050')

    # Second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    recent_result = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, recent_result.slope * years_recent + recent_result.intercept,
             'g', label='Best Fit Line: 2000–2050')

    # Plot formatting
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Save and return figure
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
