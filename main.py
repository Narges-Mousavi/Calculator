import tkinter as tk

win = tk.Tk()
win.title('Calculator')
frame = tk.Frame(bg='#182039', width=545, height=600)
text = ''
text_input = tk.StringVar()


def clear():
    global text
    text = ''
    text_input.set('')


def click_button(s):
    global text
    text = text + str(s)
    text_input.set(text)


def calculate():
    global text
    text2 = str(eval(text))
    text_input.set(text2)
    text = ''


def delete():
    global text
    text = text[:-1]
    text_input.set(text)


btn_color = '#bdbdbd'
sign_colors = '#c51162'
entry = tk.Entry(frame, bg='#96c5bd', width=14, font=('halvatica', 50), bd=4, textvariable=text_input)
entry.place(x=10, y=10)
btn_7 = tk.Button(win, text=7, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(7)).place(x=10, y=130)
btn_8 = tk.Button(win, text=8, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(8)).place(x=115, y=130)
btn_9 = tk.Button(win, text=9, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(9)).place(x=220, y=130)
btn_divide = tk.Button(win, text='÷', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button('/')).place(x=435, y=475)
btn_4 = tk.Button(win, text=4, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(4)).place(x=10, y=245)
btn_5 = tk.Button(win, text=5, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(5)).place(x=115, y=245)
btn_6 = tk.Button(win, text=6, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(6)).place(x=220, y=245)
btn_multiply = tk.Button(win, text='×', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18, 'bold'), command=lambda: click_button('*')).place(x=325, y=475)
btn_1 = tk.Button(win, text=1, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(1)).place(x=10, y=360)
btn_2 = tk.Button(win, text=2, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(2)).place(x=115, y=360)
btn_3 = tk.Button(win, text=3, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(3)).place(x=220, y=360)
btn_plus = tk.Button(win, text='+', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18, 'bold'), command=lambda: click_button('+')).place(x=325, y=360)
btn_0 = tk.Button(win, text=0, padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(0)).place(x=10, y=475)
btn_dot = tk.Button(win, text='.', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button('.')).place(x=433, y=245)
btn_minus = tk.Button(win, text='–', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button('-')).place(x=435, y=360)
btn_clear = tk.Button(win, command=lambda: clear(), text='clear', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18, 'bold')).place(x=325, y=130)
btn_rp = tk.Button(win, text='(', padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button('(')).place(x=115, y=475)
btn_lp = tk.Button(win, text=')', padx=10, bg=btn_color, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=lambda: click_button(')')).place(x=220, y=475)
btn_equal = tk.Button(win, text='=', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18), command=calculate).place(x=326, y=245)
btn_del = tk.Button(win, text='←', padx=10, bg=sign_colors, fg='#182039', width=4, height=3, bd=7, font=('cooper black', 18, 'bold'), command=delete).place(x=435, y=130)


frame.grid()
frame.mainloop()
