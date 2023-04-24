import jsonReader as jreader

Customers = jreader.readJsonFile('inputs/input_customer_example_lab_3.jsonl')
Auctions = jreader.readJsonFile('inputs/input_auctions_example_lab_3.jsonl')
for i in range(len(Customers)):
   print(i)

