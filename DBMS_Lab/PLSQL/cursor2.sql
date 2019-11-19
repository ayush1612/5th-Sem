declare
	vssn emp.ssn%type;
begin

	vssn:=&ssn;
	delete from emp
	where ssn=vssn;

	if sql%found then
		dbms_output.put_line('record deleted '||sql%rowcount);
	else
		dbms_output.put_line('record not deleted');
	end if;

	vssn:=&ssn;
	update emp
	set name='Jonas'
	where ssn=vssn;

	if sql%found then
		dbms_output.put_line('record updated '||sql%rowcount);
	else
		dbms_output.put_line('record not updated');
	end if;

	
end;
/
