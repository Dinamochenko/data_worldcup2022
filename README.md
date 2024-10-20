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


- Shot Map (excluding penalties): Displays all the shots taken by a team.
- Heatmap: Illustrates the concentration of player movements during the match, visualized through a heatmap.

### Available Stages
- Group Stage
- Round of 16
- Quarter-finals
- Semi-finals
- 3rd Place Final
- Final