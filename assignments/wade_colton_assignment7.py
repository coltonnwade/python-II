import module


def main():

    ListOfProducts = []

    while True:
        module.name = input("Enter product name: ")
        module.price = input("Enter product price: ")
        module.discountPercent = input("Enter discount percentage: ")
        choice = input("Enter another product(y/n): ")

        Item = module.Product(module.name, float(module.price), float(module.discountPercent))
        ListOfProducts.append(Item)

        if choice == "y":
            print("")
            continue
        else:
            break

    print("\nPRODUCTS: ")
    print("====================")
    for items in ListOfProducts:
        print(items.__str__(items.DiscountAmount, items.DiscountPrice))
        print("")


main()



