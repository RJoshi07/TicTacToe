#TicTacToe
grid = ["-"]*3
for i in range(3):
    grid[i] = ["-"]*3

for i in range(3):
    for j in range(3):
        print(grid[i][j], end = "")
    print()
    
player = 1
dashCount = 0
game = 0
while True:
    invalid = 1
    print()
    print("Player "+ str(player)+ ", please enter your move (row, col):")
    print()
    row, col = input(). split()
    row = int(row)
    col = int(col)
    row -= 1
    col -= 1
    if row > 2 or row < 0 or col > 2 or col < 0:
        print("Invalid move!")
    elif grid[row][col] != "-":
        print("Invalid move!")
    elif player == 1:
        grid[row][col] = "X"
        invalid = 0
        player = 3 - player
    elif player == 2:
        grid[row][col] = "O"
        invalid = 0
        player = 3 - player
    if invalid == 0:
        for i in range(3):
            for j in range(3):
                print(grid[i][j], end = "")
            print()
    #Check if player won        
    #Vertical
    for i in range(3):
        if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][0] != "-":
            game = 1
            break
    #Horizontal
    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] != "-":
            game = 1
            break
    #Diagonal
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != "-":
        game = 1
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != "-":
        game = 1
    #Check
    if game == 1:
        print()
        print(str(3 - player)+". player won!")
        break
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "-":
                dashCount += 1
    if dashCount == 0:
        print()
        print("Tie!")
        break
    else:
        dashCount = 0
