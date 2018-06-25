Ques-1

create database new;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| new                |
| performance_schema |
| pythonspot         |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> use new;
Database changed

mysql> create table Book(Book_ID int(5) primary key, Title_ID int(6), Location varchar(20), Genre varchar(20));
Query OK, 0 rows affected (0.37 sec)

mysql> create table Titles(Title_ID int(5) primary key, Title varchar(20), ISBN int(10), Publisher_ID int(10), Publication_Year varchar(20));
Query OK, 0 rows affected (0.25 sec)

mysql> create table Publishers(Publisher_ID int(5) primary key, Name varchar(20), Street_Address varchar(30), Number int(10), Zip_Code_ID int(10));
Query OK, 0 rows affected (0.29 sec)

mysql> create table Zip_Codes(Zip_Code_ID int(5) primary key, City varchar(20), State varchar(20), Zip_Code int(10));
Query OK, 0 rows affected (0.27 sec)

mysql> create table Authors_Titles(Author_Title_ID int(5) primary key, Author_ID int(20), Title_ID int(10)); Query OK, 0 rows affected (0.27 sec)

mysql> create table Authors(Author_ID int(5) primary key, First_Name varchar(20), Middle_Name varchar(20), Last_Name varchar(20));
Query OK, 0 rows affected (0.31 sec)

Ques-2

mysql> insert into Book(Book_ID, Title_ID, Location, Genre) values('1234', '456', 'Phone', 'Comic');
Query OK, 1 row affected (0.05 sec)

mysql> select * from Book;
+---------+----------+----------+-------+
| Book_ID | Title_ID | Location | Genre |
+---------+----------+----------+-------+
|    1234 |      456 | Phone    | Comic |
+---------+----------+----------+-------+
1 row in set (0.00 sec)

mysql> insert into Titles(Title_ID, Title, ISBN, Publisher_ID, Publication_Year) values('4556', 'Avengers', '2345453', '1222', '1997');
Query OK, 1 row affected (0.04 sec)

mysql> select * from Titles;
+----------+----------+---------+--------------+------------------+
| Title_ID | Title    | ISBN    | Publisher_ID | Publication_Year |
+----------+----------+---------+--------------+------------------+
|     4556 | Avengers | 2345453 |         1222 | 1997             |
+----------+----------+---------+--------------+------------------+
1 row in set (0.00 sec)

mysql> insert into Publishers(Publisher_ID, Name, Street_Address, Number, Zip_Code_ID) values('4236', 'Marvel Comics', 'abcde', '1234', '158765');
Query OK, 1 row affected (0.05 sec)

mysql> select * from Publishers;
+--------------+---------------+----------------+--------+-------------+
| Publisher_ID | Name          | Street_Address | Number | Zip_Code_ID |
+--------------+---------------+----------------+--------+-------------+
|         4236 | Marvel Comics | abcde          |   1234 |      158765 |
+--------------+---------------+----------------+--------+-------------+
1 row in set (0.00 sec)

mysql> insert into Zip_Codes(Zip_Code_ID, City, State, Zip_Code) values('6136', 'Dehradun', 'Uttarakhand', '234456');
Query OK, 1 row affected (0.04 sec)

mysql> select * from Zip_Codes;
+-------------+----------+-------------+----------+
| Zip_Code_ID | City     | State       | Zip_Code |
+-------------+----------+-------------+----------+
|        6136 | Dehradun | Uttarakhand |   234456 |
+-------------+----------+-------------+----------+
1 row in set (0.00 sec)

mysql> insert into Authors_Titles(Author_Title_ID, Author_ID, Title_ID) values('1111', '765', '2234');
Query OK, 1 row affected (0.05 sec)

mysql> select * from Authors_Titles;
+-----------------+-----------+----------+
| Author_Title_ID | Author_ID | Title_ID |
+-----------------+-----------+----------+
|            1111 |       765 |     2234 |
+-----------------+-----------+----------+
1 row in set (0.00 sec)

mysql> insert into Authors(Author_ID, First_Name, Middle_Name, Last_Name) values('15321', 'A', 'B', 'C');
Query OK, 1 row affected (0.05 sec)

mysql> select * from Authors;
+-----------+------------+-------------+-----------+
| Author_ID | First_Name | Middle_Name | Last_Name |
+-----------+------------+-------------+-----------+
|     15321 | A          | B           | C         |
+-----------+------------+-------------+-----------+
1 row in set (0.00 sec)

Ques-3

mysql> describe Book;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| Book_ID  | int(5)      | NO   | PRI | NULL    |       |
| Title_ID | int(6)      | YES  |     | NULL    |       |
| Location | varchar(20) | YES  |     | NULL    |       |
| Genre    | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> alter table Book modify Location varchar(30);
Query OK, 0 rows affected (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe Book;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| Book_ID  | int(5)      | NO   | PRI | NULL    |       |
| Title_ID | int(6)      | YES  |     | NULL    |       |
| Location | varchar(30) | YES  |     | NULL    |       |
| Genre    | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> alter table Book drop Genre;
Query OK, 0 rows affected (0.77 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe Book;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| Book_ID  | int(5)      | NO   | PRI | NULL    |       |
| Title_ID | int(6)      | YES  |     | NULL    |       |
| Location | varchar(30) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)



