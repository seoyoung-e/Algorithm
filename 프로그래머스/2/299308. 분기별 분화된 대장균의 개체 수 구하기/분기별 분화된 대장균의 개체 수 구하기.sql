-- 코드를 작성해주세요
select concat(quarter(DIFFERENTIATION_DATE),'Q') as quarter, count(id) as ECOLI_COUNT
from ECOLI_DATA 
group by 1
order by 1