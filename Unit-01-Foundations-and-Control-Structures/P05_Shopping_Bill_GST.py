# Unit 1 - P05: Shopping bill for three products
# Calculate subtotal, discount, GST and final payable amount
# Rules used: Discount = 10% of subtotal, GST = 18% on the discounted amount

DISCOUNT_RATE = 10
GST_RATE = 18

price1 = float(input("Enter price of product 1: "))
qty1 = int(input("Enter quantity of product 1: "))
price2 = float(input("Enter price of product 2: "))
qty2 = int(input("Enter quantity of product 2: "))
price3 = float(input("Enter price of product 3: "))
qty3 = int(input("Enter quantity of product 3: "))

subtotal = (price1 * qty1) + (price2 * qty2) + (price3 * qty3)
discount = subtotal * DISCOUNT_RATE / 100
after_discount = subtotal - discount
gst = after_discount * GST_RATE / 100
final_amount = after_discount + gst

print("\n----- Final Bill -----")
print(f"Subtotal       : Rs {subtotal:.2f}")
print(f"Discount (10%) : Rs {discount:.2f}")
print(f"GST (18%)      : Rs {gst:.2f}")
print(f"Final Payable  : Rs {final_amount:.2f}")
