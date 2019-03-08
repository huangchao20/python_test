import tkinter

root = tkinter.Tk()
root.title("Jason niu工作室")

group = tkinter.LabelFrame(root, text="关于区块链技术，你想了解的是哪方面的知识？", padx=5, pady=5)
group.pack(padx=15, pady=15)
LANGS = [("共识机制", 1), ("P2P网络", 2), ("加密算法", 3), ("数据存储", 4), ("智能合约", 5), ("跨链技术", 6)]

v = tkinter.IntVar()
for lang, num in LANGS:
    b = tkinter.Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

