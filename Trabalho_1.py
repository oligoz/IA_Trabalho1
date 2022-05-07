import os

def create_map(file):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, file)
    arq = open(filename,'r')
    aux = arq.readlines()
    map = []
    for linha in aux:
        map.append(list(linha[0:-1]))
    return map

def get_points(mapa):
    pontos = []
    for i in range(32):
        pontos.append(0)
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            elem = mapa[i][j]
            if elem == '0':
                pontos[0] = [i,j]
            elif elem == '1':
                pontos[1] = [i,j]
            elif elem == '2':
                pontos[2] = [i,j]
            elif elem == '3':
                pontos[3] = [i,j]
            elif elem == '4':
                pontos[4] = [i,j]
            elif elem == '5':
                pontos[5] = [i,j]
            elif elem == '6':
                pontos[6] = [i,j]
            elif elem == '7':
                pontos[7] = [i,j]
            elif elem == '8':
                pontos[8] = [i,j]
            elif elem == '9':
                pontos[9] = [i,j]
            elif elem == 'B':
                pontos[10] = [i,j]
            elif elem == 'C':
                pontos[11] = [i,j]
            elif elem == 'D':
                pontos[12] = [i,j]
            elif elem == 'E':
                pontos[13] = [i,j]
            elif elem == 'G':
                pontos[14] = [i,j]
            elif elem == 'H':
                pontos[15] = [i,j]
            elif elem == 'I':
                pontos[16] = [i,j]
            elif elem == 'J':
                pontos[17] = [i,j]
            elif elem == 'K':
                pontos[18] = [i,j]
            elif elem == 'L':
                pontos[19] = [i,j]
            elif elem == 'N':
                pontos[20] = [i,j]
            elif elem == 'O':
                pontos[21] = [i,j]
            elif elem == 'P':
                pontos[22] = [i,j]
            elif elem == 'Q':
                pontos[23] = [i,j]
            elif elem == 'S':
                pontos[24] = [i,j]
            elif elem == 'T':
                pontos[25] = [i,j]
            elif elem == 'U':
                pontos[26] = [i,j]
            elif elem == 'V':
                pontos[27] = [i,j]
            elif elem == 'W':
                pontos[28] = [i,j]
            elif elem == 'X':
                pontos[29] = [i,j]
            elif elem == 'Y':
                pontos[30] = [i,j]
            elif elem == 'Z':
                pontos[31] = [i,j]
    return pontos

def get_neighbors(map, point):
    neighbors = []
    if point[0] > 0:
        neighbors.append([point[0]-1,point[1]])
    if point[1] < len(map[0])-1:
        neighbors.append([point[0],point[1]+1])
    if point[0] < len(map)-1:
        neighbors.append([point[0]+1,point[1]])
    if point[1] > 0:
        neighbors.append([point[0],point[1]-1])
    return neighbors

def get_distance(ponto1, ponto2):
    dist = 0
    if ponto1[0] > ponto2[0]:
        dist += ponto1[0] - ponto2[0]
    else:
        dist += ponto2[0] - ponto1[0]
    if ponto1[1] > ponto2[1]:
        dist += ponto1[1] - ponto2[1]
    else:
        dist += ponto2[1] - ponto1[1]
    return dist

def find_path_step(map, points, step):
    start = points[step]
    end = points[step+1]
    margem = [start]
    caminho = [[0 for col in range(len(map[0]))] for row in range(len(map))]
    caminho[start[0]][start[1]] = ['s', 0]
    path = [end]
    while end not in margem:
        min = 100000
        current = [-1,-1]
        next_step = [-1,-1]
        remove = []
        for ponto in margem:
            neighbors = get_neighbors(map, ponto)
            if neighbors == []:
                remove.append(ponto)
            else:
                exist = None
                for vizinho in neighbors:
                    if caminho[vizinho[0]][vizinho[1]] == 0:
                        exist = 1
                        if map[vizinho[0]][vizinho[1]] == '.':
                            value = caminho[ponto[0]][ponto[1]][1] + 1 + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                        elif map[vizinho[0]][vizinho[1]] == 'R':
                            value = caminho[ponto[0]][ponto[1]][1] + 5 + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                        elif map[vizinho[0]][vizinho[1]] == 'F':
                            value = caminho[ponto[0]][ponto[1]][1] + 10 + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                        elif map[vizinho[0]][vizinho[1]] == 'A':
                            value = caminho[ponto[0]][ponto[1]][1] + 15 + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                        elif map[vizinho[0]][vizinho[1]] == 'M':
                            value = caminho[ponto[0]][ponto[1]][1] + 200 + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                        else: #destino
                            value = caminho[ponto[0]][ponto[1]][1] + get_distance(vizinho, end)
                            if value < min:
                                min = value
                                next_step = vizinho
                                current = ponto
                if exist == None:
                    remove.append(ponto)
        for ponto in remove:
            margem.remove(ponto)
        value = min - get_distance(next_step, end)
        margem.append(next_step)
        caminho[next_step[0]][next_step[1]] = [[current[0]-next_step[0],current[1]-next_step[1]],value]
    while start not in path:
        ant = caminho[path[0][0]][path[0][1]][0]
        path.insert(0,[path[0][0]+ant[0],path[0][1]+ant[1]])
    print(path)





map = create_map('mapa.txt')

points = get_points(map)

find_path_step(map,points,0)
