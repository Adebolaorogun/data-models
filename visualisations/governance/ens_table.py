import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('simulated_data.csv')
import pandas as pd
import plotly.graph_objects as go

def generate_ens_table(total_vote_range, total_proposal_range, data):
   
    filtered_data = data[(data['totalVotes'].between(*total_vote_range)) &
                         (data['totalProposalInteraction'].between(*total_proposal_range))]

    
    ens_names = filtered_data['ensName'].unique()

   
    ens_table = pd.DataFrame({'ENS Name': ens_names})

    ens_table['Total Votes'] = ens_table['ENS Name'].apply(lambda x: filtered_data[filtered_data['ensName'] == x]['totalVotes'].sum())
    ens_table['Total Proposal Interaction'] = ens_table['ENS Name'].apply(lambda x: filtered_data[filtered_data['ensName'] == x]['totalProposalInteraction'].sum())

    return ens_table

# Example usage
total_vote_range = (1000, 2000)  # Replace with the actual total vote range
total_proposal_range = (90, 100)  # Replace with the actual total proposal range
ens_table = generate_ens_table(total_vote_range, total_proposal_range, data)

# viz
fig = go.Figure(data=[go.Table(
    header=dict(values=list(ens_table.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[ens_table['ENS Name'], ens_table['Total Votes'], ens_table['Total Proposal Interaction']],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(title='ENS Names Based on Total Vote and Total Proposal Ranges')
fig.show()
