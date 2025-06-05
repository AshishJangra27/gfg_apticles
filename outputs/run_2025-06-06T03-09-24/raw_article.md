# SQL Inner Join

Last Updated :  20 May, 2025

__

Comments

__

Improve

__

  *   *   * 

__ Suggest changes

Like Article

__ Like

__ Report

****SQL INNER JOIN**** is a powerful and frequently used operation in
****relational databases****. It allows us to combine two or more tables based
on a related column, returning only the records that satisfy the join
condition

This article will explore the fundamentals of ****INNER JOIN**** , its syntax,
practical examples, and the key differences between ****INNER JOIN**** and
other types of joins, such as ****OUTER JOIN****.

## What is SQL Inner Join?

The [INNER JOIN](https://www.geeksforgeeks.org/sql-inner-join/) clause in SQL
is used to ****combine records**** from ****two**** or ****more table**** s.
The result contains only the rows that have ****matching values**** in both
tables based on a specific condition. This makes ****INNER JOIN**** a valuable
tool when we need to work with related data across multiple tables in a
database.

The key feature of an ****INNER JOIN**** is that it ****filters out rows****
from the result where there is ****no matching data**** in both tables.
Essentially, it returns a "****subset**** " of the data where the condition is
satisfied.

****Syntax:****

> SELECT columns  
> FROM table1  
> INNER JOIN table2  
> ON table1.column_name = table2.column_name;

****Key Terms****

  * **`**columns**`** : The specific columns we want to retrieve.
  * **`**table1**`******and******`**table2**`** : The two tables we are joining.
  * **`**column_name**`** : The columns from both tables that we want to match based on the join condition.

## Example of SQL INNER JOIN

Consider two tables: **`**professor**`********** and **`**teacher**`**. The
`professor` table contains data about ****professors**** , while the `teacher`
table holds information about the ****courses**** that these professors teach.
The common column between these tables is **`**ID**`** from the `professor`
table and **`**prof_id**`********** from the `teacher` table.

### ****professor table****

ID| Name| Salary  
---|---|---  
1| Rohan| 57000  
2| Aryan| 45000  
3| Arpit| 60000  
4| Harsh| 50000  
5| Tara| 55000  
  
### ****teacher Table****

course_id| prof_id| course_name  
---|---|---  
1| 1| English  
1| 3| Physics  
2| 4| Chemistry  
2| 5| Mathematics  
  
Now, we will write a query to retrieve the **`**course_id**`** ,
**`**prof_id**`** , **`**professor's Name**`** , and their
**`**Salary**`********** by joining the `professor` and `teacher` tables using
****INNER JOIN****. The query joins the `professor` table and the `teacher`
table based on the condition that the **`**ID**`** from the `professor` table
matches the **`**prof_id**`** in the `teacher` table.

****Query****

    
    
     SELECT teacher.course_id, teacher.prof_id, professor.Name, professor.Salary  
    FROM professor INNER JOIN teacher ON professor.ID = teacher.prof_id;

****Output****

course_id| prof_id| Name| Salary  
---|---|---|---  
1| 1| Rohan| 57000  
1| 3| Arpit| 60000  
2| 4| Harsh| 50000  
2| 5| Tara| 55000  
  
****Explanation:****

The output contains the ****details of professors**** and the courses they
teach. The `INNER JOIN` operation ensures that only the records where a
professor is assigned a course are included in the result. The professor who
does not teach a course (like Aryan, who is not listed in the output) is
excluded.

## Difference Between INNER JOIN and OUTER JOIN

### ****INNER JOIN****

  * Returns records that have matching values in both tables.
  * Does not include records where there is no match between the tables.

### ****OUTER JOIN****

  * Returns records even if there is no match in one of the tables.
  * Can be a ****LEFT OUTER JOIN**** , ****RIGHT OUTER JOIN**** , or ****FULL OUTER JOIN**** , depending on whether we want to include unmatched records from the left, right, or both tables.

## ****Key Points About SQL INNER JOIN****

****1\. Combines Data from Multiple Tables: INNER JOIN**** allows us to
combine data from multiple tables based on common columns, making it possible
to work with related data stored in different tables.  

****2\. Excludes Non-Matching Records: INNER JOIN**** only returns records
where there is a match in both tables based on the join condition. If there is
no match, the record will be excluded from the result set.  

****3\. Simplifies Complex Queries: INNER JOIN**** simplifies complex queries
by allowing you to work with multiple tables at once. It reduces the need for
multiple subqueries and makes database management more efficient.  

****4\. Widely Used in Relational Databases: INNER JOIN**** is widely used for
tasks such as managing customer orders, product inventories, and many other
relational datasets. It is essential for performing operations on normalized
data.

## Conclusion

****SQL INNER JOIN**** is an essential tool for combining related data across
multiple tables. By retrieving only the rows where a match is found, it helps
filter relevant information efficiently. Whether we're managing ****employee
data**** , ****courses**** , or ****customer orders**** , mastering the use of
****INNER JOIN**** is key to effective [database
](https://www.geeksforgeeks.org/what-is-database/)querying and management. It
simplifies complex queries and enhances the performance of [SQL
](https://www.geeksforgeeks.org/what-is-sql/)operations by minimizing
unnecessary data retrieval.

  

__ Comment

More info

[Advertise with us](https://www.geeksforgeeks.org/about/contact-us/?listicles)

[ Next Article ](https://www.geeksforgeeks.org/sql-outer-join/)

[SQL Outer Join](https://www.geeksforgeeks.org/sql-outer-join/)

[A __ ](https://www.geeksforgeeks.org/user/akshatsachan/)

[akshatsachan](https://www.geeksforgeeks.org/user/akshatsachan/)

Follow

__

Improve __

Article Tags :

  * [SQL](https://www.geeksforgeeks.org/category/databases/sql/)
  * [Databases](https://www.geeksforgeeks.org/category/databases/)
  * [DBMS-SQL](https://www.geeksforgeeks.org/tag/dbms-sql/)