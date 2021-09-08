import robloxpy       # library to interact with roblox api
import tkinter as tk  # library to build GUI application

# functions
def getValues():
    # get game id from entry box
    robloxGameID = gameID.get()
    # make sure that the output boxes are empty
    likeBox.delete(0, tk.END)
    dislikeBox.delete(0, tk.END)
    # fetch likes and dislikes and make them a variable
    robloxLikes = robloxpy.Game.Internal.GetGameLikes(str(robloxGameID))
    robloxDislikes = robloxpy.Game.Internal.GetGameDislikes(str(robloxGameID))
    # fill boxes with variables
    likeBox.insert(0, str(robloxLikes))
    dislikeBox.insert(0, str(robloxDislikes))

# start building window 
window = tk.Tk()
# window items
# main label
mainLabel = tk.Label(
    text="Example GUI application to interact with ROBLOX."
)
# game entry
gameEntry = tk.Frame(
    master=window
)
gameLabel = tk.Label(
    text="Game ID",
    master=gameEntry
)
gameID = tk.Entry(
    master=gameEntry
)
gameSubmit = tk.Button(
    master=gameEntry,
    text="SUBMIT",
    command=getValues
)

# likes and dislikes result
likesDislikesLBL = tk.Frame(master=window)
likesDislikesBOX = tk.Frame(master=window)
likeLabel = tk.Label(
    text="Game Likes",
    master=likesDislikesLBL
)
dislikeLabel = tk.Label(
    text="Game Dislikes",
    master=likesDislikesLBL
)
likeBox = tk.Entry(
    master=likesDislikesBOX
)
dislikeBox = tk.Entry(
    master=likesDislikesBOX
)

# pack
# main label
mainLabel.pack(
    fill=tk.BOTH,
    expand=True
)
# game entry
gameEntry.pack(
    fill=tk.BOTH,
    expand=True
)
gameLabel.pack(
    fill=tk.BOTH,
    expand=True,
    side=tk.LEFT
)
gameID.pack(
    fill=tk.BOTH,
    expand=True,
    side=tk.LEFT
)
gameSubmit.pack(
    fill=tk.BOTH,
    expand=True,
    side=tk.RIGHT
)
# likes and dislikes section
likesDislikesLBL.pack(
    fill=tk.BOTH,
    expand=True
)
likeLabel.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)
dislikeLabel.pack(
    fill=tk.BOTH,
    side=tk.RIGHT,
    expand=True
)
likesDislikesBOX.pack(
    fill=tk.BOTH,
    expand=True
)
likeBox.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)
dislikeBox.pack(
    fill=tk.BOTH,
    side=tk.RIGHT,
    expand=True
)

# initialize window
window.mainloop()