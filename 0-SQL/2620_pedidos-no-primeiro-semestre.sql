select customers.name, orders.id from customers
inner join orders on orders.id_customers = customers.id
where extract(month from orders.orders_date) between 1 and 6