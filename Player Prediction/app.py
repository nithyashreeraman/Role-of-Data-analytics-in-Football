from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

team_datasets = {
    "Bayern Munich": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Bayern Munich.xlsx",
    "Dortmund": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Dortmund.xlsx",
    "Leverkusen": "C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Leverkusen.xlsx",
    "RB Leipzig":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/RB_Leipzig.xlsx",
    "Union Berlin":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Union_Berlin.xlsx",
    "Freiburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Freiburg.xlsx",
    "Köln":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Köln.xlsx",
    "Mainz":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Mainz.xlsx",
    "Hoffenheim":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Hoffenheim.xlsx",
    "Monchengladbach":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Monchengladbach.xlsx",
    "Eintracht Frankfurt":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Eintracht_Frankfurt.xlsx",
    "Wolfsburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Wolfsburg.xlsx",
    "Bochum":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Bochum.xlsx",
    "Augsburg":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Augsburg.xlsx",
    "Stuttgart":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Stuttgart.xlsx",
    "Hertha BSC":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Hertha_BSC.xlsx",
    "Arminia Bielefeld":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Ger/21-22/Dataset/Arminia_Bielefeld.xlsx",
    "Greuther Furth":"C:/Users/91940/Desktop/College/College/VIT/College/Year/8th Sem/Capstone/Code/Player Prediction/Dataset/Ger/21-22/Greuther_Furth.xlsx",
    
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
            return render_template('index.html', 
                                   team=selected_team, 
                                   forward_midfield_players=forward_midfield_players, 
                                   defender_players=defender_players,
                                   teams=remaining_teams)  
        else:
            return render_template('index.html', error="Team dataset not found.")
    else:
        return render_template('index.html', teams=team_datasets.keys())


if __name__ == '__main__':
    app.run(debug=True, port=5001)
