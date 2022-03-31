from DFS import DFS
from Prim import primMST
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt

# Đọc và tạo một ma trận kề từ file
def createMatrixFromFile(filename):
    f = open(filename, "r")
    cities_loc = []
    listOfLocations = []
    for x in f:
        if x[0].isnumeric():
            listOfLocations.append(x)
            location = x.split(' ')
            cities_loc.append([float(location[1]), float(location[2])])
    return distance_matrix(cities_loc, cities_loc), listOfLocations


# Vẽ biển đồ
def printChart(app_tour, listOfLocations):
    routes = []
    for t in app_tour:
        for x in listOfLocations:
            if int(x[0]) == t:
                location = x.split(' ')
                routes.append([float(location[1]), float(location[2])])
    print("The route will go in order:",app_tour)
    plt.plot([i[0] for i in routes], [i[1]
             for i in routes], 'o', linestyle='solid')
    plt.show()


# Main function
matrix, listOfLocations = createMatrixFromFile("data.txt")
adj_list = primMST(matrix)
app_tour = DFS(adj_list)
printChart(app_tour, listOfLocations)
