# Ex.2
# Найти заказчиков, у которых нет ни одного заказа. Вывести имя заказчика и order_id.



SELECT c.company_name
fROM customers c
left join orders o on c.customer_id = o.customer_id
where order_id is null
group by c.company_name