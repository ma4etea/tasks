select * from product.users;

insert into product.users(name, email, age, role) values('Patrik', 'patril@mail.ru', 34, 'user');

commit;

delete from product.users as u where u.id = 28;

rollback;

savepoint sp1;

savepoint sp2;

rollback to savepoint sp1;

rollback to savepoint sp2;

start transaction read only;

begin;
insert into product.users(name, email, age, role) values('Patrik', 'patril@mail.ru', 34, 'user');
savepoint sp1;
insert into product.users(name, email, age, role) values('Patrik', 'patril@mail.ru', 34, 'user');
savepoint sp2;
insert into product.users(name, email, age, role) values('Patrik', 'patril@mail.ru', 34, 'user');
release savepoint sp2;
rollback to savepoint sp1;

select * from product.users;

commit;