from  ipl_definitions import *
from  datetime import datetime
def main():
    
    player1,player2,player3,player4 \
                            = Player('David Warner',5000,6000,'batsman','Australian',datetime(1985,1,1),{}),\
                              Player('MSD',5000,6000,'batsman','Indian',datetime(1981,1,1),{}),\
                              Player('Sachin',5000,6000,'batsman','Indian',datetime(1975,1,1),{}),\
                              Player('Dravid',5000,6000,'batsman','Indian',datetime(1976,1,1),{})
                              
    
    
    my_teams = [
                Team('Delhi Capitals','Vikas','David Warner',["Suraj","JSW"],
                     [{'name': 'bharat' , 'role' : 'batting_coach' },
                      {'name': 'ricky ponting' , 'role' : 'head_coach' }
                      ],[player1,player2]),
                Team('CSK','Ravindra','MSD',["aboli","indrajeet"],
                     [{'name': 'shivani' , 'role' : 'batting_coach' },
                      {'name': 'rahul' , 'role' : 'head_coach' }
                      ],[player4,player3])
                ]
    
    for i in my_teams:
        print(i.get_team())
    
    my_football_team = Football_team \
                        ('CSK','Ravindra','MSD',["aboli","indrajeet"],
                        [{'name': 'shivani' , 'role' : 'batting_coach' },
                        {'name': 'rahul' , 'role' : 'head_coach' }
                        ],[player4,player3],[])
    
    my_football_team.set_substitute_pool('substitute_players.txt')
    
    print(my_football_team.get_team())
        
main()    


# # regular expression 
# [] --> sets 
# a-z , A-Z , 0-9 --> ranges that you can give in the set 
# . --> everything other than \n

# Quantifiers:
#     * - 0 or more
#     + - 1 or more
#     ? - 0 or 1 
#     {m} - exactly m times
#     { m , } - minimum m max infinite 
#     {m,n} - from m to n times , greedy at max n
#     {m,n}? -- non greedy (min m stop)
#     {m,n}+ -- greedy (but it may backtrack if required and not reach till n  )
    
#     () - creates a group 
#     (?:) -- read it as a group but don't capture it 
#     (?= ... ) -- lookahead + assertion will check for ... ahead of the value 
#     (?! ... ) -- lookahead - assertion will check for not of  ... ahead of the value 
#     (?<= ... ) -- lookbehind + assertion will check for ... ahead of the value 
#     (?<! ... ) -- lookbehind - assertion will check for not of  ... ahead of the value 
#     (?p<name>) - name to the hroup 
#     (?) -- check this out 
    
#     \d -- digits
#     \D - non-digits
#     \w - alphanumberic characters 0-9 a-z A-Z _
#     \W - non alphanumeric
#     \s - white space (\t\v\0\n\r\f)
#     \S other than white space 
#     \b - word boundary 
    
    

