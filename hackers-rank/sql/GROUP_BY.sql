-- Contest Leaderboard
-- WITH: MySQL 8.0 이상에서 지원. 5.X 는 지원 안함
-- ORDER BY: 일부 설정에서 별칭 사용할 수 없을 수 있음
-- 쉼표 잘 확인하기
SELECT hs.hacker_id,
       hs.name,
       sum(hs.max_score) as total_score
FROM (
    SELECT h.hacker_id,
           h.name,
           max(s.score) AS max_score
    FROM hackers h
    JOIN submissions s ON (h.hacker_id = s.hacker_id)
    GROUP BY h.hacker_id, h.name, s.challenge_id
) AS hs
GROUP BY hs.hacker_id, hs.name
HAVING total_score > 0
ORDER BY total_score DESC, hs.hacker_id;