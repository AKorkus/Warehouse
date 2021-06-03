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


def read_format(*args):
    print("{:<10} {:<30} {:<10} {:<10} {:<15}".format(*args))


# SHOW ARTICLES..................................................................................................................
def show_articles():
    #       ofset = [int(i) for i in artlist[0][:-2].split(", ")]
    artlist = open_articles()
    header = get_header(artlist)
    read_format(*header)
    kontent = [line[:-1] for line in artlist[1:]]
    artmatrix = [line.split(", ") for line in kontent]
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
    open_articles("a", line)


# DELETE ARTICLE.................................................................................................................
def delete_article(id="nothing"):
    header = get_header()
    artmatrix = show_articles()
    if id == "nothing":
        id = input("Write article ID:")
    art_ids = []
    for i in artmatrix:
        art_ids.append(i[0])
    indeks = art_ids.index(id)
    to_be_deleted = artmatrix[indeks]
    print(to_be_deleted)
    yes_no = input("Are you sure to delete? Y/N:")
    try:
        yes_no = yes_no[0].lower()
    except:
        logging.warning("Wrong command, canceled.")
    if yes_no == "y":
        del(artmatrix[indeks])
        new_articles = line_concatenate(header)
        for row in artmatrix:
            line = line_concatenate(row)
            new_articles += line
        open_articles("w", new_articles)
    else:
        logging.debug("Cancelled.")
