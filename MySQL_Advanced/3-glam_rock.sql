-- 3. Old school band
-- List all bands with Glam rock as their main style, ranked by longevity
-- Columns: band_name, lifespan (in years)
-- Use attributes formed and split to compute lifespan. Consider ongoing bands (split NULL or 0) as current year.
-- Query filters style for 'Glam rock', computes lifespan, orders by lifespan desc
SELECT band_name,
       (COALESCE(NULLIF(split, 0), 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
