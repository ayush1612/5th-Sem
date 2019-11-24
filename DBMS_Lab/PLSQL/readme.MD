## NOTES during lab :books:

 Commands | Description 
 --- | ---
 DECLARE | to declare variables 
 BEGIN | to begin execution of the following statements 
 PRINT | to print 
 IF ELSE | Condition based execution 
 FOR LOOP | For certain number of iterations of statements 
 <br>
 <br>

# :computer:<br>
<strong>1. DECLARE ---> not necessary but used to declare variable<br>
2. BEGIN   ---> to start execution of some statements</strong>

<hr>

#### Print command


```
	dbms_output.put_line(<string>);
```

<hr>

#### Print command with concatenation using pipeline operator - ||

```
	dbms_output.put_line(<string 1> || <string 2>);
```

## IMPORTANT : Make connection with server for buffer outputs !!!!!!!!!!!

<hr>

```
	SQL> set serveroutput on
```
#### Execute plsql program with @ sign in the sql prompt
	 here plsql is directory


<hr>

```
	SQL> @plsql/first.sql
	Hello, World!

	PL/SQL procedure successfully completed.
```
#### Comments in plsql


<hr>

```
	<< comment >>
```
#### Operator


<hr>

```
	:=  Assignment
	= 	equality
```
#### Mathematical functions


<hr>

```
	mod(num1, num2)
	trunc(<expression>)
```
#### input


<hr>

```
	<var> := &<prompt_string>
```
#### if-else condition


<hr>

```
	if <condition>s then
		<statement>
	else
		<statement>
	end if;
```
#### for loop


<hr>

```
	for i in <first_val_inclusive>..<last_val_inclusive> loop
		<statements>
	end loop;
```
#### for reverse loop


<hr>

```
	for i in reverse <first_val_inclusive>..<last_val_inclusive> loop
		<statements>
	end loop;
```
#### while loop


<hr>

```
	while (<condition>) loop
		<statement>
	end loop;
```
#### procedure


<hr>

```
	PROCEDURE <procedure_name> (<var> in <type> [input args],<var> in <type> [output args]) is
		<DECLARE STATEMENT>

	BEGIN
		<STATEMENT>
	END;
```
#### implicit cursors


<hr>

```
	sql%found
	sql%rowcount
```
#### explicit cursors


<hr>

```
asssigning type from pre-existing attribute
	<var> <table_name>.<key>%type
```


<hr>
