SELECT * FROM levelupapi_gametype;
SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_event;
SELECT * FROM levelupapi_eventgamer;



SELECT
    event.id,
    event.date,
    event.time,
    event.title,
    gamer.user_id as gamer_id,
    au.first_name || ' ' || au.last_name as FullName
FROM levelupapi_event as event
JOIN levelupapi_eventgamer as gamerevent
    ON event.id = gamerevent.event_id
JOIN levelupapi_gamer as gamer
    ON gamerevent.gamer_id = gamer.id
JOIN auth_user as au
    ON gamer.id = au.id;


SELECT
    event.id,
    event.date,
    event.time,
    event.title,
    gamer.user_id as gamer_id,
    gm.title,
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