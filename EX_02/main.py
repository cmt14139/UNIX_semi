#fizzbuzz.py

def dict_fizzbuzz(num):
    dict = {n : "" for n in range(1, num + 1)}

    for i in range(1, num + 1):
        if i % 15 == 0:
            dict[i] = "fizzbuzz"
        elif i % 3 == 0:
            dict[i] = "fizz"
        elif i % 5 == 0:
            dict[i] = "buzz"
    
    return dict

print(dict_fizzbuzz(30))