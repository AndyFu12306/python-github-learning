product_name = input("请输入商品名称：")
price = float(input("请输入单价："))
quantity = int(input("请输入数量："))

total = price * quantity

print()
print(f"商品：{product_name}")
print(f"单价：{price:.2f} 元")
print(f"数量：{quantity}")
print(f"总金额：{total:.2f} 元")
