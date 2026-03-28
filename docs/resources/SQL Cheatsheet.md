# SQL Cheatsheet

A quick-reference guide to essential SQL keywords and concepts.

*Note:* SQL syntax may vary slightly between databases like MySQL, PostgreSQL, SQL Server, and SQLite.

---

## Data Querying

| Keyword     | Description                                         |
|-------------|-----------------------------------------------------|
| `SELECT`    | Retrieves data from a database.                     |
| `FROM`      | Specifies the table(s) to query data from.          |
| `WHERE`     | Filters rows based on a condition.                  |
| `GROUP BY`  | Groups rows sharing a property (used with aggregates). |
| `HAVING`    | Filters groups after `GROUP BY`.                    |
| `ORDER BY`  | Sorts the results in ascending (`ASC`) or descending (`DESC`) order. |
| `LIMIT`     | Restricts the number of returned rows.              |
| `OFFSET`    | Skips a specified number of rows.                   |
| `DISTINCT`  | Returns only unique values.                         |

---

## Conditions & Operators

| Operator     | Description                                           |
|--------------|-------------------------------------------------------|
| `=`          | Equals                                                |
| `!=`, `<>`   | Not equal                                             |
| `<`, `>`, `<=`, `>=` | Comparison operators                        |
| `BETWEEN`    | Checks if a value is within a range                  |
| `IN`         | Checks if a value exists in a list                   |
| `LIKE`       | Pattern match using `%` (wildcard) and `_` (single char) |
| `IS NULL`    | Checks for null values                               |
| `AND`, `OR`, `NOT` | Logical operators                            |

---

## Joins

| Join Type      | Description                                                      |
|----------------|------------------------------------------------------------------|
| `INNER JOIN`   | Returns only matching rows in both tables.                      |
| `LEFT JOIN`    | All rows from the left table + matches from the right.          |
| `RIGHT JOIN`   | All rows from the right table + matches from the left.          |
| `FULL JOIN`    | All rows when there's a match in either table.                  |
| `ON`           | Defines the join condition.                                      |

---

## Data Aggregation

| Function     | Description                    |
|--------------|--------------------------------|
| `COUNT()`    | Counts rows                    |
| `SUM()`      | Adds values                    |
| `AVG()`      | Calculates average             |
| `MIN()`      | Finds the minimum              |
| `MAX()`      | Finds the maximum              |
| `GROUP BY`   | Groups rows for aggregation    |
| `HAVING`     | Filters aggregated groups      |

---

## Data Manipulation (DML)

| Command        | Description                              |
|----------------|------------------------------------------|
| `INSERT INTO`  | Adds new rows to a table.                |
| `VALUES`       | Specifies values to insert.              |
| `UPDATE`       | Modifies existing data.                  |
| `SET`          | Defines columns and new values for update.|
| `DELETE`       | Removes rows from a table.               |

---

## Data Definition (DDL)

| Command        | Description                              |
|----------------|------------------------------------------|
| `CREATE TABLE` | Defines a new table.                     |
| `DROP TABLE`   | Deletes a table.                         |
| `ALTER TABLE`  | Modifies table structure.                |
| `TRUNCATE`     | Deletes all data but keeps table.        |
| `RENAME`       | Renames a table or column.               |

---

## Control Flow & Logic

| Keyword  | Description                                |
|----------|--------------------------------------------|
| `CASE`   | Conditional logic in queries.              |
| `WHEN`   | Used inside a `CASE` to define conditions. |
| `THEN`   | Returns value if `WHEN` is true.           |
| `ELSE`   | Default value if no `WHEN` condition is met.|
| `END`    | Closes the `CASE` statement.               |

---

## Advanced: Window Functions

| Keyword        | Description                                        |
|----------------|----------------------------------------------------|
| `OVER`         | Applies a window function.                        |
| `PARTITION BY` | Divides result set into partitions.               |
| `ROW_NUMBER()` | Assigns unique row numbers per partition.         |
| `RANK()`       | Ranks rows with gaps for ties.                    |
| `DENSE_RANK()` | Ranks rows without gaps for ties.                 |

---

## Transactions

| Keyword    | Description                             |
|------------|-----------------------------------------|
| `BEGIN`    | Starts a new transaction.               |
| `COMMIT`   | Saves the changes made in the transaction.|
| `ROLLBACK` | Undoes the changes in the transaction.  |
| `SAVEPOINT`| Creates a savepoint in the transaction. |

---

## Common Table Expressions (CTE)

| Keyword | Description                         |
|---------|-------------------------------------|
| `WITH`  | Declares a temporary named result set (like a subquery). |

---

## Set Operations

| Operator      | Description                                            |
|---------------|--------------------------------------------------------|
| `UNION`       | Combines results of two queries (removes duplicates).  |
| `UNION ALL`   | Combines results, includes duplicates.                 |
| `INTERSECT`   | Returns rows common to both queries.                   |
| `EXCEPT`      | Returns rows from the first query not in the second.  |

---

## Extras

| Keyword   | Description                             |
|-----------|-----------------------------------------|
| `AS`      | Renames a column or table using an alias.|
| `EXISTS`  | Checks if a subquery returns any rows.   |
| `ALL`     | Compares a value to all values in a list.|
| `ANY`     | Compares a value to any value in a list. |

---