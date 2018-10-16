time=int(input('what time is it'))
long=int(input('how long do you want your alarm to be for?'))
longmodulo=long%24
alarm=time+longmodulo
alarm=alarm%24
print('I willset off at',str(alarm)+', Doctor luigi')