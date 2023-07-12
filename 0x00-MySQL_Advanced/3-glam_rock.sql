-- Old school band
SELECT band_name, (IF(split , CAST(YEAR(split) AS INT) - CAST(YEAR(formed) AS INT), 2022 - CAST(YEAR(formed)))) AS lifespan
WHERE style = 'Glam rock'; 
