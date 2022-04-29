
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

        DA = DiscountAmount(self.price, self.discountPercent)
        DP = DiscountPrice(DiscountAmount(self.discountPercent, self.price), self.price)


        # Returns formatted string for the products
        return "{0} \nPrice: ${1} \nDiscount Percent: {2}% \nDiscount Amount: ${3:.2f} " \
               "\nDiscount Price: ${4:.2f}".format(self.name, self.price, self.discountPercent, DA, DP)