def land_the_tiles(rowIndex, columnIndex, map):
    if map[rowIndex][columnIndex] == 0:
        return False
    map[rowIndex][columnIndex] = 0

    if columnIndex - 1 >= 0:    # can go left
        land_the_tiles(rowIndex, columnIndex - 1, map)
    if columnIndex + 1 < len(map[rowIndex]):    # can go right
        land_the_tiles(rowIndex, columnIndex + 1, map)
    if rowIndex - 1 > 0:    # can go up
        land_the_tiles(rowIndex - 1, columnIndex, map)
    if rowIndex + 1 < len(map):    # can go down
        land_the_tiles(rowIndex + 1, columnIndex, map)

    return True

def count_number_of_islands(map):   # 1 will stand for land, 0 for water
    nOfIslands = 0
    for rowIndex in range(len(map)):
        for columnIndex in range(len(map[rowIndex])):
            if land_the_tiles(rowIndex, columnIndex, map):
                nOfIslands += 1
    
    return nOfIslands
