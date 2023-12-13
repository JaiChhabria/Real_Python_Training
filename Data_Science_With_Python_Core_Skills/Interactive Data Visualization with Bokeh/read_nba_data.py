import pandas as pd

# Read the csv files:
player_stats = pd.read_csv('2017-18_playerBoxScore_csv',
                           parse_dates=['gmDate'])

team_stats = pd.read_csv('2017-18_teamBoxScore_csv',
                         parse_dates=['gmDate'])

standings = pd.read_csv('2017-18_standings.csv',
                        parse_dates=['stDate'])