# Assessment 3.2 - ARRAY (dynamic program)
# Based on Assessment 3.1 algorithm. Last name: CANONIGO

def main():
    name = input("Enter your last name [CANONIGO]: ").strip().upper() or "CANONIGO"

    # Step 1: START. Create an array of size = number of letters. Set size = 0.
    arr = [None] * len(name)
    size = 0
    print(f"\nArray created with size {len(arr)}")

    # Step 2: store each letter at arr[size], then size = size + 1
    print("\n--- ADDING LETTERS ---")
    for letter in name:
        arr[size] = letter
        size += 1
        print(f"Add {letter}: {arr[:size]}")

    # Step 3: while size > 0, size = size - 1, remove arr[size]
    print("\n--- REMOVING LETTERS ---")
    while size > 0:
        size -= 1
        removed = arr[size]
        arr[size] = None
        print(f"Remove {removed}: {arr[:size]}")

    # Step 4: size = 0 -> array is empty. END.
    print("\nThe array is empty. END.")

if __name__ == "__main__":
    main()
