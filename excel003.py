import xlrd
class dkw001:
    file = "/users/kevintuan/downloads/BIOGRID-ALL-3.5.174.tab2.xlsx"
    def read1(self):#dict
        dkw = xlrd.open_workbook(filename = dkw001.file)
        sheet1 = dkw.sheet_by_name('BIOGRID-ALL-3.5.174.tab2')  # 通过名字获取表格
        dict = {}
        for i in range(1, 50):
            for j in range(24):  # excel一共24列
                ctype = sheet1.cell(i, j).ctype  # 表格的数据类型
                cell = sheet1.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                title = sheet1.cell_value(0, j)
                value = cell
                dict[title] = value
            print(dict)

    def read2(self):#print
        dkw = xlrd.open_workbook(filename=dkw001.file)
        sheet1 = dkw.sheet_by_name('BIOGRID-ALL-3.5.174.tab2')  # 通过名字获取表格
        for i in range(50):
            rows = sheet1.row_values(i)  # 获取行内容
            print(rows)

    def read3(self):
        dkw = xlrd.open_workbook(filename=dkw001.file)
        sheet1 = dkw.sheet_by_name('BIOGRID-ALL-3.5.174.tab2')  # 通过名字获取表格
        for i in range(1, 50):
            for j in range(24):  # excel一共24列
                ctype = sheet1.cell(i, j).ctype  # 表格的数据类型
                cell = sheet1.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)

                print(cell,end=' ')
            print('\n')
excel = dkw001()
excel.read1()
excel.read2()
excel.read3()