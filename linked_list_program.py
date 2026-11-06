# Assessment 3.2 - LINKED LIST (dynamic program)
# Based on Assessment 3.1 algorithm. Last name: CANONIGO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None            # Step 1: head = NULL

    def add_last(self, data):       # Step 2: link new node at the tail
        new_node = Node(data)
        if self.head is None:       # first node becomes head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_first(self):         # Step 3: remove head, move head to head.next
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        return self.head is None

    def display(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return " -> ".join(items + ["None"])


def main():
    name = input("Enter your last name [CANONIGO]: ").strip().upper() or "CANONIGO"
    linked_list = LinkedList()

    print("\n--- ADDING LETTERS ---")
    for letter in name:
        linked_list.add_last(letter)
        print(f"Add {letter}: {linked_list.display()}")

    print("\n--- REMOVING LETTERS ---")
    while not linked_list.is_empty():
        removed = linked_list.remove_first()
        print(f"Remove {removed}: {linked_list.display()}")

    # Step 4: head = NULL -> list is empty. END.
    print("\nThe linked list is empty. END.")


if __name__ == "__main__":
    main()
