declare
	num integer;
	fact integer:=1;
begin
	num:=&number;
	for i in reverse 1..num loop
		dbms_output.put_line('multiplier is : '||i);
		fact:=fact*i;
	end loop;

	dbms_output.put_line('factorial of '||num||' is : '||fact);
end;
/