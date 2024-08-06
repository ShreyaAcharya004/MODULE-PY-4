from collections import Counter

data = [{'item': 'item1', 'amount': 200}, 
        {'item': 'item2', 'amount': 300}, 
        {'item': 'item1', 'amount': 650}]

result = Counter()

for d in data:
    result[d['item']] += d['amount']

print(result)
