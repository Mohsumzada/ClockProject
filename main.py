import tkinter
import datetime as dt

color_dark = '#276678'
color_bright = '#F6F5F5'
color_bright2 = '#D3E0EA'

clock_width = 300
clock_height = 150


# SCREEN SETTINGS
screen = tkinter.Tk()
screen.title("CLOCK")
screen.minsize(width=clock_width, height=clock_height)
screen.config(bg=color_dark)


# LABEL SETTINGS
day_lbl = tkinter.Label(font=('Arial', 20),
                        bg=color_dark,
                        fg=color_bright2)
time_lbl = tkinter.Label(font=('Arial', 150),
                         bg=color_dark,
                         fg=color_bright)
day_lbl.grid(column=0, row=0, pady=10)
time_lbl.grid(column=0, row=1)


# ALL DEFS
def timer_update():
    today = dt.datetime.now()
    time = today.strftime('%H:%M:%S')
    day = today.strftime('%d/%m/%Y')
    time_lbl.config(text=f"{time}")
    day_lbl.config(text=f"{day}")
    screen.after(1000, timer_update)


# MAIN SCRIPTS
screen.after(1000, timer_update)
screen.mainloop()
