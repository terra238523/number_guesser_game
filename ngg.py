def number_guesser_game():

    def display_ascii_art():
        print("""
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\    \        
       /::::|   |               /::::\    \              /::::\    \       
      /:::::|   |      by      /::::::\    \   terra    /::::::\    \   238523   
     /::::::|   |             /:::/\:::\    \          /:::/\:::\    \     
    /:::/|::|   |            /:::/  \:::\    \        /:::/  \:::\    \    
   /:::/ |::|   |           /:::/    \:::\    \      /:::/    \:::\    \   
  /:::/  |::|   | _____    /:::/    / \:::\    \    /:::/    / \:::\    \  
 /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\  /:::/    /   \:::\ ___\ 
/:: /    |::|   /::\____\/:::/____/  ___\:::|    |/:::/____/  ___\:::|    |
\::/    /|::|  /:::/    /\:::\    \ /\  /:::|____|\:::\    \ /\  /:::|____|
 \/____/ |::| /:::/    /  \:::\    /::\ \::/    /  \:::\    /::\ \::/    / 
         |::|/:::/    /    \:::\   \:::\ \/____/    \:::\   \:::\ \/____/  
         |::::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
         |:::::/    /        \:::\  /:::/    /        \:::\  /:::/    /    
         |::::/    /          \:::\/:::/    /          \:::\/:::/    /     
         /:::/    /            \::::::/    /            \::::::/    /      
        /:::/    /              \::::/    /              \::::/    /       
        \::/    /                \::/____/                \::/____/        
         \/____/                                                           
                                                                           """)


    display_ascii_art()

    print("hey buddy :) think of a number between 1 and 1.000.000 and i'll try to guess it.")
    print("respond with:")
    print("1 if my guess is too low")
    print("2 if my guess is too high")
    print("3 if my guess is correct!!! (it's gonna be)")

    low = 1
    high = 1_000_000
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        print(f"is it {guess}???")
        feedback = input("enter 1 (too low), 2 (too high), or 3 (correct yuppee!!) :")

        # special messages start

        if feedback == "3" and guess == 238523:
            print("w-wait a minute.. you were thinking of... 238523? oh my-... t-that is my favorite number!")
            break
        if feedback == "3" and guess == 1:
            print("seriously? 1? you are the most boring person i've ever seen.")
            break
        if feedback == "3" and guess == 0:
            print("seriously? 0? you are the second most boring person i've ever seen.")
            break
        if feedback == "3" and guess == 500000:
            print("well... that was easy.")
            break
        if feedback == "3" and guess == 1000000:
            print("you always have to be the biggest, don't you?")
            break
        if feedback == "3" and guess in (3, 6, 9):
            print("Nikola Tesla thought that this number held the keys to understanding the universe")
            break
        if feedback == "3" and guess == 1089:
            print("hey! that's einstein's favorite number")
            break
        if feedback == "3" and guess == 1923:
            print("1923 is when my homeland, turkey, was founded!")
            break
        if feedback == "3" and guess == 23:
            print("yes. 23 chromosomes. hope you have them.")
            break
        if feedback == "3" and guess == 2024:
            print("that is the year this program was made in")
            break
        if feedback == "3" and guess == 13:
            print("oh no. you're gonna have some bad luck buddy.")
            break
        if feedback == "3" and guess == 42:
            print("the answer to life, universe, and everything")
            break
        if feedback == "3" and guess == 666:
            print("oooo im so scared")
            break
        if feedback == "3" and guess == 666666:
            print("now, is that scarier than 666 or what?")
            break
        if feedback == "3" and guess == 314159:
            print("nerd")
            break
        if feedback == "3" and guess == 404:
            raise ValueError("404? seriously? are you trying to kill me?")



        #special messages end

        elif feedback == "3":
            print(f"AHAHAHHAHAA!!! I KNEW IT ALL ALONG! THE {attempts} ATTEMPTS WERE JUST TO MESS WITH YOUR MIND!")
            break

        if feedback == "1":
            low = guess + 1

        elif feedback == "2":
            high = guess - 1

        elif feedback == "3":
            print(f"AHAHAHHAHAA!!! I KNEW IT ALL ALONG! THE {attempts} ATTEMPTS WERE JUST TO MESS WITH YOUR MIND!")
            break

        else:
            print("do you have a dent in your head??? the only options are 1, 2, and 3!!")

    if low > high:
        print("are you messing with me?? be consistent DUMBASS. dont just enter random inputs.")
while True:
    number_guesser_game()
    restart = input("press enter if you want to give me another shot, cowboy. close the damn terminal if you're scared.")
    if restart == 'exit':
        print("goodbye, coward.")