def Range(number, start, end):
       return start <= number <= end

number = int(input("Enter a number: "))
start = int(input("\nEnter the start of the range: "))
end = int(input("\nEnter the end of the range: "))

if Range(number, start, end):
    print("\n",number, "is in the range from", start, "to", end)
else:
    print("\n",number, "is not in the range from", start, "to", end)
