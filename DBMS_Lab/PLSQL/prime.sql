declare
	n number;
	i number;
	flag number:=1;
begin
	n:=&n;

	for i in 2..n/2 loop
		if mod(n,i)=0 then
			flag:=0;
			exit;
		end if;
	end loop;

	if flag=1 then
		dbms_output.put_line(n||' is prime');
	else
		dbms_output.put_line(n||' is not Prime');
	end if;
end;
/