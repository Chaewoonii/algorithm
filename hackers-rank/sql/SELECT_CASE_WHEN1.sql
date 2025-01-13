/* Type Of Triangle
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

- Equilateral: It's a triangle with  sides of equal length.
- Isosceles: It's a triangle with  sides of equal length.
- Scalene: It's a triangle with  sides of differing lengths.
- Not A Triangle: The given values of A, B, and C don't form a triangle.

-- Table Info: Field / Type
A / Int
B / Int
C / Int
*/

-- WHEN 구문의 순서가 중요
SELECT CASE WHEN A + B <= C THEN 'Not A Triangle'
            WHEN A = B AND B = C THEN 'Equilateral'
            WHEN A != B AND B!= C AND A!= C THEN 'Scalene'
            WHEN A = B OR A = C OR B = C THEN 'Isosceles'
            END AS triangle_type
FROM triangles;