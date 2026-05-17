select *
from clients c;

select id, first_name, last_name, email, status
from clients;


select last_name, *
from employees;

select id, first_name, last_name, email, status
from clients
where email = 'stgen.c07f156f408d.cli5@demobank.local';


select id, first_name, last_name, email, status
from clients
where status = 'ACTIVE';

select id, account_number, type, currency, balance, status
from accounts a
where type = 'CURRENT'
or type = 'SAVINGS';

select id, account_number, type, currency, balance, status
from accounts a
where type = 'CURRENT'
or type = 'SAVINGS'
order by balance asc;

select id, account_number, type, currency, balance, status, a.created_at
from accounts a
order by created_at desc;

select id, account_number, type, currency, balance, status, a.created_at
from accounts a
order by created_at desc
limit 1;


select id, account_number, type, currency, balance, status, a.created_at
from accounts a
order by created_at desc
limit 1 offset 1;

insert employees (first_name, last_name, email)
values ('Daniil', 'Nikolaev', 'asd@sadas.ry');

select *
from employees
where email = 'asd@sadas.ry';

update employees
set first_name = 'Danil'
where email = 'asd@sadas.ry';

delete from employees
where email = 'asd@sadas.ry';

select
	c.id as client_id,
	c.first_name,
	c.last_name,
	c.email,
	a.account_number,
	a.currency,
	a.balance
from clients c
join accounts a
on c.id = a.client_id
where a.balance > 100000
order by c.last_name, c.first_name, a.account_number;

-- from
-- join on
-- where
-- select
-- order by
-- limit