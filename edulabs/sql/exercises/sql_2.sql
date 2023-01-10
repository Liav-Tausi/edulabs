--SELECT * FROM movies;
--
--
--INSERT INTO movies (movie_name, release_year, director_id)
--	   VALUES ('star wars 4', 1977, 7);
--
--INSERT INTO movies (movie_name, release_year, director_id)
--	   VALUES ('star wars 5', 1980, 6);
--
--INSERT INTO movies (movie_name, release_year, director_id)
--	   VALUES ('star wars 6', 1983, 5);
--
--INSERT INTO directors(director_name, origin_country)
--	   VALUES('Richard Marquand', 'US');
--
--INSERT INTO directors(director_name, origin_country)
--	   VALUES('Irvin Kershner', 'US');
--
--INSERT INTO directors(director_name, origin_country)
--	   VALUES('George Lucas', 'US');
--
--INSERT INTO movies(length_in_min)
--VALUES (123, 45, 76)
--
--UPDATE movies set length_in_min = 341 WHERE id = 7;
--
--CREATE TABLE series(
--			 id SERIAL PRIMARY KEY,
--			 series_name VARCHAR(256)
--);
--
--INSERT INTO series(series_name) VALUES ('AVATAR trilogy');
--
--
--INSERT INTO series(series_name) VALUES ('star wars trilogy');
--
--
--
--UPDATE movies m
--SET series_id = 1
--WHERE m.movie_name LIKE '%God%';
--
--
--
--ALTER TABLE public.movies ALTER COLUMN series_id DROP NOT NULL;
--
--
--UPDATE movies SET series_id = NULL;
--
--
--ALTER TABLE public.movies ALTER COLUMN series_id DROP DEFAULT;
--
--
--ALTER TABLE movies CONSTRAINT fk_series_id FOREIGN KEY (series_id) REFERENCES series(id);
--
--
--SELECT *
--FROM movies m ;
--
----ALTER TABLE public.movies ALTER COLUMN series_id SET NOT NULL;
--
--
--create table actors(
--    id serial primary key,
--    name varchar(256) not null,
--    birth_year smallint check (birth_year > 1800)
--);
--
--
--create table movie_actors (
--    id serial primary key,
--    movie_id int not null,
--    actor_id int not null,
--    is_main_role bool not null,
--    constraint fk_movie_id foreign key (movie_id)
--        references movies(id),
--    constraint fk_actor_id foreign key (actor_id)
--        references actors(id)
--);
--
--
--select m.movie_name , a."name"  from movies m
--join movie_actors ma on m.id = ma.movie_id
--join actors a on a.id = ma.actor_id ;
--
--SELECT * from movies;
--
--
--UPDATE movies set series_id = 3 WHERE id = 16;
--


--1 Display a table that contains all the data for all the movies
-- (including to which series the movie is related, and director’s name)
SELECT m.id,
  m.movie_name,
  m.release_year ,
  m.length_in_min,
  d.director_name
FROM movies m
  JOIN directors d ON m.director_id = d.id;





--2 Display a table that contains series name and amount
-- of movies in the series
SELECT s.series_name,
	count(*)
FROM movies m JOIN series s on m.series_id = s.id
group by s.series_name;





--3 Display a table that shows director name and amount of
-- movies for this director
SELECT d.director_name,
	count(*)
FROM movies m JOIN directors d on m.director_id = d.id
group by d.director_name;




--4 Display a table that contains all the directors in the db,
-- amount of movies for each director, and amount of series for each
SELECT director_name,
	   count(m.*) as movies,
	   count(s.*) as series
FROM movies m
	JOIN directors d on m.director_id = d.id
	JOIN series s on m.series_id = s.id
group by d.director_name;




--5 Display all the movies, their series and directors that have at
-- least 2 movies in the series

SELECT m.movie_name,
	   s.series_name,
	   d.director_name
FROM movies m
JOIN directors d ON d.id = m.director_id
JOIN series s ON m.series_id = s.id
WHERE s.id in (SELECT series_id
FROM movies
GROUP BY series_id HAVING count(*) >= 2);


--6 Display movies that are not part of any series and their directors

SELECT m.movie_name,
	   d.director_name
FROM movies m
JOIN directors d ON m.director_id = d.id
WHERE series_id IS NULL;





















