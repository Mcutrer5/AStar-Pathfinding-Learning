import colorama


all_nodes = []
for x in range(10):
    for y in range(10):
        all_nodes.append([x, y])
        
def neighbors(node, collisionPoints):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    result = []
    origin = node
    diagonal = []
    
    for dir in dirs:
        # result.append([node[0] + dir[0], node[1] + dir[1]])
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if 0 <= neighbor[0] < 20 and 0 <= neighbor[1] < 10:
            result.append(neighbor)
            # if the neighbor is diagnonal, add to diagonal list
            if dir[0] != 0 and dir[1] != 0:
                diagonal.append(neighbor)
    display = []
    # print all_nodes normally but highlight the neighbors
    for node in all_nodes:
        if collisionPoints in node and node in result:
            display.append(colorama.Fore.YELLOW + str(node) + colorama.Fore.RESET)
            continue
        elif node in result:
            if node not in diagonal:
                display.append(colorama.Fore.GREEN + str(node) + colorama.Fore.RESET)
                continue
            else:
                display.append(colorama.Fore.RED + str(node) + colorama.Fore.RESET)
                continue
        elif node == origin:
            display.append(colorama.Fore.WHITE + str(node) + colorama.Fore.RESET)
            continue
        else:
            display.append(colorama.Fore.BLUE + str(node) + colorama.Fore.RESET)
            continue

    return display

while True:
    node = input("Enter a node seperated by a comma: > ")
    node = node.split(",")
    # collisionPoints = input("Enter a collision point seperated by a comma: > ")
    # collisionPoints = collisionPoints.split(",")
    # collisionPoints = [int(collisionPoints[0]), int(collisionPoints[1])]
    
    collisionPoints = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    
    node = [int(node[0]), int(node[1])]
    print('Neighbors are: \n')
    items = neighbors(node, collisionPoints)
    
    # print items in a grid on x and y axis
    for i in range(0, len(items), 10):
        print(' '.join(items[i:i+10]))
