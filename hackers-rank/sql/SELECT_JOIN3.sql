-- Population Census
SELECT sum(a.population)
FROM city a JOIN country b ON(a.countrycode = b.code)
WHERE b.continent = 'Asia';

--African Cities
SELECT a.name
FROM city a JOIN country b ON(a.countrycode = b.code)
WHERE b.continent = 'Africa';

-- Average Population of each continent
-- 소수점 버림
SELECT b.continent, floor(avg(a.population))
FROM city a JOIN country b ON (a.countrycode = b.code)
GROUP BY b.continent;

-- The Report
-- Non Equi Join
SELECT CASE WHEN b.grade >= 8 THEN a.name
       ELSE NULL END as NAME,
       b.grade as GRADE,
       a.marks as MARKS
FROM Students a, Grades b
WHERE (a.marks between b.min_mark and max_mark)
ORDER BY grade DESC, name ASC, marks ASC;

-- Ollivander's Inventory
SELECT w1.id, wp1.age, w1.coins_needed, w1.power
FROM wands w1 INNER JOIN wands_property wp1 ON (w1.code = wp1.code)
WHERE wp1.is_evil != 1
AND coins_needed = (SELECT min(coins_needed)
                    FROM wands w2 INNER JOIN wands_property wp2 ON (w2.code = wp2.code)
                    WHERE w1.power = w2.power AND wp1.age = wp2.age)
ORDER BY power DESC, age DESC;
