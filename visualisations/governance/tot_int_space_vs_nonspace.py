
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('simulated_data.csv')
def proposal_interaction_analysis(total_vote_range=None, total_proposal_range=None):
    # Filter data based on total_vote_range and total_proposal_range
    filtered_data = data.copy()
    if total_vote_range:
        filtered_data = filtered_data[(filtered_data['totalVotes'] >= total_vote_range[0]) & (filtered_data['totalVotes'] <= total_vote_range[1])]
    if total_proposal_range:
        filtered_data = filtered_data[(filtered_data['totalProposalInteraction'] >= total_proposal_range[0]) & (filtered_data['totalProposalInteraction'] <= total_proposal_range[1])]

    # Group the data by ENS name and calculate the sum of total proposal interaction in space and non-space
    grouped_data = filtered_data.groupby('ensName').agg({'totalProposalInteractionInSpace': 'sum', 'totalProposalInteractionNonSpace': 'sum'}).reset_index()

    # Create the bar chart for total proposal interaction in space and non-space
    fig = go.Figure(data=[
        go.Bar(name='In Space', x=grouped_data['ensName'], y=grouped_data['totalProposalInteractionInSpace']),
        go.Bar(name='Non-Space', x=grouped_data['ensName'], y=grouped_data['totalProposalInteractionNonSpace'])
    ])

    fig.update_layout(barmode='stack', xaxis_title='ENS Name', yaxis_title='Count',
                      title='Proposal Interaction Analysis: Total Proposal Interaction (In Space vs. Non-Space)')

    return fig

# Example usage
fig_proposal_interaction = proposal_interaction_analysis(total_vote_range=(1000, 1200), total_proposal_range=(95, 100))

# Display the proposal interaction chart
fig_proposal_interaction.show()

