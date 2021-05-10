from pyrogram import Client
from os import mkdir

if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    Client("zipBot").run()