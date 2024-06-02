# в этом файле будут задания

import worker

lessons_list = []

lesson_first = '''
<!-- Привет! Это тестовый html-файл  -->
<h1>Тестовый заголовок</h1>
'''

lessons_list.append(lesson_first)

worker.add_lessons(lessons_list)
