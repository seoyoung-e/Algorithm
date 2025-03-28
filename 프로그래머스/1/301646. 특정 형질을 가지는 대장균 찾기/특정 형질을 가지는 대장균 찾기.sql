-- 코드를 작성해주세요

select count(*) as count
from ECOLI_DATA 
where (not GENOTYPE&2) and (GENOTYPE & 4 or  GENOTYPE & 1 )