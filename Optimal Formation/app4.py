from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set Agg backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load your dataset
df = pd.read_excel('C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Optimal Formation/Dataset/Spa/Matches 22-23.xlsx')

# Function to calculate formation counts for a given team
def calculate_formation_counts(team):
    team_data = df[df['Team'] == team]
    result_counts = team_data['Formation'].value_counts()
    return result_counts

@app.route('/')
def index():
    # Get unique team names
    teams = df['Team'].unique()
    return render_template('index4.html', teams=teams)


@app.route('/get_formation', methods=['POST'])
def get_formation():
    team = request.form['team']
    formation_counts = calculate_formation_counts(team)

    # Plotting pie chart
    labels = formation_counts.index.tolist()
    sizes = formation_counts.values.tolist()
    explode = [0.1] * len(labels)  # Explode all slices for better visualization
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title(f'Formations for {team}')
    
    # Convert plot to base64 encoded string
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    # Specify custom colors for the key
    custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    key = {label: color for label, color in zip(labels, custom_colors)}
    
    # Get the best formation
    best_formation = formation_counts.idxmax()

    # Get unique team names
    teams = df['Team'].unique()
    return render_template('formation4.html', team=team, plot_data=plot_data, teams=teams, best_formation=best_formation, key=key)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5014)
