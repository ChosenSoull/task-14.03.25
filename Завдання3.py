def main():
    print("Програма обчислення підсумкових продажів за зміну\n")
    
    hourly_sales = []
    for hour in range(1, 9):
        while True:
            try:
                sales = int(input(f"Введіть кількість проданих одиниць за {hour} годину: "))
                if sales < 0:
                    raise ValueError
                hourly_sales.append(sales)
                break
            except ValueError:
                print("Помилка! Введіть ціле невід'ємне число.\n")
    
    total = sum(hourly_sales)
    
    print("\nГодина | Продажі")
    print("-------------------")
    for idx, sales in enumerate(hourly_sales, 1):
        print(f"{idx:6} | {sales:7}")
    
    print("\nПідсумкові продажі за зміну:", total)

if __name__ == "__main__":
    main()