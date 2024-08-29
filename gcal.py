import tkinter as tk

# Fungsi klik Tombol
def button_click(value):
    current_text = result_var.get()
    if value == 'C':
        result_var.set('')
        history_listbox.delete(0, tk.END)
    elif value == '⌫':
        result_var.set(current_text[:-1])
    elif value == '=':
        try:
            expression = current_text.replace('×', '*').replace('÷', '/')
            result = str(eval(expression))
            result_var.set(result)
            history_listbox.insert(tk.END, f"{current_text} = {result}")
        except:
            result_var.set('Error')
    else:
        result_var.set(current_text + value)

# Fungsi Window
def show_window():
    # Inisialisasi Variable Global
    global result_var, history_listbox 

    # Inisialisasi Object Tkinter
    window = tk.Tk()

    # Inisialisasi Variable
    window_width = 250
    window_height = 400

    # Inisialisasi Posisi Center Window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_win = int((screen_width / 2) - (window_width / 2))
    y_win = int((screen_height / 2) - (window_height / 2))

    # Inisialisasi Window
    window.title("GCalculator 2.0")
    window.geometry(f'{window_width}x{window_height}+{x_win}+{y_win}')
    window.resizable(False, False)
    window.config(bg='black')

    # Inisialisasi Variabel untuk hasil
    result_var = tk.StringVar()

    # Membuat Frame History
    frm_his = tk.Frame(window, bg='black')
    frm_his.pack(expand=True, fill='both')

    # Membuat Frame Window
    frm_win = tk.Frame(window, bg='black')
    frm_win.pack(expand=True, fill='both')

    # Membuat Frame Tombol
    frm_btn = tk.Frame(window, bg='black')
    frm_btn.pack(expand=True, fill='both')

    # Membuat Listbox History
    history_listbox = tk.Listbox(frm_his, height=2, font=('Calibri', 15), justify='right', bd=0, highlightthickness=0, bg='black', fg='white')
    history_listbox.pack(expand=True, fill='both', padx=5, pady=5)

    # Membuat Entry Display
    ent_dis = tk.Entry(frm_win, textvariable=result_var, font=('Calibri', 25), justify='right', bd=0, bg='black', fg='white')
    ent_dis.pack(expand=True, fill='both', padx=10, pady=10)

    # Membuat List Tombol
    btns = [
        ('C', 1, 0, 1, '#4A4A4A', 'white'), ('⌫', 1, 1, 1, '#4A4A4A', 'white'), ('%', 1, 2, 1, '#4A4A4A', 'white'), ('÷', 1, 3, 1, '#FF4F1B', 'white'),
        ('7', 2, 0, 1, '#333333', 'white'), ('8', 2, 1, 1, '#333333', 'white'), ('9', 2, 2, 1, '#333333', 'white'), ('×', 2, 3, 1, '#FF4F1B', 'white'),
        ('4', 3, 0, 1, '#333333', 'white'), ('5', 3, 1, 1, '#333333', 'white'), ('6', 3, 2, 1, '#333333', 'white'), ('-', 3, 3, 1, '#FF4F1B', 'white'),
        ('1', 4, 0, 1, '#333333', 'white'), ('2', 4, 1, 1, '#333333', 'white'), ('3', 4, 2, 1, '#333333', 'white'), ('+', 4, 3, 1, '#FF4F1B', 'white'),
        ('0', 5, 0, 1, '#333333', 'white'), ('00', 5, 1, 1, '#333333', 'white'), ('.', 5, 2, 1, '#333333', 'white'), ('=', 5, 3, 1, '#FF4F1B', 'white')
    ]

    # Membuat Looping Tombol
    for (text, row, col, colspan, bg, fg) in btns:
        btn = tk.Button(frm_btn, text=text, font=('Calibri', 18), fg=fg, bg=bg, bd=0, command=lambda value=text: button_click(value))
        btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=0, pady=0)

    # Menyesuaikan ukuran baris dan kolom dalam frame tombol
    for i in range(1, 6):
        frm_btn.rowconfigure(i, weight=1)
    for j in range(4):
        frm_btn.columnconfigure(j, weight=1)

    # Menampilkan Window
    window.mainloop()

if __name__ == "__main__":
    show_window()
