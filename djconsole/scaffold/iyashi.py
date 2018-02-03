import random


def select_photo():
    photo_list = [
        "https://d3ndb5jjirqkbj.cloudfront.net/wp/wp-content/uploads/2016/01/honyomi001_img01.jpg",
        "",
        "",
        ""
    ]

    return photo_list[random.randint(0, 3)]
