--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

-- Started on 2024-04-13 22:18:46 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 229 (class 1259 OID 17652)
-- Name: card; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.card (
    card_id integer NOT NULL,
    card_name character varying(10)
);


ALTER TABLE public.card OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17478)
-- Name: competitions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.competitions (
    competition_id integer NOT NULL,
    season_id integer,
    competition_name character varying(50),
    competition_gender character varying(10),
    country_name character varying(30),
    season_name character varying(30)
);


ALTER TABLE public.competitions OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 17488)
-- Name: country; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.country (
    country_id integer NOT NULL,
    country_name character varying(40)
);


ALTER TABLE public.country OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17608)
-- Name: dribbles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dribbles (
    event_id integer,
    match_id integer,
    outcome_id integer,
    nutmeg boolean,
    overrun boolean,
    no_touch boolean
);


ALTER TABLE public.dribbles OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 17593)
-- Name: events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.events (
    event_id integer NOT NULL,
    index integer,
    "timestamp" character varying(30),
    minute integer,
    second integer,
    type_id integer,
    possesion integer,
    play_pattern_id integer,
    team_id integer,
    player_id integer,
    position_id integer,
    location character varying(30),
    duration character varying(15),
    under_pressure boolean,
    off_camera boolean,
    "out" boolean
);


ALTER TABLE public.events OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17657)
-- Name: foul_committed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foul_committed (
    event_id integer,
    advantage boolean,
    counterpress boolean,
    offensive boolean,
    penalty boolean,
    card_id integer,
    type_id integer
);


ALTER TABLE public.foul_committed OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17670)
-- Name: goalkeeper; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.goalkeeper (
    event_id integer,
    match_id integer,
    position_id integer,
    technique_id integer,
    technique_name character varying(30),
    body_part character varying(20),
    type_id integer,
    outcome_id integer
);


ALTER TABLE public.goalkeeper OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17565)
-- Name: lineup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lineup (
    team_id integer,
    player_id integer,
    team_name character varying(100)
);


ALTER TABLE public.lineup OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17583)
-- Name: managers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.managers (
    manager_id integer NOT NULL,
    manager_name character varying(100),
    manager_nickname character varying(50),
    dob character varying(40),
    country_id integer
);


ALTER TABLE public.managers OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17520)
-- Name: matches; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.matches (
    match_id integer NOT NULL,
    competition_id integer,
    country_name character varying(30),
    season_id integer,
    match_date date,
    kick_off time without time zone,
    stadium_id integer,
    referee_id integer,
    home_team_id integer,
    away_team_id integer,
    home_team_score integer,
    away_team_score integer
);


ALTER TABLE public.matches OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17621)
-- Name: passes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.passes (
    event_id integer,
    match_id integer,
    player_id integer,
    length character varying(30),
    end_location character varying(30),
    assisted_shot_id character varying(100),
    backheel boolean,
    deflected boolean,
    miscommunication boolean,
    cross_pass boolean,
    switch boolean,
    shot_assist boolean,
    goal_assist boolean,
    body_part character varying(20),
    type_id integer,
    outcome_id integer,
    technique_id integer,
    technique_name character varying(30)
);


ALTER TABLE public.passes OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17555)
-- Name: players; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.players (
    player_id integer NOT NULL,
    country_id integer,
    player_name character varying(100),
    player_nickname character varying(50),
    jersey_number integer
);


ALTER TABLE public.players OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17503)
-- Name: referees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.referees (
    referee_id integer NOT NULL,
    name character varying(100)
);


ALTER TABLE public.referees OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 17473)
-- Name: season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.season (
    season_id integer NOT NULL,
    season_name character varying(30)
);


ALTER TABLE public.season OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 17639)
-- Name: shots; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shots (
    event_id integer,
    match_id integer,
    key_pass_id character varying(100),
    end_location character varying(30),
    aerial_won boolean,
    follows_dribble boolean,
    first_time boolean,
    open_goal boolean,
    statsbomb_xg numeric(15,10),
    deflected boolean,
    technique_id integer,
    body_part character varying(20),
    type_id integer,
    outcome_id integer
);


ALTER TABLE public.shots OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17493)
-- Name: stadium; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stadium (
    stadium_id integer NOT NULL,
    stadium_name character varying(50),
    country_id integer
);


ALTER TABLE public.stadium OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 17508)
-- Name: team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team (
    team_id integer NOT NULL,
    country_id integer,
    team_name character varying(100),
    team_gender character varying(10),
    team_group character varying(40)
);


ALTER TABLE public.team OWNER TO postgres;

--
-- TOC entry 3714 (class 0 OID 17652)
-- Dependencies: 229
-- Data for Name: card; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.card (card_id, card_name) FROM stdin;
\.


--
-- TOC entry 3701 (class 0 OID 17478)
-- Dependencies: 216
-- Data for Name: competitions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.competitions (competition_id, season_id, competition_name, competition_gender, country_name, season_name) FROM stdin;
9	27	1. Bundesliga	male	Germany	2015/2016
1267	107	African Cup of Nations	male	Africa	2023
16	4	Champions League	male	Europe	2018/2019
87	84	Copa del Rey	male	Spain	1983/1984
37	90	FA Women's Super League	female	England	2020/2021
1470	274	FIFA U20 World Cup	male	International	1979
43	106	FIFA World Cup	male	International	2022
1238	108	Indian Super league	male	India	2021/2022
11	90	La Liga	male	Spain	2020/2021
81	48	Liga Profesional	male	Argentina	1997/1998
7	235	Ligue 1	male	France	2022/2023
44	107	Major League Soccer	male	United States of America	2023
116	68	North American League	male	North and Central America	1977
49	3	NWSL	female	United States of America	2018
2	27	Premier League	male	England	2015/2016
12	27	Serie A	male	Italy	2015/2016
55	43	UEFA Euro	male	Europe	2020
35	75	UEFA Europa League	male	Europe	1988/1989
53	106	UEFA Women's Euro	female	Europe	2022
72	107	Women's World Cup	female	International	2023
\.


--
-- TOC entry 3702 (class 0 OID 17488)
-- Dependencies: 217
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.country (country_id, country_name) FROM stdin;
68	England
\.


--
-- TOC entry 3711 (class 0 OID 17608)
-- Dependencies: 226
-- Data for Name: dribbles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dribbles (event_id, match_id, outcome_id, nutmeg, overrun, no_touch) FROM stdin;
\.


--
-- TOC entry 3710 (class 0 OID 17593)
-- Dependencies: 225
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.events (event_id, index, "timestamp", minute, second, type_id, possesion, play_pattern_id, team_id, player_id, position_id, location, duration, under_pressure, off_camera, "out") FROM stdin;
\.


--
-- TOC entry 3715 (class 0 OID 17657)
-- Dependencies: 230
-- Data for Name: foul_committed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.foul_committed (event_id, advantage, counterpress, offensive, penalty, card_id, type_id) FROM stdin;
\.


--
-- TOC entry 3716 (class 0 OID 17670)
-- Dependencies: 231
-- Data for Name: goalkeeper; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.goalkeeper (event_id, match_id, position_id, technique_id, technique_name, body_part, type_id, outcome_id) FROM stdin;
\.


--
-- TOC entry 3708 (class 0 OID 17565)
-- Dependencies: 223
-- Data for Name: lineup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lineup (team_id, player_id, team_name) FROM stdin;
\.


--
-- TOC entry 3709 (class 0 OID 17583)
-- Dependencies: 224
-- Data for Name: managers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.managers (manager_id, manager_name, manager_nickname, dob, country_id) FROM stdin;
\.


--
-- TOC entry 3706 (class 0 OID 17520)
-- Dependencies: 221
-- Data for Name: matches; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.matches (match_id, competition_id, country_name, season_id, match_date, kick_off, stadium_id, referee_id, home_team_id, away_team_id, home_team_score, away_team_score) FROM stdin;
3749052	2	England	44	2004-02-07	16:00:00	\N	\N	\N	\N	1	3
3749522	2	England	44	2003-12-26	13:00:00	\N	\N	\N	\N	3	0
\.


--
-- TOC entry 3712 (class 0 OID 17621)
-- Dependencies: 227
-- Data for Name: passes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.passes (event_id, match_id, player_id, length, end_location, assisted_shot_id, backheel, deflected, miscommunication, cross_pass, switch, shot_assist, goal_assist, body_part, type_id, outcome_id, technique_id, technique_name) FROM stdin;
\.


--
-- TOC entry 3707 (class 0 OID 17555)
-- Dependencies: 222
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.players (player_id, country_id, player_name, player_nickname, jersey_number) FROM stdin;
\.


--
-- TOC entry 3704 (class 0 OID 17503)
-- Dependencies: 219
-- Data for Name: referees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.referees (referee_id, name) FROM stdin;
\.


--
-- TOC entry 3700 (class 0 OID 17473)
-- Dependencies: 215
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.season (season_id, season_name) FROM stdin;
27	2015/2016
107	2023
4	2018/2019
1	2017/2018
2	2016/2017
26	2014/2015
25	2013/2014
24	2012/2013
23	2011/2012
22	2010/2011
21	2009/2010
41	2008/2009
39	2006/2007
37	2004/2005
44	2003/2004
76	1999/2000
277	1972/1973
71	1971/1972
276	1970/1971
84	1983/1984
268	1982/1983
279	1977/1978
90	2020/2021
42	2019/2020
274	1979
106	2022
3	2018
55	1990
54	1986
51	1974
272	1970
270	1962
269	1958
108	2021/2022
40	2007/2008
38	2005/2006
278	1973/1974
48	1997/1998
275	1981
235	2022/2023
68	1977
86	1986/1987
43	2020
75	1988/1989
30	2019
\.


--
-- TOC entry 3713 (class 0 OID 17639)
-- Dependencies: 228
-- Data for Name: shots; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shots (event_id, match_id, key_pass_id, end_location, aerial_won, follows_dribble, first_time, open_goal, statsbomb_xg, deflected, technique_id, body_part, type_id, outcome_id) FROM stdin;
\.


--
-- TOC entry 3703 (class 0 OID 17493)
-- Dependencies: 218
-- Data for Name: stadium; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stadium (stadium_id, stadium_name, country_id) FROM stdin;
\.


--
-- TOC entry 3705 (class 0 OID 17508)
-- Dependencies: 220
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team (team_id, country_id, team_name, team_gender, team_group) FROM stdin;
\.


--
-- TOC entry 3529 (class 2606 OID 17656)
-- Name: card card_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.card
    ADD CONSTRAINT card_pkey PRIMARY KEY (card_id);


--
-- TOC entry 3509 (class 2606 OID 17482)
-- Name: competitions competitions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competitions
    ADD CONSTRAINT competitions_pkey PRIMARY KEY (competition_id);


--
-- TOC entry 3511 (class 2606 OID 17492)
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (country_id);


--
-- TOC entry 3527 (class 2606 OID 17597)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (event_id);


--
-- TOC entry 3525 (class 2606 OID 17587)
-- Name: managers managers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.managers
    ADD CONSTRAINT managers_pkey PRIMARY KEY (manager_id);


--
-- TOC entry 3521 (class 2606 OID 17524)
-- Name: matches matches_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_pkey PRIMARY KEY (match_id);


--
-- TOC entry 3523 (class 2606 OID 17559)
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (player_id);


--
-- TOC entry 3515 (class 2606 OID 17507)
-- Name: referees referees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.referees
    ADD CONSTRAINT referees_pkey PRIMARY KEY (referee_id);


--
-- TOC entry 3507 (class 2606 OID 17477)
-- Name: season season_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season
    ADD CONSTRAINT season_pkey PRIMARY KEY (season_id);


--
-- TOC entry 3513 (class 2606 OID 17497)
-- Name: stadium stadium_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadium
    ADD CONSTRAINT stadium_pkey PRIMARY KEY (stadium_id);


--
-- TOC entry 3517 (class 2606 OID 17512)
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (team_id);


--
-- TOC entry 3519 (class 2606 OID 17514)
-- Name: team team_team_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_team_name_key UNIQUE (team_name);


--
-- TOC entry 3530 (class 2606 OID 17483)
-- Name: competitions competitions_season_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competitions
    ADD CONSTRAINT competitions_season_id_fkey FOREIGN KEY (season_id) REFERENCES public.season(season_id);


--
-- TOC entry 3546 (class 2606 OID 17611)
-- Name: dribbles dribbles_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dribbles
    ADD CONSTRAINT dribbles_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- TOC entry 3547 (class 2606 OID 17616)
-- Name: dribbles dribbles_match_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dribbles
    ADD CONSTRAINT dribbles_match_id_fkey FOREIGN KEY (match_id) REFERENCES public.matches(match_id);


--
-- TOC entry 3544 (class 2606 OID 17603)
-- Name: events events_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- TOC entry 3545 (class 2606 OID 17598)
-- Name: events events_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.team(team_id);


--
-- TOC entry 3553 (class 2606 OID 17665)
-- Name: foul_committed foul_committed_card_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foul_committed
    ADD CONSTRAINT foul_committed_card_id_fkey FOREIGN KEY (card_id) REFERENCES public.card(card_id);


--
-- TOC entry 3554 (class 2606 OID 17660)
-- Name: foul_committed foul_committed_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foul_committed
    ADD CONSTRAINT foul_committed_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- TOC entry 3555 (class 2606 OID 17673)
-- Name: goalkeeper goalkeeper_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goalkeeper
    ADD CONSTRAINT goalkeeper_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- TOC entry 3556 (class 2606 OID 17678)
-- Name: goalkeeper goalkeeper_match_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goalkeeper
    ADD CONSTRAINT goalkeeper_match_id_fkey FOREIGN KEY (match_id) REFERENCES public.matches(match_id);


--
-- TOC entry 3540 (class 2606 OID 17573)
-- Name: lineup lineup_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lineup
    ADD CONSTRAINT lineup_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- TOC entry 3541 (class 2606 OID 17568)
-- Name: lineup lineup_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lineup
    ADD CONSTRAINT lineup_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.team(team_id);


--
-- TOC entry 3542 (class 2606 OID 17578)
-- Name: lineup lineup_team_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lineup
    ADD CONSTRAINT lineup_team_name_fkey FOREIGN KEY (team_name) REFERENCES public.team(team_name);


--
-- TOC entry 3543 (class 2606 OID 17588)
-- Name: managers managers_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.managers
    ADD CONSTRAINT managers_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(country_id);


--
-- TOC entry 3533 (class 2606 OID 17550)
-- Name: matches matches_away_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_away_team_id_fkey FOREIGN KEY (away_team_id) REFERENCES public.team(team_id);


--
-- TOC entry 3534 (class 2606 OID 17525)
-- Name: matches matches_competition_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_competition_id_fkey FOREIGN KEY (competition_id) REFERENCES public.competitions(competition_id);


--
-- TOC entry 3535 (class 2606 OID 17545)
-- Name: matches matches_home_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_home_team_id_fkey FOREIGN KEY (home_team_id) REFERENCES public.team(team_id);


--
-- TOC entry 3536 (class 2606 OID 17540)
-- Name: matches matches_referee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_referee_id_fkey FOREIGN KEY (referee_id) REFERENCES public.referees(referee_id);


--
-- TOC entry 3537 (class 2606 OID 17530)
-- Name: matches matches_season_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_season_id_fkey FOREIGN KEY (season_id) REFERENCES public.season(season_id);


--
-- TOC entry 3538 (class 2606 OID 17535)
-- Name: matches matches_stadium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_stadium_id_fkey FOREIGN KEY (stadium_id) REFERENCES public.stadium(stadium_id);


--
-- TOC entry 3548 (class 2606 OID 17624)
-- Name: passes passes_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passes
    ADD CONSTRAINT passes_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- TOC entry 3549 (class 2606 OID 17629)
-- Name: passes passes_match_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passes
    ADD CONSTRAINT passes_match_id_fkey FOREIGN KEY (match_id) REFERENCES public.matches(match_id);


--
-- TOC entry 3550 (class 2606 OID 17634)
-- Name: passes passes_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passes
    ADD CONSTRAINT passes_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- TOC entry 3539 (class 2606 OID 17560)
-- Name: players players_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(country_id);


--
-- TOC entry 3551 (class 2606 OID 17642)
-- Name: shots shots_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shots
    ADD CONSTRAINT shots_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- TOC entry 3552 (class 2606 OID 17647)
-- Name: shots shots_match_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shots
    ADD CONSTRAINT shots_match_id_fkey FOREIGN KEY (match_id) REFERENCES public.matches(match_id);


--
-- TOC entry 3531 (class 2606 OID 17498)
-- Name: stadium stadium_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadium
    ADD CONSTRAINT stadium_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(country_id);


--
-- TOC entry 3532 (class 2606 OID 17515)
-- Name: team team_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(country_id);


-- Completed on 2024-04-13 22:18:47 EDT

--
-- PostgreSQL database dump complete
--

