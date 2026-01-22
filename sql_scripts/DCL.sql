create role backender login password 'pass';

alter role backender superuser;

drop role backender;

grant select on product.users to backender;

grant insert on product.users to backender;

revoke insert on product.users from backender;

CREATE USER backender1 WITH PASSWORD 'pass';

CREATE ROLE backender2 LOGIN PASSWORD 'pass' CREATEDB;

