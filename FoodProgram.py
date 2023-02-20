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

    order_total = 0

    # cID, name, address, email, phone, mem_status, date, item_name, cost

    for transaction in dict:
        cID = dict[transaction][3]
        if cID == 570:
            cost = dict[transaction][2]
            # order_total += cost
            transaction1 = fc.Transaction(
                "570",
                "Danni Sellyar",
                "97 Mitchell Way Hewitt Texas 76712",
                "dsellyarft@gmpg.org",
                "254-555-9362",
                "False",
                dict[transaction][0],
                dict[transaction][1],
                dict[transaction][2],
            )
            order_total += cost
            print("Customer Name:", transaction1.get_name())
            print("Phone Number:", transaction1.get_phone())
            print(
                f"Order Item:{transaction1.get_item_name()} Price: ${format(transaction1.get_cost(), '.2f')}"
            )
            print(f"Total: ${format(order_total, '.2f')}")

    for transaction in dict:
        cID = dict[transaction][3]
        if cID == 569:
            cost = dict[transaction][2]
            # order_total += cost
            transaction1 = fc.Transaction(
                "569",
                "Aubree Himsworth",
                "1172 Moulton Hill Waco Texas 76710",
                "ahimsworthfs@list-manage.com",
                "254-555-2273",
                "True",
                dict[transaction][0],
                dict[transaction][1],
                dict[transaction][2],
            )
            transaction1.get_mem_status()
            if transaction1.get_mem_status == "True":
                order_total += cost * 0.8
            print("Customer Name:", transaction1.get_name())
            print("Phone Number:", transaction1.get_phone())
            print(
                f"Order Item:{transaction1.get_item_name()} Price: ${format(transaction1.get_cost(), '.2f')}"
            )
            print(f"Total: ${format(order_total, '.2f')}")


main()
