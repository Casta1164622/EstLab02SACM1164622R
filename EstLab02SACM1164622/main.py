import jsonReader as jreader
import customerPriority as customerP

Customers = jreader.readJsonFile('inputs/input_customer_example_lab_3.jsonl')
Auctions = jreader.readJsonFile('inputs/input_auctions_example_lab_3.jsonl')

for i in range(len(Auctions)):
    OrderedCustomerList = customerP.orderCustomerPriority(Auctions[i]['customers'])
    AuctionWinner = customerP.getCustomer(OrderedCustomerList,Auctions[i]['rejection'])
    print(i)

