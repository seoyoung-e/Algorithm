-- 코드를 작성해주세요

with a as (select EMP_NO, sum(score) as score
from HR_GRADE group by EMP_NO order by score desc limit 1)


select score,h.EMP_NO,	EMP_NAME,	POSITION,	EMAIL
from HR_EMPLOYEES h inner join a on h.EMP_NO=a.EMP_NO