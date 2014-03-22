# A program for Task of the "Basics of programming"
# "KAPE Gallery"  v. 1.1.2
# To Open your images you have to change the argument PATH_GALLERY and ADDRES
# which located on the 22 and 23 lines.
# For example: PATH_GALLERY='C:\\Users\\1\\Desktop\\фотографии\\'
#              ADDRES = ' "C:\\Users\\1\\Desktop\\фотографии\\" '
# Programm have been written on the Python 2.7.5 and 2.7.6
# and not tested with the Python 2.7.7 and more newer.
# This program have "Open source softwre" license.
# Thank you for using our project, we wish that you will be pleased.


import os
from Tkinter import *
import tkFileDialog
import subprocess
from PIL import Image
from PIL import ImageTk


# Paths for Gallery
PATH_GALLERY = 'C:\\Users\\user\\Desktop\\Программрование\\Python\\Task2\\arts\\'
ADDRES=' "C:\\Users\\user\\Desktop\\Программрование\\Python\Task2\\arts\\" '
PATH_GALLERY_OPEN = ADDRES


# List of the Paths to images of the gallery
image_list = []
# List with NAMEs of images of the gallery
text_list = []
# Reset the counter of the pictures number
CURRENT = 0


# Creating the window "About"
def About():
    """
    Данная функция создаёт новое окно About с определённым текстовым набором

    Возвращаемое значение: None
    """
    ABOUT_WINDOW = Tk()
    ABOUT_WINDOW.title('About')
    ABOUT_WINDOW.maxsize(420,120)
    ABOUT_WINDOW.minsize(420,120)
    INFO = """ "KAPE Gallery"\nСоздатели: Круглова А.В.
                     Привалов Е.В.\nСтуденты группы 1652, СПбНИУ ИТМО\n
                     Программа написана на Языке программирования Python 2.7
                \n\t\t\t\tKAPE Gallery, 2014 ©All Rights Reserved"""
    lab = Label(ABOUT_WINDOW,text=INFO.decode('cp1251'))
    lab.pack() 


# Looking for images at the Gallery Path and entry their NAMEs
# and path into special lists
def OpenPicture():
    """ Данная функция находит всевозможные файлы в папке указанной заранее,
        запоминает полный адрес к найденному файлу, добавляет полные адрес и
        имя файла в соответствующие листы image_list и text_list


        Возвращаемое значение: None
    """
    global FULL_NAME
    for ROOT, DIRS, FILES in os.walk(PATH_GALLERY): 
        for NAME in FILES:
            FULL_NAME = os.path.join(ROOT, NAME)
            image_list.append(FULL_NAME)
            text_list.append(NAME)


# Opening the directory of the gallery
def OpenDirectory():
    """ Данная функция открывает директорию с файлами галереи

        Возвращаемое значение: None
    """
    subprocess.Popen('explorer' + PATH_GALLERY_OPEN)


# INFOrmation about image
def Configuration():
    """ Данная функция создаёт новое окно Configuration, в котором
        указан путь к файлу в текстовой форме и свойства самого файла

        Возвращаемое значение: None
    """
    OpenPicture()
    CONFIGURATION_WINDOW = Tk()
    INFO = 'Расположение изображения: ' + FULL_NAME
    INFO2 = '\n\nIn development for unknown period'
    CONFIGURATION_WINDOW.maxsize(760,300)
    CONFIGURATION_WINDOW.minsize(760,300)
    CONFIGURATION_WINDOW.title('Configuration')
    lab = Label(CONFIGURATION_WINDOW, text=INFO.decode('cp1251'))
    lab.pack()
    lab2 = Label(CONFIGURATION_WINDOW, text = INFO2.decode('cp1251'))
    lab2.pack()


# INFOrmation about us
def ContactUs():
    """
    Данная функция создаёт новое окно Contact us с определённым текстовым набором

    Возвращаемое значение: None
    """
    ABOUT_WINDOW = Tk()
    ABOUT_WINDOW.title('Contact us')
    ABOUT_WINDOW.maxsize(300,150)
    ABOUT_WINDOW.minsize(300,150)
    INFO = """ Contact us:\n\nSocial: \nvk.com/i_lovee/ (Kruglova A.)\nvk.com/indavant/ (Privalov E.)"""
    INFO2 = """\n\nE-mails: \nnactina@list.ru\nclohik94@mail.ru
            """
    lab = Label(ABOUT_WINDOW,text=INFO.decode('cp1251'))
    lab.pack()
    lab2 = Label(ABOUT_WINDOW,text=INFO2.decode('cp1251'))
    lab2.pack() 


# Changing the image(forward/back)
def ChangePicture(SHIFT):
    """ Данная функция перебирает лист с файлами, добавленными функцией
        OpenPicture, а так же выводит информацию о названии файла на экран

    Аргументы: SHIFT

    Возвращаемое значение: None
    """
    OpenPicture()
    global CURRENT, image_list
    if not (0 <= CURRENT + SHIFT < len(image_list)):
        # что тут было? :D
        return
    CURRENT += SHIFT
    IMAGE = Image.open(image_list[CURRENT])
    PHOTO = ImageTk.PhotoImage(IMAGE)
    label['text'] = text_list[CURRENT]
    label['image'] = PHOTO
    label.PHOTO = PHOTO


# Main program's body
ROOT = Tk()
ROOT.title('KAPE Gallery')
ROOT.maxsize(650,560)
ROOT.minsize(650,560)
MAIN_MENU = Menu(ROOT)    # Creating menu
ROOT.config(menu=MAIN_MENU)    # Add Menu to the Main Window
FILE_MENU = Menu(MAIN_MENU)    # Creating submenu
FILE_MENU2 = Menu(MAIN_MENU)    # Creating submenu №2
FILE_MENU3 = Menu(MAIN_MENU)    # Creating submenu №3
MAIN_MENU.add_cascade(label="File", menu=FILE_MENU)
FILE_MENU.add_command(label="Open Gallery", command=OpenDirectory)
FILE_MENU.add_separator()
FILE_MENU.add_command(label="Exit", command=ROOT.destroy)
canvas = Canvas(ROOT, width=600, height=600,bg='green')
MAIN_MENU.add_cascade(label="Options", menu=FILE_MENU3)
FILE_MENU3.add_command(label="Configuration", command=Configuration)
MAIN_MENU.add_cascade(label="Help", menu=FILE_MENU2)
FILE_MENU2.add_command(label="About", command=About)
FILE_MENU2.add_separator()
FILE_MENU2.add_command(label="Contact us", command=ContactUs)
label = Label(ROOT, compound=TOP)
label.pack()
# Zone for buttons
frame = Frame(ROOT)
frame.pack()
# Button to change the picture(back)
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Previous picture',
       command=lambda: ChangePicture(-1)).pack(side=LEFT)
# Button to change the picture(forward)
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Next picture',
       command=lambda: ChangePicture(+1)).pack(side=LEFT)
# Button fo closing the program
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Quit',
       command=ROOT.destroy).pack(side=LEFT)
# Initial сondition of the program 
ChangePicture(0)
ROOT.mainloop()
