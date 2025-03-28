-- 코드를 작성해주세요

select id, ifnull(CHILD_COUNT,0) as CHILD_COUNT
from ECOLI_DATA e left join 
(select parent_id, count(*) as CHILD_COUNT
from ECOLI_DATA group by parent_id) c on e.id=c.parent_id
order by 1