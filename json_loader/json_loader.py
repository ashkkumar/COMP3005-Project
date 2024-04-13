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

conn = psycopg.connect(
    dbname=root_database_name,
    user=db_username,
    password=db_password,
    host=db_host,
    port=db_port)


def insert_season(matches_data):
    insert_query = """
    INSERT INTO Season (
        season_id, season_name
    ) VALUES (
        %(season_id)s,%(season_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_competition(competition_data):
    insert_query = """
    INSERT INTO Competitions (
        competition_id, season_id, competition_name, competition_gender, conutry_name, season_name
    ) VALUES (
        %(competition_id)s,%(season_id)s,%(competition_name)s,%(competition_gender)s,%(country_name)s,%(season_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for comp in competition_data:
            cur.execute(insert_query, comp)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_country(matches_data):
    insert_query = """
    INSERT INTO Country (
        country_id, country_name
    ) VALUES (
        %(country_id)s,%(country_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_stadium(matches_data):
    insert_query = """
    INSERT INTO Stadium (
        stadium_id, stadium_name, country_id
    ) VALUES (
        %(stadium_id)s,%(stadium_name)s,%(country_id)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_referees(matches_data):
    insert_query = """
    INSERT INTO Referees (
        referee_id, name
    ) VALUES (
        %(referee_id)s,%(name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_team(matches_data):
    insert_query = """
    INSERT INTO Team (
        team_id, country_id, team_name, team_gender, team_group  
    ) VALUES (
        %(team_id)s,%(country_id)s,%(team_name)s,%(team_gender)s,%(team_group)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_matches(matches_data):
    insert_query = """
    INSERT INTO Matches (
        match_id, competition_id, country_name, season_id, match_date, kick_off, stadium_id, referee_id,
        home_team_id, away_team_id, home_team_score, away_team_score
    ) VALUES (
        %(match_id)s,%(competition_id)s,%(country_name)s,%(season_id)s,%(match_date)s,%(kick_off)s,
        %(stadium_id)s,%(referee_id)s,%(home_team_id)s,%(away_team_id)s,%(home_team_score)s,%(away_team_score)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_players(matches_data):
    insert_query = """
    INSERT INTO Players (
        player_id, country_id, player_name, player_nickname, jersey_number
    ) VALUES (
        %(player_id)s,%(country_id)s,%(player_name)s,%(player_nickname)s,%(jersey_number)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_lineup(matches_data):
    insert_query = """
    INSERT INTO Lineup (
        team_id, player_id, team_name
    ) VALUES (
        %(team_id)s,%(player_id)s,%(team_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_managers(matches_data):
    insert_query = """
    INSERT INTO Managers (
        manager_id, manager_name, manager_nickname, dob, country_id
    ) VALUES (
        %(manager_id)s,%(manager_name)s,%(manager_nickname)s,%(dobs),%(country_id)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_events(events_data):
    insert_query = """
    INSERT INTO Events (
        event_id, index, timestamp, minute, second, type_id, possession, play_pattern_id, team_id,
        player_id, position_id, location, duration, under_pressure, off_camera, out
    ) VALUES (
        %(event_id)s,%(index)s,%(timestamp)s,%(minute)s,%(second)s,%(type_id)s,%(possession)s,
        %(play_pattern_id)s,%(team_id)s,%(player_id)s,%(position_id)s,%(location)s,%(duration)s,
        %(under_pressure)s,%(off_camera)s,%(out)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each event
        for event in events_data:
            # Transform 'location' from a list to a point if necessary
            if 'location' in event and isinstance(event['location'], list):
                event['location'] = f"({event['location'][0]}, {event['location'][1]})"
            cur.execute(insert_query, event)

        # Commit the transactions
        conn.commit()
        print("Events data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_dribbles(matches_data):
    insert_query = """
    INSERT INTO Dribbles (
        event_id, match_id, outcome_id, nutmeg, overrun, no_touch
    ) VALUES (
        %(event_id)s,%(match_id)s,%(outcome_id)s,%(nutmeg)s,%(overrun)s,%(no_touch)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_passes(passes_data):
    insert_query = """
    INSERT INTO Passes (
        event_id, match_id, player_id, length, end_location, assisted_shot_id, backheel, 
        deflected, miscommunication, cross_pass, switch, shot_assist, goal_assist,
        body_part, type_id, outcome_id, technique_id, technique_name
    ) VALUES (
        %(event_id)s,%(match_id)s,%(player_id)s,%(length)s,%(end_location)s,%(assisted_shot_id)s,
        %(backheel)s,%(deflected)s,%(miscommunication)s,%(cross_pass)s,%(switch)s,%(shot_assist)s,
        %(goal_assist)s,%(body_part)s,%(type_id)s,%(outcome_id)s,%(technique_id)s,%(technique_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each pass
        for pass_data in passes_data:
            # Ensure that boolean fields are boolean in Python
            for bool_field in ['backheel', 'deflected', 'miscommunication', 'cross_pass', 'switch', 'shot_assist',
                               'goal_assist']:
                if bool_field in pass_data:
                    pass_data[bool_field] = bool(pass_data[bool_field])
            cur.execute(insert_query, pass_data)

        # Commit the transactions
        conn.commit()
        print("Passes data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_shots(shots_data):
    insert_query = """
    INSERT INTO Shots (
        event_id, match_id, key_pass_id, end_location, aerial_won, follows_dribble, first_time,
        open_goal, statsbomb_xg, deflected, technique_id, body_part, type_id, outcome_id
    ) VALUES (
        %(event_id)s,%(match_id)s,%(key_pass_id)s,%(end_location)s,%(aerial_won)s,%(follows_dribble)s,
        %(first_time)s,%(open_goal)s,%(statsbomb_xg)s,%(deflected)s,%(technique_id)s,%(body_part)s,
        %(type_id)s,%(outcome_id)s 
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each shot
        for shot in shots_data:
            # Ensure that boolean fields are boolean in Python
            for bool_field in ['aerial_won', 'follows_dribble', 'first_time', 'open_goal', 'deflected']:
                if bool_field in shot:
                    shot[bool_field] = bool(shot[bool_field])
            # Cast statsbomb_xg to float
            if 'statsbomb_xg' in shot:
                shot['statsbomb_xg'] = float(shot['statsbomb_xg'])
            cur.execute(insert_query, shot)

        # Commit the transactions
        conn.commit()
        print("Shots data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_card(matches_data):
    insert_query = """
    INSERT INTO Card (
        card_id, card_name
    ) VALUES (
        %(card_id)s,%(card_name)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_fouls(matches_data):
    insert_query = """
    INSERT INTO Foul_Committed (
        event_id, advantage, counterpress, offensive, penalty, card_id, type_id
    ) VALUES (
        %(event_id)s,%(advantage)s,%(counterpress)s,%(offensive)s,%(penalty)s,%(card_id)s,%(type_id)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_goalkeepers(matches_data):
    insert_query = """
    INSERT INTO Goalkeeper (
        event_id, match_id, position_id, technique_id, technique_name, body_part, type_id, outcome_id
    ) VALUES (
        %(event_id)s,%(match_id)s,%(position_id)s,%(technique_id)s,%(technique_name)s,
        %(body_part)s,%(type_id)s,%(outcome_id)s
    );
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for match in matches_data:
            cur.execute(insert_query, match)

        # Commit the transactions
        conn.commit()
        print("Matches data inserted successfully.")
    except psycopg.DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


# Assuming you have a JSON file with matches data
# Replace 'path_to_your_json_file.json' with the path to your JSON file
# with open('path_to_your_json_file.json', 'r') as file:
#   matches_data = json.load(file)

# Call the function to insert data
# insert_matches(matches_data)


def import_matches(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        insert_matches(data)
        insert_team(data)
        insert_managers(data)
        insert_stadium(data)
        insert_referees(data)
        insert_season(data)
    return


def import_competitions(jfile):
    with open(jfile, 'r') as file:
        insert_competition(json.load(file))
    return


def import_events(jfile):
    with open(jfile, 'r') as file:
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
        insert_lineup(data)
        insert_team(data)
        insert_players(data)
        insert_card(data)
        insert_country(data)
    return


def import_all_data():
    path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data"
    # match data 18/19
    # match data 02/03
    jfile = os.path.join(path, "matches", "2", "44.json")
    import_matches(jfile)
    jfile = os.path.join(path, "matches", "11", "4.json")
    import_matches(jfile)
    # match data 19/20
    jfile = os.path.join(path, "matches", "11", "42.json")
    import_matches(jfile)
    # match data 20/21
    jfile = os.path.join(path, "matches", "11", "90.json")
    import_matches(jfile)

    # competitions
    jfile = os.path.join(path, "competitions.json")
    import_competitions(jfile)

    # events
    event_path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/events"
    for file in os.listdir(event_path):
        import_events(file)

    # lineups
    lineup_path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/lineups"
    for file in os.listdir(lineup_path):
        import_lineups(file)

    conn.close()


import_all_data()
