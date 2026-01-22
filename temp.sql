select user_id
from orders
group by user_id
having sum(amount) > 2000
and count(
    case
        when status = 'paid'
        and created_at > date '2024-06-01' then 1
    end
) > 0
and count(
    case
        when status = 'canceled' then 1
    end
) <= 2

--orders(
--  id,
--  user_id,
--  amount,
--  status,
--  created_at
--)