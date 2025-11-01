class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


with open("sales.txt.txt", "r") as f:
    lines = f.readlines()

products = []

for line in lines:
    line = line.replace("\n", "")
    split = line.split(",")
    product = Product(split[0], float(split[1]), int(split[2]))
    products.append(product)

count_of_prod = 0
count_of_transactions = len(products)
some_of_sold = 0
most_of_sold = 0
best_selling_product = max(products, key=lambda pd: pd.quantity)

for product in products:
    count_of_prod += product.quantity
    some_of_sold += product.price

print("تعداد ترکنش ها: ", count_of_transactions)
print("مجموع فروش: %d دلار" % count_of_transactions)
print("پرفروش ترین کالا: %s (فروش %d عدد)" % (best_selling_product.product_name, best_selling_product.quantity))
average = some_of_sold / count_of_transactions
print(f"میانگین مبلغ خرید: {average * 100:.2f}% دلار")

