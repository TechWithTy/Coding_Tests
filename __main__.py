# Interview Prep https://docs.google.com/document/d/1p5LSSRSmcFat2iMPyX4WNm7kt2oQiO5yXclDyP3-cnc/edit#
# ```
# append():
# extend():
# insert():
# remove():
# pop():
# index():
# count():
# sort():
# reverse():
# ```
from typing import List, Optional, Tuple

#  for loop that will print 0/2/4/6/8
import time 
nums = [0,2,4,6,8]

# Goodbye then exit the application
def test_py (input_nums: List[int]) :
    while(1):
        try:
         for i,num in  enumerate(nums):
                    time.sleep(1)
                    print(num)
        except KeyboardInterrupt:
            print("Goodbye!")
            break

test_py(nums)
        
    
    
    