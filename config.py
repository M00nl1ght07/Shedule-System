#=====================================================================
#CONFIG PATHS

root = '/timetable'
PATH = "C:/Users/Home/Desktop/test2" #директория проекта
UPLOAD_FOLDER = '/upload'
OUTPUT_FOLDER = '/output'
STATIC_EX = f'{PATH}/static/example.xlsx'
#=====================================================================

#=====================================================================
#ALLOWED FILES TO UPLOAD
ALLOWED_EXTENSIONS = {'docx', 'xlsx'}
ALLOWED_EXTENSIONS_STR = 'docx, xlsx'
#=====================================================================
#UPLOAD KEY
key = '9df3b01c60df20d13843841ff0d4482c'

#=====================================================================
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#=====================================================================
