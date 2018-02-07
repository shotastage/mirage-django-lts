# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import random


def select_photo():
    photo_list = [
        "https://d3ndb5jjirqkbj.cloudfront.net/wp/wp-content/uploads/2016/01/honyomi001_img01.jpg",
        "https://d3bhdfps5qyllw.cloudfront.net/org/82/820a49238d405ab5abfd92538a381cb4_1080x1339_h.jpg",
        "https://www.suruga-ya.jp/database/pics/game/g3333021.jpg",
        "https://i.ytimg.com/vi/Im0I4Zs-n3E/maxresdefault.jpg",
        "https://d3ndb5jjirqkbj.cloudfront.net/wp/wp-content/uploads/2016/01/honyomi001_topimage.jpg"
    ]

    return photo_list[random.randint(0, len(photo_list) - 1)]
