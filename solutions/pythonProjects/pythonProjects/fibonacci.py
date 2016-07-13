# start with printing out fibonacci to the Nth number
# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7

n = int(input("Nth fibonacci number to go to: "))

first = 0
second = 1
print("{}".format(second))
for i in range(1,n):
    third = second
    second += first
    first = third
    print("{} ".format(second))

def fib(n):
    series[1]

def main():
    print(fib(int(input("Nth fibonacci number to go to: "))))


if __name__ == '__main__':
    main()