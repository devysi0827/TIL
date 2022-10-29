# Programmers : 조건에 맞는 회원 수 구하기

```sql
SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE GROUP BY USER_ID,PRODUCT_ID HAVING COUNT(*) >=2 ORDER BY USER_ID, PRODUCT_ID DESC
```

GROUP BY 로 그루핑을 하고 그 수가 2 이상인 경우를 찾으면 된다.