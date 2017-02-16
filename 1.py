h = [i for i in range(1,61,1)]
green = sorted(h[::6] + h[1::6] + h[2::6])
from datetime import datetime
if datetime.now().minute in green:
    print('green')
else:
    print('red')
