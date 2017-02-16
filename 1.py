h = [i for i in range(1,61,1)]
green = sorted(h[::5] + h[1::5] + h[2::5])
from datetime import datetime
if datetime.now().minute in green:
    print('green')
else:
    print('red')
