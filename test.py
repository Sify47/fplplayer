import requests
import json
import pandas as pd
url = f"https://fantasy.premierleague.com/api/entry/420085/event/1/picks/"
url1 = "https://fantasy.premierleague.com/api/bootstrap-static/"
r = requests.get(url)
t = requests.get(url1)
data = r.json()
response_dict = t.json()

# # Team id's
# teams = response_dict['teams']

# team_list = []
# for team in teams:
#     team_id = {
#         team['code'] : team['name']
#     }
#     team_list.append(team_id)
    
# team_dict = {}
# for team in team_list:
#     team_dict.update(team)

# # Position id's
# element_types = response_dict['element_types']

# position_list = []
# for element_type in element_types:
#     position_id = {
#         element_type['id'] : element_type['plural_name_short']
#     }
#     position_list.append(position_id)
    
# position_dict = {}
# for position in position_list:
#     position_dict.update(position)

# wanted_features = ['first_name', 'second_name', 'team_code','element_type','news','now_cost', 'total_points', 'minutes',
#                    'form',  'value_season', 'points_per_game', 'value_form',
#                     'goals_scored', 'assists', 'dreamteam_count','clean_sheets', 
#                    'goals_conceded', 'own_goals','penalties_saved', 'penalties_missed',
#                    'yellow_cards', 'red_cards', 'saves', 'bonus',
#                    'influence', 'creativity', 'threat', 'ict_index', 'selected_by_percent'
#                   ]
# player_data = response_dict['elements']
# # Converting the list of players to a DataFrame
# players_df = pd.DataFrame(player_data)
# # Choosing only the columns that we want
# players_df = players_df[wanted_features]
# players_df.head()
# print(response_dict['elements'][594])
import re
for i in response_dict['elements']:
    if i['id'] == 24:
        print(i['photo'][:-4])