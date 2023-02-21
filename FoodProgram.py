import FoodClass as fc


# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
def main():
    dict = {
        "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
        "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
        "trans3": ["2/15/2023", "The Octoveg", 16, 570],
        "trans4": ["2/15/2023", "The Octoburger", 20, 570],
    }

    """
    customer1 = fc.Customer(
        570,
        "Danni Sellyar",
        "97 Mitchell Way Hewitt Texas 76712",
        "dsellyarft@gmpg.org",
        "254-555-9362",
        "False",
    )
    """

    customer1 = fc.Customer(
        569,
        "Aubree Himsworth",
        "1172 Moulton Hill Waco Texas 76710",
        "ahimsworthfs@list-manage.com",
        "254-555-2273",
        "True",
    )

    order_total = 0

    customer_transaction = []

    for transaction in dict:
        cID = dict[transaction][3]
        if cID == customer1.get_cID():
            customer_transaction.append(
                fc.Transaction(
                    dict[transaction][0],
                    dict[transaction][1],
                    dict[transaction][2],
                    dict[transaction][3],
                )
            )

    print("Customer Name:", customer1.get_name())
    print("Phone Number:", customer1.get_phone())

    for transaction in customer_transaction:
        cost = transaction.get_cost()
        print(
            f"Order Item: {transaction.get_item_name()} Price: ${format(cost, '.2f')}"
        )

        order_total += cost

    print(f"Total: ${format(order_total, '.2f')}")

    if customer1.get_mem_status() == "True":
        discount = order_total * 0.2
        order_total -= discount
        print(f"Member Discount: ${format(discount, '.2f')}")

    print(f"Total after Discount: ${format(order_total, '.2f')}")


main()
