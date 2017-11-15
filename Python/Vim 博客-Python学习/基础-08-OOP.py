class Brid(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

class Chicken(Brid):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Brid):
    way_of_move = 'fly'
    possible_in_KFC = False

class heppyBrid(Brid):
    def __init__ (self,more_word):
        print ("we are happy bird.",more_word)

summer = heppyBrid("happy happy")

'''
chicken = Chicken()
oriole = Oriole()

print (chicken.have_feather,chicken.way_of_move)
print (oriole.have_feather,oriole.way_of_move)

print ("after move:",summer.move(2,3))
'''
