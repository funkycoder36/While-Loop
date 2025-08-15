num = int(input("Enter a number: "))
rev = 0

temp = num
while temp>0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)

if rev == num:
    print("\nit is a palindrome number")
else:
    print("\nit is not a palindrome number")