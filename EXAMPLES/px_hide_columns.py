#!/usr/bin/env python
import openpyxl as px


def main():
    """program entry point"""
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']

    update_sheet(ws)

    wb.save('presidents6.xlsx')


def update_sheet(ws):
    """Misc updates to styles and formats"""

    # hide inauguration columns
    ws.column_dimensions.group(start='H', end='I', hidden=True)


if __name__ == '__main__':
    main()
