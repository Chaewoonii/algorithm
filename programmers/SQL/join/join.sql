-- 없어진 기록 찾기
-- 동물 입양기록(outs)에는 있는데 보호 기록(ins)에는 없는 동물
SELECT o.animal_id, o.name
FROM animal_ins i RIGHT OUTER JOIN animal_outs o ON (i.animal_id = o.animal_id)
WHERE i.animal_id IS NULL;

-- 있었는데요 없었습니다
-- 보호 시작일보다 입양일이 더 빠른 동물 조회
-- Datetime 은 더 빠른 것이 더 작은 것.
SELECT i.animal_id, i.name
FROM ANIMAL_INS i JOIN ANIMAL_OUTS o ON (i.animal_id = o.animal_id)
WHERE i.datetime > o.datetime
ORDER BY i.datetime;

-- 오랜기간 보호한 동물 1
SELECT i.name, i.datetime AS DATETIME
FROM ANIMAL_INS i LEFT OUTER JOIN ANIMAL_OUTS o ON (i.animal_id = o.animal_id)
WHERE o.animal_id IS NULL
ORDER BY i.datetime ASC
LIMIT 3;

-- ***
-- 보호소에서 중성화한 동물
SELECT i.animal_id, i.animal_type, i.name
FROM ANIMAL_INS i JOIN ANIMAL_OUTS o ON (i.animal_id = o.animal_id)
WHERE i.sex_upon_intake LIKE "Intact%"
    AND o.sex_upon_outcome REGEXP("Spayed|Neutered")  -- !
-- o.sex_upon_intake LIKE "Spayed%" OR o.sex_upon_intake LIKE "Neutered%" : % 생략
ORDER BY i.animal_id;
-- ***

--상품 별 오프라인 매출 구하기
SELECT p.product_code, SUM(p.price * o.sales_amount) AS SALES
FROM product p JOIN offline_sale o ON (p.product_id = o.product_id)
GROUP BY p.product_code
ORDER BY SALES DESC, p.product_code ASC;

-- 상품을 구매한 회원 비율 구하기
WITH user_2021 AS(
    SELECT * FROM user_info WHERE YEAR(joined) = 2021
)

SELECT YEAR(sales_date) AS YEAR,
        MONTH(sales_date) AS MONTH,
        COUNT(DISTINCT user_id) AS PURCHASED_USERS,
        ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM user_2021), 1) AS PURCHASED_RATIO
FROM online_sale
WHERE user_id IN (SELECT user_id FROM user_2021)
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;