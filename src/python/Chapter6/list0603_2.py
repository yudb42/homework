import tkinter

def click_btn():
    button["text"] = "クリックしました"

root = tkinter.Tk() #ウィンドウの部品を作る
root.title("初めてのボタン")
root.geometry("800x600")
button = tkinter.Button(root, text="クリックしてください", font=("Times New Roman", 24), command=click_btn) #ボタンの部品を作る
button.place(x=200, y=100) #ウィンドウにボタンを配置
root.mainloop()