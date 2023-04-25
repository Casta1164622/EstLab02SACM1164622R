import jsonReader as jreader
import customerPriority as customerP
import binaryTree as bt

Customers = jreader.readJsonFile('inputs/input_customer_example_lab_3.jsonl')
Auctions = jreader.readJsonFile('inputs/input_auctions_example_lab_3.jsonl')

for i in range(len(Customers)):
    if(i == 0):
        CustomersTree = bt.Node(Customers[i])
    else:
        CustomersTree.insert(Customers[i])

for i in range(len(Auctions)):
    OrderedCustomerList = customerP.orderCustomerPriority(Auctions[i]['customers'])
    AuctionWinner = customerP.getCustomer(OrderedCustomerList,Auctions[i]['rejection'])
    WinnerData = bt.search(CustomersTree,AuctionWinner['dpi'])

