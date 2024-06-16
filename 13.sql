SELECT name from stars
JOIN people ON stars.person_id = people.id
WHERE stars.movie_id IN (SELECT stars.movie_id from stars WHERE stars.person_id IN (SELECT people.id from people WHERE people.name = "Kevin Bacon" AND people.birth = 1958))