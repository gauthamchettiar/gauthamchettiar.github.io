WITH raw_data AS (
    SELECT *
    FROM read_json_auto('products.json')
),
flattened_price AS (
    SELECT product_code, 
        price.*
    from (
            UNPIVOT (
                SELECT product_code,
                    price.*
                FROM raw_data
            ) ON COLUMNS(* EXCLUDE product_code) INTO NAME city VALUE price
        )
),
flattened_approx AS (
    SELECT product_code,
        approx.*
    FROM raw_data
)
SELECT rd.product_code, 
    fp.city, fp.cp, fp.sp,
    fa.min, fa.max, fa.qty
FROM raw_data rd
RIGHT JOIN flattened_price AS fp
ON rd.product_code = fp.product_code 
INNER JOIN flattened_approx AS fa 
ON fp.product_code = fa.product_code;