-- 코드를 작성해주세요
with recursive tmp as (
    #초기값 세팅
    select id, parent_id, 1 as generation
    from ecoli_data where parent_id is null
    
    union all
    #재귀
    select s.id, s.parent_id, tmp.generation + 1
    from tmp join ecoli_data s
    on tmp.id = s.parent_id
)

select count(*) as count, generation
from tmp
where id not in (
    select distinct parent_id
    from tmp where parent_id is not null)
group by 2 order by 2
