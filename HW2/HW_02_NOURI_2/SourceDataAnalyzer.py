class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

with open("sales.txt.txt", "r") as f:
    lines = f.readlines()

products = []

for line in lines:
    line = line.strip()
    split = line.split(",")
    product = Product(split[0], float(split[1]), int(split[2]))
    products.append(product)

count_of_transactions = len(products)
total_sold = 0
count_of_prod = 0

for product in products:
    total_sold += product.price * product.quantity
    count_of_prod += product.quantity# مجموع تعداد کالا

best_selling_product = max(products, key=lambda pd: pd.quantity)  # پرفروش‌ترین کالا
average = total_sold / count_of_transactions

print("تعداد تراکنش ها:", count_of_transactions)
print("مجموع فروش: %d دلار" % total_sold)
print("پرفروش ترین کالا: %s (فروش %d عدد)" % (best_selling_product.product_name, best_selling_product.quantity))
print(f"میانگین مبلغ خرید: {average:.2f} دلار")
print("مجموع کل کالاهای فروخته شده:", count_of_prod)
