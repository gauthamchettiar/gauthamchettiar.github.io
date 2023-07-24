import pandas as pd

df = pd.read_json("products.json")

pd.concat(
    [
        df,
        pd.json_normalize(df["quantity"]),
    ],
    axis=1,
)
flat_json = pd.DataFrame(
    [
        (id, city, price["cp"], price["sp"])
        for id, v in zip(df["product_code"], df["price"].to_list())
        for city, price in v.items()
    ],
    columns=["product_code", "city", "cp", "sp"],
)

df = flat_json.merge(df, on="product_code", how="left")
