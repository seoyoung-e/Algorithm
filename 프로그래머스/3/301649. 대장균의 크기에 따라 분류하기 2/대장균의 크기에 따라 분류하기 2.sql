-- 코드를 작성해주세요

WITH ranked AS (
    SELECT ID, SIZE_OF_COLONY,
           NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS q FROM ECOLI_DATA)

select ID,
case q WHEN 1 THEN 'CRITICAL'
           WHEN 2 THEN 'HIGH'
           WHEN 3 THEN 'MEDIUM'
           WHEN 4 THEN 'LOW'
       END AS COLONY_NAME
from ranked order by 1