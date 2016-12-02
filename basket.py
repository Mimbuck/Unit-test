# Basket is a simple class for a MVP stage shopping application
# You can make a new basket by adding a name, list of products and a price
# You can return the name of the customer, the contents of the basket and the price
# You can add items later as well
# You can count the new price if you have a discount

# TODO: exception handling, user input...

class Basket:
    def __init__(self, customer, contents, price, vat):
        self.customer = customer
        self.contents = contents
        self.price = price
        self.vat = vat
    
    def return_customer(self):
        return self.customer
        
    def return_contents(self):
        return self.contents

    def return_price(self):
        return self.price

    def add_product(self, product, product_price):
        self.contents.append(product)
        self.price += product_price

    def delete_product(self, product, product_price):
        for i in self.contents:
            if i == product:
                self.contents.remove(product)
        self.price -= product_price
                    
    def count_discount_price(self, percent):
        discount = percent / 100.0
        return self.price - self.price * discount

    def calculate_average_price(self):
        return self.price / len(self.contents)

    def calculate_vat(self):
        vat = 0.24
        return self.price - self.price * vat
        
# Making a test object:
jarin_ostoskori = Basket("Jari", ["maito","banaani","hernekeitto"], 15, 0.24)

print(jarin_ostoskori.calculate_average_price())
