import yaml #type: ignore


class Enemy:
    
    
    def __init__(self) :
        self._file_path="enpm605_spring2024/Practice/config.yaml"
        self._attack_power=None
        self._skeleton_names=list()
        self.skeleton_health=list()
        self.skeleton_positions=list()
        self.skeleton_shield_power=list()
        
             
        
    
    
    def extract_enemies(self):
        """
        Extract enemy data from the YAML file.
        """

        try:
            with open(self._file_path, "r") as file:
            # try:
                data = yaml.safe_load(file)
                self._attack_power=data["maze"]["enemies"]["attack_power"]
                for skeleton_data in data["maze"]["enemies"]["skeletons"]:
                    self._skeleton_names.append(skeleton_data["skeleton"]["name"])
                    self.skeleton_health.append(skeleton_data["skeleton"]["health"])
                    self.skeleton_positions.append(skeleton_data["skeleton"]["position"])
                    self.skeleton_shield_power.append(skeleton_data["skeleton"]["shield_power"])
        except FileNotFoundError:
            print('file path in enemy class is incorrect', FileNotFoundError)
            # # Retrieve the enemies: dragons
            # for dragon_data in data["maze"]["enemies"]["dragons"]:
            #     position = tuple(dragon_data["dragon"]["position"])
            #     self._dragon_positions.append(position)
            # self._dragon_emoji = data["maze"]["enemies"]["dragon_emoji"]

        #     # Retrieve the enemies: skeletons
        #     for skeleton_data in data["maze"]["enemies"]["skeletons"]:
        #         position = tuple(skeleton_data["skeleton"]["position"])
        #         self._skeleton_positions.append(position)
        #     self._skeleton_emoji = data["maze"]["enemies"]["skeleton_emoji"]
        # # except yaml.YAMLError as e:
        # #     print(f"Error parsing YAML file: {e}")
        # return datax


    @property
    def skeleton_names(self):
        Enemy.extract_enemies(self)
        return self._skeleton_names
    
    @property
    def attack_power(self):
        Enemy.extract_enemies(self)
        return self._attack_power           
class Skeleton(Enemy):
    """
    A class representing a skeleton enemy in the game. All skeletons have a shield power. The health of a skeleton is 50.
    
    Attributes:
        shield_power (int): The power of the skeleton's shield.
    """
    # data=Enemy.extract_enemies
    # print(data["maze"])
    def __init__(self, shield_power=int, name="Skeleton"):
        super().__init__(name=name, health=50, attack_power=5, position=[0,0])
        self._shield_power = shield_power

    def attack(self, player, damage): 
        # had to copy def from Enemy because it was abstraction method (python expects re-definiton)
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🧟🗡️ {self._name} attacks {player.name}!")
        player.take_damage(damage) 
     
        
    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        super().take_damage(damage - self._shield_power)        

# def extract_enemies():
#         """
#         Extract enemy data from the YAML file.
#         """

#         with open("enpm605_spring2024/Practice/config.yaml", "r") as file:
#             try:
#                 data = yaml.safe_load(file)
#                 print(data["maze"]["enemies"]["skeletons"])
#                 skeleton_names=list()
#                 skeleton_health=list()
#                 skeleton_positions=list()
#                 skeleton_shield_power=list()
#                 for skeleton_data in data["maze"]["enemies"]["skeletons"]:
#                     skeleton_names.append(skeleton_data["skeleton"]["name"])
#                     skeleton_health.append(skeleton_data["skeleton"]["health"])
#                     skeleton_positions.append(skeleton_data["skeleton"]["position"])
#                     skeleton_shield_power.append(skeleton_data["skeleton"]["shield_power"])
#                 # Retrieve the enemies: dragons
#                 print(skeleton_names, skeleton_health, skeleton_positions, skeleton_shield_power)
#                 _dragon_positions=list()
#                 for dragon_data in data["maze"]["enemies"]["dragons"]:
#                     position = tuple(dragon_data["dragon"]["position"])
#                     _dragon_positions.append(position)
                
#                 _dragon_emoji = data["maze"]["enemies"]["dragon_emoji"]
#                 print(_dragon_positions)
#                 # Retrieve the enemies: skeletons
#                 # _skeleton_positions=list()
#                 # for skeleton_data in data["maze"]["enemies"]["skeletons"]:
#                 #     position = tuple(skeleton_data["skeleton"]["position"])
#                 #     _skeleton_positions.append(position)
#                 _skeleton_emoji = data["maze"]["enemies"]["skeleton_emoji"]
#             except yaml.YAMLError as e:
#                 print(f"Error parsing YAML file: {e}")

# extract_enemies()

enemy1=Enemy()
print(enemy1.skeleton_names)
print(enemy1.attack_power)
