# Code by IKrehan #

from tkinter import *


def average_opt(event):
    global secondary_background
    global entry_image

    root2 = Toplevel()
    root2.title('Calculadora')
    root2.geometry('470x270')


    #Background
    background_average = Canvas(root2, height=500, width=500)
    background_average.pack(expand=YES, anchor=NW)
    background_average.create_image(0, 0, image=secondary_background, anchor=NW)


    def calculate(event):
        # Calculate the average
        media = (2 * grade1.get() + 2 * grade2.get() + grade3.get()) / 5

        # Change Result Label
        background_average.itemconfig(result_label, text='Sua nota é {:.1f}'.format(media))

    # Labels: Show informations for user
        # parcial label
    background_average.create_text(90, 30, text='Parcial:', font=('Segoe Print', 14, 'bold'), fill='white')

        # bimestral label
    background_average.create_text(90, 80, text='Bimestral:', font=('Segoe Print', 14, 'bold'), fill='white')
    
        # trabalho label
    background_average.create_text(90, 130, text='NTD:', font=('Segoe Print', 14, 'bold'), fill='white')

        # Result Label (Just visible after the button execute)
    result_label = background_average.create_text(230, 220, text='', font=('Segoe Print', 14, 'bold'), fill='white')

    # Entrys: Colect the informations from users
    grade1 = IntVar()
    grade2 = IntVar()
    grade3 = IntVar()

    e1 = Entry(background_average, textvariable=grade1, bd=0, highlightthickness=0)
    e2 = Entry(background_average, textvariable=grade2, bd=0, highlightthickness=0)
    e3 = Entry(background_average, textvariable=grade3, bd=0, highlightthickness=0)
    background_average.create_window(300, 30, window=e1, height=15, width=50)
    background_average.create_window(300, 80, window=e2, height=15, width=50)
    background_average.create_window(300, 130, window=e3, height=15, width=50)

    background_average.create_image(300, 30, image=entry_image)
    background_average.create_image(300, 80, image=entry_image)
    background_average.create_image(300, 130, image=entry_image)
    
    # Buttons: Execute a command
    calculate_button = background_average.create_text(180, 170, text='Calcular', font=('Segoe Print', 16, 'bold'), fill='white')
    background_average.tag_bind(calculate_button, '<Button-1>', calculate)


def necessarygrade_opt(event):
    global entry_image
    global third_background

    root4 = Toplevel()
    root4.title('Nota Necessária')
    root4.geometry('470x270')

    #Canvas
    necessary_grade_background = Canvas(root4, height=500, width=500)
    necessary_grade_background.pack(expand=YES, anchor=NW)


    # Background
    necessary_grade_background.create_image(0, 0, image=third_background, anchor=NW)


    def calculate_necessary_grade(event):
        necessarygrade = (5 * wanted_grade.get() - 2 * parcial.get() - trabalho.get()) / 2

        if necessarygrade <= 10 and necessarygrade >= 0:
            necessary_grade_background.itemconfig(result_label, text='Para alcançar esta média é preciso tirar {}'.format(necessarygrade))

        else:
            necessary_grade_background.itemconfig(result_label, text='É impossível alcançar essa média')


    # Labels: Show informations for user
        # parcial label
    necessary_grade_background.create_text(90, 30, text='Parcial:', font=('Segoe Print', 14, 'bold'), fill='white')

        # bimestral label
    necessary_grade_background.create_text(90, 80, text='NTD:', font=('Segoe Print', 14, 'bold'), fill='white')
    
        # trabalho label
    necessary_grade_background.create_text(90, 130, text='Média Desejada:', font=('Segoe Print', 14, 'bold'), fill='white')

        # Result Label (Just visible after the button execute)
    result_label = necessary_grade_background.create_text(230, 200, text='', font=('Segoe Print', 13, 'bold'), fill='white')

    # Entrys: Colect the informations from users
    parcial = IntVar()
    trabalho = IntVar()
    wanted_grade = IntVar()

    e1 = Entry(necessary_grade_background, textvariable=parcial, bd=0, highlightthickness=0)
    e2 = Entry(necessary_grade_background, textvariable=trabalho, bd=0, highlightthickness=0)
    e3 = Entry(necessary_grade_background, textvariable=wanted_grade, bd=0, highlightthickness=0)
    necessary_grade_background.create_window(300, 30, window=e1, height=15, width=50)
    necessary_grade_background.create_window(300, 80, window=e2, height=15, width=50)
    necessary_grade_background.create_window(300, 130, window=e3, height=15, width=50)

    necessary_grade_background.create_image(300, 30, image=entry_image)
    necessary_grade_background.create_image(300, 80, image=entry_image)
    necessary_grade_background.create_image(300, 130, image=entry_image)
    
    # Buttons: Execute a command
    calculate_button = necessary_grade_background.create_text(180, 170, text='Calcular', font=('Segoe Print', 16, 'bold'), fill='white')
    necessary_grade_background.tag_bind(calculate_button, '<Button-1>', calculate_necessary_grade)



def yourgrade_opt(event):
    global entry_image
    global fourth_background

    root3 = Toplevel()
    root3.title('Sua Nota')
    root3.geometry('470x270')

    # Canvas
    yourgrade_background = Canvas(root3, width=500, height=500)
    yourgrade_background.pack(expand=YES, anchor=NW)

     # Background
    yourgrade_background.create_image(0, 0, image=fourth_background, anchor=NW)


    def calculate_YourGrade(event):
        grade = (achieved_scores.get() / total_scores.get()) * 10
        if achieved_scores.get() > total_scores.get():
            yourgrade_background.itemconfig(result_label, text='É impossivel ultrapassar o\nnúmero máximo de scores')
        else:
            yourgrade_background.itemconfig(result_label, text='A nota alcançada é {:.1f}'.format(grade))

    # Labels: Show informations for user
        # scores totais
    yourgrade_background.create_text(120, 30, text='Scores Totais:', font=('Segoe Print', 14, 'bold'), fill='white')
        # scores obtidos
    yourgrade_background.create_text(125, 90, text='Scores Obtidos:', font=('Segoe Print', 14, 'bold'), fill='white')


    # Entry: Colect the informations from users
    total_scores = IntVar()
    achieved_scores = IntVar()

    e1 = Entry(yourgrade_background, textvariable=total_scores, bd=0, highlightthickness=0)
    e2 = Entry(yourgrade_background, textvariable=achieved_scores, bd=0, highlightthickness=0)

    yourgrade_background.create_window(320, 30, window=e1, width=50, height=15)
    yourgrade_background.create_window(320, 90, window=e2, width=50, height=15)

    # Customize Entrys
    yourgrade_background.create_image(322, 30, image=entry_image)
    yourgrade_background.create_image(322, 90, image=entry_image)


    # Buttons: Execute a command
    button_yourgrade = yourgrade_background.create_text(200, 150, text='Calcular', font=('Segoe Print', 16, 'bold'), fill='white')
    yourgrade_background.tag_bind(button_yourgrade, '<Button-1>', calculate_YourGrade)


    # Result Label (Only visible after the button execute)
    result_label = yourgrade_background.create_text(220, 210, text='', font=('Segoe Print', 14, 'bold'), fill='white')



root = Tk()
root.title('Calculadora Escolar')


# Window will be in the middle of screen
root.update_idletasks()
x = root.winfo_screenwidth()/ 2 - root.winfo_reqwidth()
y = root.winfo_screenheight()/ 2 - root.winfo_reqheight()
root.geometry("470x270+%d+%d" % (x, y))

# Images for backgrounds are loaded here
main_background = PhotoImage(file='imgs/background.gif')
secondary_background = PhotoImage(file='imgs/background_average.gif')
third_background = PhotoImage(file='imgs/background_necessarygrade.gif')
fourth_background = PhotoImage(file='imgs/background_yourgrade.gif')
entry_image = PhotoImage(file='imgs/entry.gif')

# Background
screen = Canvas(root, height=270, width=470)
screen.pack(expand=YES, fill=BOTH)
screen.create_image(0, 0, image=main_background, anchor=NW)


# button for open average window
media_button = screen.create_text(60, 130, text='Média', font=('Segoe Print', 16, 'bold'), fill='white')
screen.tag_bind(media_button, '<Button-1>', average_opt)

# button for open necessary grade window
necessarygrade_button = screen.create_text(210, 130, text='Nota Necessária', font=('Segoe Print', 16, 'bold'), fill='white')
screen.tag_bind(necessarygrade_button, '<Button-1>', necessarygrade_opt)

# button for open you grade window
yourgrade_button = screen.create_text(380, 130, text='Sua Nota', font=('Segoe Print', 16, 'bold'), fill='white')
screen.tag_bind(yourgrade_button, '<Button-1>', yourgrade_opt)


root.mainloop()
