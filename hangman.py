import random

def hangman(word):#wordは問題の答え。
   #正誤判定のための素材。
    wrong = 0
    stages = ["",
             "______      ",
             "|           ",
             "|     |     ",
             "|     0     ",
             "|    /|＼   ",
             "|    / ＼   ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    #ウェルカムメッセージ！
    print("ハングマンへようこそ！")

   #ゲームのループ。
    while wrong < len(stages):#ハングマンが未完成の時True。
       #出題メッセージと回答欄。
        print("\n")
        msg = "1文字を予想してね。"
        char = input(msg)
        #正誤判定
        if char in rletters:
            idx = rletters.index(char)
            board[idx] = char
            rletters[idx] = "$"
        else:
            wrong += 1
        #スコア表示
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        #勝敗判定
        if "_" not in board:
            print("あなたの勝ちです！")
            print(" ".join(board))
            win = True
            break

    #勝敗判定
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は{}".format(word))

#答えのリスト。
words = ["chocolate", "cake", "cheese", "bread", "steak"]
#プログラム起動時にリストからランダムに答えを一つ決める。
hangman(words[random.randint(0, 4)])
