from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

team_datasets = {
    "Bayern Munich": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Bayern_Munich.xlsx",
    "Dortmund": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Dortmund.xlsx",
    "RB Leipzig":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/RB_Leipzig.xlsx",
    "Union Berlin":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Union_Berlin.xlsx",
    "Freiburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Freiburg.xlsx",
    "Leverkusen": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Leverkusen.xlsx",
    "Eintracht Frankfurt":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Eintracht_Frankfurt.xlsx",
    "Wolfsburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Wolfsburg.xlsx",
    "Mainz":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Mainz.xlsx",
    "Monchengladbach":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Monchengladbach.xlsx",
    "Koln":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Koln.xlsx",
    "Hoffenheim":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Hoffenheim.xlsx",
    "Werder Bremen":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Werder_Bremen.xlsx",
    "Bochum":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Bochum.xlsx",
    "Eintracht Frankfurt":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Eintracht_Frankfurt.xlsx",
    "Augsburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Augsburg.xlsx",
    "Stuttgart":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Stuttgart.xlsx",
    "Schalke":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Schalke.xlsx",
    "Hertha BSC":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/22-23/Hertha_BSC.xlsx"
    
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
            return render_template('index2.html', 
                                   team=selected_team, 
                                   forward_midfield_players=forward_midfield_players, 
                                   defender_players=defender_players,
                                   teams=remaining_teams) 
        else:
            return render_template('index2.html', error="Team dataset not found.")
    else:
        return render_template('index2.html', teams=team_datasets.keys())


if __name__ == '__main__':
    app.run(debug=True,port=5002)
