/* write your SQL query below */

SELECT ReportsTo, COUNT(ReportsTo) 'Members', ROUND(AVG(Age)) 'Average Age' FROM maintable_G0KI3 WHERE ReportsTo IS NOT NULL GROUP BY ReportsTo ORDER BY ReportsTo;