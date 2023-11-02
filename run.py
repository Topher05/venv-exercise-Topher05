import emoji
import pyjokes



while True:
    userInput = input("q: quit program \njoke: get a joke \ngrav: enables antigravity\n:")
    if userInput == 'q': 
        print(emoji.emojize('Have a nice day :thumbs_up:'))
        break
    elif userInput == 'joke':
        print(pyjokes.get_joke())
    elif userInput == 'grav':
        import antigravity
    else :
        print('incorrect input try again\n')



