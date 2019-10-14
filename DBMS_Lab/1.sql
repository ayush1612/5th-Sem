# CREATING A TABLE NAMED "EMPLOYEE" HAVING THE ATTRIBUTES 'NAME',SALARY,DATE OF JOINING,YEARS OF EXPERIENCE,DEPARTMENT NUMBER

CREATE TABLE EMPLOYEE
(NAME VARCHAR(15),
SALARY NUMBER,
DOJ DATE,
YOE NUMBER,
DEPTNO NUMBER,
PRIMARY KEY(DEPTNO));


SQL> DESCRIBE EMPLOYEE;
 Name					   Null?    Type
 ----------------------------------------- -------- ----------------------------
 NAME						    VARCHAR2(15)
 SALARY 					    NUMBER
 DOJ						    DATE
 YOE						    NUMBER
 DEPTNO 				   NOT NULL NUMBER


# SIMILARLY CREATE A TABLE NAMED PROJECT

CREATE TABLE PROJECT
(PROJECTNO VARCHAR(10),
PROJECTAREA VARCHAR(10),
PRIMARY KEY(PROJECTNO));

# CREATE A TABLE NAMED ASSIGNED_IN WHICH WILL BE REFERENCING TO THE TABLES NAMED EMPLOYEE AND THE TABLE PROJECT

CREATE TABLE ASSIGNED_IN
(DEPTNO NUMBER,
PROJECTNO VARCHAR(2),
FOREIGN KEY(DEPTNO) REFERENCES EMPLOYEE(DEPTNO),
FOREIGN KEY(PROJECTNO) REFERENCES PROJECT(PROJECTNO),
PRIMARY KEY(DEPTNO,PROJECTNO));


SQL> DESCRIBE ASSIGNED_IN;
 Name					   Null?    Type
 ----------------------------------------- -------- ----------------------------
 DEPTNO 				   NOT NULL NUMBER
 PROJECTNO				   NOT NULL VARCHAR2(2)



SQL> DESCRIBE PROJECT;
 Name					   Null?    Type
 ----------------------------------------- -------- ----------------------------
 PROJECTNO				   NOT NULL VARCHAR2(10)
 PROJECTAREA					    VARCHAR2(15)




SQL> INSERT INTO EMPLOYEE VALUES('KANEKI',200000,TO_DATE('1998-12-16','YYYY-MM-DD'),2,2);

1 row created.

SQL> SELECT * FROM EMPLOYEE;

NAME		    SALARY DOJ		    YOE     DEPTNO
--------------- ---------- --------- ---------- ----------
KANEKI		    200000 16-DEC-98	      2 	 2




SQL> INSERT INTO EMPLOYEE VALUES('MIDo',250000,'16-DEC-1998',2,4);

1 row created.

SQL> SELECT * FROM EMPLOYEE;

NAME		    SALARY DOJ		    YOE     DEPTNO
--------------- ---------- --------- ---------- ----------
KANEKI		    200000 16-DEC-98	      2 	 2
MIDORIYA	    250000 16-DEC-99	      2 	 3
MIDo		    250000 16-DEC-98	      2 	 4



