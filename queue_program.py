# Assessment 3.2 - QUEUE / FIFO (dynamic program)
# Based on Assessment 3.1 algorithm. Last name: CANONIGO

class Queue:
    def __init__(self):
        self.items = []             # Step 1: create an empty queue

    def enqueue(self, item):        # Step 2: ENQUEUE at the rear
        self.items.append(item)

    def dequeue(self):              # Step 3: DEQUEUE from the front
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


def main():
    name = input("Enter your last name [CANONIGO]: ").strip().upper() or "CANONIGO"
    queue = Queue()

    print("\n--- ENQUEUE LETTERS ---")
    for letter in name:
        queue.enqueue(letter)
        print(f"Enqueue {letter}: {queue.display()}")

    print("\n--- DEQUEUE LETTERS ---")
    while not queue.is_empty():
        removed = queue.dequeue()
        print(f"Dequeue {removed}: {queue.display()}")

    # Step 4: the queue is empty. END.
    print("\nThe queue is empty. END.")


if __name__ == "__main__":
    main()
