def bubble_sort(number):
  for i in range(len(number)-1,0,-1):
    for j in range(i):
      if number[j]>number[j+1]:
        number[j],number[j+1]=number[j+1],number[j]

  print(number)
number=[5,4,3,2,1 ]
bubble_sort(number)