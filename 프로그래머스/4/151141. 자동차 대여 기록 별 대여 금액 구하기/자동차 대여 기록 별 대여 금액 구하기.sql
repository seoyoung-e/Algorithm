-- 코드를 입력하세요
with history as (select history_id,h.car_id,c.car_type, daily_fee, DATEDIFF(END_DATE,START_DATE)+1 as day,
case when DATEDIFF(END_DATE,START_DATE)+1 >=90 then '90일 이상'
    when DATEDIFF(END_DATE,START_DATE)+1 >=30 then '30일 이상'
    when DATEDIFF(END_DATE,START_DATE)+1 >=7 then '7일 이상'
    else 'none' end as duration_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
inner join CAR_RENTAL_COMPANY_CAR C ON c.car_id = h.car_id
where c.CAR_TYPE ='트럭') 

SELECT history_id, 
    ROUND(h.daily_fee * h.day * 
          (100 - IFNULL(p.discount_rate,0)) / 100) AS FEE
FROM history h LEFT JOIN car_rental_company_discount_plan AS p 
    ON p.duration_type = h.duration_type AND p.car_type = h.car_type
ORDER BY 2 DESC, 1 DESC