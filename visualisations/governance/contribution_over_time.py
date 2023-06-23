import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('simulated_data.csv')
def contribution_over_time_analysis(data, date_column, count_column):
    data[date_column] = pd.to_datetime(data[date_column])
    data['month'] = data[date_column].dt.month
    data['year'] = data[date_column].dt.year

    data = data[data['year'] >= 2022]
    contribution_counts = data.groupby(['year', 'month'])[count_column].size().reset_index(name='count')

    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(data=contribution_counts, x='month', y='count', hue='year', palette='Set2', alpha=0.8)
    ax.fill_between(contribution_counts['month'], contribution_counts['count'], alpha=0.2)
    plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Contributions Over Time')
    plt.legend(title='Year')
    plt.show()

# Example usage
contribution_over_time_analysis(data, 'date_created', 'totalProposalInteraction')