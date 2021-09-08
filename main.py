import robloxpy       # library to interact with roblox api
import tkinter as tk  # library to build GUI application

# start building window 
window = tk.Tk()
# window items
mainLabel = tk.Label(
    text="Example GUI application to interact with ROBLOX."
)

# functions

# pack
mainLabel.pack()

# initialize window
window.mainloop()