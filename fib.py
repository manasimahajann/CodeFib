 
  
def Fibonacci(n):  
    if n<=1: 
        return n 
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
   
def main():
    number = int(input("Enter a positive integer: ")) 
    try: 
        fibSeq =[]
        if(isinstance(number, int) and number >= 0):
            for i in range(number): 
                fibSeq.append(Fibonacci(i)) 
            print("Fibonacci sequence: " + str(tuple(fibSeq)))
        else:
            print("Enter a valid input")
    except ValueError:
        print("Please enter positive integer value.")
    except Exception as e:
        print(e)
 
if __name__ == "__main__":
    main()
  
