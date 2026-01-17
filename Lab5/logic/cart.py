from models.product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        # Operator "in"
        return product in self.products

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."
        lines = [f"- {p}" for p in self.products]
        return "Zawartość koszyka:\n" + "\n".join(lines) + f"\nSuma: {self.total_price()} PLN"