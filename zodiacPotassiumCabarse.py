year = int(input("Please enter a year (1900 or later): "))

while year < 1900:
    print("I'm sorry, please enter a year from 1900 onwards.")
    year = int(input("Enter a year: "))

zodiac = [
    ("Rat", "鼠", "Shǔ"),
    ("Ox", "牛", "Niú"),
    ("Tiger", "虎", "Hǔ"),
    ("Rabbit", "兔", "Tù"),
    ("Dragon", "龍", "Lóng"),
    ("Snake", "蛇", "Shé"),
    ("Horse", "馬", "Mǎ"),
    ("Goat", "羊", "Yáng"),
    ("Monkey", "猴", "Hóu"),
    ("Rooster", "雞", "Jī"),
    ("Dog", "狗", "Gǒu"),
    ("Pig", "豬", "Zhū")
]

animal, chinese, pinyin = zodiac[(year - 4) % 12]

print("Your Chinese Zodiac sign is", animal, chinese, "/", pinyin)