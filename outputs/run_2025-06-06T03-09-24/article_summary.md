```markdown
# SQL INNER JOIN

## Core Concept

Combines rows from two or more tables based on a related column. Returns only rows with matching values based on a specified condition.

## Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

*   `columns`: Columns to retrieve.
*   `table1`, `table2`: Tables to join.
*   `column_name`: Columns used for matching.

## Example

Consider `professor` and `teacher` tables:

**professor Table:**

| ID | Name  | Salary |
| -- | ----- | ------ |
| 1  | Rohan | 57000  |
| 2  | Aryan | 45000  |
| 3  | Arpit | 60000  |
| 4  | Harsh | 50000  |
| 5  | Tara  | 55000  |

**teacher Table:**

| course\_id | prof\_id | course\_name |
| ---------- | -------- | ------------ |
| 1          | 1        | English      |
| 1          | 3        | Physics      |
| 2          | 4        | Chemistry    |
| 2          | 5        | Mathematics  |

**Query:**

```sql
SELECT teacher.course_id, teacher.prof_id, professor.Name, professor.Salary
FROM professor INNER JOIN teacher ON professor.ID = teacher.prof_id;
```

**Output:**

| course\_id | prof\_id | Name  | Salary |
| ---------- | -------- | ----- | ------ |
| 1          | 1        | Rohan | 57000  |
| 1          | 3        | Arpit | 60000  |
| 2          | 4        | Harsh | 50000  |
| 2          | 5        | Tara  | 55000  |

## INNER JOIN vs. OUTER JOIN

*   **INNER JOIN:** Returns only matching rows from both tables. Excludes non-matching rows.
*   **OUTER JOIN:** Returns records even if there is no match in one of the tables.  Can be LEFT, RIGHT, or FULL OUTER JOIN.
```