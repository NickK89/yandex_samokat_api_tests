```sql
SELECT c.login,
        COUNT(o.id) AS "Count of Orders" 
FROM "Couriers" AS c 
LEFT JOIN "Orders" AS o ON o.id = c.id 
WHERE o."inDelivery" is true 
GROUP BY c.login;
```
