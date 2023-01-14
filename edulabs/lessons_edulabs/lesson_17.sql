CREATE TABLE movies (
		id SERIAL PRIMARY KEY,
		movie_name VARCHAR(256) NOT NULL,
		release_year SMALLINT NOT NULL,
		imdb_reating FLOAT
);



INSERT
	INTO
	movies (movie_name,
	release_year,
	imdb_reating)
VALUES
('The godfather',
1972,
9.2);



INSERT
	INTO
	movies (movie_name,
	release_year,
	imdb_reating)
VALUES
('The Shawshank Redemption',
1994,
9.8);



UPDATE
	movies
SET
	imdb_reating = 9.2
WHERE
	id = 1;



INSERT
	INTO
	movies (movie_name,
	release_year)
VALUES
('The Green Mile', 1999);




UPDATE
	movies
SET
	imdb_reating = 9.5
WHERE
	id = 2;



DELETE FROM movies WHERE id = 4;


CREATE TABLE directors (
		id SERIAL PRIMARY KEY,
		director_name VARCHAR(256) NOT NULL,
		origin_country VARCHAR(128)
);



INSERT INTO directors(director_name)
VALUES('Frank Darabont');



INSERT INTO directors(director_name, origin_country)
VALUES('Quenrin Tarantino', 'israel');



INSERT INTO directors(director_name, origin_country)
VALUES('Francis Ford Coppola', 'Italy');



DELETE FROM directors WHERE id = 4;


SELECT * FROM directors;


SELECT * FROM movies;


ALTER TABLE movies
        ADD COLUMN director_id int CONSTRAINT fk_director_id FOREIGN KEY (director_id) REFERENCES directors;


ALTER TABLE movies ALTER COLUMN director_id SET NOT NULL;


UPDATE movies set director_id = 1 WHERE id = 2;


INSERT INTO movies (movie_name, release_year, director_id)
	   VALUES ('pulp fiction', 1994, 3);


INSERT INTO movies (movie_name, release_year, director_id)
	   VALUES ('Django Unchaind', 2012, 3);


---------------for showing----------------

SELECT * FROM movies
		 CROSS JOIN directors;


SELECT * FROM movies m
		 JOIN directors d ON m.director_id = d.id;


SELECT m.movie_name, m.release_year, d.director_name FROM movies m ----OR JUST  JOIN
		 INNER JOIN directors d ON m.director_id = d.id;



SELECT m.movie_name, m.release_year, d.director_name FROM movies m
		LEFT JOIN directors d ON m.director_id = d.id; ----IF MOVIE DONT HAVE DIRECTOR STILL PRINT IT



SELECT m.movie_name, m.release_year, d.director_name FROM movies m
		RIGHT JOIN directors d ON m.director_id = d.id; ----IF DIRECTOR DONT HAVE MOVIE STILL PRINT IT



SELECT m.movie_name, m.release_year, d.director_name FROM movies m
		FULL OUTER JOIN directors d ON m.director_id = d.id; ----IF DIRECTOR DONT HAVE MOVIE STILL PRINT IT OR IF MOVIE DONT HAVE DIRECTOR STILL PRINT IT




















