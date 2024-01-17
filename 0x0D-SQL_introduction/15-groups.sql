-- count occuarance of a certain
-- record and tabulate
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score;
