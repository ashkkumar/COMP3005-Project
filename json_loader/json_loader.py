# Json File loader
import json
import os
import psycopg2

# Gonna load json files tpo database

# db variables
root_database_name = "project_database"
db_username = 'postgres'
db_password = '1234'
db_host = 'localhost'
db_port = '5432'

conn = psycopg2.connect(
    dbname=root_database_name,
    user=db_username,
    password=db_password,
    host=db_host,
    port=db_port)

cur = conn.cursor()

competitions_directory = "data/competitions"
matches_directory = "data/matches"
lineups_directory = "data/lineups"
events_directory = "data/events"

with open(competitions_directory) as file:
    competitions_data = json.load(file)

    for competition in competitions_data:
        if (competition["competition_name"] == "Premier League" and competition["season_name"] == "2003/2004") or \
                (competition["competition_name"] == "La Liga" and competition["season_name"] in ["2020/2021",
                                                                                                 "2019/2020",
                                                                               "2018/2019"]):
            cur.execute("""
                INSERT INTO season (season_id, season_name)
                VALUES (%s, %s)
                ON CONFLICT (season_id) DO NOTHING
            """, (competition["season_id"], competition["season_name"]))

            cur.execute("""
                INSERT INTO competitions (
                    competition_id, season_id,  competition_name,
                    competition_gender, country_name, season_name
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (competition_id) DO NOTHING

            """, (
                competition["competition_id"], competition["season_id"],
                competition["competition_name"], competition["competition_gender"],
                competition["country_name"], competition["season_name"]
            ))

for season_directory in os.listdir(matches_directory):
    season_path = os.path.join(matches_directory, season_directory)
    if season_directory.startswith("."):
        continue

    for match_file in os.listdir(season_path):
        match_path = os.path.join(season_path, match_file)

        with open(match_path) as file:
            match_data = json.load(file)

            for match in match_data:

                if (match["competition"]["competition_name"] == "Premier League" and match["season"][
                    "season_name"] == "2003/2004") or (
                        match["competition"]["competition_name"] == "La Liga" and match["season"]["season_name"] in [
                        "2020/2021", "2019/2020", "2018/2019"]):

                    cur.execute("""
                        SELECT competition_id FROM competitions WHERE competition_id = %s
                    """, (match["competition"]["competition_id"],))

                    competition_id = cur.fetchone()[0]

                    cur.execute("""
                        SELECT season_id FROM season WHERE season_id = %s
                    """, (match["season"]["season_id"],))

                    season_id = cur.fetchone()[0]

                    cur.execute("""
                        INSERT INTO country (country_id, country_name)
                        VALUES (%s, %s)
                        ON CONFLICT (country_id) DO NOTHING
                    """, (
                        match["home_team"]["country"]["id"], match["home_team"]["country"]["name"]
                    ))

                    cur.execute("""
                        INSERT INTO country (country_id, country_name)
                        VALUES (%s, %s)
                        ON CONFLICT (country_id) DO NOTHING
                    """, (
                        match["away_team"]["country"]["id"], match["away_team"]["country"]["name"]
                    ))

                    cur.execute("""
                        INSERT INTO team (team_id, team_name, team_gender, team_group, country_id)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (team_id) DO NOTHING
                    """, (
                        match["home_team"]["home_team_id"], match["home_team"]["home_team_name"],
                        match["home_team"]["home_team_gender"], match["home_team"]["home_team_group"],
                        match["home_team"]["country"]["id"]
                    ))

                    cur.execute("""
                        INSERT INTO team (team_id, team_name, team_gender, team_group, country_id)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (team_id) DO NOTHING
                    """, (
                        match["away_team"]["away_team_id"], match["away_team"]["away_team_name"],
                        match["away_team"]["away_team_gender"], match["away_team"]["away_team_group"],
                        match["away_team"]["country"]["id"]
                    ))
                    referee_id = None
                    stadium_id = None

                    if "referee" in match:
                        cur.execute("""
                            INSERT INTO country (country_id, country_name)
                            VALUES (%s, %s)
                            ON CONFLICT (country_id) DO NOTHING
                        """, (
                            match["referee"]["country"]["id"], match["referee"]["country"]["name"]
                        ))

                        cur.execute("""
                            INSERT INTO referees (referee_id, name)
                            VALUES (%s, %s)
                            ON CONFLICT (referee_id) DO NOTHING
                            RETURNING referee_id
                        """, (
                            match["referee"]["id"], match["referee"]["name"],
                        ))
                        referee_id = cur.fetchone()[0] if cur.rowcount > 0 else None

                    if "stadium" in match:
                        cur.execute("""
                            INSERT INTO country (country_id, country_name)
                            VALUES (%s, %s)
                            ON CONFLICT (country_id) DO NOTHING
                        """, (
                            match["stadium"]["country"]["id"], match["stadium"]["country"]["name"]
                        ))

                        cur.execute("""
                            INSERT INTO stadium (stadium_id, stadium_name, country_id)
                            VALUES (%s, %s, %s)
                            ON CONFLICT (stadium_id) DO NOTHING
                            RETURNING stadium_id
                        """, (
                            match["stadium"]["id"], match["stadium"]["name"],
                            match["stadium"]["country"]["id"]
                        ))
                        stadium_id = cur.fetchone()[0] if cur.rowcount > 0 else None

                    cur.execute("""
                        INSERT INTO matches (
                            match_id, competition_id, country_name, season_id, match_date, kick_off, stadium_id,
                            referee_id, home_team_id, away_team_id, home_team_score, away_team_score
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (match_id) DO NOTHING
                    """, (
                        match["match_id"],
                        competition_id, match["competition"]["country_name"], season_id, match["match_date"],
                        match["kick_off"], stadium_id, referee_id,
                        match["home_team"]["home_team_id"], match["away_team"]["away_team_id"],
                        match["home_score"], match["away_score"]
                    ))

                    # do this last
                    for team_key in ['home_team', 'away_team']:
                        team = match[team_key]
                        managers = team.get('managers')
                        if managers:
                            for manager in managers:
                                manager_id = manager['id']
                                manager_name = manager['name']
                                manager_nickname = manager.get(
                                    'nickname')
                                dob = manager['dob']
                                country_id = manager['country']['id']

                                cur.execute("""
                                       INSERT INTO Managers (manager_id, manager_name, manager_nickname, dob, country_id)
                                       VALUES (%s, %s, %s, %s, %s)
                                       ON CONFLICT (manager_id) DO NOTHING
                                   """, (manager_id, manager_name, manager_nickname, dob, country_id))

for lineup_file in os.listdir(lineups_directory):
    lineup_path = os.path.join(lineups_directory, lineup_file)
    match_id = int(lineup_file.split(".")[0])

    cur.execute(""" SELECT match_id FROM matches WHERE match_id = %s """, (match_id,))
    if cur.fetchone() is None:
        continue

    with open(lineup_path) as file:
        lineup_data = json.load(file)

        for team_lineup in lineup_data:

            team_id = team_lineup["team_id"]
            team_name = team_lineup["team_name"]

            cur.execute(""" SELECT team_id FROM team WHERE team_id = %s """, (team_id,))
            if cur.fetchone() is None:
                exit()

            for player in team_lineup["lineup"]:

                country_id = player["country"]["id"] if "country" in player and "id" in player["country"] else None
                country_name = player["country"]["name"] if "country" in player and "name" in player[
                    "country"] else None

                if country_id is not None:
                    cur.execute("""
                        INSERT INTO country (country_id, country_name)
                        VALUES (%s, %s)
                        ON CONFLICT (country_id) DO NOTHING
                    """, (country_id, country_name))

                cur.execute("""
                    INSERT INTO players (player_id, player_name, player_nickname, country_id)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (player_id) DO NOTHING
                """, (
                    player["player_id"], player["player_name"], player["player_nickname"],
                    country_id
                ))

                cur.execute(""" 
                INSERT INTO lineup (team_id, player_id, team_name)
                VALUES (%s, %s, %s)
                """, (team_id, player["player_id"], team_name
                      ))

                position_ids = set()

                for position in player["positions"]:
                    position_ids.add((position["position_id"], position["position"]))

                card_types = set()
                reason_types = set()

                for card in player["cards"]:
                    card_types.add(card["card_type"])

                for card in player["cards"]:
                    cur.execute("""
                        INSERT INTO card (card_id, card_name)
                        VALUES (%s, %s
                        )
                        ON CONFLICT (card_id) DO NOTHING

                            ;
                    """, (
                        player["player_id"], card["card_type"],
                    ))

for event_file in os.listdir(events_directory):
    event_path = os.path.join(events_directory, event_file)
    match_id = int(event_file.split('.')[0])

    cur.execute(""" SELECT match_id FROM matches WHERE match_id = %s """, (match_id,))
    if cur.fetchone() is None:
        continue

    with open(event_path, 'r') as file:
        event_data = json.load(file)

        for event in event_data:
            event_id = event["id"]
            cur.execute("""
                INSERT INTO Events (
                    event_id, index, timestamp, minute, second, type_id, possesion,
                    play_pattern_id, team_id, player_id, position_id, location,
                    duration, under_pressure, off_camera, out
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (event_id) DO NOTHING;
            """, (
                event["id"], event['index'], event['timestamp'], event['minute'],
                event['second'], event['type']['id'], event['possession'], event['play_pattern']['id'],
                event['team']['id'], event.get('player', {}).get('id'), event.get('position', {}).get('id'),
                json.dumps(event.get('location')), event.get('duration'), event.get('under_pressure', False),
                event.get('off_camera', False), event.get('out', False)
            ))

            if 'dribble' in event:
                cur.execute("""
                    INSERT INTO Dribbles (
                        event_id, match_id, outcome_id, nutmeg, overrun, no_touch
                    ) VALUES (%s, %s, %s, %s, %s, %s);
                """, (
                    event['id'],
                    match_id,
                    event['dribble'].get('outcome_id'),
                    event['dribble'].get('nutmeg', False),
                    event['dribble'].get('overrun', False),
                    event['dribble'].get('no_touch', False)
                ))

            if 'pass' in event:
                passes = event['pass']
                recipient_id = passes["recipient"]["id"] if "recipient" in passes else None
                body_part_name = passes["body_part"]["name"] if "body_part" in passes else None

                cur.execute("""
                    INSERT INTO Passes (
                        event_id, match_id, player_id, length, end_location, assisted_shot_id,
                        backheel, deflected, miscommunication, cross_pass, switch, shot_assist,
                        goal_assist, body_part, type_id, outcome_id, technique_id, technique_name
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    event_id,
                    match_id,
                    recipient_id, passes["length"], passes["end_location"],
                    passes.get("assisted_shot_id"), passes.get("backheel"), passes.get("deflected"),
                    passes.get("miscommunication"),
                    passes.get("cross_pass"), passes.get("switch"), passes.get("shot_assist"),
                    passes.get("goal_assist"), body_part_name,
                    passes.get('type', {}).get('id'), passes.get('outcome', {}).get('id'),
                    passes.get('technique', {}).get('id'), passes.get('technique', {}).get('name')

                ))

            if 'shot' in event:
                shot = event['shot']
                player_id = event['player']['id'] if 'player' in event else None
                end_location_str = json.dumps(
                    shot['end_location']) if 'end_location' in shot else None

                cur.execute("""
                    INSERT INTO Shots (
                        event_id, match_id, player_id, key_pass_id, end_location, aerial_won, follows_dribble,
                        first_time, open_goal, statsbomb_xg, deflected, technique_id, body_part, type_id, outcome_id
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    event_id,
                    match_id,
                    player_id,
                    shot.get('key_pass_id'),
                    end_location_str,
                    shot.get('aerial_won', False),
                    shot.get('follows_dribble', False),
                    shot.get('first_time', False),
                    shot.get('open_goal', False),
                    shot.get('statsbomb_xg'),
                    shot.get('deflected', False),
                    shot.get('technique_id'),
                    shot['body_part'].get('name') if 'body_part' in shot else None,
                    shot['type']['id'],
                    shot['outcome']['id'],
                ))

            if 'goalkeeper' in event:
                goalkeeper = event['goalkeeper']
                cur.execute("""
                    INSERT INTO Goalkeeper (
                        event_id, match_id, position_id, technique_id, technique_name, body_part, type_id, outcome_id
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    event_id,
                    match_id,
                    goalkeeper.get('position', {}).get('id'),
                    goalkeeper.get('technique', {}).get('id'),
                    goalkeeper.get('technique', {}).get('name'),
                    goalkeeper.get('body_part', {}).get('name'),
                    event['type']['id'],
                    goalkeeper.get('outcome', {}).get('id'),
                ))

    conn.commit()

print("Finished loading data")

conn.commit()
conn.close()
