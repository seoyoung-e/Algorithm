-- 코드를 입력하세요
SELECT MCDP_CD as '진료과 코드', count('진료과 코드') as '5월예약건수'
from APPOINTMENT 
where APNT_YMD like '2022-05%'
group by 1 order by 2,1
