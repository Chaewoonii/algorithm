/*
Pivot the Occupation column in OCCUPATIONS
so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation.
The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
Note: Print NULL when there are no more names corresponding to an occupation.

-- Table Info: Field / Type
- name / str
- occupation / str

*/

SELECT
    MAX(CASE WHEN occupation = "Doctor" THEN name END) AS doctor,
    MAX(CASE WHEN occupation = "Professor" THEN name END) AS professor,
    MAX(CASE WHEN occupation = "Singer" THEN name END) AS singer,
    MAX(CASE WHEN occupation = "Actor" THEN name END) AS actor
FROM (
    SELECT
        ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name) AS r_num,
        occupation,
        name
    FROM occupations
) AS ordered_occupations
GROUP BY r_num
ORDER BY r_num;