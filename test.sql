SELECT * FROM levelupapi_gametype;


CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.title,
    g.maker,
    g.game_type_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
;



CREATE VIEW EVENTS_BY_USER AS
SELECT
    event.id,
    event.date,
    event.time,
    event.title,
    gamer.user_id as gamer_id,
    gm.title as title,
    au.first_name || ' ' || au.last_name as full_name
FROM levelupapi_event as event
JOIN levelupapi_eventgamer as gamerevent
    ON event.id = gamerevent.event_id
JOIN levelupapi_gamer as gamer
    ON gamerevent.gamer_id = gamer.id
JOIN auth_user as au
    ON gamer.user_id = au.id
JOIN levelupapi_game as gm
    ON event.game_id = gm.id;