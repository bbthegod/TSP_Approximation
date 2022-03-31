import sys

def minKey(graphLength, key, mstSet):
    min = sys.maxsize
    for v in range(graphLength):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index

def primMST(matrix):

    graphLength = len(matrix)
    graph = matrix
    adj = []
    adj_list = {}

    # Các giá trị được sử dụng để chọn ra đường đi ngắn nhất
    key = [sys.maxsize] * graphLength

    # Mảng lưu lại các giá trị của cây
    parent = [None] * graphLength

    # Chọn đỉnh đầu tiên là đỉnh bắt đầu
    key[0] = 0
    
    #Mảng đánh dấu các điểm đã đi qua
    mstSet = [False] * graphLength

    parent[0] = -1

    for _ in range(graphLength):

        # Chọn một đỉnh liền kề có quãng đường đi ngắn nhất từ tập hợp các đỉnh chưa được xử lý
        u = minKey(graphLength, key, mstSet)

        # Đánh đỉnh u thành đã đi qua
        mstSet[u] = True

        # Chỉ cập nhật giá trị dist của các đỉnh liền kề của đỉnh đã chọn nếu khoảng cách hiện tại
        # lớn hơn khoảng cách mới và đỉnh không nằm trong cây đường đi ngắn nhất
        for v in range(graphLength):

            # graph[u][v] phải là các quãng đường đi lớn hơn không
            # mstSet[v] phải là các đỉnh chưa được đi qua
            # Cập nhật lại key[v] nếu graph[u][v] nhỏ hơn key[v]
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Tạo ra một danh sách gồm các điểm liền kề của một điểm
    for i in range(1, graphLength):
        adj.append([parent[i], i])
    for i in range(0, graphLength-1):
        u, v = adj[i][0], adj[i][1]

        if u in adj_list:
            if v not in adj_list[u]:
                adj_list[u].append(v)
        else:
            adj_list[u] = [v]

        if v in adj_list:
            if u not in adj_list[v]:
                adj_list[v].append(u)
        else:
            adj_list[v] = [u]

    return adj_list