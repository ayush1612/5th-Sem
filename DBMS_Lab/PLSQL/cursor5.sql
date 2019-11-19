DECLARE
	CURSOR emp_cur is select ssn, name, salary from emp;
	emp_rec emp_cur%rowtype;
BEGIN
	OPEN emp_cur;
	LOOP
		FETCH emp_cur into emp_rec;
		EXIT WHEN emp_cur%notfound;
		DBMS_OUTPUT.put_line(emp_rec.ssn||' '||emp_rec.name);
	END LOOP;
	CLOSE emp_cur;
END;
/