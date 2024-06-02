# это основной файл комплекса, в котором будет импортировано все остальное

import worker

worker.start()

worker.readfile('index.html')
#worker.check()

worker.writefile('index.html')
worker.check()
