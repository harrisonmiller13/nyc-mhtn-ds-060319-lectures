from dictionaryball import game_dictionary

def game_dict():
    return game_dictionary

# def dict_var():
#     homeplayer = game_dict()['home']['players']
#     awayplayer = game_dict()['away']['players']
#     all_players = {**homeplayer,**awayplayer}
#     homename = game_dict()['home']['team_name']
#     awayname = game_dict()['away']['team_name']

def num_points_scored (player):
    homeplayer = game_dict()['home']['players']
    awayplayer = game_dict()['away']['players']
    all_players = {**homeplayer,**awayplayer}
    return all_players[player]['points']

def shoe_size (player):
    homeplayer = game_dict()['home']['players']
    awayplayer = game_dict()['away']['players']
    all_players = {**homeplayer,**awayplayer}
    return all_players[player]['shoe']

def team_colors (team_name):
    homename = game_dict()['home']['team_name']
    awayname = game_dict()['away']['team_name']
    if team_name == homename:
        return game_dict()['home']['colors']
    return game_dict()['away']['colors']
        

def team_names ():
    homename = game_dict()['home']['team_name']
    awayname = game_dict()['away']['team_name']
    return [homename, awayname]

def player_stats (player):
    homeplayer = game_dict()['home']['players']
    awayplayer = game_dict()['away']['players']
    all_players = {**homeplayer,**awayplayer}
    return all_players[player]

def player_numbers (team):
    home = game_dict()['home']
    homeplayer = game_dict()['home']['players']
    awayplayer = game_dict()['away']['players']
    jersey_numbers = []
    if team == home['team_name']:
        for player, stats in homeplayer.items():
            jersey_numbers.append (stats ['number'])
    else:
        for player, stats in awayplayer.items():
            jersey_numbers.append (stats['number'])
    return jersey_numbers



