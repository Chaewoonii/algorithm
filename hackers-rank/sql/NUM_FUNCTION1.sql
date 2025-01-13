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

-- Weather Observation Station 2
SELECT round(sum(lat_n), 2), round(sum(long_w), 2) FROM station;

-- Weather Observation Station 12
-- truncate: 버림 함수
SELECT truncate(sum(lat_n), 4) FROM station WHERE lat_n > 38.7880 and lat_n < 137.2345;

-- Weather Observation Station 14
SELECT truncate(max(lat_n), 4) FROM station WHERE lat_n < 137.2345;

-- Weather Observation station 15
SELECT round(long_w, 4) FROM station WHERE lat_n < 137.2345 ORDER BY lat_n DESC LIMIT 1;

-- Weather Observation station 16
SELECT round(min(lat_n), 4) FROM station WHERE lat_n > 38.7880;

-- Weather Observation station 17
SELECT round(long_w, 4) FROM station WHERE lat_n > 38.7880 ORDER BY lat_n LIMIT 1;

-- Weather Observation station 18
SELECT round(((max(long_w) - min(long_w)) + (max(lat_n) - min(lat_n))), 4) FROM station;

-- Weather Observation station 19
-- sqrt(): 제곱근 함수
-- power(n, m): n의 m제곱 / oracle: power, mysql: pow
SELECT round(
            sqrt(
                power((max(long_w) - min(long_w)), 2)
                + power((max(lat_n) - min(lat_n)), 2)
            )
        , 4)
FROM station;

-- Weather Observation Station 20
-- oracle: median 함수
SELECT round(median(lat_n), 4) FROM station;

-- mysql: percent rank 함수 이용
-- percent_rank(): 인수로 지정한 값의 그룹 내 상대적 위치를 나타내는 백분위 순위를 반환
SELECT round(lat_n, 4) FROM station
WHERE lat_n in (
    SELECT lat_n FROM (
        SELECT lat_n,
               percent_rank() over(order by lat_n) as p_rank
        FROM station
                      ) p_station
    WHERE p_rank = 0.5
);



