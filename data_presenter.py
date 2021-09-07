# invoice = open("CupcakeInvoices.csv") 
# for row in invoice:
#     print(row)
# invoice.close()

# invoice = open("CupcakeInvoices.csv")
# for row in invoice:
#     row = row.split(",")
#     print(row[2])
# invoice.close()

# invoice = open("CupcakeInvoices.csv")
# for row in invoice:
#     row = row.rstrip("\n").split(",")
#     order_price = int(row[-2])* float(row[-1])
#     print("Invoice:", round(order_price,2))
# invoice.close()

# invoice = open("CupcakeInvoices.csv")
# for row in invoice:
#     row = row.rstrip("\n").split(",")
#     order_price = order_price + (int(row[-2])* float(row[-1]))
# print("Total:", round(order_price,2))
# invoice.close()

labels =["Chocolate", "Strawberry", "Vanilla"]
chocolate = []
strawberry = []
vanilla = []

invoice = open("CupcakeInvoices.csv")
for row in invoice:
    row = row.split(",")
    if row[2] == "Chocolate":
        chocolate.append((int(row[-2])* float(row[-1])))
    elif row[2] == "Strawberry":
        strawberry.append((int(row[-2])* float(row[-1])))
    else:
        vanilla.append((int(row[-2])* float(row[-1])))

total = []
total.append(round(sum(chocolate), 2))
total.append(round(sum(strawberry), 2))
total.append(round(sum(vanilla), 2))

# print(total)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9, 3))
plt.bar(labels, total)
plt.suptitle("Cupcake Sales by Type")
plt.xlabel("Type of Cupcake")
plt.ylabel("Revenue ($)")
plt.show()