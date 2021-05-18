def binary_search(list, item):
    print()
    low = 0
    high = len(list) - 1
    count = 0

    while low <= high:
        count += 1
        print()
        print(f'guess {count}')
        mid = int((low + high) / 2)
        guess = list[mid]
        print(f'mid: {mid}, guess: {guess}')
        if guess == item:
            print(f'correct answer {guess}')
            return guess
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print(f'number {item} not found in list')
    return None

mylist = [1, 3, 5, 7, 9]

binary_search(mylist, 5)
binary_search(mylist, 3)
binary_search(mylist, 9)
binary_search(mylist, -1)
