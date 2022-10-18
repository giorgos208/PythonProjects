
# Rock Paper Scissor


computer_plays = "RPSRPSRPSPPRSRSRPSPR"
i = 0
user_play = (input("Pick Rock Paper Scissor (R,P,S): "))

while (user_play != ""):
    draw = False;
    win = False;
    if (user_play != "R" and  user_play != "P" and user_play != "S" and user_play != "r" and  user_play != "p" and user_play != "s"):
        user_play = (input("Wrong input! Pick Rock Paper Scissor (R,P,S) or press to enter to stop: "))
    else:
        if (computer_plays[i] == "R"):
            if (user_play == "R" or user_play == "r"):
                draw = True
            elif (user_play == "P" or user_play == "p"):
                win = True
            else: win = False

        elif (computer_plays[i] == "P" or user_play == "p"):
            if (user_play == "P"):
                draw = True
            elif (user_play == "R" or user_play == "r"):
                win = False
            else: win = True

        else:
            if (user_play == "S" or user_play == "s"):
                draw = True
            elif (user_play == "R" or user_play == "r"):
                win = True
            else: win = False


        if (draw):
            print ("Computer chose:"+ computer_plays[i] +". It's a draw!")
        elif (win):
            print ("Computer chose:"+ computer_plays[i] +". You won!")
        else:
            print ("Computer chose:"+ computer_plays[i] +". You lost!")
        if (i == len(computer_plays) - 1):
            i = 0
        else: i += 1
        user_play = (input("Pick Rock Paper Scissor (R,P,S): "))
