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


def insert_season1(data):
    conn = connect()
    cur = conn.cursor()
    for match in data:
        season_data = match['season']
        try:
            print("Inserting season with data:", season_data)  # Debug output
            insert_query = "INSERT INTO Season (season_id, season_name) VALUES (%(season_id)s, %(season_name)s) ON CONFLICT (season_id) DO NOTHING;"
            cur.execute(insert_query, season_data)
            conn.commit()
        except Exception as e:
            print(f"Failed to insert season data due to: {e}")
            conn.rollback()

def insert_competition(competition_data):
    conn = connect()
    insert_query = """
    INSERT INTO competitions (
        competition_id, season_id, competition_name, competition_gender, country_name, season_name
    ) VALUES (
        %(competition_id)s, %(season_id)s ,%(competition_name)s,%(competition_gender)s,%(country_name)s,%(season_name)s
    )
    ON CONFLICT (competition_id) DO UPDATE SET
    competition_name = EXCLUDED.competition_name,
    competition_gender = EXCLUDED.competition_gender,
    country_name = EXCLUDED.country_name,
    season_name = EXCLUDED.season_name;
    """
    try:
        # Connect to the database
        cur = conn.cursor()

        # Insert each match
        for comp in competition_data:
            cur.execute(insert_query, comp)

        # Commit the transactions
        conn.commit()
        print("Comp data inserted successfully.")
    except psycopg.DatabaseError as e:
       # if conn:
        #    conn.rollback()
        print(f"Error comps: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_country(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO country (
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
        print("country data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
         #   conn.rollback()
        print(f"Error countries: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_stadium(data):
    # Assuming data is a list of matches, and each match contains a 'stadium' key
    conn = connect()
    cur = conn.cursor()
    for match in data:
        stadium_data = {
            'stadium_id': match['stadium']['id'],
            'stadium_name': match['stadium']['name'],
            'country_id': match['stadium']['country']['id']
        }
        try:
            print("Inserting stadium with data:", stadium_data)  # Debug output
            insert_query = """
            INSERT INTO stadium (stadium_id, stadium_name, country_id)
            VALUES (%(stadium_id)s, %(stadium_name)s, %(country_id)s)
            ON CONFLICT (stadium_id) DO UPDATE SET
                stadium_name = EXCLUDED.stadium_name,
                country_id = EXCLUDED.country_id;
            """
            cur.execute(insert_query, stadium_data)
            conn.commit()
        except Exception as e:
            print(f"Failed to insert stadium data for Stadium ID {stadium_data['stadium_id']} due to: {e}")
            conn.rollback()


def insert_referees(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO referees (
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
        print("ref data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
         #   conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_team(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO team (
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
        print("team data inserted successfully.")
    except psycopg.DatabaseError as e:
       # if conn:
        #    conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_matches(matches_data):
    conn = connect()
    cur = conn.cursor()
    for match in matches_data:
        try:
            # Prepare match data for insertion
            match_data = {
                'match_id': match['match_id'],  # Ensure this key exists in your JSON data
                'away_team_id': match['away_team']['away_team_id'],
                'away_team_score': match['away_score'],
                'competition_id': match['competition']['competition_id'],
                'country_name': match['competition']['country_name'],
                'home_team_id': match['home_team']['home_team_id'],
                'home_team_score': match['home_score'],
                'referee_id': match.get('referee', {}).get('referee_id', None),
                'season_id': match['season']['season_id'],
                'stadium_id': match['stadium']['id']
            }

            # Insert match data
            insert_query = """
                       INSERT INTO Matches (
                           match_id, away_team_id, away_team_score, competition_id, country_name, 
                           home_team_id, home_team_score, referee_id, season_id, stadium_id
                       ) VALUES (
                           %(match_id)s, %(away_team_id)s, %(away_team_score)s, %(competition_id)s, %(country_name)s, 
                           %(home_team_id)s, %(home_team_score)s, %(referee_id)s, %(season_id)s, %(stadium_id)s
                       );
                       """
            cur.execute(insert_query, match_data)
            conn.commit()

        except Exception as e:
            print(f"Failed to insert data for match ID {match['match_id']} due to: {e}")
            conn.rollback()


def insert_players(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO players (
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
        print("players data inserted successfully.")
    except psycopg.DatabaseError as e:
      #  if conn:
            #conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_lineup(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO lineup (
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
        print("lineup data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
           # conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_managers(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO managers (
        manager_id, manager_name, manager_nickname, dob, country_id
    ) VALUES (
        %(manager_id)s,%(manager_name)s,%(manager_nickname)s,%(dob)s,%(country_id)s
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
        print("Managers data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
            #conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_events(events_data):
    conn = connect()
    insert_query = """
    INSERT INTO events (
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
       # if conn:
           # conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_dribbles(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO dribbles (
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
        print("dribs data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
          #  conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_passes(passes_data):
    conn = connect()
    insert_query = """
    INSERT INTO passes (
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
        #if conn:
          #  conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_shots(shots_data):
    conn = connect()
    insert_query = """
    INSERT INTO shots (
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
       # if conn:
         #   conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_card(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO card (
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
        print("card data inserted successfully.")
    except psycopg.DatabaseError as e:
        #if conn:
          #  conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_fouls(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO foul_committed (
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
        print("fouls data inserted successfully.")
    except psycopg.DatabaseError as e:
       # if conn:
        #    conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_goalkeepers(matches_data):
    conn = connect()
    insert_query = """
    INSERT INTO goalkeeper (
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
        print("goalkeepers data inserted successfully.")
    except psycopg.DatabaseError as e:
       # if conn:
        #    conn.rollback()
        print(f"Error keepers: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def import_matches(jfile):
    with open(jfile, 'r') as file:
        data = json.load(file)
        insert_matches(data)
        insert_team(data)
        insert_stadium(data)
        insert_referees(data)
        insert_season1(data)
        insert_managers(data)
    return


def import_competitions(jfile):
    with open(jfile, 'r') as file:
        insert_competition(json.load(file))
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
        insert_lineup(data)
        insert_team(data)
        insert_players(data)
        insert_card(data)
        insert_country(data)
    return


def import_all_data():
    conn = connect()

    path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/"
    jfile = os.path.join(path, "competitions.json")

    import_competitions(jfile)

    # match data 02/03


    # competitions

    # events
    event_path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/events/"
    for file in os.listdir(event_path):
        import_events(file)

    # lineups
    lineup_path = "/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/lineups/"
    for file in os.listdir(lineup_path):
        import_lineups(file)

    conn.close()


def import_from_directory(directory):

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
                # Determine the type of data based on the filename and call appropriate import function
                if 'matches' in filename.lower():
                    import_matches(full_path)
                elif 'competitions' in filename.lower():
                    import_competitions(full_path)
                elif 'events' in filename.lower():
                    import_events(full_path)
                elif 'lineups' in filename.lower():
                    import_lineups(full_path)
                else:
                    print(f"Skipped: {filename}")
            else:
                print(f"File not processed (not JSON): {filename}")

# Process the parent directory recursively
import_from_directory("/Users/ashkumar/PycharmProjects/COMP3005-Project/json_loader/data/")
