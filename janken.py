#ランダム
import random as rd
HandList:dict = {
        "1" : "グー",
        "2" : "チョキ",
        "3" : "パー"
    }
def handInput():
    userHandId = input("手を決めてください\nグー:1\nチョキ:2\nパー:3\n>>")
    userHand = HandList[userHandId]
    return userHand   
def computerHandGenerate():
    computerHandId = rd.randint(1,3)
    computerhand = HandList[computerHandId]
    return computerhand
def winnerCheck(userHand:str,computerHand:str):
    if userHand == "グー":
        if computerHand == "グー":
            winner = None
        if computerHand == "チョキ":
            winner = "user"
        if computerHand == "パー":
            winner = "computer"
    if userHand == "チョキ":
        if computerHand == "グー":
            winner = "computer"
        if computerHand == "チョキ":
            winner = None
        if computerHand == "パー":
            winner = "user"
    if userHand == "パー":
        if computerHand == "グー":
            winner = "user"
        if computerHand == "チョキ":
            winner = "computer"
        if computerHand == "パー":
            winner = None
    return winner
def game():
    userhand = handInput()
    computerhand = computerHandGenerate()
    winner = winnerCheck(userHand=userhand,computerHand=computerhand)
    print(f"勝者は{winner}です！")
if __name__ == "__main__":
    game()
        
        
    