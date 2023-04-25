import heapSort as heap
def orderCustomerPriority(customerList):
    heap.heapSort(customerList)
    return customerList

def getCustomer(priorityList,rejections):
    return priorityList[rejections]



