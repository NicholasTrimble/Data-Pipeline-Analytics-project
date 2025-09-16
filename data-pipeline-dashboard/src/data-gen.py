from pathlib import Path
import csv, random
from datetime import datetime, timedelta
from faker import Faker

# Where to save files
DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

fake = Faker()  # library that generates fake names, emails, etc.

def generate_users(n=10):
    users = []
    for i in range(1, n+1):
        users.append({
            "user_id": i,
            "email": fake.email(),
            "signup_date": datetime.now().date(),
            "country": fake.country()
        })
    return users

def generate_products(n=5):
    products = []
    for i in range(1, n+1):
        products.append({
            "product_id": i,
            "name": f"Product {i}",
            "category": random.choice(["books", "electronics", "clothing"]),
            "price": round(random.uniform(5, 100), 2)
        })
    return products

def generate_orders(users, products, n=20):
    orders = []
    for i in range(1, n+1):
        user = random.choice(users)
        product = random.choice(products)
        orders.append({
            "order_id": i,
            "user_id": user["user_id"],
            "product_id": product["product_id"],
            "quantity": random.randint(1, 5),
            "price": product["price"],
            "order_datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return orders

def write_csv(filename, rows, fieldnames):
    with open(DATA_DIR / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    users = generate_users(50)
    products = generate_products(10)
    orders = generate_orders(users, products, 100)

    write_csv("users.csv", users, ["user_id", "email", "signup_date", "country"])
    write_csv("products.csv", products, ["product_id", "name", "category", "price"])
    write_csv("orders.csv", orders, ["order_id", "user_id", "product_id", "quantity", "price", "order_datetime"])
