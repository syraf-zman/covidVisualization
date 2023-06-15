import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('Set2')
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

import csv


def plot_line():
    data=pd.read_csv('deaths_state2.csv')

    # Convert the 'date' column to datetime type
    data['date'] = pd.to_datetime(data['date'])

    # Filter the data for the year 2021
    data_2021 = data[data['date'].dt.year == 2021]

    # Calculate the sum of mortality cases per month for W.P. Putrajaya
    putrajaya_data_2021 = data_2021[data_2021['state'] == 'W.P. Putrajaya']
    putrajaya_monthly_deaths = putrajaya_data_2021.groupby(data_2021['date'].dt.month)['deaths_new'].sum()

    # Calculate the sum of mortality cases per month for Kelantan
    kelantan_data_2021 = data_2021[data_2021['state'] == 'Kelantan']
    kelantan_monthly_deaths = kelantan_data_2021.groupby(data_2021['date'].dt.month)['deaths_new'].sum()

    # Define date_ranges with month values
    date_ranges = [(2021, month) for month in range(0, 12)]  # January to December

    # Plotting the line chart
    plt.figure(figsize=(12, 6))
    plt.plot([month for (_, month) in date_ranges], putrajaya_monthly_deaths, label='W.P. Putrajaya')
    plt.plot([month for (_, month) in date_ranges], kelantan_monthly_deaths, label='Kelantan')
    plt.xlabel('Month')
    plt.ylabel('Sum of Mortality Cases')
    plt.title('Trends in Mortality Cases (2021) - W.P. Putrajaya vs Kelantan')
    plt.legend()
    plt.grid(True)
