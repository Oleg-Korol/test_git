# Ex.3
# Найти активные (поле discontinued) продукты из категории Condiments и Meat/Poultry, которых в продаже менее 100 единиц
# Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.

SELECT product_name,units_in_stock,s.contact_name,s.phone
fROM products p
inner join categories c on c.category_id = p.category_id
inner join suppliers s on p.supplier_id = s.supplier_id
where category_name='Meat/Poultry' or category_name= 'Condiments' and units_in_stock>100 and discontinued>0
group by product_name, units_in_stock, s.contact_name, s.phone
