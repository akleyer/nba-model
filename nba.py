#! /usr/bin/python3

import pprint
import matplotlib.pyplot as plt
import numpy as np
import json

from game import Game
from player import Player
from team import Team
from stats import Stats


def import_stats(file_name):
    with open(file_name) as inf:
        return inf.readlines()

def main():
    game_id_tracker = []
    stats = import_stats("asa_stats.csv")
    stat_tracker = Stats()
    for line in stats:
        split_line = line.split(',')

        game_id = split_line[0].replace("\"","")

        if game_id == "game_id":
            continue

        if game_id in game_id_tracker:
            continue
        else:
            game_id_tracker.append(game_id)

        # print(split_line)
        # print("")

        team1_h_a = split_line[3]
        if team1_h_a == "A":
            team2_h_a = "H"
        else:
            team2_h_a = "A"

        team1_name = split_line[4]
        team2_name = split_line[12]

        team1_score = float(split_line[5])
        team1_efg = float(split_line[7])
        team1_tov = float(split_line[8])
        team1_orb = float(split_line[9])
        team1_ft = float(split_line[10])
        team2_score = float(split_line[13])
        team2_efg = float(split_line[15])
        team2_tov = float(split_line[16])
        team2_orb = float(split_line[17])
        team2_ft = float(split_line[18])

        team1 = Team(team1_name, team1_h_a, team1_score, team1_efg, team1_tov,
                     team1_orb, team1_ft, [])
        team2 = Team(team2_name, team2_h_a, team2_score, team2_efg, team2_tov,
                     team2_orb, team2_ft, [])

        game = Game(game_id, team1, team2)
        stat_tracker.add_game(game)

    x = []
    y = []
    w = 0
    num_games = len(stat_tracker.games)
    # max_win = 0
    w05 = 0
    wn05 = 0
    w25 = 0
    wn25 = 0
    w50 = 0
    wn50 = 0
    w100 = 0
    wn100 = 0
    w200 = 0
    wn200 = 0
    wn05_games = 0
    w05_games = 0
    wn25_games = 0
    w25_games = 0
    wn50_games = 0
    w50_games = 0
    w100_games = 0
    wn100_games = 0
    w200_games = 0
    wn200_games = 0
    for game in stat_tracker.games:
        team1, team2 = game.get_teams()
        team1_obj, team1_factor = team1
        team2_obj, team2_factor = team2

        team1_name = team1_obj.get_name()
        team1_score = team1_obj.get_score()
        team1_efg = team1_obj.get_efg()
        team1_tov = team1_obj.get_tov()
        team1_orb = team1_obj.get_orb()
        team1_ft = team1_obj.get_ft()

        team2_name = team2_obj.get_name()
        team2_score = team2_obj.get_score()
        team2_efg = team2_obj.get_efg()
        team2_tov = team2_obj.get_tov()
        team2_orb = team2_obj.get_orb()
        team2_ft = team2_obj.get_ft()
        # print(f"{team1_name:<5}{team1_score:<7}{round(team1_factor,1):<5}{round(team1_efg,1):<7}{team1_tov:<7}{team1_orb:<7}{round(team1_ft,1):<7}")
        # print(f"{'':<17}({round(team1_efg*0.5,1)})({round(team1_tov*0.3,1)})({round(team1_orb*0.15,1)})({round(team1_ft*0.05,1)})")
        # print(f"{team2_name:<5}{team2_score:<7}{round(team2_factor,1):<5}{round(team2_efg,1):<7}{team2_tov:<7}{team2_orb:<7}{round(team2_ft,1):<7}")
        # print(f"{'':<17}({round(team2_efg*0.5,1)})({round(team2_tov*0.3,1)})({round(team2_orb*0.15,1)})({round(team2_ft*0.05,1)})")
        # print("")
        # print("")

        x.append(team1_factor - team2_factor)
        y.append(team1_score - team2_score)

        if team1_factor > team2_factor:
            if team1_score > team2_score:
                w += 1

        t1t2d = team1_factor - team2_factor
        if t1t2d >= 0.0 and t1t2d <= 1.0:
            w05_games += 1
            if team1_score > team2_score:
                w05 += 1
        if t1t2d >= 1.0 and t1t2d <= 2.5:
            w25_games += 1
            if team1_score > team2_score:
                w25 += 1
        if t1t2d >= 2.5 and t1t2d <= 5.0:
            w50_games += 1
            if team1_score > team2_score:
                w50 += 1
        if t1t2d >= 5 and t1t2d <= 10:
            w100_games += 1
            if team1_score > team2_score:
                w100 += 1
        if t1t2d >= 10 and t1t2d <= 20:
            w200_games += 1
            if team1_score > team2_score:
                w200 += 1
        if t1t2d <= 0 and t1t2d >= 1:
            wn05_games += 1
            if team1_score > team2_score:
                wn05 += 1
        if t1t2d <= -1 and t1t2d >= -2.5:
            wn25_games += 1
            if team1_score > team2_score:
                wn25 += 1
        if t1t2d <= -2.5 and t1t2d >= -5.0:
            wn50_games += 1
            if team1_score > team2_score:
                wn50 += 1
        if t1t2d <= -5.0 and t1t2d >= -10:
            wn100_games += 1
            if team1_score > team2_score:
                wn100 += 1
        if t1t2d <= -10 and t1t2d >= -20.0:
            wn200_games += 1
            if team1_score > team2_score:
                wn200 += 1

        if team2_factor > team1_factor:
            if team2_score > team1_score:
                w += 1

        t2t1d = team2_factor - team1_factor
        if t2t1d >= 0.0 and t2t1d <= 1.0:
            w05_games += 1
            if team2_score > team1_score:
                w05 += 1
        if t2t1d >= 1.0 and t2t1d <= 2.5:
            w25_games += 1
            if team2_score > team1_score:
                w25 += 1
        if t2t1d >= 2.5 and t2t1d <= 5.0:
            w50_games += 1
            if team2_score > team1_score:
                w50 += 1
        if t2t1d >= 5 and t2t1d <= 10.0:
            w100_games += 1
            if team2_score > team1_score:
                w100 += 1
        if t2t1d >= 10 and t2t1d <= 20.0:
            w200_games += 1
            if team2_score > team1_score:
                w200 += 1
        if t2t1d <= 0 and t2t1d >= -1:
            wn05_games += 1
            if team2_score > team1_score:
                wn05 += 1
        if t2t1d <= -1 and t2t1d >= -2.5:
            wn25_games += 1
            if team2_score > team1_score:
                wn25 += 1
        if t2t1d <= -2.5 and t2t1d >= -5.0:
            wn50_games += 1
            if team2_score > team1_score:
                wn50 += 1
        if t2t1d <= -5 and t2t1d >= -10:
            wn50_games += 1
            if team2_score > team1_score:
                wn50 += 1
        if t2t1d <= -10 and t2t1d >= -20:
            wn200_games += 1
            if team2_score > team1_score:
                wn200 += 1

        # if abs(team1_score - team2_score) > max_win:
        #     max_win = abs(team1_score - team2_score)

    x = np.array(x)
    y = np.array(y)

    #find line of best fit
    a, b = np.polyfit(x, y, 1)

    # plotting the points
    plt.scatter(x, y)

    #add line of best fit to plot
    plt.plot(x, a*x+b)

    # print(f"Function: Spread = factor * {round(a,3)} + {round(b,3)} ")
    # print("")
    # print(f"Win Pct w/ Negative Factor -20.0 to -10.0 : {round((wn200/wn200_games)*100, 2)}%")
    # print(f"Win Pct w/ Negative Factor -10.0 to -5.0  : {round((wn100/wn100_games)*100, 2)}%")
    # print(f"Win Pct w/ Negative Factor -5.0 to -2.5   : {round((wn50/wn50_games)*100, 2)}%")
    # print(f"Win Pct w/ Negative Factor -2.5 to -1.0   : {round((wn25/wn25_games)*100, 2)}%")
    # print(f"Win Pct w/ Negative Factor -1.0 to 0.0    : {round((wn05/wn05_games)*100, 2)}%")
    # print(f"Win Pct w/ Positive Factor 0.0 to 1.0     : {round((w05/w05_games)*100, 2)}%")
    # print(f"Win Pct w/ Positive Factor 1.0 to 2.5     : {round((w25/w25_games)*100, 2)}%")
    # print(f"Win Pct w/ Positive Factor 2.5 to 5.0     : {round((w50/w50_games)*100, 2)}%")
    # print(f"Win Pct w/ Positive Factor 5.0 to 10.0    : {round((w100/w100_games)*100, 2)}%")
    # print(f"Win Pct w/ Positive Factor 10.0 to 20.0   : {round((w200/w200_games)*100, 2)}%")

    x1 = np.array([-15,-7.5,-3.75,-1.75,-0.5,0.5,1.75,3.75,7.5,15])
    y1 = np.array([(wn200/wn200_games)*100, (wn100/wn100_games)*100, (wn50/wn50_games)*100, (wn25/wn25_games)*100, (wn05/wn05_games)*100, (w05/w05_games)*100, (w25/w25_games)*100, (w50/w50_games)*100, (w100/w100_games)*100, (w200/w200_games)*100])

    #find line of best fit
    a1, b1 = np.polyfit(x1, y1, 1)


    # function to show the plot
    #plt.show()

    nba_stats = {}

    with open("nba_stats.csv") as new_inf:
        team_stats = new_inf.readlines()
        for team in team_stats:
            stats = team.split(',')

            team_name = stats[0]
            nba_stats[team_name] = {
                "offense":{
                    "efg" : float(stats[6]),
                    "ft" : float(stats[7]),
                    "tov" : float(stats[8]),
                    "orb" : float(stats[9]),
                    "min" : float(stats[5]) * 5
                },
                "defense":{
                    "efg" : float(stats[10]),
                    "ft" : float(stats[11]),
                    "tov" : float(stats[12]),
                    "orb" : float(stats[13])
                }
            }

    # print("")
    # print("Max Win: " + str(max_win))

    player_stats = {}

    with open("player_stats.csv") as player_in:
        lines = player_in.readlines()
        for line in lines:
            sl = line.split(',')

            name = sl[1]
            if name == 'PLAYER': continue

            team = sl[2]
            gp = int(sl[4])
            min = float(sl[7])
            orb = float(sl[14])
            drb = float(sl[15])
            try:
                orbr = orb * 100 / (orb + drb)
            except:
                orbr = 0
            to = float(sl[17])
            efg = float(sl[18])
            player = Player(name, team, gp, min, orbr, to, efg)
            player_stats[name] = player

    with open("player_stats_def.csv") as player_in:
        lines = player_in.readlines()
        for line in lines:
            sl = line.split(',')
            name = (sl[2] + ' ' + sl[1]).replace("\"","").strip()
            # print(name)
            # print(sl[17])
            # print(sl[18])
            # print(float(sl[17]) + float(sl[18]))
            try:
                orb = round(float(sl[17]) * 100 / ( float(sl[17]) + float(sl[18]) ), 2)
            except:
                orb = 0
            # print(orb)
            to = round((float(sl[21]) * 100) / ((float(sl[9])) + (float(sl[15]) * 0.44) + (float(sl[20])) + (float(sl[21]))),2)
            efg = round((float(sl[8]) + (float(sl[11]))*0.5) / float(sl[9]) * 100,2)
            player_stats[name].set_opp_orb(orb)
            player_stats[name].set_opp_to(to)
            player_stats[name].set_opp_efg(efg)

    injury_list = {}
    with open("nba_injuries.csv") as inj:
        lines = inj.readlines()
        for line in lines:
            split_line = line.split(',')
            team, player = split_line
            if team not in injury_list:
                injury_list[team] = []
            injury_list[team].append(player_stats[player.strip()])

    t1_injuries = []
    t2_injuries = []

    def calc_efg(team_efg, team_min, players):
        if not players:
            return team_efg
        # print(f"Team EFG: {team_efg}")
        # print(f"Team Min: {team_min}")
        player_total_efg = 0
        player_min_pct_tracking = 0
        player_weighted_efg_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            efg = player.get_efg()

            # print(f"Player EFG: {efg}")
            player_total_efg += efg
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{efg:<7}...{round(player_min_pct * 100,2):<7}")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_efg = efg * player_min_pct
            player_weighted_efg_total += player_weighted_efg

        all_player_weighted_efg = player_weighted_efg_total / player_min_pct_tracking
        # print(f"All Player Weighted EFG: {all_player_weighted_efg}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_efg_delta = all_player_weighted_efg - team_efg
        player_opp_delta = team_efg - player_efg_delta
        # print(f"Player Opp EFG: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_efg = ((remaining_pct * team_efg) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team EFG: {round(new_team_efg,2)}")
        # print()
        return new_team_efg

    def calc_tov(team_tov, team_min, players):
        if not players:
            return team_tov
        # print(f"Team TOV: {team_tov}")
        # print(f"Team Min: {team_min}")
        player_total_tov = 0
        player_min_pct_tracking = 0
        player_weighted_tov_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            tov = player.get_tov()

            # print(f"Player TOV: {tov}")
            player_total_tov += tov
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{tov:<7}...{round(player_min_pct * 100,2):<7}")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_tov = tov * player_min_pct
            player_weighted_tov_total += player_weighted_tov

        all_player_weighted_tov = player_weighted_tov_total / player_min_pct_tracking
        # print(f"All Player Weighted TOV: {all_player_weighted_tov}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_tov_delta = all_player_weighted_tov - team_tov
        player_opp_delta = team_tov - player_tov_delta
        # print(f"Player Opp TOV: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_tov = ((remaining_pct * team_tov) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team TOV: {round(new_team_tov,2)}")
        # print()
        return new_team_tov

    def calc_orb(team_orb, team_min, players):
        if not players:
            return team_orb
        # print(f"Team ORB: {team_orb}")
        # print(f"Team Min: {team_min}")
        player_total_orb = 0
        player_min_pct_tracking = 0
        player_weighted_orb_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            orb = player.get_orb()

            # print(f"Player ORB: {orb}")
            player_total_orb += orb
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{orb:<7}...{round(player_min_pct * 100,2):<7}..")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_orb = orb * player_min_pct
            player_weighted_orb_total += player_weighted_orb

        all_player_weighted_orb = player_weighted_orb_total / player_min_pct_tracking
        # print(f"All Player Weighted ORB: {all_player_weighted_orb}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_orb_delta = all_player_weighted_orb - team_orb
        player_opp_delta = team_orb - player_orb_delta
        # print(f"Player Opp ORB: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_orb = ((remaining_pct * team_orb) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team ORB: {round(new_team_orb,2)}")
        # print()
        return new_team_orb

    def calc_ft(team_ft, team_min, players):
        if not players:
            return team_ft
        # print(f"Team FT: {team_ft}")
        # # print(f"Team Min: {team_min}")
        # player_total_orb = 0
        # player_min_pct_tracking = 0
        # player_weighted_orb_total = 0
        # for player in players:
        #     name = player.get_name()
        #     mins = player.get_min()
        #     # print(f"Player Min: {mins}")
        #     orb = player.get_orb() * 5
        #
        #     # print(f"Player ORB: {orb}")
        #     player_total_orb += orb
        #     player_min_pct = mins / team_min
        #     print(f"{name:<20}...{orb:<7}...{round(player_min_pct * 100,2):<7}..")
        #     # print(f"Player Min Pct: {player_min_pct}")
        #     player_min_pct_tracking += player_min_pct
        #     player_weighted_orb = orb * player_min_pct
        #     player_weighted_orb_total += player_weighted_orb
        #
        # all_player_weighted_orb = player_weighted_orb_total / player_min_pct_tracking
        # # print(f"All Player Weighted ORB: {all_player_weighted_orb}")
        # # print(f"All Player Min: {player_min_pct_tracking}")
        # player_opp_pct = player_min_pct_tracking
        # player_orb_delta = all_player_weighted_orb - team_orb
        # player_opp_delta = team_orb - player_orb_delta
        # # print(f"Player Opp ORB: {player_opp_delta}")
        # remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # # print(f"Remaining Pct: {remaining_pct}")
        # new_team_orb = ((remaining_pct * team_orb) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        new_team_ft = team_ft
        # print(f"New Team FT: {new_team_ft}")
        # print()
        return new_team_ft

    def calc_efg_def(team_efg, team_min, players):
        if not players:
            return team_efg
        # print(f"Team EFG: {team_efg}")
        # print(f"Team Min: {team_min}")
        player_total_efg = 0
        player_min_pct_tracking = 0
        player_weighted_efg_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            efg = player.get_efg_d()

            # print(f"Player EFG: {efg}")
            player_total_efg += efg
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{efg:<7}...{round(player_min_pct * 100,2):<7}")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_efg = efg * player_min_pct
            player_weighted_efg_total += player_weighted_efg

        all_player_weighted_efg = player_weighted_efg_total / player_min_pct_tracking
        # print(f"All Player Weighted EFG: {all_player_weighted_efg}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_efg_delta = all_player_weighted_efg - team_efg
        player_opp_delta = team_efg - player_efg_delta
        # print(f"Player Opp EFG: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_efg = ((remaining_pct * team_efg) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team EFG: {round(new_team_efg,2)}")
        # print()
        return new_team_efg

    def calc_tov_def(team_tov, team_min, players):
        if not players:
            return team_tov
        # print(f"Team TOV: {team_tov}")
        # print(f"Team Min: {team_min}")
        player_total_tov = 0
        player_min_pct_tracking = 0
        player_weighted_tov_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            tov = player.get_tov_d()

            # print(f"Player TOV: {tov}")
            player_total_tov += tov
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{tov:<7}...{round(player_min_pct * 100,2):<7}")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_tov = tov * player_min_pct
            player_weighted_tov_total += player_weighted_tov

        all_player_weighted_tov = player_weighted_tov_total / player_min_pct_tracking
        # print(f"All Player Weighted TOV: {all_player_weighted_tov}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_tov_delta = all_player_weighted_tov - team_tov
        player_opp_delta = team_tov - player_tov_delta
        # print(f"Player Opp TOV: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_tov = ((remaining_pct * team_tov) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team TOV: {round(new_team_tov,2)}")
        # print()
        return new_team_tov

    def calc_orb_def(team_orb, team_min, players):
        if not players:
            return team_orb
        # print(f"Team ORB: {team_orb}")
        # print(f"Team Min: {team_min}")
        player_total_orb = 0
        player_min_pct_tracking = 0
        player_weighted_orb_total = 0
        for player in players:
            name = player.get_name()
            mins = player.get_min()
            # print(f"Player Min: {mins}")
            orb = player.get_orb_d()

            # print(f"Player ORB: {orb}")
            player_total_orb += orb
            player_min_pct = mins / team_min
            # print(f"{name:<20}...{orb:<7}...{round(player_min_pct * 100,2):<7}..")
            # print(f"Player Min Pct: {player_min_pct}")
            player_min_pct_tracking += player_min_pct
            player_weighted_orb = orb * player_min_pct
            player_weighted_orb_total += player_weighted_orb

        all_player_weighted_orb = player_weighted_orb_total / player_min_pct_tracking
        # print(f"All Player Weighted ORB: {all_player_weighted_orb}")
        # print(f"All Player Min: {player_min_pct_tracking}")
        player_opp_pct = player_min_pct_tracking
        player_orb_delta = all_player_weighted_orb - team_orb
        player_opp_delta = team_orb - player_orb_delta
        # print(f"Player Opp ORB: {player_opp_delta}")
        remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # print(f"Remaining Pct: {remaining_pct}")
        new_team_orb = ((remaining_pct * team_orb) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        # print(f"New Team ORB: {round(new_team_orb,2)}")
        # print()
        return new_team_orb

    def calc_ft_def(team_ft, team_min, players):
        if not players:
            return team_ft
        # print(f"Team FT: {team_ft}")
        # # print(f"Team Min: {team_min}")
        # player_total_orb = 0
        # player_min_pct_tracking = 0
        # player_weighted_orb_total = 0
        # for player in players:
        #     name = player.get_name()
        #     mins = player.get_min()
        #     # print(f"Player Min: {mins}")
        #     orb = player.get_orb() * 5
        #
        #     # print(f"Player ORB: {orb}")
        #     player_total_orb += orb
        #     player_min_pct = mins / team_min
        #     print(f"{name:<20}...{orb:<7}...{round(player_min_pct * 100,2):<7}..")
        #     # print(f"Player Min Pct: {player_min_pct}")
        #     player_min_pct_tracking += player_min_pct
        #     player_weighted_orb = orb * player_min_pct
        #     player_weighted_orb_total += player_weighted_orb
        #
        # all_player_weighted_orb = player_weighted_orb_total / player_min_pct_tracking
        # # print(f"All Player Weighted ORB: {all_player_weighted_orb}")
        # # print(f"All Player Min: {player_min_pct_tracking}")
        # player_opp_pct = player_min_pct_tracking
        # player_orb_delta = all_player_weighted_orb - team_orb
        # player_opp_delta = team_orb - player_orb_delta
        # # print(f"Player Opp ORB: {player_opp_delta}")
        # remaining_pct = 1 - (player_min_pct_tracking + player_opp_pct)
        # # print(f"Remaining Pct: {remaining_pct}")
        # new_team_orb = ((remaining_pct * team_orb) + (player_opp_pct * player_opp_delta)) / (remaining_pct + player_opp_pct)

        new_team_ft = team_ft
        # print(f"New Team FT: {new_team_ft}")
        # print()
        return new_team_ft

    print("Games Today")
    with open("nba_games_today.csv") as inf:
        games = inf.readlines()
        for game in games:
            t1_injuries = []
            t2_injuries = []
            teams = game.split(',')
            team1, t1_odds, t1_ml, team2, t2_odds, t2_ml = teams

            if team1 in injury_list:
                t1_injuries = injury_list[team1]
            if team2 in injury_list:
                t2_injuries = injury_list[team2]

            # print("="*20)
            # print(f"GAME: {team1} vs {team2}")
            # print("="*20)
            #
            # print("Injury List")
            # print(' ' + '_'*41)
            # print(f"|{team1:<20}|{team2:<20}|")
            max_injury_len = len(t1_injuries) if len(t1_injuries) >= len(t2_injuries) else len(t2_injuries)
            for index in range(max_injury_len):
                try:
                    tmp1 = t1_injuries[index].get_name()
                except:
                    tmp1 = ""
                try:
                    tmp2 = t2_injuries[index].get_name()
                except:
                    tmp2 = ""
            #     print(f"|{tmp1:<20}|{tmp2:<20}|")
            # print(' ' + '-'*41)

            t1os = nba_stats[team1]["offense"]
            t2os = nba_stats[team2]["offense"]
            t1ds = nba_stats[team1]["defense"]
            t2ds = nba_stats[team2]["defense"]

            #print(f"> {team1} Offense")
            t1_efg = calc_efg(t1os["efg"], t1os["min"], t1_injuries)
            t1_tov = calc_tov(t1os["tov"], t1os["min"], t1_injuries)
            t1_orb = calc_orb(t1os["orb"], t1os["min"], t1_injuries)
            t1_ftr = calc_ft(t1os["ft"], t1os["min"], t1_injuries)

            #print(f"> {team1} Defense")
            t1_efg_d = calc_efg_def(t1ds["efg"], t1os["min"], t1_injuries)
            t1_tov_d = calc_tov_def(t1ds["tov"], t1os["min"], t1_injuries)
            t1_orb_d = calc_orb_def(t1ds["orb"], t1os["min"], t1_injuries)
            t1_ftr_d = calc_ft_def(t1ds["ft"], t1os["min"], t1_injuries)

            #print(f"> {team2} Offense")
            t2_efg = calc_efg(t2os["efg"], t2os["min"], t2_injuries)
            t2_tov = calc_tov(t2os["tov"], t2os["min"], t2_injuries)
            t2_orb = calc_orb(t2os["orb"], t2os["min"], t2_injuries)
            t2_ftr = calc_ft(t2os["ft"], t2os["min"], t2_injuries)

            #print(f"> {team2} Defense")
            t2_efg_d = calc_efg_def(t2ds["efg"], t2os["min"], t2_injuries)
            t2_tov_d = calc_tov_def(t2ds["tov"], t2os["min"], t2_injuries)
            t2_orb_d = calc_orb_def(t2ds["orb"], t2os["min"], t2_injuries)
            t2_ftr_d = calc_ft_def(t2ds["ft"], t2os["min"], t2_injuries)


            t1_o_factor = ((0.5*t1_efg) - (0.3*t1_tov) + (0.15*t1_orb) + (0.05*t1_ftr*100))
            t1_d_factor = ((0.5*t1_efg_d) - (0.3*t1_tov_d) + (0.15*t1_orb_d) + (0.05*t1_ftr_d*100))

            t2_o_factor = ((0.5*t2_efg) - (0.3*t2_tov) + (0.15*t2_orb) + (0.05*t2_ftr*100))
            t2_d_factor = ((0.5*t2_efg_d) - (0.3*t2_tov_d) + (0.15*t2_orb_d) + (0.05*t2_ftr_d*100))

            t1_net_factor = round(t1_o_factor - t1_d_factor,1)
            t2_net_factor = round(t2_o_factor - t2_d_factor,1)

            t1_game_factor = round((t1_net_factor - t2_net_factor) * 2.53, 1)
            t2_game_factor = round((t2_net_factor - t1_net_factor) * 2.53, 1)

            t1_spread = ((t1_game_factor * a + b) - 1.5) * -1
            t2_spread = ((t2_game_factor * a + b) + 1.5) * -1

            win_prob1 = round(t1_game_factor * a1 + b1,2)
            win_prob2 = round(t2_game_factor * a1 + b1,2)

            t1_odds_play = round((t1_spread - float(t1_odds)) * -25)
            t2_odds_play = round((t2_spread - float(t2_odds)) * -25)

            t1_ml = float(t1_ml)
            t2_ml = float(t2_ml.strip())

            if t1_ml < 0:
                t1_imp_prob = (-1 * (t1_ml)) / (-1 * (t1_ml) + 100)
            else:
                t1_imp_prob = 100 / (t1_ml + 100)

            if t2_ml < 0:
                t2_imp_prob = (-1 * (t2_ml)) / (-1 * (t2_ml) + 100)
            else:
                t2_imp_prob = 100 / (t2_ml + 100)

            t1_imp_prob = round(t1_imp_prob * 100,2)
            t2_imp_prob = round(t2_imp_prob * 100,2)


            t1_ml_play = round(((win_prob1 - t1_imp_prob)-2.5)*12.5*win_prob1/50)
            t2_ml_play = round(((win_prob2 - t2_imp_prob)-2.5)*12.5*win_prob2/50)

            # print(" " + '_' * 103)
            # print(f"|{'Team':<5}|{'Team Net Factor':<16}|{'Team Game Factor':<17}|{'Win Prob %':<11}|{'Impl Prob %':<12}|{'ML Play':<7}|{'Proj Spread':<12}|{'Odds':<5}|{'Odds Play':<10}|")
            # print(f"|{team1:<5}|{t1_net_factor:<16}|{t1_game_factor:<17}|{win_prob1:<11}|{t1_imp_prob:<12}|{t1_ml_play:<7}|{round(t1_spread,1):<12}|{t1_odds:<5}|{t1_odds_play:<10}|")
            # print(f"|{team2:<5}|{t2_net_factor:<16}|{t2_game_factor:<17}|{win_prob2:<11}|{t2_imp_prob:<12}|{t2_ml_play:<7}|{round(t2_spread,1):<12}|{t2_odds:<5}|{t2_odds_play:<10}|")
            # print(" " + '-' * 103)
            # print()

    def calc_team_factor(team, players_list):
        total_efg = 0
        total_orb = 0
        total_tov = 0
        total_opp_efg = 0
        total_opp_orb = 0
        total_opp_tov = 0
        total_min = 0
        num_players = len(players_list)
        for player, proj_mins in players_list:
            pm = float(proj_mins)

            try:
                player_efg = player_stats[player].get_efg()
                player_orb = player_stats[player].get_orb()
                player_tov = player_stats[player].get_tov()
                player_opp_efg = player_stats[player].get_opp_efg()
                player_opp_orb = player_stats[player].get_opp_orb()
                player_opp_tov = player_stats[player].get_opp_tov()
            except:
                print(f"Couldn't find: {player}")
                player_efg = nba_stats[team]["offense"]["efg"]
                player_tov = nba_stats[team]["offense"]["tov"]
                player_orb = nba_stats[team]["offense"]["orb"]
                player_opp_efg = nba_stats[team]["defense"]["efg"]
                player_opp_orb = nba_stats[team]["defense"]["orb"]
                player_opp_tov= nba_stats[team]["defense"]["tov"]
                continue

            total_efg += (player_efg * pm)
            total_orb += (player_orb * pm)
            total_tov += (player_tov * pm)
            total_opp_efg += (player_opp_efg * pm)
            total_opp_orb += (player_opp_orb * pm)
            total_opp_tov += (player_opp_tov * pm)
            total_min += pm

        team_efg = total_efg / total_min
        team_orb = total_orb / total_min
        team_tov = total_tov / total_min
        team_ft = nba_stats[team]["offense"]["ft"]
        team_opp_efg = total_opp_efg / total_min
        team_opp_orb = total_opp_orb / total_min
        team_opp_tov = total_opp_tov / total_min
        team_opp_ft = nba_stats[team]["defense"]["ft"]
        team_off_factor = ((0.5*team_efg) - (0.3*team_tov) + (0.15*team_orb) + (0.05*team_ft*100))
        team_def_factor = ((0.5*team_opp_efg) - (0.3*team_opp_tov) + (0.15*team_opp_orb) + (0.05*team_opp_ft*100))
        team_net_factor = round(team_off_factor - team_def_factor,1)
        return team_net_factor

    with open("nba_games_today.csv") as inf:
        games = inf.readlines()
        for game in games:
            team1, t1_odds, t1_ml, team2, t2_odds, t2_ml = game.split(',')
            lineup_file = open('lineups.json')
            lineup_data = json.load(lineup_file)

            if team1 not in lineup_data or team2 not in lineup_data: continue

            team1_factor = calc_team_factor(team1, lineup_data[team1])
            team2_factor = calc_team_factor(team2, lineup_data[team2])

            t1_game_factor = round((team1_factor - team2_factor) * 2.53, 1)
            t2_game_factor = round((team2_factor - team1_factor) * 2.53, 1)

            t1_spread = ((t1_game_factor * a + b) - 1.5) * -1
            t2_spread = ((t2_game_factor * a + b) + 1.5) * -1

            win_prob1 = round(t1_game_factor * a1 + b1,2)
            win_prob2 = round(t2_game_factor * a1 + b1,2)

            t1_odds_play = round((t1_spread - float(t1_odds)) * -25)
            t2_odds_play = round((t2_spread - float(t2_odds)) * -25)

            t1_ml = float(t1_ml)
            t2_ml = float(t2_ml.strip())

            if t1_ml < 0:
                t1_imp_prob = (-1 * (t1_ml)) / (-1 * (t1_ml) + 100)
            else:
                t1_imp_prob = 100 / (t1_ml + 100)

            if t2_ml < 0:
                t2_imp_prob = (-1 * (t2_ml)) / (-1 * (t2_ml) + 100)
            else:
                t2_imp_prob = 100 / (t2_ml + 100)

            t1_imp_prob = round(t1_imp_prob * 100,2)
            t2_imp_prob = round(t2_imp_prob * 100,2)


            t1_ml_play = round(((win_prob1 - t1_imp_prob)-2.5)*12.5*win_prob1/50)
            t2_ml_play = round(((win_prob2 - t2_imp_prob)-2.5)*12.5*win_prob2/50)

            print(" " + '_' * 103)
            print(f"|{'Team':<5}|{'Team Net Factor':<16}|{'Team Game Factor':<17}|{'Win Prob %':<11}|{'Impl Prob %':<12}|{'ML Play':<7}|{'Proj Spread':<12}|{'Odds':<5}|{'Odds Play':<10}|")
            print(f"|{team1:<5}|{team1_factor:<16}|{t1_game_factor:<17}|{win_prob1:<11}|{t1_imp_prob:<12}|{t1_ml_play:<7}|{round(t1_spread,1):<12}|{t1_odds:<5}|{t1_odds_play:<10}|")
            print(f"|{team2:<5}|{team2_factor:<16}|{t2_game_factor:<17}|{win_prob2:<11}|{t2_imp_prob:<12}|{t2_ml_play:<7}|{round(t2_spread,1):<12}|{t2_odds:<5}|{t2_odds_play:<10}|")
            print(" " + '-' * 103)
            print()
main()
