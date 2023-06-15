import matplotlib.pyplot as plt

def plot_line():
    dates = ['Mac 21', 'Apr 21', 'May 21', 'Jun 21', 'July 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21']
    new_deaths = [137, 234, 1290, 2374, 3854, 7638, 9669, 2577, 1515, 1063]
    vaccine_administered = [688273, 757204, 1578666, 5260951, 12817487, 14444816, 9402941, 5725986, 3014627, 4125648]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(dates, new_deaths, marker='o', linestyle='-', color='b', label='New Deaths')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('New Deaths', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(dates, vaccine_administered, marker='o', linestyle='-', color='r', label='Vaccine Administered')
    ax2.set_ylabel('Vaccine Administered', color='r')
    ax2.tick_params('y', colors='r')

    plt.title('New Deaths vs Vaccine Administered in Malaysia in 2021')
    plt.xticks(rotation=45)

    plt.tight_layout()