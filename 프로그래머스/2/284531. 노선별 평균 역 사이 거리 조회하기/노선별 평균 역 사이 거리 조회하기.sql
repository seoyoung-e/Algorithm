-- 코드를 작성해주세요
select route, concat(round(sum(D_BETWEEN_DIST),1),'km') as TOTAL_DISTANCE,
    concat(round(SUM(D_BETWEEN_DIST)/COUNT(*),2),'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE 
group by 1 
order by sum(D_BETWEEN_DIST) desc
                          
                          
      

