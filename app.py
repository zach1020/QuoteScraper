import tkinter as tk 
import quote_scraper as qs

quote_text = qs.quote
quote_author = qs.author

# Create window
window = tk.Tk()
window.title("Random Quote")
window.resizable(width=False, height=False)

# Set window size
window.geometry('1500x1000')

# Create a label to contain our text
text = tk.Label(master=window, text='\n'+quote_text+'\n\n--'+quote_author, font=("Helvetica", 40), wraplength=1000, justify='center')


text.pack()

window.mainloop()