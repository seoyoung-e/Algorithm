-- 코드를 입력하세요
select concat('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) as file_path
from USED_GOODS_FILE 
where BOARD_ID= (SELECT BOARD_ID from USED_GOODS_BOARD 
order by views desc limit 1)
order by  FILE_ID desc