-- Old school band
SELECT band_name, (IF(split , CAST(YEAR(split) AS INT) - CAST(YEAR(formed) AS INT), 2022 - CAST(YEAR(formed)))) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'; 
