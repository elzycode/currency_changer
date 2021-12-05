with open('currency_data.txt') as f:
     lines = f.readlines()

currencyDict = {}
for line in lines :
    parse = line.split("\t")
    currencyDict[parse[0]] = parse[1]

print(currencyDict)
amount = int(input("Enter amount:\n"))

print("Enter The Currecy name you want to convert this amount to? Available Options:\n", currencyDict.keys())
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")