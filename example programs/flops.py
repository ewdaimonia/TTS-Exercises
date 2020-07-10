import random
from datetime import datetime
startTime = datetime.now()

for x in range(100000):
    #print(random.random() * random.random())
    random.random() * random.random()

print(datetime.now() - startTime)
