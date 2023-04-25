import jsonReader as jreader
import heapSort as heap
import customerPriority as customerP

Customers = jreader.readJsonFile('inputs/input_customer_example_lab_3.jsonl')
Auctions = jreader.readJsonFile('inputs/input_auctions_example_lab_3.jsonl')

for i in range(len(Auctions)):
    data1 =customerP.orderCustomerPriority(Auctions[i]['customers'])
    print(i)

