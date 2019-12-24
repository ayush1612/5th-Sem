CREATE TABLE EMPLOYEE(
    SSN VARCHAR(20),
    NAME VARCHAR(20),
    DEPTNO NUMBER,
    PRIMARY KEY(SSN)
);

CREATE TABLE PROJECT(
    PROJECTNO NUMBER,
    PROJECTAREA VARCHAR(20),
    PRIMARY KEY(PROJECTNO)
);


CREATE TABLE ASSIGNED_TO(
    USN VARCHAR(20),
    PROJECTNO NUMBER,
    FOREIGN KEY(USN) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE,
    FOREIGN KEY(PROJECTNO) REFERENCES PROJECT(PROJECTNO) ON DELETE CASCADE,
    PRIMARY KEY(USN,PROJECTNO)
);

INSERT INTO EMPLOYEE VALUES ('IS001','KANEKI',1);
INSERT INTO EMPLOYEE VALUES ('IS002','KITRETSU',1);
INSERT INTO EMPLOYEE VALUES ('IS003','TANJIROU',2);
INSERT INTO EMPLOYEE VALUES ('IS004','BAKUGO',2);
INSERT INTO EMPLOYEE VALUES ('IS005','TODOROKI',3);


INSERT INTO PROJECT VALUES(1,'RESEARCH');
INSERT INTO PROJECT VALUES(2,'DATABASE');
INSERT INTO PROJECT VALUES(20,'DATA STRUCTURES');

INSERT INTO ASSIGNED_TO VALUES('IS001',1);
INSERT INTO ASSIGNED_TO VALUES('IS002',20);
INSERT INTO ASSIGNED_TO VALUES('IS002',1);
INSERT INTO ASSIGNED_TO VALUES('IS003',1);
INSERT INTO ASSIGNED_TO VALUES('IS003',2);

SELECT USN FROM ASSIGNED_TO
WHERE PROJECTNO = (
        SELECT PROJECTNO FROM PROJECT
        WHERE PROJECTAREA='DATABASE'
);

SELECT DEPTNO,COUNT(DEPTNO)
FROM EMPLOYEE
GROUP BY(DEPTNO);

UPDATE ASSIGNED_TO SET PROJECTNO = 20 WHERE USN = 'IS001'
