declare
	vssn emp.ssn%type;
	vsalary emp.salary%type;
begin
	vssn:=&ssn;
	select salary into vsalary from emp
	where ssn=vssn;
	dbms_output.put_line('record '||vsalary);
end;
/