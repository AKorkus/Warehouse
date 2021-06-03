from sys import path
import ArticleFunctions as artf
import logging
logging.basicConfig(level=logging.DEBUG)


def here():
    return path[0]


def exit_mag():
    exit()


def show_commands():
    for i in funktions:
        line = f"{i+':':<20} {funktions[i][1]}"
        print(line)


funktions = {
    "commands": [show_commands, "Shows available commands."],
    "exit": [exit_mag, "Quit program."],
    "articles": [artf.show_articles, "Shows articles database."],
    "artadd": [artf.add_article, "Adds article to data base"],
    "artdel": [artf.delete_article, "Deletes article from database"]
}


def exekute(funktion, *args):
    funktions[funktion][0](*args)


def kommand():
    show_commands()
    kommand_line = input(
        "Write command with arguments after space, to get list of commands, write \'commands\':")
    kommand_list = kommand_line.split(" ")
    funktion = kommand_list[0]
    try:
        args = kommand_list[1:]
    except:
        pass
    try:
        exekute(funktion, *args)
    except:
        logging.warning("Wrong Command!!!")


while True:
    kommand()
