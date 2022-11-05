# Найти заказчиков(customer) и обслуживающих их заказы сотрудкников(employees)
# Заказчики и сотрудники из города London, доставка осуществляется компанией Speedy Express.
# Вывести компанию заказчика и ФИО сотрудника.


SELECT c.company_name,last_name,first_name
fROM customers c
inner join employees e on c.city = e.city
inner join orders o on e.employee_id = o.employee_id
inner join shippers s on o.ship_via = s.shipper_id
where c.city='London' and e.city='London' and s.company_name='Speedy Express'
group by c.company_name, last_name, first_name;