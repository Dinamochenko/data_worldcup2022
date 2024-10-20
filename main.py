from statsbombpy import sb
import mplsoccer as mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, to_hex

CDM_COMPETITION_ID = 43
CDM_SEASON_ID = 106


stages = [
    ("GROUP STAGE MATCHES", "Group Stage"),
    ("ROUND OF 16 MATCHES", "Round of 16"),
    ("QUARTER-FINALS MATCHES", "Quarter-finals"),
    ("SEMI-FINALS MATCHES", "Semi-finals"),
    ("3RD PLACE FINAL MATCHES", "3rd Place Final"),
    ("FINAL MATCHES", "Final")
]

def choose_match(matches):
    infos = []
    for stage_name, stage in stages:
        print(stage_name)
        stage_matches = matches[matches['competition_stage'] == stage]

        for index, data in stage_matches.iterrows():
            print(f"{data['match_id']} | {data['home_team']} vs {data['away_team']}" )
            info = {'id': data['match_id'], 
                     'home_team' : data['home_team'], 
                     'away_team' : data['away_team'],
                     'home_score': data['home_score'],
                     'away_score': data['away_score']}
            infos.append(info)
        print()

    return infos

def choose_home_player(match_id_int, home_team):
        players_home = []
        players_home_selected = []

        home_player = get_lineups(match_id_int, home_team)
        
        for index, row in home_player.iterrows():
            print(f"ID: {row['player_id']} | Name: {row['player_name']}")
            home_player_to_add = {
            'id': row['player_id'],
            'name': row['player_name']
            }
            players_home.append(home_player_to_add)
        
        while(42):
            print(f'\nChoose a player from {home_team}')
            home_player_id = int(input())

            for player_home in players_home:
                if home_player_id == player_home['id']:
                    players_home_selected.append(player_home)
                    print('\n')
                    return players_home_selected
            
            print("\nThe ID doesn't exist start again\n")

def choose_away_player(match_id_int, away_team):
        players_away = []
        players_away_selected = []

        away_player = get_lineups(match_id_int, away_team)
        for index, row in away_player.iterrows():
            print(f"ID: {row['player_id']} | Name: {row['player_name']}")
            away_player_to_add = {
            'id': row['player_id'],
            'name': row['player_name']
            }
            players_away.append(away_player_to_add)
        
        while(42):
            print(f'\nChoose a player from {away_team}')
            away_player_id = int(input())

            for player_away in players_away:
                if away_player_id == player_away['id']:
                    players_away_selected.append(player_away)
                    print('\n')
                    return players_away_selected
            
            print("\nThe ID doesn't exist start again\n")

def choose_players(match_id_int, home_team, away_team):
    players_home_selected = choose_home_player(match_id_int, home_team)
    players_away_selected = choose_away_player(match_id_int, away_team)
    
    return players_home_selected, players_away_selected
        

def get_event_match_id(match_id):
    events = sb.events(match_id = match_id)
    return events


def get_lineups(match_id, team):
    return sb.lineups(match_id=match_id)[team]

##PITCH
def show_pitch_passes(x1, y1, x2, y2, title):
    pitch = mpl.Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw(figsize=(9, 6))

    p = pitch.arrows(x1, y1, x2, y2, alpha=0.8, color="red", headaxislength=3, headlength=3, headwidth=4, width=2, ax=ax)
    ax.set_title(title, fontsize=20)

def show_pitch_shot(x, y, xg, goal, title):
    pitch = mpl.Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw(figsize=(9, 6))
    p = pitch.scatter(x, y, s=xg*100, c=goal, alpha=0.8, ax=ax)
    ax.set_title(title, fontsize=20)

def show_heatmap(x, y, title):
    pitch = mpl.Pitch()
    fig, ax = pitch.draw(figsize=(9, 6))
    k = pitch.kdeplot(x, y, cmap='Reds', fill=True, levels=10, alpha=0.8, ax=ax)
    ax.set_title(title, fontsize=20)

def display_pitch():
    plt.show()


## ANALYSIS

def passes_analysis(events, player_id, name):
    try:
        passes = events[(events['type'] == "Pass") & (events['player_id'] == player_id)]
        coordinates = passes[['location', 'pass_end_location']]
        x1, y1 = np.array(coordinates['location'].tolist()).T
        x2, y2 = np.array(coordinates['pass_end_location'].tolist()).T
        title = f"Pass : {name}"
        show_pitch_passes(x1, y1, x2, y2, title)
        return 1
    except:
        return 0

def shot_analysis_without_penalty(events, team):
    shots = events[(events['type'] == "Shot") & (events['team'] == team) & (events['shot_type'] != "Penalty")]
    x, y = np.array(shots['location'].tolist()).T
    xg = np.array(shots['shot_statsbomb_xg'].tolist())
    goal = ["red" if g == "Goal" else 'black' for g in shots['shot_outcome'].to_list()]
    title = f"Shot without Penalties : {team}"
    show_pitch_shot(x, y, xg, goal, title)

def heatmaps(events, team):
    arg_events = events[~pd.isna(events['location']) &
                    (events['team'] == team)]
    x, y = np.array(arg_events['location'].tolist()).T
    title = f"Heatmap : {team}"
    show_heatmap(x, y, title)




def main():

    while(42):
        matches = sb.matches(competition_id=CDM_COMPETITION_ID, season_id=CDM_SEASON_ID)
        infos = choose_match(matches)

        print("Please type the ID of the match choosen : ")
        
        match_id = input()
        match_id_int = int(match_id)
        
        for info in infos:
            found = 0
            if match_id_int == info["id"]:
                print(f'\nYou choose {info["home_team"]} vs {info["away_team"]} | Score {info["home_score"]} - {info["away_score"]}\n')
                event = get_event_match_id(match_id)
                
                players_home_selected, players_away_selected = choose_players(match_id_int, info["home_team"], info["away_team"])

                good_player_home = 0
                good_player_away = 0
                
                while good_player_home == 0 or good_player_away == 0 :
                    if (good_player_home == 0):
                        good_or_not_home = passes_analysis(event, int(players_home_selected[0]["id"]), players_home_selected[0]["name"])
                    if (good_player_away == 0):
                        good_or_not_away = passes_analysis(event, int(players_away_selected[0]["id"]), players_away_selected[0]["name"])
                    
                    if good_or_not_home == 1:
                        good_player_home = 1
                    if good_or_not_away == 1:
                        good_player_away = 1
                    
                    if good_player_home == 0:
                        print(f"\nImpossible to fetch data for the choosen player. Select another player from {info['home_team']}\n")
                        players_home_selected = choose_home_player(match_id_int, info["home_team"])
                    
                    if good_player_away == 0:
                        print(f"\nImpossible to fetch data for the choosen player. Select another player from {info['away_team']}\n")
                        players_away_selected = choose_away_player(match_id_int, info["away_team"])


                shot_analysis_without_penalty(event, info["home_team"])
                shot_analysis_without_penalty(event, info["away_team"])

                heatmaps(event, info["home_team"])
                heatmaps(event, info["away_team"])
                
                print("\nClose all the windows to search a new match !\n")
                display_pitch()
                
                found = 1
        
        if found == 0:
            print("\nThe ID doesn't exists start again\n")
    

main()