from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

team_datasets = {
    "Real Madrid": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Real Madrid.xlsx",
    "Barcelona": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Barcelona.xlsx",
    "Atlético Madrid": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Atlético Madrid.xlsx",
    "Sevilla": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Sevilla.xlsx",
    "Real Betis": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Real Betis.xlsx",
    "Real Sociedad": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Real Sociedad.xlsx",
    "Villarreal": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Villarreal.xlsx",
    "Athletic Club": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Athletic Club.xlsx",
    "Valencia": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Valencia.xlsx",
    "Osasuna": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Osasuna.xlsx",
    "Celta Vigo": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Celta Vigo.xlsx",
    "Rayo Vallecano": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Rayo Vallecano.xlsx",
    "Elche": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Elche.xlsx",
    "Espanyol": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Espanyol.xlsx",
    "Getafe": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Getafe.xlsx",
    "Mallorca": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Mallorca.xlsx",
    "Cádiz": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Cádiz.xlsx",
    "Granada": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Granada.xlsx",
    "Levante": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Levante.xlsx",
    "Alavés": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/21-22/Alavés.xlsx"
}

def get_player_data(file_path):
    df = pd.read_excel(file_path)
    forward_midfield_players = df[df['Pos'].str.contains('FW|MF', na=False)].sort_values(by='G+A/90', ascending=False)
    defender_players = df[df['Pos'] == 'DF'].sort_values(by=['PrgP', 'PrgR'], ascending=False)
    return forward_midfield_players.to_html(index=False), defender_players.to_html(index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_team = request.form['team']
        if selected_team in team_datasets:
            forward_midfield_players, defender_players = get_player_data(team_datasets[selected_team])
            remaining_teams = [team for team in team_datasets.keys() if team != selected_team]
            return render_template('index3.html', 
                                   team=selected_team, 
                                   forward_midfield_players=forward_midfield_players, 
                                   defender_players=defender_players,
                                   teams=remaining_teams)  
        else:
            return render_template('index3.html', error="Team dataset not found.")
    else:
        return render_template('index3.html', teams=team_datasets.keys())


if __name__ == '__main__':
    app.run(debug=True, port=5003)
