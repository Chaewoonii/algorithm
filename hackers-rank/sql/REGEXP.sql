-- Weather Observation Station 6
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
-- REGEXP: MySql의 정규 표현식. (Oracle은 REGEXP_LIKE 등)
-- ^: ~로 시작 하는(앞에 붙임)
-- |: OR 표현
SELECT DISTINCT city FROM station WHERE city REGEXP("^a|^e|^i|^o|^u");

-- Weather Observation Station 7
-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
-- $: ~로 끝나는(뒤에 붙임)
SELECT DISTINCT city FROM station WHERE city REGEXP("a$|e$|i$|o$|u$");

-- Weather Observation Station 8
-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city REGEXP("^a|^e|^i|^o|^u") AND city REGEXP("a$|e$|i$|o$|u$");

-- Weather Observation Station 9
-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
-- REGEXP 가 아닌 것을 찾을 때는 REGEXP 앞에 NOT 을 붙인다.
SELECT DISTINCT city FROM station WHERE city NOT REGEXP("^a|^e|^i|^o|^u");

-- Weather Observation Station 10
-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city NOT REGEXP("a$|e$|i$|o$|u$");

-- Weather Observation Station 11
-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city NOT REGEXP("^a|^e|^i|^o|^u") OR city NOT REGEXP("a$|e$|i$|o$|u$");

-- Weather Observation Station 12
-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city NOT REGEXP("^a|^e|^i|^o|^u") AND city NOT REGEXP("a$|e$|i$|o$|u$");