from colorama import Fore

print(Fore.LIGHTCYAN_EX + """
███████╗███████╗███████╗██╗      ██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██╔════╝██║      ██╔══██╗██╔═══██╗╚══██╔══╝
█████╗  █████╗  █████╗  ██║█████╗██████╔╝██║   ██║   ██║   
██╔══╝  ██╔══╝  ██╔══╝  ██║╚════╝██╔══██╗██║   ██║   ██║   
██║     ███████╗███████╗███████╗ ██████╔╝╚██████╔╝   ██║   
╚═╝     ╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   
                                                           
""" + Fore.RESET)

print("Hi!! What's your name?")
name = input()
print("Oh! " + name + " Nice to meet you!")
print("And, how are you?")
feel = input()
if feel == "Good":
    print("I'm glad to hear it!")
elif feel == "good":
    print("I'm glad to hear it!")
elif feel == "Bad":
    print("I am sorry!")
elif feel == "bad":
    print("I am sorry!")
else:
    print(Fore.RED + "Please, choose good or bad." + Fore.RESET)

print(Fore.LIGHTYELLOW_EX + "Goodbye!" + Fore.RESET)


input("")