import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('simulated_data.csv')


def ens_analysis(ens_names):
  
    filtered_data = data[data['ensName'].isin(ens_names)]

    x_values = list(ens_names)
    total_votes = []
    total_proposal_interaction = []

    for ens_name in ens_names:
        ens_data = filtered_data[filtered_data['ensName'] == ens_name]
        total_votes.append(ens_data['totalVotes'].iloc[0])
        total_proposal_interaction.append(ens_data['totalProposalInteraction'].iloc[0])

    sorted_indices = sorted(range(len(total_votes)), key=lambda k: total_votes[k], reverse=True)
    sorted_x_values = [x_values[i] for i in sorted_indices]
    sorted_total_votes = [total_votes[i] for i in sorted_indices]
    sorted_total_proposal_interaction = [total_proposal_interaction[i] for i in sorted_indices]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=sorted_x_values, y=sorted_total_votes, name='Total Votes'))
    fig.add_trace(go.Bar(x=sorted_x_values, y=sorted_total_proposal_interaction, name='Total Proposal Interaction'))

    fig.update_layout(
        title='Total Votes and Proposal Interaction by ENS Name',
        xaxis_title='ENS Name',
        yaxis_title='Count',
        barmode='group'
    )

    fig.show()



# Example usage
names = [
 'a68cdb55',
 '26474088',
 'db462029',
 '16b7fdbc',
 '1526d396',
 '3f63107e',
 'd5eb9a2c',
 '66b94da0',
 '5e008061'
 ]
ens_analysis(names)

