-- 코드를 입력하세요
select year(sales_date) as year, month(sales_date) as month,gender,count(distinct user_id) as users
from ONLINE_SALE left join user_info using(user_id)
where gender is not null
group by year, month, gender
order by year, month, gender