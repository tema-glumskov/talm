# в этом файле прописываются основные функции обучающей платформы - чтение файла, запись файла, а также формирования списка вопросов


def add_lessons(lessons_list):
    global lessons
    global points
    lessons = lessons_list
    points = 0
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
    global points
    for line in file_lines:
        if '<h1>' in line and '</h1>' in line:
            points += 1
            print('Успех!')
            break
        else:
            print('Неуспех :(')
    print(f'Вы набрали {points} баллов из {len(lessons)}')

    

def getlessons():
    lessons_list = []
    lesson_first = '''
<!-- привет! это тестовый html-файл  -->
<h1>тестовый заголовок</h1>
    '''
    lessons_list.append(lesson_first)
    add_lessons(lessons_list)

def start():
    getlessons()