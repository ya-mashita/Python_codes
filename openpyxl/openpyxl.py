def getMergedCellValue(sheet, cell):
    cell_index = cell.coordinate
    for range_ in sheet.merged_cells.ranges:
        merged_cells = list(openpyxl.utils.rows_from_range(str(range_)))
        for row in merged_cells:
            if cell_index in row:
                return sheet[merged_cells[0][0]].value
        return sheet[cell_index].value
