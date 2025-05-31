#=>Ques:-Write a program to print numbers from n to 1.input = 5, output = 5 4 3 2 1.
def print_n_to_1(n):
  #base case
  if n == 0:
    return

  print(n) #this will print 5 4 3 2 1
  #recursive case
  print_n_to_1(n-1)
  print(n) #this will print 1 2 3 4 5

n = int(input("Enter a no. n: "))
print_n_to_1(n)