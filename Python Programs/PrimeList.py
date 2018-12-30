check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
check=True
for j in check_prime:

   for i in range(2,j):
       if j%i==0:
           print(j,"is not a prime number")
           print(i,"is a factor of",j)
           break
   else:
       print(j,"is prime number")