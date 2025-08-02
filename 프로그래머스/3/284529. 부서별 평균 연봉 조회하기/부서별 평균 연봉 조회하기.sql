-- 코드를 작성해주세요
with a as (select DEPT_ID,round(avg(sal)) as AVG_SAL
from HR_EMPLOYEES group by 1 order by 2 desc)

select DEPT_ID,DEPT_NAME_EN,AVG_SAL
from a left join HR_DEPARTMENT using(DEPT_ID)