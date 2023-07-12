-- Old school band
SELECT band_name, IF(split , YEAR(split) - YEAR(formed), 2022 - YEAR(formed)) AS lifespan
WHERE style = 'Glam rock'; 
