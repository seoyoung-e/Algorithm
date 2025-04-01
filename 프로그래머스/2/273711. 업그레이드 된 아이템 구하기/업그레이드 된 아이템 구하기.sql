-- 코드를 작성해주세요
select a.ITEM_ID,ITEM_NAME,RARITY
from ITEM_INFO a inner join item_tree b on a.item_id=b.item_id
where b.PARENT_ITEM_ID in (select item_id from item_info where RARITY="RARE") #가장 부모만 레어면 됨
order by a.ITEM_ID desc
