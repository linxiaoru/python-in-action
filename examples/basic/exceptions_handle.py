try:
    text = input('Enter something --> ')
except EOFError:            # Press ctrl + d 
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:   # Press ctrl + c
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))