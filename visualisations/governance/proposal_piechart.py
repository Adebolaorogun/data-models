import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('simulated_data.csv')
def proposal_interaction_range_pie_chart(total_proposal_range):
    # Filter the data based on the specified total proposal interaction range
    filtered_data = data[(data['totalProposalInteraction'] >= total_proposal_range[0]) &
                         (data['totalProposalInteraction'] <= total_proposal_range[1])]

    # Get the filtered ENS names
    filtered_ens_names = filtered_data['ensName'].unique()

    # Calculate the percentage of ENS names in the filtered data compared to the total ENS names
    filtered_percentage = len(filtered_ens_names) / len(data['ensName'].unique()) * 100

    # Calculate the percentage of ENS names not in the filtered data
    remaining_percentage = 100 - filtered_percentage

    # Create a pie chart to visualize the percentages
    labels = ['filtered Ens names', 'Remaining ENS Names']
    values = [filtered_percentage, remaining_percentage]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig.update_layout(title='Percentage of ENS Names based on proposal interaction in Filtered Range',
                      showlegend=True)

    fig.show()


# Example usage
proposal_interaction_range_pie_chart([100, 500])