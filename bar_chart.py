import pandas as pd
import numpy as np

import seaborn as sns
sns.set_palette('Set2')
import matplotlib.pyplot as plt

import csv

def plot_bar():
    df=pd.read_csv('vax_state.csv')

    # Assuming you have a DataFrame named 'df' containing the vaccination data
    # Convert the 'date' column to Timestamp
    df['date'] = pd.to_datetime(df['date'])

    # Define the population for each state
    population = {
        'Johor': 4000000,
        'Kedah': 2200000,
        'Kelantan': 1800000,
        'Melaka': 1000000,
        'Negeri Sembilan': 1200000,
        'Pahang': 1600000,
        'Perak': 2500000,
        'Perlis': 300000,
        'Pulau Pinang': 1700000,
        'Sabah': 3400000,
        'Sarawak': 2500000,
        'Selangor': 7000000,
        'Terengganu': 1200000,
        'W.P. Kuala Lumpur': 2000000,
        'W.P. Labuan': 100000,
        'W.P. Putrajaya': 100000
    }

    # Filter the data from date 2/24/2021 to 12/31/2021
    start_date = pd.to_datetime('2021-02-24')
    end_date = pd.to_datetime('2021-12-31')
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)].copy()

    # Calculate the vaccination rate for each state as a percentage
    filtered_df.loc[:, 'vaccination_rate'] = (filtered_df.groupby('state')['daily'].transform('sum') / (filtered_df['state'].map(population) * 4)) * 100

    # Calculate the vaccination rate for each state
    vaccination_rate = filtered_df.groupby('state')['vaccination_rate'].mean()

    # Sort the states and vaccination rates in ascending order
    sorted_indices = np.argsort(vaccination_rate)
    sorted_states = [state for state in vaccination_rate.index[sorted_indices]]
    sorted_vaccination_rate = [vaccination_rate[i] for i in sorted_indices]

    # Create a horizontal bar chart
    plt.barh(sorted_states, sorted_vaccination_rate)

    # Set the title and labels
    plt.title("Vaccination Rate against COVID-19 in Malaysia (2021)")
    plt.xlabel("Vaccination Rate (%)")
    plt.ylabel("State")

    # Add the values at the end of each bar
    for i, rate in enumerate(sorted_vaccination_rate):
        plt.text(rate, i, f"{rate:.2f}", ha='left', va='center')
