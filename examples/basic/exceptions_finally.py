import sys
import time

f = None
try:
    f = open('poem.txt')
    # 常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()      # 打印到屏幕上
        print('Press ctrl+c now')
        # 为了确保它能运行一段时间
        time.sleep(2)   # 休眠两秒
except IOError:
    print('Could not find file opem..txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print('(Cleaning up: Closed the file)')
