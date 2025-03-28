-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME, 
CASE
        when SEX_UPON_INTAKE LIKE 'Neutered%' then 'O'
        when SEX_UPON_INTAKE LIKE 'Spayed%' then 'O'
        ELSE 'X'
        END AS 중성화
from ANIMAL_INS ;