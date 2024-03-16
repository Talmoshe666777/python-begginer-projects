from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()
# printer.pprint()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("----------------------------")
        print(f"{home_team['triCode']} VS {away_team['triCode']}")
        print(f"{home_team['score']} VS {away_team['score']}")
        print(f"{clock} VS {period['current']}")


def get_stats():
    stats = get_links()['leagueTeamsStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    # filter returns filter object so better convert to list.
    # lambda is an anonymous function that let us use a condition that returns true or false.
    teams = list(filter(lambda x: x['team'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']  # points per game
        print(f"{i + 1}. {name} - {nickname} - {ppg}")


get_stats()
get_scoreboard()
