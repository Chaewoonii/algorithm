/*
<학생들이 원하는 노트북 공동구매>
- laptops: 노트북ID(laptop_id),  가격(price) 정보
- students: 학생 정보, 원하는 노트북 정보(desired_latop_id)

학생들이 원하는 노트북이 laptops에 있다면 10% 할인해서 구매 가능(5대 단위)
laptops에 없는 노트북을 원한다면 150만원 지급

1. 학생들이 원하는 노트북별 개수 세기 5대 단위 (5로 나눈 몫, 나머지
2. laptops에 원하는 노트북이 있는지 판별하기
3. 계산: laptops에 없다면(key is null) 150만원, 있다면 5대 단위로 10% 할인 적용(*0.9*5)
*/

-- 원하는 노트북의 개수를 5로 나눈 몫, 나머지 구하기
-- 몫: truncate 버림을 이용. 하지만 정수나눗셈은 정수만 반환해서 그냥 /만 써도 된다.
    -- truncate(sum(desired_laptop_id) / 5, 0)
    -- sum(desired_laptop_id) / 5 >> 몫 반환. 이래도 된다.
WITH laptop_count AS (
    SELECT
    desired_laptop_id,
    truncate(sum(desired_laptop_id) / 5, 0) AS cnt1,
    sum(desired_laptop_id) % 5 AS cnt2
FROM students s
GROUP BY desired_laptop_id
)

SELECT
    sum(
        CASE
            WHEN l.laptop_id IS NULL THEN 1500000 -- laptops에 없다면 150만원
            ELSE (lc.cnt1 * 5 * l.price * 0.9) + (lc.cnt2 * l.price) -- laptops에 있다면 5대 단위로 10% 할인, 나머지는 정가.
        END
    ) AS TOTAL_PRICE
FROM laptop_count lc
LEFT OUTER JOIN laptops l
ON lc.desired_laptop_id = l.laptop_id

