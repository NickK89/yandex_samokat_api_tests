```sql
SELECT 
    track,
    CASE WHEN finished = true THEN 'WHEN cancelled' = true THEN 'ELSE 0 END AS status
FROM 
    "Orders";
```
