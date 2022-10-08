import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    f = '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(t1, f) 
    d2 = datetime.strptime(t2, f) 
    diff = (d2-d1).total_seconds()  
    return str(abs(int(diff)))
