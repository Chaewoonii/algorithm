

/* Higher Than 75 Marks
Query the Name of any student in STUDENTS who scored higher than  Marks.
Order your output by the last three characters of each name.
If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, basics.),
secondary sort them by ascending ID.
-- Table Info: Field / Type
id / Int
name / String
marks / Int */
SELECT name FROM students WHERE marks > 75 ORDER BY RIGHT(name, 3), id;

/* Employee Names
Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
-- Table Info: Field / Type
employee_id / Int
name / String
months / Int
salary / Int */
SELECT name FROM employee ORDER BY name;

/* Employee Salaries
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee
having a salary greater than  per month who have been employees for less than  months.
Sort your result by ascending employee_id.
-- Table Info: Field / Type
employee_id / Int
name / String
months / Int
salary / Int */
SELECT name FROM employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id;

-- Top Earners
/*
earnings 에 따라 그룹화 및 정렬한 후, 첫 번째 행만 조회
*/
SELECT salary * months as earnings, count(*)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC LIMIT 1;