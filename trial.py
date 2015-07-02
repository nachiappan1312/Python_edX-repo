
def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]

def SimpleDivide(item, denom):
   return item / denom
FancyDivide([0,2,4], 0)