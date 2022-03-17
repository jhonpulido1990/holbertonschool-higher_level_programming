-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_genres.name
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id 
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = "DEXTER" ORDER BY tv_genres.name ASC;
