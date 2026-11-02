def calculate_total(price, quantity):
    return price * quantity


def classify_order(order_total):
    if order_total >= 10000:
        return "大额订单"
    elif order_total >= 5000:
        return "中等订单"
    else:
        return "普通订单"


def print_order_result(product_name, order_total, order_level):
    print(f"药品：{product_name}")
    print(f"订单金额：{order_total:.2f} 元")
    print(f"订单等级：{order_level}")
    print()


def process_order(order):
    product_name = order["product_name"]
    price = order["price"]
    quantity = order["quantity"]

    order_total = calculate_total(price, quantity)
    order_level = classify_order(order_total)

    print_order_result(product_name, order_total, order_level)


orders = [
    {
        "product_name": "阿莫西林",
        "price": 25,
        "quantity": 500,
    },
    {
        "product_name": "头孢克肟",
        "price": 18,
        "quantity": 300,
    },
    {
        "product_name": "布洛芬",
        "price": 12,
        "quantity": 200,
    },
]


def main():
    for order in orders:
        process_order(order)


if __name__ == "__main__":
    main()
