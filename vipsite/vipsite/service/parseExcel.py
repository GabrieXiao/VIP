__author__ = 'ming'
import xlrd


def read(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheets()[0]
    nrows = sheet.nrows
    for i in xrange(nrows):
        row = sheet.row(1)
        for cell in row:
            print cell.value,
        print ""





if __name__ == "__main__":
    import sys
    read(sys.argv[1])
