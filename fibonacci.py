# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    if not isinstance(n,int):
        print("Function is only valid of integers");
        return None;
    elif n < 0:
        print("Function not valid for negative values");
        return None;
        
    if n==0:
        return 0;
    if n==1:
        return 1;
    else:
        return (fibonacci(n-1) + fibonacci(n-2));
    

print(fibonacci(-1));