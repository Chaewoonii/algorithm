/*
-- Table Info: Field / Type
ID / NUMBER
CITY / VARCHAR2(21)
STATE / VARCHAR2(2)
LAT_N / NUMBER
LONG_W / NUMBER
*/

-- Weather Observation Station 1
-- Query a list of CITY and STATE from the STATION table
SELECT city, state FROM station;

-- Weather Observation Station 3
-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
SELECT DISTINCT city FROM station WHERE id % 2 = 0;

-- Weather Observation Station 4
-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table
SELECT count(*) - count(DISTINCT city) FROM station;

-- Weather Observation Station 5
-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city), city LIMIT 1;
SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city)DESC, city LIMIT 1;

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