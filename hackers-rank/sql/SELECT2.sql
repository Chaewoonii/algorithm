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

