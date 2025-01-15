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