-- 코드를 입력하세요
SELECT car_id, round(avg(DATEDIFF(END_DATE,START_DATE)+1),1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY group by car_id having AVERAGE_DURATION>=7
order by average_duration desc, car_id desc