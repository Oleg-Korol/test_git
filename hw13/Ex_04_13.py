# Ex.4
# Подсчитать количество товаров в каждой категории, вывести по убыванию.

SELECT category_name ,count(product_name) as all_products
fROM products p
inner join categories c on c.category_id = p.category_id
inner join suppliers s on p.supplier_id = s.supplier_id

group by category_name
order by all_products DESC
