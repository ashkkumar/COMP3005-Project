# Json File loader
import json
import psycopg
# Gonna load json files tpo database

#db variables
root_database_name = "project_database"
query_database_name = "query_database"
db_username = 'postgres'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'

conn = psycopg.connect(
    dbname= root_database_name,
    user= db_username,
    password= db_password,
    host=db_host,
    port= db_port)

def insert_season(matches_data):
    insert_query = """
    INSERT INTO Season (
        season_id
        season_name
    ) VALUES (
        %s,%s
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
        competition_id,
        season_id,
        competition_name,
        competition_gender,
        conutry_name,
        season_name
    ) VALUES (
        %s,%s,%s,%s,%s,%s
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
        country_id
        country_name
    ) VALUES (
        %s,%s
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
        stadium_id
        stadium_name
        country_id
    ) VALUES (
        %s,%s,%s
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
        referee_id
        name
    ) VALUES (
        %s,%s
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
        team_id
        country_id,
        team_name,
        team_gender,
        team_group  
    ) VALUES (
        %s,%s,%s,%s,%s
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
        match_id,
        competition_id,
        country_name,
        season_id,
        match_date,
        kick_off,
        stadium_id,
        referee_id,
        home_team_id,
        away_team_id,
        home_team_score,
        away_team_score
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
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
        player_id, 
        country_id,
        player_name,
        player_nickname,
        jersey_number
    ) VALUES (
        %s,%s,%s,%s,%s
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
        team_id
        player_id,
        team_name
    ) VALUES (
        %s,%s,%s
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
        manager_id,
        manager_name,
        manager_nickname,
        dob,
        country_id
    ) VALUES (
        %s,%s,%s,%s,%s
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
        event_id,
        index,
        timestamp,
        minute,
        second,
        type_id,
        possession,
        play_pattern_id,
        team_id,
        player_id,
        position_id,
        location,
        duration,
        under_pressure,
        off_camera,
        out
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
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
        event_id,
        match_id,
        outcome_id,
        nutmeg,
        overrun,
        no_touch
    ) VALUES (
        %s,%s,%s,%s,%s,%s
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
        event_id,
        match_id,
        player_id,
        length,
        end_location,
        assisted_shot_id,
        backheel,
        deflected,
        miscommunication,
        cross_pass,
        switch,
        shot_assist,
        goal_assist,
        body_part,
        type_id,
        outcome_id,
        technique_id,
        technique_name
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
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
        event_id,
        match_id,
        key_pass_id,
        end_location,
        aerial_won,
        follows_dribble,
        first_time,
        open_goal,
        statsbomb_xg,
        deflected,
        technique_id,
        body_part,
        type_id,
        outcome_id
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s 
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
        card_id
        card_name
    ) VALUES (
        %s,%s
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
        event_id,
        advantage,
        counterpress,
        offensive,
        penalty,
        card_id,
        type_id
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s
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
        event_id,
        match_id,
        position_id,
        technique_id,
        technique_name,
        body_part,
        type_id,
        outcome_id
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s
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
#with open('path_to_your_json_file.json', 'r') as file:
 #   matches_data = json.load(file)

# Call the function to insert data
#insert_matches(matches_data)


def import_json():
    return
