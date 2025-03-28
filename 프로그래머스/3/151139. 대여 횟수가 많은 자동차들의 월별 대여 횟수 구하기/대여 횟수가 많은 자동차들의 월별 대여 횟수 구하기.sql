-- 코드를 입력하세요
with id as (select CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE between '2022-08-01' and '2022-10-31' 
group by car_id having count(history_id)>=5)

SELECT month(START_DATE) as month,car_id , count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where car_id in (select * from id) and START_DATE between '2022-08-01' and '2022-10-31' 
group by month,CAR_ID
having records>0 order by 1,2 desc