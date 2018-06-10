def printTable(table: object) -> object:
    col_widths = [0] * len(table)

    for row_index in range(len(table)):
        for field in table[row_index]:
            if len(field) > col_widths[row_index]:
                col_widths[row_index] = len(field)

    # print formatted table, rotated 90*
    for row_index in range(len(table[0])):
        for col_index in range(len(table)):
            table[col_index][row_index] = table[col_index][row_index].rjust(col_widths[col_index])
            print(table[col_index][row_index], end=' ')
        print()

table = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

printTable(table)
print()
print()

