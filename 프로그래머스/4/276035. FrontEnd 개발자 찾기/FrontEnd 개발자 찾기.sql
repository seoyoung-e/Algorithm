-- 코드를 작성해주세요
select id, email, first_name,last_name from DEVELOPERS 
where skill_code & (select sum(code) from skillcodes where category like 'Front%')
order by 1