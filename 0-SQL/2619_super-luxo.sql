select products.name, providers.name, products.price from products  
inner join providers on providers.id = products.id_providers
inner join categories on categories.id = products.id_categories
where categories.name like 'Super Luxury' and products.price >= 1000