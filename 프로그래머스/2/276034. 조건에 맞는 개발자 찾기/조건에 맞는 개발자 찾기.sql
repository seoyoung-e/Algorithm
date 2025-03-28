-- 코드를 작성해주세요
SELECT ID,EMAIL, FIRST_NAME,LAST_NAME FROM DEVELOPERS 
WHERE SKILL_CODE & (select sum(code) from SKILLCODES
where name in ('Python','C#'))
ORDER BY 1
