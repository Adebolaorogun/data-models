from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import uuid

app = Flask(__name__)

# Load the simulated data from the CSV file
data = pd.read_csv('simulated_data.csv')

# Define the available columns for user selection
available_columns = {
    'totalVotes': 'Total Votes',
    'op_token': 'OP Token',
    'op_tokens_voting': 'OP Tokens for Voting',
    'followCount': 'Follow Count',
    'totalProposalInteraction': 'Total Proposal Interaction',
    'totalNft': 'Total NFT'
}

# Home page
@app.route('/')
def home():
    return render_template('base.html')

# Governance Model
@app.route('/governance', methods=['GET', 'POST'])
def governance():
    if request.method == 'POST':
        column = request.form.get('column')
        value = int(request.form.get('value'))
        
        if column and value:
            # Perform analysis based on column and value
            if column == 'totalVotes':
                votes_count = data[column].value_counts()
                top_voters = votes_count[votes_count >= value].head(10)
                
                # Visualization: Bar chart for top voters
                plt.figure(figsize=(10, 6))
                plt.bar(top_voters.index, top_voters.values)
                plt.xlabel('Wallet Address')
                plt.ylabel('Total Votes')
                plt.title('Top Voters')
                plt.xticks(rotation=45)
                chart_image = f'governance_votes_{uuid.uuid4()}.png'
                plt.savefig(f'static/images/{chart_image}')
                plt.close()

            elif column == 'totalProposalInteraction':
                interactions_count = data[column].value_counts()
                top_interactors = interactions_count[interactions_count >= value].head(10)
                
                # Visualization: Bar chart for top interactors
                plt.figure(figsize=(10, 6))
                plt.bar(top_interactors.index, top_interactors.values)
                plt.xlabel('Wallet Address')
                plt.ylabel('Total Interactions')
                plt.title('Top Interactors')
                plt.xticks(rotation=45)
                chart_image = f'governance_interactions_{uuid.uuid4()}.png'
                plt.savefig(f'static/images/{chart_image}')
                plt.close()

            # Add more analysis options based on other columns

            return render_template('governance.html', column=column, value=value, chart_image=chart_image)

    return render_template('governance.html', columns=available_columns)

# Reputation Model
@app.route('/reputation', methods=['GET', 'POST'])
def reputation():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('reputation.html', column=selected_column, value=selected_value)

    return render_template('reputation.html', columns=available_columns)

# Token Voting Model
@app.route('/token_voting', methods=['GET', 'POST'])
def token_voting():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('token_voting.html', column=selected_column, value=selected_value)

    return render_template('token_voting.html', columns=available_columns)

# NFT Interaction Model
@app.route('/nft_interaction', methods=['GET', 'POST'])
def nft_interaction():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('nft_interaction.html', column=selected_column, value=selected_value)

    return render_template('nft_interaction.html', columns=available_columns)

# Social Media Model
@app.route('/social_media', methods=['GET', 'POST'])
def social_media():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('social_media.html', column=selected_column, value=selected_value)

    return render_template('social_media.html', columns=available_columns)

if __name__ == '__main__':
    app.run(debug=True)
