"""
 Customer Class - that has the following attributes
  - customerid, name, address, email, phone, member_status (True or False). 
  The Customer class’s __init__ method should accept an argument for each attribute. 
  The Customer class should have accessor methods only for each attribute. 
"""

class Customer: 
    def __init__(self, cID, name, address, email, phone, mem_status): 
        self.__cID = cID
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__mem_status = mem_status

    def get_cID(self):
        return self.__cID

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone
    
    def get_mem_status(self):
        return self.__mem_status

"""
Transaction Class - that has the following attributes
 - date, item name,cost and customerid. 
 The Procedure class’s __init__ method should accept an argument for each attribute. 
 The Procedure class should have accessor methods only for each attribute.
"""

class Transaction(Customer):
    def __init__(self, cID, name, address, email, phone, mem_status, date, item_name, cost): 
        Customer.__init__(self, cID, name, address, email, phone, mem_status)

        self.__date = date
        self.__item_name = item_name
        self.__cost = cost 

    def get_date(self):
        return self.__date

    def get_item_name(self):
        return self.__item_name

    def get_cost(self):
        return self.__cost

    