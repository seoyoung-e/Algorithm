-- 코드를 입력하세요
SELECT REST_ID,	REST_NAME,	FOOD_TYPE,	FAVORITES,	ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO A INNER JOIN REST_REVIEW B USING(REST_ID)
WHERE ADDRESS LIKE '서울%'
GROUP BY REST_ID
ORDER BY SCORE DESC,FAVORITES DESC ;