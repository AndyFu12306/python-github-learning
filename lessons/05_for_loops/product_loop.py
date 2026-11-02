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

for order in orders:
    product_name = order["product_name"]
    price = order["price"]
    quantity = order["quantity"]

    order_total = price * quantity

    if order_total >= 10000:
        order_level = "大额订单"
    elif order_total >= 5000:
        order_level = "中等订单"
    else:
        order_level = "普通订单"

    print(f"商品：{product_name}")
    print(f"总金额：{order_total:.2f} 元")
    print(f"订单等级：{order_level}")
    print()

print("全部订单处理完成")
