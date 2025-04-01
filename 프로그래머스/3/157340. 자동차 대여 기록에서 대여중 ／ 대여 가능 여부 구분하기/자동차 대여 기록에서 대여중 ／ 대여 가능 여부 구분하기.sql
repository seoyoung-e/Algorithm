-- 코드를 입력하세요
with a as (select distinct car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where '2022-10-16' between START_DATE and END_DATE) #대여중

SELECT h.car_id,
       CASE WHEN a.car_id IS NOT NULL THEN '대여중' 
            ELSE '대여 가능'  END AS AVAILABILITY
FROM (SELECT DISTINCT car_id FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) h
LEFT JOIN a ON h.car_id = a.car_id
ORDER BY 1 DESC;