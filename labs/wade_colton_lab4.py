# Colton Wade
# Lab 4

# Main
def main():
    header()
    sales = get_quarterly_sales()
    process_sales(sales)


# Header
def header():
    print("The Quarterly Sales Program\n") # Title of Program


# Get Quarterly Sales
def get_quarterly_sales():
    # Gets input for Q1-4 and stores it in a list called sales
    Q1 = input("Enter Sales for Q1: ")
    Q2 = input("Enter Sales for Q2: ")
    Q3 = input("Enter Sales for Q3: ")
    Q4 = input("Enter Sales for Q4: ")
    sales = [int(Q1), int(Q2), int(Q3), int(Q4)]  # Converts the string input to int to perform calculation
    return sales  # returns sales list


# Process Sales
def process_sales(sales):
    print("")

    # Gets the sum of sales
    Sum = sum(sales)
    print("Total: {0}".format(float(Sum)))

    # Gets the average of sales
    Avg = Sum/len(sales)
    print("Average Quarter: ${0}".format(float(Avg)))

    # Gets the minimum of sales
    low = min(sales)
    print("Lowest Quarter: ${0}".format(float(low)))

    # Gets the max of sales
    high = max(sales)
    print("Highest Quarter: ${0}".format(float(high)))



main()  # Call's Main

