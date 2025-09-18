import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "sqlite:///data/warehouse.db"

def run_etl():
#this is where I extract the data
    users = pd.read_csv("data/raw/users.csv")
    products = pd.read_csv("data/raw/products.csv")
    orders = pd.read_csv("data/raw/orders.csv")

# this is where I Transform the data
    orders["total_price"] = orders["quantity"] * orders["price"]

# now to load the data

    engine = create_engine(DB_PATH)
    users.to_sql("users", engine, if_exists="replace", index=False)
    products.to_sql("products", engine, if_exists="replace", index=False)
    orders.to_sql("orders", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    run_etl()