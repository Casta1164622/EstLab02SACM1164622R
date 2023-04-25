import jsonReader as jreader
import heapSort as heap

Customers = jreader.readJsonFile('inputs/input_customer_example_lab_3.jsonl')
Auctions = jreader.readJsonFile('inputs/input_auctions_example_lab_3.jsonl')

arr = [1,42,42,542,5,53,52,245,245,56,631]
heap.heapSort(arr)


for i in range(len(Auctions)):
   print(i)

