# data_worldcup2022

# Football Match Analysis Tool

This project provides tools to analyze football (soccer) matches, using data from the [StatsBomb API](https://github.com/statsbomb/statsbombpy) and visualizations with [mplsoccer](https://mplsoccer.readthedocs.io/en/latest/). You can select matches from the 2022 FIFA World Cup.

## Features

- Fetch match data from the World Cup (group stages to finals).
- Select and analyze specific players for passing data.
- Generate pitch visualizations of passes, shots (excluding penalties), and heatmaps.

## Requirements

- Python 3.7 or higher
- Libraries:
  - `statsbombpy`
  - `mplsoccer`
  - `numpy`
  - `pandas`
  - `matplotlib`

You can install these dependencies using the following command:

```
pip3 install statsbombpy mplsoccer kloppy numpy pandas matplotlib
```

# Usage

## Clone the repository
```
git clone https://github.com/Dinamochenko/data_worldcup2022.git
cd data_worldcup2022
```
## Run the script
`python3 main.py`

## Instructions:
- Select a match from the list by entering its ID.
- Choose a player from each team to analyze passes.
- Visualize passes, shots (excluding penalties), and heatmaps for the selected players and teams.
- Close all visualization windows to analyze another match

# Example
After selecting a match, you will see options for choosing players from the home and away teams. Based on your selection, the tool will generate visualizations:

- Pass Map: Shows the passing patterns of a selected player.
![LionelMessi](https://github.com/user-attachments/assets/4bf32352-de66-4bb6-a5d6-c8acf4919646)
![KylianMbappe](https://github.com/user-attachments/assets/aab95c3e-a040-4a77-b4b3-93fcd901b7df)

- Shot Map (excluding penalties): Displays all the shots taken by a team.
![ShotsArgentina](https://github.com/user-attachments/assets/7a39fa3b-14f8-4419-a732-505afd0d2222)
![ShotsFrance](https://github.com/user-attachments/assets/ba3a9e9e-50b9-42f9-a905-df180ca6bbd8)

- Heatmap: Illustrates the concentration of player movements during the match, visualized through a heatmap.
![ArgentinaHeatMap](https://github.com/user-attachments/assets/7a6e9496-6a23-4472-a0e1-5ad21c28ea68)
![FranceHeatMap](https://github.com/user-attachments/assets/c4129c13-b826-4039-99ad-47a8fe5da9c7)


### Available Stages
- Group Stage
- Round of 16
- Quarter-finals
- Semi-finals
- 3rd Place Final
- Final
