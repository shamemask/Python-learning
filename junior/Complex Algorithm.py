#62895378961010
#
#Примеры алгоритмов с разной сложностью включают:
#1. (линейная сложность) --Linear Complexity
#Линейная сложность алгоритма определяется как число операций, необходимых для выполнения алгоритма, 
#которое растет пропорционально входным данным. Это означает, что при добавлении дополнительных данных 
#время выполнения алгоритма также будет расти. Примеры алгоритмов с линейной сложностью включают поиск 
#по массиву, проход по графу и сортировку вставками.
#поиск по массиву, --Searching through an array
def linear_search(arr, target): 
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
    return -1
	
#проход по графу и --Graph traversal
def graph_traversal(graph, start): 
    visited = set() 
    stack = [start] 
    while stack: 
        vertex = stack.pop() 
        if vertex not in visited: 
            visited.add(vertex) 
            for neighbor in graph[vertex]: 
                stack.append(neighbor) 
    return visited
	
#сортировку вставками --Insertion Sort
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        temp = arr[i] 
        j = i - 1 
        while j >= 0 and temp < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = temp 
    return arr
	
#2. (логарифмическая сложность) --Logarithmic Complexity
#Логарифмическая сложность алгоритма определяется как число операций, необходимых для выполнения алгоритма, 
#которое растет незначительно при увеличении входных данных. Примеры алгоритмов с логарифмической сложностью 
#включают поиск по бинарному дереву поиска, сортировку слиянием и хэширование.
#поиск по бинарному дереву поиска, --Binary Search Tree
def binary_search_tree(arr, target): 
    if arr is None or len(arr) == 0: 
        return -1 
    mid = len(arr) // 2 
    if arr[mid] == target: 
        return mid 
    elif target < arr[mid]: 
        return binary_search_tree(arr[:mid], target) 
    else: 
        return binary_search_tree(arr[mid + 1:], target)
		
#сортировку слиянием и --Merge Sort
def merge_sort(arr): 
    if len(arr) == 1: 
        return arr 
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:]) 
    return merge(left, right) 
	
#хэширование --Hashing
def hashing(arr): 
    hash_table = dict() 
    for item in arr: 
        if item in hash_table: 
            hash_table[item] += 1 
        else: 
            hash_table[item] = 1 
    return hash_table
	
#3. (квадратичная сложность) --Quadratic Complexity
#Квадратичная сложность алгоритма определяется как число операций, необходимых для выполнения алгоритма, которое растет квадратично с увеличением входных данных. Примеры алгоритмов с квадратичной сложностью включают сортировку пузырьком, перебор и метод разделяй и властвуй.
#сортировку пузырьком, --Bubble Sort
def bubble_sort(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr) - i - 1): 
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr 
	
#перебор и --Brute Force
def brute_force(arr, target): 
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
    return -1 
	
#метод разделяй и властвуй --Divide and Conquer
def divide_and_conquer(arr, target): 
    if len(arr) == 0: 
        return -1 
    mid = len(arr) // 2 
    if arr[mid] == target: 
        return mid 
    elif target < arr[mid]: 
        return divide_and_conquer(arr[:mid], target) 
    else: 
        return divide_and_conquer(arr[mid + 1:], target)
		
#4. (кубическая сложность) --Cubic Complexity
#Кубическая сложность алгоритма определяется как число операций, необходимых для выполнения алгоритма, которое растет кубически с увеличением входных данных. Примеры алгоритмов с кубической сложностью включают поиск в ширину, решение квадратичного программирования и трехмерные свертки.
#поиск в ширину, --Breadth-First Search
def breadth_first_search(graph, start): 
    visited = set() 
    queue = [start] 
    while queue: 
        vertex = queue.pop(0) 
        if vertex not in visited: 
            visited.add(vertex) 
            for neighbor in graph[vertex]: 
                queue.append(neighbor) 
    return visited
	
#решение квадратичного программирования и --Quadratic Programming
def quadratic_programming(matrix, target): 
    n = len(matrix) 
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)] 
    dp[0][0] = 0 
    for i in range(1, n + 1): 
        for j in range(1, target + 1): 
            if matrix[i - 1] <= j: 
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - matrix[i - 1]]) 
            else: 
                dp[i][j] = dp[i - 1][j] 
    return dp[n][target]
	
#трехмерные свертки --Three-Dimensional Convolution
def three_dimensional_convolution(matrix, kernel): 
    n = len(matrix) 
    m = len(kernel) 
    convolved = [[[0] * m for _ in range(n)] for __ in range(n)] 
    for i in range(n): 
        for j in range(n): 
            for k in range(m): 
                for l in range(m): 
                    convolved[i][j][k] += matrix[i + k][j + l] * kernel[k][l] 
    return convolved
	
#5. (экспоненциальная сложность) --Exponential Complexity
#Экспоненциальная сложность определяется как число операций, необходимое для выполнения алгоритма, растущее с экспонентой от входных данных, то есть на каждое добавление элемента время выполнения алгоритма увеличивается в экспоненциальное число раз. Примеры алгоритмов с экспоненциальной сложностью включают рекурсивные алгоритмы, такие как перебор и бэктрекинг.
#рекурсивные алгоритмы, --Recursive Algorithms
def recursive_algorithm(arr): 
    if len(arr) == 0: 
        return [] 
    else: 
        return [arr[0]] + recursive_algorithm(arr[1:]) 
		
#перебор --Brute Force
def brute_force(arr): 
    if len(arr) == 0: 
        return [] 
    else: 
        result = [] 
        for i in range(len(arr)): 
            x = arr[i] 
            remaining = arr[:i] + arr[i + 1:] 
            for p in brute_force(remaining): 
                result.append([x] + p) 
        return result

#бэктрекинг --Backtracking 
def backtracking(arr, target): 
    if len(arr) == 0: 
        return [] 
    if arr[0] > target: 
        return backtracking(arr[1:], target) 
    else: 
        without_first = backtracking(arr[1:], target) 
        with_first = backtracking(arr[1:], target - arr[0]) 
        with_first = [[arr[0]] + wf for wf in with_first] 
        return with_first + without_first
        
#6. (факториальная сложность) --Factorial Complexity
#Алгоритмы с факториальной сложностью имеют сложность O (n!), то есть время выполнения алгоритма увеличивается на n факториал при добавлении каждого элемента. Примеры алгоритмов с факториальной сложностью включают перебор и бэктрекинг.
#перебор --Brute Force
def brute_force(arr, target): 
    if len(arr) == 0: 
        return [] 
    else: 
        result = [] 
        for i in range(len(arr)): 
            x = arr[i] 
            remaining = arr[:i] + arr[i + 1:] 
            for p in brute_force(remaining): 
                if sum(p) == target: 
                    result.append([x] + p) 
        return result
        
#бэктрекинг --Backtracking
def backtracking(arr, target): 
    if len(arr) == 0: 
        return [] 
    if arr[0] > target: 
        return backtracking(arr[1:], target) 
    else: 
        without_first = backtracking(arr[1:], target) 
        with_first = backtracking(arr[1:], target - arr[0]) 
        with_first = [[arr[0]] + wf for wf in with_first] 
        return with_first + without_first