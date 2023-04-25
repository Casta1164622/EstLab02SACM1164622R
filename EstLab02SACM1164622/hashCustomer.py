def hashCustomer(CustomerData):
    hashValue = 1 
    addingFactor = 0
    for information in CustomerData:
        asciiValues = list(str(CustomerData.get(information)).encode('ascii'))
        for value in asciiValues:
                hashValue = hashValue*(value+addingFactor)
                addingFactor += value
    return hex(hashValue+addingFactor)
