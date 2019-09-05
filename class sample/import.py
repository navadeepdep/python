import hello
from datetime import datetime



def call():   
    #hello.callme()  
    print(hello.add(5, 10))
    
    ctemps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    tempDict = {t: (t *2) for t in ctemps if t < 100}
    print(tempDict)

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    newTeam = {k:v for team in (team1, team2) for k, v in team.items() if k == 'Jameson'}
    print(newTeam)

    # print(hello.mul(45,2)) 
    # hello.hello1.called()

if __name__ == "__main__":call()