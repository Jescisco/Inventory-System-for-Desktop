PRODUCTS_QUERYS={
    "create_product":"INSERT INTO products(name,code,purchase_price,sale_price,existence) VALUES(?,?,?,?,?)",
    "read_product":"SELECT * FROM products WHERE code=?",
    "read_products":"SELECT * FROM products ORDER BY existence ASC",
    "read_update_product":"SELECT * FROM products WHERE id!=? AND code=?",
    "update_product":"UPDATE products SET name=?,code=?,purchase_price=?,sale_price=?,existence=? WHERE id=?",
    "delete_product":"DELETE FROM products WHERE id=?",
    "add_product_existence":"UPDATE products SET existence=? WHERE id=?",
    "substract_product_existence":"UPDATE products SET existence=existence-? WHERE id=?",
    "search_products":"SELECT * FROM products WHERE name LIKE CONCAT('%',?,'%')"
}

SALES_QUERYS={
    "register_sale":"INSERT INTO sales(code,lot,sale_price,date) VALUES (?,?,?,CURRENT_DATE())",
    "verify_product":"SELECT * FROM sales WHERE code=? AND date=CURRENT_DATE()",
    "update_sale":"UPDATE sales SET lot=lot+?,sale_price=sale_price+? WHERE code=? AND date=CURRENT_DATE()"
}

STORE_QUERYS={
    "read_sales":"SELECT s.id,p.name,s.code,s.lot,s.sale_price,s.date FROM products as p INNER JOIN sales as s ON p.code=s.code ORDER BY p.name,s.date ASC",
    "read_sales_of_the_day":"SELECT s.id,p.name,s.code,s.lot,s.sale_price,s.date FROM products as p INNER JOIN sales as s ON p.code=s.code WHERE s.date=? ORDER BY p.name ASC"
}