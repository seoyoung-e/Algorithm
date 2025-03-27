-- 코드를 입력하세요
with d as (select AUTHOR_ID, sales, category, price, author_name
from (select * from BOOK_SALES where sales_date like '2022-01%')q 
left join book b using(book_id) left join author a using(author_id))

select AUTHOR_ID, author_name, category,sum(sales*price) as total_sales
from d group by author_id,category order by author_id,category desc