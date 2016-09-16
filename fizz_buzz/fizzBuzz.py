

#Created by Carlos Barcenas Sanchez
#Sept 16, 2016

for i in range(1,101):
    x = i/3.0
    y = i/5.0

    isMult3 = float(x).is_integer()
    isMult5 = float(y).is_integer()

    if(isMult3 and isMult5):
        print "Fizz-Buzz"
    elif(isMult3):
        print "Fizz"
    elif(isMult5):
        print "Buzz"
    else:
        print i


