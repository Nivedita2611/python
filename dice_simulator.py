# wap to create a function that will
# generate random 3 dice numbers and if all 3 match, then
# display "you win" else display "you lose/ try again"
import random
def streak():
    dices = ['1','2','3','4','5','6',]
    selection = random.choices(dices, k =3)
    if selection[0] == selection[1] == selection[2]:
        return selection, "you win"
    else:
        return selection,"you lose/you try"


ans,msg = streak()
print('rolling the dices...')
print(" ".join(ans))
print(msg)

