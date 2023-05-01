from docx import Document
import os
import config


def get_names_list(doc_name: str):
    print('HEEEEEEELLLLOOO')
    print(doc_name)
    file_name = doc_name.split('.')[:-1]
    file_name = "".join(file_name)
    print("!FDFDFDF!", file_name)

    print(f'{file_name}.txt')
    if os.path.isfile(f'{file_name}.txt'):
        f = open(f'{file_name}.txt', "r", encoding="utf8") # Правка! (не обращать внимание, все исправлено!)
        res = f.read()
        print(res)
        f.close()
        return res.split('\n')

    else:
        print('no file')
        doc = Document(doc_name)
        tables = doc.tables
    
        teachers_names = set()
    
        for table in tables:
            for row in table.rows:
                string = [element.text for element in row.cells]
                name_1 = list(string[3])
                name_2 = list(string[5])
                
                if name_1 != []:
                    if '-' not in name_1 and name_1[-3] == '.':
                        teachers_names.add(rename(string[3]))
                if name_2 != []:
                    if '-' not in name_2 and name_2[-3] == '.':
                        teachers_names.add(rename(string[5]))
        print(list(teachers_names))
        res = []
        for val in list(teachers_names):
            if val != None :
                res.append(val)

        res = sorted(res)
        res = "\n".join(res)
        print(res)
        f = open(f'{file_name}.txt', "w")
        f.write(res)
        f.close()

        return res.split('\n')
        
def rename(string: str):
    if string[-1] == '.' and string[-3] == '.':
        return string
    elif string[-1] == ',' and string[-3] == '.':
        string = list(string)
        string[-1] = '.'
        return ''.join([s for s in string])