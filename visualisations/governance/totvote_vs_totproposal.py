
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('simulated_data.csv')
def ens_analysis(total_vote_range=None, total_proposal_range=None):
    filtered_data = data.copy()
    if total_vote_range:
        filtered_data = filtered_data[(filtered_data['totalVotes'] >= total_vote_range[0]) & (filtered_data['totalVotes'] <= total_vote_range[1])]
    if total_proposal_range:
        filtered_data = filtered_data[(filtered_data['totalProposalInteraction'] >= total_proposal_range[0]) & (filtered_data['totalProposalInteraction'] <= total_proposal_range[1])]

    grouped_data = filtered_data.groupby('ensName').agg({'totalVotes': 'sum', 'totalProposalInteraction': 'sum'}).reset_index()
    grouped_data.sort_values('totalVotes', ascending=True, inplace=True)

    # viz
    fig = go.Figure(data=[
        go.Bar(name='Total Votes', x=grouped_data['ensName'], y=grouped_data['totalVotes']),
        go.Bar(name='Total Proposal Interaction', x=grouped_data['ensName'], y=grouped_data['totalProposalInteraction'])
    ])

    fig.update_layout(barmode='stack', xaxis_title='ENS Name', yaxis_title='Count',
                      title='Total Votes and Total Proposal Interaction by ENS Name')

    return fig

# Example usage
fig_ens_analysis = ens_analysis(total_vote_range=(1900, 2000), total_proposal_range=(90, 100))

fig_ens_analysis.show()

