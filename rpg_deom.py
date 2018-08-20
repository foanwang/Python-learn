import rpg 

def drwa_fight(role):
    print(role, end='')
    role.fight()

swordman =  rpg.SwordsMan('Justin', 1, 200)
print('SwordsMan', swordman)
drwa_fight(swordman)

magician = rpg.Magician('Minica', 1, 130)
print('Maginian', magician)
drwa_fight(magician)
