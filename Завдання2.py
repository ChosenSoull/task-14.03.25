import random

a = [random.randint(1, 100) for _ in range(10)]
sum_even = sum(x for x in a if x % 2 == 0)

print(f"Список: {a}")
print(f"Парні елементи: {[x for x in a if x % 2 == 0]}")
print(f"Сума парних елементів: {sum_even}")
