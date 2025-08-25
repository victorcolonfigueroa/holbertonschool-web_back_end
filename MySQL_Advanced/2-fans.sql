-- 2. Best band ever!
-- Rank country origins of bands by total number of (non-unique) fans
-- Column names must be: origin, nb_fans
-- This script can be executed on any database after importing metal_bands.sql
-- Query to aggregate fans by origin and order descending by total fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
