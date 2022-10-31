# Ex.2
# Найти заказчиков, у которых нет ни одного заказа. Вывести имя заказчика и order_id.


#У кого нет заказов не нашел, вывел всех у кого нет ship_region


SELECT c.company_name,ship_region
fROM customers c
left join orders o on c.customer_id = o.customer_id
where ship_region is null
group by c.company_name, ship_region