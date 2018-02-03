import random


def select_photo():
    photo_list = [
        "https://d3ndb5jjirqkbj.cloudfront.net/wp/wp-content/uploads/2016/01/honyomi001_img01.jpg",
        "https://d3bhdfps5qyllw.cloudfront.net/org/82/820a49238d405ab5abfd92538a381cb4_1080x1339_h.jpg",
        "https://www.suruga-ya.jp/database/pics/game/g3333021.jpg",
        "https://www.suruga-ya.jp/database/pics/game/g3333021.jpg"
    ]

    return photo_list[random.randint(0, 3)]
