begin

for rec in (select * from emp) loop
	if rec.name like 'A%' then
	dbms_output.put_line(rec.ssn||' '||rec.name||' '||rec.salary);
	end if;
end loop;

update emp
set salary=salary+(salary*0.5)
where ssn=102;

end;
/