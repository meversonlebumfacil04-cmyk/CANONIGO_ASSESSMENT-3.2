# Assessment 3.2 - STACK / LIFO (dynamic program)
# Based on Assessment 3.1 algorithm. Last name: CANONIGO

class Stack:
    def __init__(self):
        self.items = []             # Step 1: create an empty stack

    def push(self, item):           # Step 2: PUSH
        self.items.append(item)

    def pop(self):                  # Step 3: POP the top item
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


def main():
    name = input("Enter your last name [CANONIGO]: ").strip().upper() or "CANONIGO"
    stack = Stack()

    print("\n--- PUSH LETTERS ---")
    for letter in name:
        stack.push(letter)
        print(f"Push {letter}: {stack.display()}")

    print("\n--- POP LETTERS ---")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Pop {popped}: {stack.display()}")

    # Step 4: the stack is empty. END.
    print("\nThe stack is empty. END.")


if __name__ == "__main__":
    main()
