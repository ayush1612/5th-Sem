declare
	vssn emp.ssn%type;
begin
	vssn:=&ssn;
	delete from emp
	where ssn=vssn;
end;
/
