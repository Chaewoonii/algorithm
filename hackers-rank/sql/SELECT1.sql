/*
-- Table INFO: Field / Type
ID / NUMBER
NAME / VARCHAR2(17)
COUNTRYCODE / VARCHAR2(3)
DISTRICT / VARCHAR2(20)
POPULATION / NUMBER
*/

-- Revising the Select Query1
--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
SELECT * FROM city WHERE population > 100000 AND countrycode = "USA";

-- Revising the Select Query2
-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
SELECT name FROM city WHERE population > 120000 and countrycode = "USA";

-- Select ALL
-- Query all columns (attributes) for every row in the CITY table.
SELECT * FROM city;

-- Select By ID
-- Query all columns for a city in CITY with the ID 1661.
SELECT * FROM city WHERE id = 1661;

-- Japanese Cities' Attributes
-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM city WHERE countrycode = "JPN"

-- Japanese Cities' Names
-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
select name from city where countrycode = "JPN";

