def heapify(arr, n, i):
    smallest = i #Empezamos desde el mas pequeño
    l = 2 * i + 1 # nodo izquierdo
    r = 2 * i + 2 # nodo derecho
 
    # Si el hijo izquierdo es mas pequeño que la raiz
    if l < n and arr[l] < arr[smallest]:
        smallest = l
 
    # Si el hijo derecho es mas pequeño que la raiz y el mas pequeño de los dos
    if r < n and arr[r] < arr[smallest]:
        smallest = r
 
    # Si el mas pequeño no es la raiz
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])
 
        #Heapify a los subarboles recursivazmente
        heapify(arr, n, smallest)
 
# Funcion heapsort (MinHeap de mayor a menor)
def heapSort(arr):
    n = len(arr)
     
    # Construimos el heap
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)
 
    # Extraemos uno a uno los elementos del heap
    for i in range(n-1, -1, -1):
         
        # Movemos la raiz actual al final
        arr[0], arr[i] = arr[i], arr[0]

        # heapidy al heap reducido
        heapify(arr, i, 0)