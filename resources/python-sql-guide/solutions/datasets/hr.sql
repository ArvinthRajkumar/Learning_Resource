CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO departments VALUES (1,'Engineering'),(2,'Sales'),(3,'Data'),(4,'HR');
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments(id),
                        manager_id INTEGER REFERENCES employees(id), salary INTEGER NOT NULL, hire_date TEXT NOT NULL);
INSERT INTO employees VALUES
 (1,'Alice',1,NULL,150000,'2018-03-01'),(2,'Bob',1,1,120000,'2019-06-15'),(3,'Carol',1,1,120000,'2020-01-10'),
 (4,'Dan',2,1,90000,'2019-09-01'),(5,'Eve',2,4,95000,'2021-04-12'),(6,'Frank',2,4,85000,'2022-08-30'),
 (7,'Grace',3,1,110000,'2020-11-05'),(8,'Heidi',3,7,105000,'2021-02-20'),(9,'Ivan',3,7,105000,'2023-01-09'),
 (10,'Judy',NULL,1,70000,'2023-05-01');
