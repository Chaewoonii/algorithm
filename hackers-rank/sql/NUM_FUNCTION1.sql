-- Revising Aggregations
-- sum: 합계
SELECT sum(population) FROM city WHERE district = "California";

-- Population Density Difference
-- max: 주어진 컬럼에서 최댓값
-- min: 주어진 컬럼에서 최솟값
SELECT max(population) - min(population) FROM city;

-- HackerRank, Average Population
-- round(col, n): 반올림 함수, 소숫점 n+1번째 자리에서 반올림하여 소숫점 n번째 자리까지 출력
-- 자릿수 미 지정 시 소숫점 첫 번째 자리에서 반올림.
SELECT round(avg(population)) FROM city;

-- HackerRank, The Blunder
-- 0 삭제: 2004 --> 24 : replace 사용, 숫자에서 문자열로 자동 형변환
-- ceil 올림 함수
SELECT ceil(
       avg(salary) - avg(replace(salary, '0', ''))
       )
FROM employees;