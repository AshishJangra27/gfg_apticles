```markdown
# SQL Joins: Core Concepts

SQL joins combine data from multiple tables using logical relationships. Different join types return different result sets based on matching rows.

## Join Types

*   **INNER JOIN**: Returns rows only when there is a match in *both* tables.
*   **LEFT JOIN**: Returns *all* rows from the *left* table, and matched rows from the *right* table.  `NULL` if no match.
*   **RIGHT JOIN**: Returns *all* rows from the *right* table, and matched rows from the *left* table. `NULL` if no match.
*   **FULL JOIN**: Returns *all* rows when there is a match in *either* table. `NULL` if no match in one table.

## Syntax

```sql
SELECT table1.column1, table1.column2, table2.column1, ...
FROM table1
JOIN_TYPE table2
ON table1.matching_column = table2.matching_column;
```

Where `JOIN_TYPE` is one of `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, or `FULL JOIN`. `JOIN` alone defaults to `INNER JOIN`.  `LEFT OUTER JOIN`, `RIGHT OUTER JOIN` and `FULL OUTER JOIN` are equivalent.

## INNER JOIN Logic

1.  Examine each row combination between the two tables.
2.  If `table1.matching_column = table2.matching_column` is true, include the combined row in the result set.
3.  Otherwise, discard the row combination.

## LEFT JOIN Logic

1.  Start with all rows from the left table (`table1`).
2.  For each row in `table1`, find matching rows in `table2` based on `table1.matching_column = table2.matching_column`.
3.  If a match is found, combine the rows.
4.  If no match is found, combine the row from `table1` with `NULL` values for the columns of `table2`.

## RIGHT JOIN Logic

1.  Start with all rows from the right table (`table2`).
2.  For each row in `table2`, find matching rows in `table1` based on `table1.matching_column = table2.matching_column`.
3.  If a match is found, combine the rows.
4.  If no match is found, combine the row from `table2` with `NULL` values for the columns of `table1`.

## FULL JOIN Logic

1.  Perform a `LEFT JOIN` of `table1` and `table2`.
2.  Perform a `RIGHT JOIN` of `table1` and `table2`.
3.  Combine the results of the `LEFT JOIN` and `RIGHT JOIN`. If a row exists in both results, it only appears once in the final result.

## NATURAL JOIN

Joins tables based on columns with the same name and data type.

*   Tables must have at least one common column with the same name and data type.
*   Uses `CROSS JOIN` internally.
*   Only tuples having the same values in the common columns are included in the result.
```sql
SELECT *
FROM Employee
NATURAL JOIN Department;
```