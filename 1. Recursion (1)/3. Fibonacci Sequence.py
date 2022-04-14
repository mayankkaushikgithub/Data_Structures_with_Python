# Fibonacci Sequence using Recursion

def fibo_Seq(n):
    a = 0
    b = 1
    for i in range(n):

        if i > n:
            return
        a, b = b, a+b
        print(a, end=" ")

n = int(input("\nEnter the no. upto which you want series to be printed:"))
fibo_Seq(n)



def search_fibo_seq(m):
    if m == 1 or m == 2:
        return 1
    fib_n_1 = search_fibo_seq(m-1)
    fib_n_2 = search_fibo_seq(m-2)
    output = fib_n_1 + fib_n_2
    return output


m = int(input("\nEnter the no. you want to search for:(in series)"))
position = search_fibo_seq(m)
print(position)

