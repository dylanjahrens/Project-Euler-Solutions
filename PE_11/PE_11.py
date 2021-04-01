#Find the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid

with open("PE_11_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_grid = [line.strip() for line in file_lines]
    #input_grid is a list of 20 strings with 20 numbers

    grid_list = []

    for strings in input_grid:
        lists = strings.split()
        grid_list.append(lists)
        #grid_list is a list of 20 lists of 20 numbers
    #to see the grid: print(grid_list)

    max_product = 0
    row_index = 0
    assigned_number = 0

    for line in grid_list:
        col_index = 0
        row_index +=1

        for number in line:
            #right, down, diagonal right down, diagonal right up 
            #left, up, diagonal left down and up will repeat

            if col_index < 17:
                right = int(number) * int(line[col_index + 1]) * int(line[col_index + 2]) * int(line[col_index + 3])
                if right > max_product:
                    max_product = right

            if row_index < 17:
                #row_index has already had 1 added to it, will start at 1
                down = int(number) * int(grid_list[row_index][col_index]) * int(grid_list[row_index+1][col_index]) * int(grid_list[row_index+2][col_index])
                if down > max_product:
                    max_product = down

            if col_index < 17 and row_index <17:
                diag_r_d = int(number) * int(grid_list[row_index][col_index+1]) * int(grid_list[row_index+1][col_index+2]) * int(grid_list[row_index+2][col_index+3])
                if diag_r_d > max_product:
                    max_product = diag_r_d

            if col_index < 17 and row_index > 3 :
                diag_r_u = int(number) * int(grid_list[row_index-2][col_index+1]) * int(grid_list[row_index-3][col_index+2]) * int(grid_list[row_index-4][col_index+3])
                if diag_r_u > max_product:
                    max_product = diag_r_u
            
            col_index += 1 

    print(max_product)

