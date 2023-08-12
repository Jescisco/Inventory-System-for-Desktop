PRODUCTS_QUERYS={
    "create_product":"INSERT INTO products(name,code,purchase_price,sale_price,existence) VALUES(?,?,?,?,?)",
    "read_product":"SELECT * FROM products WHERE code=?",
    "read_products":"SELECT * FROM products ORDER BY code DESC",
    "read_update_product":"SELECT * FROM products WHERE id!=? AND code=?",
    "update_product":"UPDATE products SET name=?,code=?,purchase_price=?,sale_price=?,existence=? WHERE id=?",
    "delete_product":"DELETE FROM products WHERE id=?",
    "add_product_existence":"UPDATE products SET existence=? WHERE id=?",
    "search_products":"SELECT * FROM products WHERE name LIKE CONCAT('%',?,'%')"
}