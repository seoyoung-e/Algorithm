-- 코드를 작성해주세요
select case 
    when skill_code & (select sum(CODE) from SKILLCODES where CATEGORY like 'Front%')
        and  skill_code & (select CODE from SKILLCODES where NAME = 'PYTHON') then 'A'
    when skill_code & (select CODE from SKILLCODES where NAME = 'C#') then 'B'
    when skill_code & (select sum(CODE) from SKILLCODES where CATEGORY like 'Front%') then 'C'
    end as grade, id,EMAIL
from DEVELOPERS
having grade is not null
order by grade, id;