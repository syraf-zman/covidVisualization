import matplotlib.pyplot as plt

def plot_pie():
    # Data
    pfizer = 45059689
    sinovac = 21571049
    AstraZeneca = 5708446
    Sinophram = 44296
    CanSino = 226626
    # Pie chart labels and values
    labels = ['Pfizer', 'Sinovac', 'AstraZeneca', 'Sinophram', 'CanSino']
    values = [pfizer, sinovac, AstraZeneca, Sinophram, CanSino]

    # Create pie chart
    plt.pie(values, labels=None, autopct='%1.1f%%')

    # Add a title
    plt.title('Distribution of vaccine manufacturers used in Malaysia.  ')

    # Create legend
    plt.legend(labels=[f'{label} ({value / sum(values) * 100:.1f}%)\n{value:,}' for label, value in zip(labels, values)]
            , loc='upper right', bbox_to_anchor=(1.515, 1))
