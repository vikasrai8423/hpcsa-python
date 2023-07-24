class Team:
    league_name  = ''

    @classmethod
    def get_team_name(cls):
        return cls.team_name
	
    @classmethod
    def set_team_name(cls,team_name):
        cls.team_name = team_name

    def __init__(self,name,owner,captain,sponsers,support_staff,players):	
        self.name = name
        self.owner = owner
        self.captain = captain
        self.sponsers = sponsers
        self.support_staff = support_staff
        self.players = players
	
    def get_team(self):
        v =  f'{self.name},{self.owner},{self.captain},{self.sponsers},{self.support_staff},'
        
        for i in self.players:
            v += i.get_player_details() + ','
        return v 

class Player:
	def __init__(self,name,base_price,actual_price,role,nationality,dob,misc_stats):
		self.name         = name
		self.base_price   = base_price
		self.actual_price = actual_price
		self.role         = role
		self.nationality  = nationality
		self.dob          = dob
		self.misc_stats   = misc_stats
		
	def get_player_details(self):
		return f'{self.name},{self.base_price},{self.actual_price},{self.role},{self.nationality},{self.dob},{self.misc_stats}'

    
class Venue:
  def __init__(self,name,location,capacity):
    self.name     =  name    
    self.location =  location
    self.capacity =  capacity
	
    def get_venue(self):
        return f'{self.name},{self.location},{self.capacity}'
		
class Fixture:
	def  __init__(self,name1,owner1,captain1,sponsers1,support_staff1,players1,
					   name2,owner2,captain2,sponsers2,support_staff2,players2,
					   name,location,capacity,winner_team):
		self.team1 = Team.set_team(name1,owner1,captain1,sponsers1,support_staff1,players1)
		self.team2 =Team.set_team(name2,owner2,captain2,sponsers2,support_staff2,players2)
		self.venue =Venue.__init__(name,location,capacity),
		self.winner_team = winner_team
					   
	
	
	def set_a_fixture(self, team1, team2,venue):
		self.team1 = team1
		self.team2 = team2
		self.venue = venue
		
	def get_a_fixture(self):
		return f'{self.team1},{self.team2},{self.venue}'
		
	def set_outcome(self,winner_team):
		self.winner_team = winner_team
  
  
class Football_team(Team):
   
    def __init__(self, name, owner, captain, sponsers, support_staff, players, substitute_pool):
            super().__init__(name, owner, captain, sponsers, support_staff, players)
            self.substitute_pool = substitute_pool
            
    def get_team(self):
            v=  super().get_team() 
            for i in self.substitute_pool:
                v += i + ' , '
            return v  
    
    def set_substitute_pool(self, file_name):
        try:
            with ( open(file_name) as fh):
                for line in fh:
                    self.substitute_pool = line.split(',')
        except FileNotFoundError:
            print("FIle is not present , please check the name / path of the file ")              
