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

    # special messages start
    special_messages = {
        238523: "w-wait a minute.. you were thinking of... 238523? oh my-... t-that is my favorite number!",
        1: "seriously? 1? you are the most boring person i've ever seen.",
        500000: "well... that was easy.",
        1000000: "you always have to be the biggest, don't you?",
        1089: "hey! that's einstein's favorite number.",
        1923: "1923 is when my homeland, turkey, was founded!",
        23: "yes. 23 chromosomes. hope you have them.",
        2024: "that is the year this program was made in.",
        13: "oh no. you're gonna have some bad luck buddy.",
        42: "the answer to life, universe, and everything. if you'd believe that LMAO",
        666: "oooo I'm so scared.",
        666666: "now, is that scarier than 666 or what?",
        314159: "nerd",
        404: "404? seriously? are you trying to kill me?",
        18: "that is how old you should be to have sex in most countries.",
        11: "these go to eleven.",
        3: "they say third time's the charm. mathematically, it's impossible for me to find this with 3 attempts",
        30: "my girlfriend thinks this number is funny...",
        2: "that is how many times john f. kennedy got shot.,",
        64: "a whole stack? cool.",
        80085: "yeah, yeah. i know. boobs. very funny.",
        69: "how old are you??",
        420: "somebody is about to get baked.",
        800813: "who doesn't like em'?",
        1337: "hell yeah brother",
        58008: "that's just boobies upside down. what's wrong with you?",
        181: "a lesbian 69, nice.",
        25: "spongebob thinks that's funnier than 24!",
        555: "hahaha",
        808: "bob",
        451: "fahrenheit",
        4: "you'd be dead if you were in japan.",
        7: "lucky.",
        911: "what's your emergency?",
        1111: "you just keep seeing this number, don't you? it doesn't have a meaning though.",
        325832: "that's 238523 backwards. are you anti-me or something?",
        1939: "you must be either a tankie or some edgy 'neo-nazi' kid.",
        1980: "did you have a mullet back then?",
        999999: "very creative.",
        999998: "ok that's a little creative.",
        37: "let's go justin!!",
        727: "when you fucking see it.",
        9: "9 for mortal men doomed to die.",
        5: "i like 5. it's easy to do calculations with.",
        40000: "warhammer",
        101: "wizard101",
        500001: "i was pretty close at first, eh?",
        499999: "i was pretty close at first, eh?",
        21: "okay, now do this for 21 days."




}
    # special messages end



    while True:
        guess = (low + high) // 2
        attempts += 1

        print(f"is it {guess}???")
        feedback = input("enter 1 (too low), 2 (too high), or 3 (correct yuppee!!) :")

        if feedback == "help":
            print("""
            1. if you want to restart the game, just enter 3 and enter again.
            2. if you want info about the game, enter 'info'.
            """)
            continue

        if feedback == "info":
            print("""
            number_guesser_game.
            made with python.
            made in turkey.
            made by terra238523.
            made as a beginner project.
            there are 50 special messages in the game.
            """)
            continue


        if feedback == "1":
            low = guess + 1

        elif feedback == "2":
            high = guess - 1

        elif feedback == "3":
            if guess in special_messages:
                if guess == 404:
                    raise ValueError(special_messages[guess])
                print(special_messages[guess])
            else:
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