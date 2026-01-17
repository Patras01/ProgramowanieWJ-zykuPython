from Lab5.models.product import Product
from Lab5.logic.cart import Cart
p1 = Product("Laptop", 3500, "electronics")
p2 = Product("Monitor", 1200, "electronics")
p3 = Product("Jabłko", 2.5, "food")
print(f"Czy p1 == p2? {p1 == p2}")
produkty = [p1, p2, p3]
produkty.sort()
print(f"Posortowane: {produkty}")
cart = Cart()
cart.add_product(p1)
cart.add_product(p3)
print(f"Liczba produktów: {len(cart)}")
print(f"Czy Laptop w koszyku? {p1 in cart}")
print(f"Łączna cena: {cart.total_price()}")
print("-" * 20)
print(cart)