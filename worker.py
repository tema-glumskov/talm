# в этом файле прописываются основные функции обучающей платформы - чтение файла, запись файла, а также формирования списка вопросов


def add_lessons(lessons_list):
    global lessons
    lessons = lessons_list
    print(lessons) 

def readfile(file):
    global file_data
    global file_lines
    with open(file, 'r', encoding='utf-8') as f:
        file_lines = f.readlines()

def savefile(file):
    pass

def writefile(file):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(lessons[0])

def check():
    for line in file_lines:
        if '<h1>' in line and '</h1>' in line:
            print('Успех!')
            break
        else:
            print('Неуспех :(')

def start():
    pass

lessons_list = []

lesson_first = '''
<!-- привет! это тестовый html-файл  -->
<h1>тестовый заголовок</h1>
'''

lessons_list.append(lesson_first)

add_lessons(lessons_list)
