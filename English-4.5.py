print("==============")
print(">>>Unit?/?<<<")
print("==============")
word = [
">笑う", "laugh",
">実は", "actually",
">好意的な、", "friendly",
">あたたかい", "warm",
">晴れた", "sunny",
">曇った", "cloudy",
">雨の", "rainy",
">自転車", "bike",
">子供", "child",
">子供の複数形", "children",
">結構な", "fine",
">やぁ、どうしたのかな？", "What's up?",
">...してはどうですか？", "why don't you?",
">...の世話をする", "look after",
">いつかまた", "some other time",
">ユニバーサルデザイン", "universal design",
">製品", "product",
">簡単に", "easily",
">安全に", "safely",
">もし...ならば", "if"
]
count = 0
while count<10:
    tword = word[count*2]
    print(tword)
    inputword = input('日本語に合う英単語を入力してください。⇒')
    if inputword==word[count*2+1]:
        print('正解です。')
        if count==10:
            break
        else:
            count = count+1
            continue
    else:
        print('不正解です。\n正解は%s'%(word[count*2+1]))
        if count==10:
            break
        else:
            count = count+1
            continue
