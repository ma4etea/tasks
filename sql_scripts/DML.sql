select * from product.users;

insert into product.users(name, email, age) 
values('Bob', 'bob@email.com', 25)
returning *;

delete from product.users as u where u.id = 6;

update product.users as u set age = 31 where u.id = 5
returning *;

with tmp (id, name, email, age) as (
	select 4, 'Mike', 'mike@mike.com', 37
)
merge into product.users as u using tmp as t on t.id = u.id
when matched then
	update set
		name = t.name,
		email = t.email,
		age = t.age
when not matched then
	insert (id, name, email, age)
	values (t.id, t.name, t.email, t.age);