/* Top Competitors
Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard!
Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge.
Order your output in descending order by the total number of challenges in which the hacker earned a full score.
If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
-- Table Info: Field / Type
    1) HACKERS
      - hacker_id / Int
      - name / String
    2) DIFFICULTY
      - difficulty_level / Int
      - score / Int
    3) CHALLENGES
      - challenge_id / Int
      - hacker_id / Int
      - difficulty_level / Int
    4) SUBMISSIONS
      - submission_id / Int
      - hacker_id / Int
      - challenge_id / Int
      - score / Int
*/

SELECT A.hacker_id, A.name
FROM hackers A RIGHT OUTER JOIN submissions B ON (A.hacker_id = B.hacker_id)
    LEFT OUTER JOIN challenges C ON (B.challenge_id = C.challenge_id)
    LEFT OUTER JOIN difficulty D ON (C.difficulty_level = D.difficulty_level)
WHERE B.score = D.score
GROUP BY A.hacker_id, A.name
HAVING COUNT(A.hacker_id) > 1
ORDER BY COUNT(A.hacker_id) DESC, hacker_id;

