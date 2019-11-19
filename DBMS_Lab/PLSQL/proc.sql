DECLARE
	t number;
	fact1 number;

PROCEDURE 	factorial (n in number, fact out number) is
	i number;

	begin
		fact:=1;
		for i in 1..n 
		loop
			fact:=fact*i;
		end loop;
	end;

BEGIN
	t:=&t;
	factorial(t,fact1);
	dbms_output.put_line('Factorial of '||t||' is : '||fact1);
END;
/
