class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self. types = types
    self.description = description
    self.is_caught = is_caught
  
  def speak(self):
    print(self.name + ' ' + self.name + '!')
  
  def display_details(self):
    print('Entry number: ' + str(self.entry) +'\nName: ' + self.name +'\nType: '+ self.types + '\nDescription: '+ self.description + '\n ')
    if self.is_caught == True:
      print(self.name + ' has already been caught! \n')
    else:
      print(self.name + ' has not yet been caught! \n')

pikachu = Pokemon(25, 'Pikachu', 'Electric', 'It has small electric sacs on both its cheeks. If threatend, it looses electric charges from the sacs.', True)

pikachu.speak()
pikachu.display_details()

squirtle = Pokemon(7, 'Squirtle', 'Water', 'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.', False)

squirtle.speak()
squirtle.display_details()

clefairy = Pokemon(35, 'Clefairy', 'Fairy', 'On nights with a full moon, Clefairy gather from all over and dance. Bathing in moonlight makes them float. ', True)

clefairy.speak()
clefairy.display_details()