from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

team_datasets = {
    "Barcelona": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Barcelona.xlsx",
    "Real Madrid": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Real Madrid.xlsx",
    "Atlético Madrid": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Atlético Madrid.xlsx",
    "Real Sociedad": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Real Sociedad.xlsx",
    "Villarreal": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Villarreal.xlsx",
    "Real Betis": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Real Betis.xlsx",
    "Osasuna": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Osasuna.xlsx",
    "Athletic Club": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Athletic Club.xlsx",
    "Mallorca": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Mallorca.xlsx",
    "Girona": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Girona.xlsx",
    "Rayo Vallecano": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Rayo Vallecano.xlsx",
    "Sevilla": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Sevilla.xlsx",
    "Celta Vigo": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Celta Vigo.xlsx",
    "Cádiz": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Cádiz.xlsx",
    "Getafe": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Getafe.xlsx",
    "Valencia": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Valencia.xlsx",
    "Almería": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Almería.xlsx",
    "Valladolid": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Valladolid.xlsx",
    "Espanyol": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Espanyol.xlsx",
    "Elche": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Spa/22-23/Elche.xlsx"
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
            return render_template('index4.html', 
                                   team=selected_team, 
                                   forward_midfield_players=forward_midfield_players, 
                                   defender_players=defender_players,
                                   teams=remaining_teams)  
        else:
            return render_template('index4.html', error="Team dataset not found.")
    else:
        return render_template('index4.html', teams=team_datasets.keys())


if __name__ == '__main__':
    app.run(debug=True, port=5004)
