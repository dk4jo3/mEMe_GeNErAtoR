import random

def memegen():

  original = input("Enter input : ")
  c_list = []

  for c in original:
    c_list.append(c)

  for i in c_list:
    meme_list = []
    choice = random.choice([True, False])
    if choice == True:
      print (i)
      #i = str.swapcase(i)
      #meme_list.append(i)
    else: 
      pass
      #meme_list.append(i)

  meme_result = "".join(meme_list)
  print (meme_result)
  print (meme_list)


memegen()

