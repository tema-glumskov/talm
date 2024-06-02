# в этом файле будут задания

import worker

lessons_list = []

lesson_first = '''
<!-- привет! это тестовый html-файл  -->
<h1>тестовый заголовок</h1>
'''

lessons_list.append(lesson_first)

worker.add_lessons(lessons_list)