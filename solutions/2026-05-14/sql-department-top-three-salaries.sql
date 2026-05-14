-- Department Top Three Salaries (LeetCode 185, Hard)
-- ---------------------------------------------------
-- Source: https://leetcode.com/problems/department-top-three-salaries/
--
-- A company's executives want, per department, every employee whose
-- salary is among the three highest *distinct* salaries in that
-- department. Ties at any rank should *all* be included (e.g. if two
-- people share the top salary, they're both "top earners").
--
-- Schema (LeetCode):
--   Employee(id, name, salary, departmentId)
--   Department(id, name)
--
-- Output columns: Department, Employee, Salary  (any order).
--
-- Approach
-- --------
-- Use DENSE_RANK() partitioned by department, ordered by salary DESC.
-- DENSE_RANK() (not RANK() or ROW_NUMBER()) is the right choice:
--   - ROW_NUMBER would drop tied salaries arbitrarily.
--   - RANK would skip ranks after ties — two #1s would mean no #2.
--   - DENSE_RANK keeps "top three *distinct* salaries", which is what
--     the prompt asks for.
--
-- Filter rk <= 3 and join back to Department for the human-readable name.
--
-- Complexity: O(n log n) due to the window sort within each partition,
-- plus an O(n) hash join to the (small) Department table.
--
-- Hand-checked on:
--   IT: salaries [90, 90, 85, 82, 70] -> dense ranks 1, 1, 2, 3, 4
--       => keep the first four rows.
--   Sales: salaries [60, 30] -> both within top 3, both kept.

WITH ranked AS (
    SELECT
        e.departmentId,
        e.name      AS employee_name,
        e.salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS rk
    FROM Employee AS e
)
SELECT
    d.name          AS Department,
    r.employee_name AS Employee,
    r.salary        AS Salary
FROM ranked AS r
JOIN Department AS d
  ON d.id = r.departmentId
WHERE r.rk <= 3
ORDER BY d.name, r.salary DESC, r.employee_name;

-- Pitfalls / notes
-- ----------------
-- 1. Use DENSE_RANK, not RANK or ROW_NUMBER (see comment above).
-- 2. Don't forget the JOIN to Department — Employee only has departmentId.
-- 3. The trailing ORDER BY is for deterministic test output; LC
--    accepts any order.
