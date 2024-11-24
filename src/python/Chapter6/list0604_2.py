import tkinter
root = tkinter.Tk() #ウィンドウの部品を作る
root.title("初めての画面表示")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="iroha.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()