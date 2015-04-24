# Stage 2

from monster import Monster
class Dragon(Monster):
  size = 1

# __str__ challenges


from game import Game
class GameScore(Game):
  pass

from game import Game
class GameScore(Game):  
  def __str__(self):
    return "Player {}: {}; Player {}: {}".format(1,self.score[0],2,self.score[1])

 def score(self,player):
  if player == 1 :
    self.current_score[0] =  1
  else:
    self.current_score[1] =  1

# Word count

def word_count(inp):
  str_temp = inp.lower() 
  inp_list = str_temp.split()
  my_dict = dict()
  count = int(0)
  for i in inp_list:
      my_dict[inp_list[count]] = str_temp.count(inp_list[count])
      count = count+1
  return my_dict
  
  def word_count(inp):
  str_temp = inp.lower() 
  inp_list = str_temp.split()
  my_dict = dict()
  count = int(0)
  for i in inp_list:     
   my_dict[i] = inp_list.count(i)
  return my_dict
  
      items = list(range(1,20))

# iLilst Items      

def first_4(items):
  return items[:4]
  
def odds(items):
  return items[1::2]  
  
def first_and_last_4(items):
  return items[:4] + items[-4:] 

the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
the_list.insert(0,the_list.pop(3))
the_list.remove('a')
the_list.remove(False)
del the_list[:]  


from character import Character
class Warrior(Character):
  weapon = 'sword'
  
  def rage(self):
    self.attack_limit = 20

 def __str__(self):
    return ""
