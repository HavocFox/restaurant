class Node():
    def __init__(self, meals, table):
        self.meals = meals
        self.table = table
        self.next = None

class Orders():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, meals, table):
        new_order = Node(meals, table)
        meals = [meals]
        if self.head == None:   # If list is empty, this new order shall be everything
            self.head = new_order
            self.tail = new_order
        else:       # It isn't empty!
            self.tail.next = new_order  # So it finds the tail and sets the next thing after that to be our new thing.
            self.tail = new_order       # But the tail is also the new thing because it's what's last entered.

    def cook_order(self):
        if self.head == None:
            return "Can't cook from empty order list!"
        else:
            removed = self.head
            self.head = self.head.next
            return removed.meals, removed.table
            
    def delete_order(self, table):
        current = self.head
        previous = None
        while current is not None:
            if current.table == table:
                if previous is None:  # Deleting the head of the list
                    self.head = current.next
                    if self.head is None:  # If the list becomes empty, update the tail to None
                        self.tail = None
                else:
                    previous.next = current.next
                    if current.next is None:  # If we're deleting the tail, update the tail to the previous node
                        self.tail = previous
                return current.meals, current.table
            previous = current
            current = current.next
        return "Order not found!"
    
    def view_orders(self):
        current = self.head
        previous = None
        while current is not None:
            print(f"Table: {current.table}\nMeals Ordered: {current.meals}")
            if current.next is not None:  # Is there something to print next?
                previous = current
                current = current.next
            else:
                print("\nThat's all orders.")
                return

    

orders = Orders()
orders.add_order(["Pasta", "Breadsticks"], 1)
orders.add_order("Pizza", 2)
orders.add_order("Salad", 3)
orders.add_order(["Pasta", "More Pasta"], 45)
# Testing seeing all orders
orders.view_orders()
# Now, we cook one
orders.cook_order()
# Testing seeing all orders
orders.view_orders()
# Now, we remove a specific one
orders.delete_order(3)
# See if the deletion worked.
orders.view_orders()



