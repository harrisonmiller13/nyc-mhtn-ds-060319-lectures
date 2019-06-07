from dictionaryball import game_dictionary

def game_dict():
    return game_dictionary

homeplayer = game_dict()['home']['players']
awayplayer = game_dict()['away']['players']
all_players = {**homeplayer,**awayplayer}
homename = game_dict()['home']['team_name']
awayname = game_dict()['away']['team_name']

def num_points_scored (player):
    return all_players[player]['points']

def shoe_size (player):
    return all_players[player]['shoe']

def team_colors (team_name):
    if team_name == homename:
        return game_dict()['home']['colors']
    return game_dict()['away']['colors']

def whos_playing ():
    return homename + ' ' + 'vs' + ' ' + awayname


