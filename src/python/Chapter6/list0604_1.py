import tkinter
root = tkinter.Tk() #ウィンドウの部品を作る
root.title("初めてのキャンバス")
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()
root.mainloop()