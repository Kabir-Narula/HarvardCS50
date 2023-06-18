-- 1
SELECT title FROM movies WHERE year='2008';
-- 2
SELECT birth FROM people WHERE name='Emma Stone';
-- 3
SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC;
-- 4
SELECT count(movie_id) FROM ratings WHERE rating = '10.0';
-- 5
SELECT title,year FROM movies WHERE title LIKE "%Harry Potter%" ORDER BY year ASC;
-- 6
SELECT AVG(rating) FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);
-- 7
SELECT title, rating FROM movies JOIN ratings ON ratings.movie_id = movies.id WHERE year = 2010 ORDER BY rating DESC, title ASC;
-- 8
SELECT name FROM people JOIN stars ON stars.person_id = people.id JOIN movies ON stars.movie_id = movies.id WHERE title = 'Toy Story';
-- 9
SELECT name FROM people JOIN stars ON stars.person_id = people.id JOIN movies ON stars.movie_id = movies.id WHERE year = 2004 ORDER BY birth;
-- 10
SELECT name FROM people JOIN directors ON directors.person_id = people.id JOIN movies ON directors.movie_id = movies.id JOIN ratings ON ratings.movie_id = movies.id WHERE rating >= 9.0;
-- 11
SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON stars.person_id = people.id JOIN ratings ON ratings.movie_id = movies.id WHERE name = 'Chadwick Boseman' ORDER BY rating DESC LIMIT 5;
-- 12
SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON stars.person_id = people.id WHERE name = 'Johnny Depp' INTERSECT SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON stars.person_id = people.id WHERE name = 'Helena Bonham Carter';
-- 13
SELECT name FROM people JOIN stars ON stars.person_id = people.id JOIN movies ON movies.id = stars.movie_id WHERE title IN (SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON stars.person_id = people.id WHERE name = 'Kevin Bacon') AND name != 'Kevin Bacon';