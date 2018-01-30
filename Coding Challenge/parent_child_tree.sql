SELECT ID,
(CASE
 WHEN P_ID IS NULL THEN 'ROOT' -- only root node has no parent
 WHEN ID IN (SELECT P_ID FROM TREE) THEN 'INNER' -- inner nodes must be parents of others
 ELSE 'LEAF'
 END)
FROM TREE
ORDER BY ID;
