import json
import re


class FileHandler:
    def __init__(self):
        self.player_data = {}
   
    # -----
    # additional verification method to check if data exists
    # -----
    # def no_data(self):
    #     if self.player_data:
    #         return False
    #     else:
    #         return True
    
    def player_data_from_json(self, input_file: str):
        with open(input_file) as f:
            data = f.read()
        players_from_json = json.loads(data)
        while len(self.player_data) < len(players_from_json):
            for player_info in players_from_json:
                s = []
                for key in player_info.keys():
                    s.append(player_info[key])
                player = Player(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
                self.player_data[s[0]] = player 
        print(f"read the data of {len(self.player_data)} players")
        return self.player_data
        

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    def __str__(self):
        return f"{self.name:21}{self.team}{self.goals:4} + {self.assists:2} = {self.assists + self.goals:3}"

class HockeyApp:
    def __init__(self):
        self.all_players_dict = FileHandler()
    
    # -----
    # additional verification that can be added to methods to check if data exists
    # -----
    # def data_exists(self):
    #     if self.all_players_dict.no_data():
    #         print("No data available")
    #     else:
    #         return True
    
    # starts the application
    def execute(self):
        self.commands()
        while True:
            print("")
            try:
                command = int(input("command: "))
            except:
                print("invalid command")
                continue
            match command:
                case 0: break
                case 1: self.search_for_player()
                case 2: 
                    teams = sorted(self.teams())
                    for team in teams:
                        print(team)
                case 3: 
                    countries = sorted(self.countries())
                    for country in countries:
                        print(country)
                case 4: self.players_in_team()
                case 5: self.players_from_country()
                case 6: self.most_points()
                case 7: self.most_goals()
                case _: self.commands()
    
    # available commands
    def commands(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    # seaches for player by name
    def search_for_player(self):
        inpt = input("name: ")
        regexpinpt = f"({inpt})"
        for key in self.all_players_dict.player_data:
            if re.search(regexpinpt.lower(), key.lower()):
                print(self.all_players_dict.player_data[key])
    
    # displays list of unique teams
    def teams(self):
        return set([player.team for player in self.all_players_dict.player_data.values()])
    
    # displays list of unique countries
    def countries(self):
        return set([player.nationality for player in self.all_players_dict.player_data.values()])

    # helper function for methods below
    def sorted_score_reverse_list(self):
        scores = list(set([(player.goals + player.assists) for player in self.all_players_dict.player_data.values()]))
        scores.sort()
        return scores[::-1]
    
    # displays players of a specified team
    def players_in_team(self):
        def total_score(player: Player):
            return player.goals + player.assists
        inpt = input("team: ")
        players = [player for player in self.all_players_dict.player_data.values() if player.team == inpt]
        result = sorted(players, key=total_score, reverse = True)
        for i in result:
            print(i)

    # displays players of a specified country
    def players_from_country(self):
        inpt = input("team: ")
        for score in self.sorted_score_reverse_list():
            for player in self.all_players_dict.player_data.values():
                if score == player.goals + player.assists and player.nationality == inpt:
                    print(player)
    
    # displays top n players who scored most overall (goals + assists) in alphabetical order
    # if two players have the same score, whoever has scored the higher number of goals comes first 
    def most_points(self):
        n = int(input("how many: "))
        def player_total(player: Player):
            return player.goals + player.assists
        def player_goals(player: Player):
            return player.goals
        players = [player for player in self.all_players_dict.player_data.values()]
        result1 = sorted(players, key=player_goals, reverse=True)
        result2 = sorted(result1, key=player_total, reverse = True)
        for i in range(n):
            print(result2[i])


    # displays top n players who scored most goals
    # if two players have the same number of goals, whoever has played the lower number of games comes first
    def most_goals(self):
        n = int(input("how many: "))
        def player_goals(player: Player):
            return player.goals
        def player_games(player: Player):
            return player.games
        players = [player for player in self.all_players_dict.player_data.values()]
        result1 = sorted(players, key=player_games)
        result2 = sorted(result1, key=player_goals, reverse=True)
        for i in range(n):
            print(result2[i])


# program begin
input_file = input("file name: ")
application = HockeyApp()
application.all_players_dict.player_data_from_json(input_file)
application.execute()



