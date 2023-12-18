from stuff import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard,Enemies
import random
#defining the choose class method to be reusable


#all enemies

#testing

# # # class TestAttack():
# # #     def __init__(self,name,base_damage):
# # #         self.name = name
# # #         self.base_damage = base_damage
# # #     def calculate(self,enemy): 
# # #         return self.base_damage-(self.base_damage-(self.base_damage*enemy.defense))
# # #     def __str__(self):
# # #         return (f'name:{self.name};damage:{self.base_damage}')










<<<<<<< Updated upstream

=======
Player.better_choose_class()
def enemy_attack(player):
    global random_skill
    random_skill=random.choice(attacks)
    player.health = player.health - random_skill.base_damage
>>>>>>> Stashed changes







# def encounter(enemy,player,chosens_skill):
#     while player.health >0:
#         if enemy.health > 0:
#             print(enemy.__dict__)
#             print()
#             print_skills()
#             global chosen_skill
#             chosens_skill = choose_skill()
#             enemy.health = enemy.health - chosens_skill.base_damage
#             print(enemy.__dict__)
#             print()
#             enemy_attack(chosen)
#             player.health = player.health - (0.8*random_skill.base_damage)
#             print(f'{enemy} used {random_skill.name} on you!')
#             print()
#             print(player.__dict__)
#         elif enemy.health <=0:
#             print("youve defeated the enemy,move on")
#             print(f"you have gained {player.money} coins")
#             break
#     if player.health <=0:
#         print("youve died")
# encounter(goblin,chosen,chosen_skill)
