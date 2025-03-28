-- 코드를 작성해주세요
select e1.id, genotype, PARENT_GENOTYPE 
from 
(select id, parent_id, genotype from ECOLI_DATA) e1
left join
(select id, genotype as PARENT_GENOTYPE from ECOLI_DATA) e2
on e1.parent_id=e2.id
where (e1.GENOTYPE & e2.PARENT_GENOTYPE) = e2.PARENT_GENOTYPE  #둘이 공통되는 형질을 부모가 모두 보유하고 있음
order by id