
-- HackerRank: Challenges
-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

WITH challenge_counts AS (
    SELECT h.hacker_id as hacker_id, h.name as name, COUNT(challenge_id) as c_cnt
    FROM hackers h JOIN challenges c ON (h.hacker_id = c.hacker_id)
    GROUP BY hacker_id, name
)

SELECT hacker_id, name, c_cnt
FROM challenge_counts
WHERE c_cnt IN (SELECT max(c_cnt) FROM challenge_counts)
    OR c_cnt NOT IN (SELECT c_cnt FROM challenge_counts GROUP BY c_cnt HAVING COUNT(*) > 1)
ORDER BY c_cnt DESC, hacker_id;