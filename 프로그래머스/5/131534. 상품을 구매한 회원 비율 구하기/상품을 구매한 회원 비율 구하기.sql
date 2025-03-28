#select count(*) from user_info where year(joined)=2021

with a as (SELECT DISTINCT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH, U.USER_ID
    FROM ONLINE_SALE S JOIN USER_INFO U ON S.USER_ID = U.USER_ID AND YEAR(JOINED) = 2021),
    b as (select count(*) from user_info where year(joined)=2021)

select year,month,count(*) as PURCHASED_USERS, round(count(*)/(select * from b),1) as PUCHASED_RATIO
from a
GROUP BY 1,2 ORDER BY 1,2