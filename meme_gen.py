import random

def memegen():
  original = input("Enter input")
  c_list = []
  for c in original:
    c_list.append(c)
  meme_list = []
  for i in c_list:
    choice = random.choice([True, False])
    if choice == True:
      i = str.swapcase(i)
      meme_list.append(i)
    else: 
      meme_list.append(i)
  meme_result = "".join(meme_list)
  print (meme_result)
    
memegen()

