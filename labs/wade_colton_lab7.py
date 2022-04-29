# Colton Wade Lab 7

# Creates Class Product
class Product:

    # Method Constructor
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    # Method to calculate the Discount Amount
    def DiscountAmount(self, price, discountPercent):
        discount_Amount = (discountPercent / 100) * price
        return discount_Amount

    # Method to calculate Discount Price
    def DiscountPrice(self, discountAmount, price):
        discount_Price = price - discountAmount
        return discount_Price

    # Str method to return a formatted string of the object
    def __str__(self, DiscountAmount, DiscountPrice):

        # Sets discountAmount and discountPrice = to the result of the methods, so the return string is not as long
        discountAmount = DiscountAmount(self.price, self.discountPercent)
        discountPrice = DiscountPrice(discountAmount, self.price)

        # Returns formatted string for the products
        # return "PRODUCT DATA \nName: {0} \nPrice: ${1} \n{1} ${2}\nDiscount Percent: {3}% Discount Amount: ${4:.2f} " \
        #        "Discount Price: ${5:.2f}".format(self.price, self.name, self.price, self.discountPercent,
        #                                          discountAmount, discountPrice, self.price)
        return "PRODUCT DATA \n{0}{1} \nName: {2} \nPrice: ${3} \nDiscount Percent: {4}% " \
               "Discount Amount: ${5:.2f} Discount Price: ${6:.2f}".format(self.name, self.price, self.name, self.price,
                                                                 self.discountPercent, discountAmount, discountPrice)


# instantiates and prints product one
P1 = Product("American Professional II Stratocaster®", 1499.99, 5)
print(P1.__str__(P1.DiscountAmount, P1.DiscountPrice))

print("")

# instantiates and prints product two
P2 = Product("Custom Streaming Gaming PC ", 1999.99, 2)
print(P2.__str__(P2.DiscountAmount, P2.DiscountPrice))