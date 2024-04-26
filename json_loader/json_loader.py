# Json File loader
import json
import psycopg
import os

# Gonna load json files tpo database

# db variables
root_database_name = "project_database"
query_database_name = "query_database"
db_username = 'postgres'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'


def connect():
    conn = psycopg.connect(
        dbname=root_database_name,
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port)
    return conn


def insert_seasons(seasons_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for season in seasons_data:
        try:
            # Prepare season data for insertion
            season_data = {
                'season_id': season['season_id'],  # Ensure this key exists in your JSON data
                'season_name': season['season_name']
            }

            # Insert season data
            insert_query = """
                INSERT INTO Season (season_id, season_name) VALUES (%(season_id)s, %(season_name)s)
                ON CONFLICT (season_id) DO NOTHING;
            """
            cur.execute(insert_query, season_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for season ID {season['season_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_competitions(competitions_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for competition in competitions_data:
        try:
            # Prepare competition data for insertion
            competition_data = {
                'competition_id': competition['competition_id'],  # Ensure this key exists in your data
                'season_id': competition['season_id'],
                'competition_name': competition['competition_name'],
                'competition_gender': competition['competition_gender'],
                'country_name': competition['country_name'],
                'season_name': competition['season_name']
            }

            # Insert competition data
            insert_query = """
                INSERT INTO Competitions (
                    competition_id, season_id, competition_name, competition_gender, 
                    country_name, season_name
                ) VALUES (
                    %(competition_id)s, %(season_id)s, %(competition_name)s, %(competition_gender)s, 
                    %(country_name)s, %(season_name)s
                )
                ON CONFLICT (competition_id) DO NOTHING;
            """
            cur.execute(insert_query, competition_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for competition ID {competition['competition_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_countries(countries_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for country in countries_data:
        try:
            # Prepare country data for insertion
            country_data = {
                'country_id': country['id'],  # Ensure this key exists in your data
                'country_name': country['name']
            }

            # Insert country data
            insert_query = """
                INSERT INTO Country (country_id, country_name) 
                VALUES (%(country_id)s, %(country_name)s);
            """
            cur.execute(insert_query, country_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for country ID {country['country_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_stadiums(match_data):
    conn = connect()  # This function should connect to your PostgreSQL database
    cur = conn.cursor()

    for match in match_data:
        try:
            # Check if 'stadium' key is present in the match data
            if 'stadium' in match and 'id' in match['stadium'] and 'name' in match['stadium']:
                stadium_data = {
                    'stadium_id': match['stadium']['id'],
                    'stadium_name': match['stadium']['name'],
                    'country_id': match['stadium']['country']['id']  # Ensure country ID exists in your country table
                }

                # SQL query to insert stadium data
                insert_query = """
                    INSERT INTO Stadium (stadium_id, stadium_name, country_id)
                    VALUES (%(stadium_id)s, %(stadium_name)s, %(country_id)s)
                    ON CONFLICT (stadium_id) DO NOTHING;
                """
                cur.execute(insert_query, stadium_data)
                conn.commit()
            else:
                print(f"Missing required stadium data in match ID {match['match_id']}")
        except Exception as e:
            print(f"Failed to insert data for stadium ID {match.get('stadium', {}).get('id', 'Unknown')} due to: {e}")
            conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()



def insert_referees(referees_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for referee in referees_data:
        try:
            # Prepare referee data for insertion
            referee_data = {
                'referee_id': referee['referee_id'],  # Ensure this key exists in your data
                'name': referee['name']
            }

            # Insert referee data
            insert_query = """
                INSERT INTO REFEREES (referee_id, name) VALUES (%(referee_id)s, %(name)s);
            """
            cur.execute(insert_query, referee_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for referee ID {referee['referee_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_teams(teams_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for team in teams_data:
        try:
            # Prepare team data for insertion
            team_data = {
                'team_id': team['team_id'],  # Ensure this key exists in your data
                'country_id': team['country_id'],  # Make sure this country_id already exists in the Country table
                'team_name': team['team_name'],
                'team_gender': team['team_gender'],
                'team_group': team['team_group']
            }

            # Insert team data
            insert_query = """
                INSERT INTO Team (team_id, country_id, team_name, team_gender, team_group) VALUES (%(team_id)s, %(country_id)s, %(team_name)s, %(team_gender)s, %(team_group)s);
            """
            cur.execute(insert_query, team_data)
            conn.commit()

        except Exception as e:
            team_id = team.get('team_id', 'Unknown')
            print(f"Failed to insert data for team ID {team['team_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_matches(matches_data):
    conn = connect()
    cur = conn.cursor()

    required_keys = [
        'match_id', 'competition', 'home_team', 'away_team',
        'season', 'match_date', 'kick_off', 'home_score', 'away_score'
    ]

    for match in matches_data:
        if not all(key in match for key in required_keys):
            print(f"Missing required keys in match data: {match}")
            continue

        try:
            # Extracting nested data correctly
            match_data = {
                'match_id': match['match_id'],
                'competition_id': match['competition']['competition_id'],
                'country_name': match['competition']['country_name'],
                'season_id': match['season']['season_id'],
                'match_date': match['match_date'],
                'kick_off': match['kick_off'],
                'stadium_id': match.get('stadium', {}).get('id', None),
                'referee_id': match.get('referee', {}).get('id', None),
                'home_team_id': match['home_team']['home_team_id'],
                'away_team_id': match['away_team']['away_team_id'],
                'home_team_score': match['home_score'],
                'away_team_score': match['away_score']
            }

            country_data = {
                'country_id': match['home_team']['country']['id'],  # Ensure this key exists in your data
                'country_name': match['home_team']['country']['name']
            }

            # Insert match data into the database
            insert_query = """
                INSERT INTO Matches (
                    match_id, competition_id, country_name, season_id, match_date, kick_off,
                    stadium_id, referee_id, home_team_id, away_team_id, home_team_score, away_team_score
                ) VALUES (
                    %(match_id)s, %(competition_id)s, %(country_name)s, %(season_id)s, %(match_date)s, %(kick_off)s,
                    %(stadium_id)s, %(referee_id)s, %(home_team_id)s, %(away_team_id)s, %(home_team_score)s, %(away_team_score)s
                );
            """
            cur.execute(insert_query, match_data)
            conn.commit()

            insert_query = """
                            INSERT INTO Country (country_id, country_name) 
                            VALUES (%(country_id)s, %(country_name)s);
                        """
            cur.execute(insert_query, country_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for match ID {match['match_id']} due to: {e}")
            # conn.rollback()

    cur.close()
    conn.close()


def insert_players(players_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for player in players_data:
        try:
            # Prepare player data for insertion
            player_data = {
                'player_id': player['player_id'],  # Ensure this key exists in your data
                'country_id': player['country_id'],  # Make sure this country_id already exists in the Country table
                'player_name': player['player_name'],
                'player_nickname': player.get('player_nickname', None),  # Optional field
                'jersey_number': player['jersey_number']
            }

            # Insert player data
            insert_query = """
                INSERT INTO Players (player_id, country_id, player_name, player_nickname, jersey_number) VALUES (%(player_id)s, %(country_id)s, %(player_name)s, %(player_nickname)s, %(jersey_number)s);
            """
            cur.execute(insert_query, player_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for player ID {player['player_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_lineups(lineups_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for lineup in lineups_data:
        try:
            # Prepare lineup data for insertion
            lineup_data = {
                'team_id': lineup['team_id'],  # Ensure this team_id exists in the Team table
                'player_id': lineup['player_id'],  # Ensure this player_id exists in the Players table
                'team_name': lineup['team_name']  # Ensure this team_name corresponds to the team_id in the Team table
            }

            # Insert lineup data
            insert_query = """
                INSERT INTO Lineup (team_id, player_id, team_name) VALUES (%(team_id)s, %(player_id)s, %(team_name)s);
            """
            cur.execute(insert_query, lineup_data)
            conn.commit()

        except Exception as e:
            print(
                f"Failed to insert data for lineup with team ID {lineup['team_id']} and player ID {lineup['player_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_managers(managers_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for manager in managers_data:
        try:
            # Prepare manager data for insertion
            manager_data = {
                'manager_id': manager['manager_id'],  # Ensure this key exists in your data
                'manager_name': manager['manager_name'],
                'manager_nickname': manager.get('manager_nickname', None),  # Optional field
                'dob': manager['dob'],
                'country_id': manager['country_id']  # Make sure this country_id exists in the Country table
            }

            # Insert manager data
            insert_query = """
                INSERT INTO Managers (manager_id, manager_name, manager_nickname, dob, country_id) VALUES (%(manager_id)s, %(manager_name)s, %(manager_nickname)s, %(dob)s, %(country_id)s);
            """
            cur.execute(insert_query, manager_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for manager ID {manager['manager_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_events(events_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for event in events_data:
        try:
            # Prepare event data for insertion
            event_data = {
                'event_id': event['event_id'],  # Ensure this key exists in your data
                'index': event['index'],
                'timestamp': event['timestamp'],
                'minute': event['minute'],
                'second': event['second'],
                'type_id': event['type_id'],
                'possesion': event['possesion'],
                'play_pattern_id': event['play_pattern_id'],
                'team_id': event['team_id'],  # Ensure this team_id exists in the Team table
                'player_id': event['player_id'],  # Ensure this player_id exists in the Players table
                'position_id': event['position_id'],
                'location': event['location'],
                'duration': event['duration'],
                'under_pressure': event['under_pressure'],
                'off_camera': event['off_camera'],
                'out': event['out']
            }

            # Insert event data
            insert_query = """
                INSERT INTO Events (
                    event_id, index, timestamp, minute, second, type_id, possesion, play_pattern_id,
                    team_id, player_id, position_id, location, duration, under_pressure, off_camera, out
                ) VALUES (
                    %(event_id)s, %(index)s, %(timestamp)s, %(minute)s, %(second)s, %(type_id)s, %(possesion)s, %(play_pattern_id)s,
                    %(team_id)s, %(player_id)s, %(position_id)s, %(location)s, %(duration)s, %(under_pressure)s, %(off_camera)s, %(out)s
                );
            """
            cur.execute(insert_query, event_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for event ID {event['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_dribbles(dribbles_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for dribble in dribbles_data:
        try:
            # Prepare dribble data for insertion
            dribble_data = {
                'event_id': dribble['event_id'],  # Ensure this event_id exists in the Events table
                'match_id': dribble['match_id'],  # Ensure this match_id exists in the Matches table
                'outcome_id': dribble['outcome_id'],
                'nutmeg': dribble['nutmeg'],
                'overrun': dribble['overrun'],
                'no_touch': dribble['no_touch']
            }

            # Insert dribble data
            insert_query = """
                INSERT INTO Dribbles (event_id, match_id, outcome_id, nutmeg, overrun, no_touch) VALUES (%(event_id)s, %(match_id)s, %(outcome_id)s, %(nutmeg)s, %(overrun)s, %(no_touch)s);
            """
            cur.execute(insert_query, dribble_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for dribble with event ID {dribble['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_passes(passes_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for pass_ in passes_data:
        try:
            # Prepare pass data for insertion
            pass_data = {
                'event_id': pass_['event_id'],  # Ensure this event_id exists in the Events table
                'match_id': pass_['match_id'],  # Ensure this match_id exists in the Matches table
                'player_id': pass_['player_id'],  # Ensure this player_id exists in the Players table
                'length': pass_['length'],
                'end_location': pass_['end_location'],
                'assisted_shot_id': pass_.get('assisted_shot_id', None),  # Optional field
                'backheel': pass_['backheel'],
                'deflected': pass_['deflected'],
                'miscommunication': pass_['miscommunication'],
                'cross_pass': pass_['cross_pass'],
                'switch': pass_['switch'],
                'shot_assist': pass_['shot_assist'],
                'goal_assist': pass_['goal_assist'],
                'body_part': pass_['body_part'],
                'type_id': pass_['type_id'],
                'outcome_id': pass_['outcome_id'],
                'technique_id': pass_['technique_id'],
                'technique_name': pass_['technique_name']
            }

            # Insert pass data
            insert_query = """
                INSERT INTO Passes (
                    event_id, match_id, player_id, length, end_location, assisted_shot_id, backheel, deflected, 
                    miscommunication, cross_pass, switch, shot_assist, goal_assist, body_part, type_id, outcome_id,
                    technique_id, technique_name
                ) VALUES (
                    %(event_id)s, %(match_id)s, %(player_id)s, %(length)s, %(end_location)s, %(assisted_shot_id)s, 
                    %(backheel)s, %(deflected)s, %(miscommunication)s, %(cross_pass)s, %(switch)s, %(shot_assist)s, 
                    %(goal_assist)s, %(body_part)s, %(type_id)s, %(outcome_id)s, %(technique_id)s, %(technique_name)s
                );
            """
            cur.execute(insert_query, pass_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for pass with event ID {pass_['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_shots(shots_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for shot in shots_data:
        try:
            # Prepare shot data for insertion
            shot_data = {
                'event_id': shot['event_id'],  # Ensure this event_id exists in the Events table
                'match_id': shot['match_id'],  # Ensure this match_id exists in the Matches table
                'key_pass_id': shot.get('key_pass_id', None),  # Optional field
                'end_location': shot['end_location'],
                'aerial_won': shot['aerial_won'],
                'follows_dribble': shot['follows_dribble'],
                'first_time': shot['first_time'],
                'open_goal': shot['open_goal'],
                'statsbomb_xg': shot['statsbomb_xg'],
                'deflected': shot['deflected'],
                'technique_id': shot['technique_id'],
                'body_part': shot['body_part'],
                'type_id': shot['type_id'],
                'outcome_id': shot['outcome_id']
            }

            # Insert shot data
            insert_query = """
                INSERT INTO Shots (
                    event_id, match_id, key_pass_id, end_location, aerial_won, follows_dribble, 
                    first_time, open_goal, statsbomb_xg, deflected, technique_id, body_part, 
                    type_id, outcome_id
                ) VALUES (
                    %(event_id)s, %(match_id)s, %(key_pass_id)s, %(end_location)s, %(aerial_won)s, 
                    %(follows_dribble)s, %(first_time)s, %(open_goal)s, %(statsbomb_xg)s, 
                    %(deflected)s, %(technique_id)s, %(body_part)s, %(type_id)s, %(outcome_id)s
                );
            """
            cur.execute(insert_query, shot_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for shot with event ID {shot['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_cards(cards_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for card in cards_data:
        try:
            # Prepare card data for insertion
            card_data = {
                'card_id': card['card_id'],  # Ensure this key exists in your data
                'card_name': card['card_name']
            }

            # Insert card data
            insert_query = """
                INSERT INTO Card (card_id, card_name) VALUES (%(card_id)s, %(card_name)s);
            """
            cur.execute(insert_query, card_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for card ID {card['card_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_fouls(fouls_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for foul in fouls_data:
        try:
            # Prepare foul data for insertion
            foul_data = {
                'event_id': foul['event_id'],  # Ensure this event_id exists in the Events table
                'advantage': foul['advantage'],
                'counterpress': foul['counterpress'],
                'offensive': foul['offensive'],
                'penalty': foul['penalty'],
                'card_id': foul.get('card_id'),  # Optional, may be None if no card was given
                'type_id': foul['type_id']
            }

            # Insert foul data
            insert_query = """
                INSERT INTO Foul_Committed (
                    event_id, advantage, counterpress, offensive, penalty, card_id, type_id
                ) VALUES (
                    %(event_id)s, %(advantage)s, %(counterpress)s, %(offensive)s, %(penalty)s, %(card_id)s, %(type_id)s
                );
            """
            cur.execute(insert_query, foul_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for foul with event ID {foul['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def insert_goalkeepers(goalkeepers_data):
    conn = connect()  # Assume a 'connect' function is available to connect to your database
    cur = conn.cursor()

    for goalkeeper in goalkeepers_data:
        try:
            # Prepare goalkeeper data for insertion
            goalkeeper_data = {
                'event_id': goalkeeper['event_id'],  # Ensure this event_id exists in the Events table
                'match_id': goalkeeper['match_id'],  # Ensure this match_id exists in the Matches table
                'position_id': goalkeeper['position_id'],
                'technique_id': goalkeeper['technique_id'],
                'technique_name': goalkeeper['technique_name'],
                'body_part': goalkeeper['body_part'],
                'type_id': goalkeeper['type_id'],
                'outcome_id': goalkeeper['outcome_id']
            }

            # Insert goalkeeper data
            insert_query = """
                INSERT INTO Goalkeeper (
                    event_id, match_id, position_id, technique_id, technique_name, body_part, type_id, outcome_id
                ) VALUES (
                    %(event_id)s, %(match_id)s, %(position_id)s, %(technique_id)s, %(technique_name)s, %(body_part)s, %(type_id)s, %(outcome_id)s
                );
            """
            cur.execute(insert_query, goalkeeper_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for goalkeeper with event ID {goalkeeper['event_id']} due to: {e}")
            # conn.rollback()  # Roll back the transaction on error

    cur.close()
    conn.close()


def import_matches(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        insert_stadiums(data)
        insert_matches(data)
        insert_teams(data)
        insert_referees(data)
        insert_managers(data)
    return


def import_competitions(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        insert_seasons(data)
        insert_competitions(data)
    return


def import_events(jfile):
    with open(jfile, 'r') as file:
        print(file)
        data = json.load(file)
        insert_events(data)
        insert_dribbles(data)
        insert_fouls(data)
        insert_passes(data)
        insert_shots(data)
        insert_goalkeepers(data)
    return


def import_lineups(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        insert_lineups(data)
        insert_teams(data)
        insert_players(data)
        insert_cards(data)
    return


def import_from_directory(directory):

    comp_path = os.path.join("/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/competitions.json")
    import_competitions(comp_path)

    path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/matches"
    jfile = os.path.join(path, "2", "44.json")
    import_matches(jfile)
    # match data 18/19
    jfile = os.path.join(path, "11", "4.json")
    import_matches(jfile)
    # match data 19/20
    jfile = os.path.join(path, "11", "42.json")
    import_matches(jfile)
    # match data 20/21
    jfile = os.path.join(path, "11", "90.json")
    import_matches(jfile)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                full_path = os.path.join(root, filename)
                if 'events' in filename.lower():
                    import_events(full_path)
                elif 'lineups' in filename.lower():
                    import_lineups(full_path)
                else:
                    print(f"Skipped: {filename}")
            else:
                print(f"File not processed (not JSON): {filename}")


# Process the parent directory recursively
import_from_directory("/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/")

