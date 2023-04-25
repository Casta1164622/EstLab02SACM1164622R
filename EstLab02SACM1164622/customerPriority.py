import heapSort as heap
def orderCustomerPriority(customerList):

    BudgetList = []
    for i in range(len(customerList)):
        BudgetList.append(customerList[i]['budget'])

    heap.heapSort(customerList)
    return customerList




