/*
Given the table schemas below, write a query to print the company_code, founder name,
total number of lead managers, total number of senior managers, total number of managers,
and total number of employees. Order your output by ascending company_code.

-- Table Info: Field /Type
  1) company
    - company_code / str
    - founder / str
  2) lead_manager
    - lead_manager_code / str
    - company_code / str
  3) senior_manager
    - senior_manager_code / str
    - lead_manager_code / str
    - company_code / str
  4) manager
    - manager_code / str
    - senior_manager_code / str
    - lead_manager_code / str
    - company_code / str
  5) employee
    - employee_code / str
    - manager_code / str
    - senior_manager_code / str
    - lead_manager_code / str
    - company_code / str
*/

/* 풀이
1. 그룹 내에서 중복을 제외하고 수를 세야 하므로 distinct를 사용
2. 데이터 누락을 방지하기 위해 큰 범위부터 left outer join을 수행
   - 순차적으로 일치하는 컬럼을 사용하여 정렬
4. group by 절이 사용되면 select에 group by에 사용된 컬럼 혹은 집계함수만 사용되어야 함
5. company_code 를 기준으로 정렬
 */
SELECT A.company_code,
       A.founder,
       count(DISTINCT B.lead_manager_code),
       count(DISTINCT C.senior_manager_code),
       count(DISTINCT D.manager_code),
       count(DISTINCT E.employee_code)
FROM company A LEFT OUTER JOIN lead_manager B ON (A.company_code = B.company_code)
    LEFT OUTER JOIN senior_manager C ON (B.lead_manager_code = C.lead_manager_code)
    LEFT OUTER JOIN manager D ON (C.senior_manager_code = D.senior_manager_code)
    LEFT OUTER JOIN employee E ON (D.manager_code = E.manager_code)
GROUP BY A.company_code, B.founder
ORDER BY company_code;