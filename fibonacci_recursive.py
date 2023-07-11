#fibonacci series with recursive and stack diagram: fibonacciStackDiagram.png
def fibonacci(n):
    if n <= 0:
        #print("n <= 0, return []")
        return []
    elif n == 1:
        #print("n == 1, return [0]")
        return [0]
    elif n == 2:
        #print("n == 2, return [0, 1]")
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        #print(sequence[-1], "+", sequence[-2], "=", sequence[-1] + sequence[-2])
        sequence.append(sequence[-1] + sequence[-2])
        #print("after appending:", sequence)
        return sequence

# Test the function
n_terms = 6
fib_seq = fibonacci(n_terms)
print("main series:", fib_seq)
