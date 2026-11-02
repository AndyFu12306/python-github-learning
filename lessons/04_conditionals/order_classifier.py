product_name = input("请输入商品名称：")
price = float(input("请输入单价："))
quantity = int(input("请输入数量："))

order_total = price * quantity

if order_total >= 10000:
    order_level = "大额订单"
elif order_total >= 5000:
    order_level = "中等订单"
else:
    order_level = "普通订单"

print()
print(f"商品：{product_name}")
print(f"单价：{price:.2f} 元")
print(f"数量：{quantity}")
print(f"总金额：{order_total:.2f} 元")
print(f"订单等级：{order_level}")
