import sys
import colorama
from commands import package, gamemode, help

def main(args):
    if len(args) < 1:
        print("Usage: spm <command>")
        print("Comandos disponíveis: package, gamemode, help")
        sys.exit(1)

    command = args[0]
    if command == "package":
        package.main(args[1:])
    elif command == "gamemode":
        gamemode.main(args[1:])
    elif command == "help":
        help.main(args[1:])
    else:
        print(f"{colorama.Fore.RED}Invalid command. Use spm help for more informations.{colorama.Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
