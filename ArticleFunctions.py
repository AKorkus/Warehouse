from sys import path
import logging

logging.basicConfig(level=logging.DEBUG)


def here():
    return path[0]


def line_concatenate(line):
    conjunction = ", "
    new_line = conjunction.join(line)
    new_line = new_line+"\n"
    return new_line


def open_articles(mode="r", kontent=""):
    with open(here()+"/ArticleBase.txt", mode) as base:
        if mode == "r":
            artlist = base.readlines()
        else:
            base.write(kontent)
            artlist = kontent
    return artlist


def get_header(artlist=open_articles()):
    return artlist[0][:-1].split(", ")


def select_row(id):
    orly = id == "nothing"
    artmatrix = show_articles(orly)
    if id == "nothing":
        id = input("Write article ID:")
    art_ids = []
    for i in artmatrix:
        art_ids.append(i[0])
    indeks = art_ids.index(id)
    modline = artmatrix[indeks]
    print(modline)
    return (artmatrix, indeks)


def read_format(*args):
    print("{:<10} {:<30} {:<10} {:<10} {:<15}".format(*args))


def approve():
    yes_no = input("Save changes? Y/N:")
    try:
        yes_no = yes_no[0].lower()
    except:
        logging.warning("Wrong command, canceled.")
    if yes_no != "y":
        logging.debug("Cancelled.")
        return "Cancel"
    return "Proceed"


# SHOW ARTICLES..................................................................................................................
def show_articles(orly=True):
    #       ofset = [int(i) for i in artlist[0][:-2].split(", ")]
    artlist = open_articles()
    header = get_header(artlist)
    read_format(*header)
    kontent = [line[:-1] for line in artlist[1:]]
    artmatrix = [line.split(", ") for line in kontent]
    if not orly:
        return(artmatrix)
    for line in artmatrix:
        read_format(*line)
    return (artmatrix)

# ADD ARTICLE....................................................................................................................


def add_article():
    artlist = open_articles()
    header = get_header(artlist)
    line = str(len(artlist))+", "
    for column in header[1:]:
        cell = input(column + ":")
        cell.replace(",", ".")
        line += cell + ", "
    line = line[:-2] + "\n"
    yes_no = approve()
    if yes_no == "Cancel":
        return
    open_articles("a", line)


# DELETE ARTICLE.................................................................................................................
def delete_article(id="nothing"):
    header = get_header()
    artmatrix, indeks = select_row(id)
    yes_no = approve()
    if yes_no == "Cancel":
        return
    del(artmatrix[indeks])
    new_articles = line_concatenate(header)
    for row in artmatrix:
        line = line_concatenate(row)
        new_articles += line
    open_articles("w", new_articles)

# MODIFY ARTICLE..................................................................................................................


def modify_article(id="nothing"):
    header = get_header()
    artmatrix, indeks = select_row(id)
    old_line = artmatrix[indeks]
    line = ""
    for i in range(len(header)):
        column = header[i]
        old_cell = old_line[i]
        cell = input(column + ": " + old_cell + "->")
        cell.replace(",", ".")
        if len(cell) == 0:
            cell = old_cell
        line += cell + ", "
    line = line[:-2]
    yes_no = approve()
    if yes_no == "Cancel":
        return
    artmatrix[indeks] = line.split(", ")
    new_articles = line_concatenate(header)
    for row in artmatrix:
        line = line_concatenate(row)
        new_articles += line
    open_articles("w", new_articles)
