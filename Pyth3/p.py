def binary_search(lis,number):
  mid_point=len(lis)//2
  if lis[mid_point]==number:
    return True

  else:
    if number<lis[mid_point]:
      return binary_search(lis[:mid_point],number)

    else:
      return binary_search(lis[mid_point:],number)

lis=[84,56,78,43,69,88]
number=78
print(binary_search(lis,number))