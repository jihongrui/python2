#!/usr/bin/env python
# jihongrui@jsqix.com

from pymongo import MongoClient
from Link_mongo import link

URL = link('dbserver.cy3.cn',57017,'server','super_administrator','gab110xqgabjb110',)
link = MongoClient(URL)
DB = link.server

tab = DB.test



datas = [
    {"goods_id": 1, "cat_id": 4, "goods_name": "KD876", "goods_number": 1, "click_count": 7, "shop_price": 1388.00,
     "add_time": 1240902890},
    {"goods_id": 4, "cat_id": 8, "goods_name": "\u8bfa\u57fa\u4e9aN85\u539f\u88c5\u5145\u7535\u5668",
     "goods_number": 17, "click_count": 0, "shop_price": 58.00, "add_time": 1241422402},
    {"goods_id": 3, "cat_id": 8, "goods_name": "\u8bfa\u57fa\u4e9a\u539f\u88c55800\u8033\u673a", "goods_number": 24,
     "click_count": 3, "shop_price": 68.00, "add_time": 1241422082},
    {"goods_id": 5, "cat_id": 11, "goods_name": "\u7d22\u7231\u539f\u88c5M2\u5361\u8bfb\u5361\u5668", "goods_number": 8,
     "click_count": 3, "shop_price": 20.00, "add_time": 1241422518},
    {"goods_id": 6, "cat_id": 11, "goods_name": "\u80dc\u521bKINGMAX\u5185\u5b58\u5361", "goods_number": 15,
     "click_count": 0, "shop_price": 42.00, "add_time": 1241422573},
    {"goods_id": 7, "cat_id": 8, "goods_name": "\u8bfa\u57fa\u4e9aN85\u539f\u88c5\u7acb\u4f53\u58f0\u8033\u673aHS-82",
     "goods_number": 20, "click_count": 0, "shop_price": 100.00, "add_time": 1241422785},
    {"goods_id": 8, "cat_id": 3, "goods_name": "\u98de\u5229\u6d669@9v", "goods_number": 1, "click_count": 9,
     "shop_price": 399.00, "add_time": 1241425512},
    {"goods_id": 9, "cat_id": 3, "goods_name": "\u8bfa\u57fa\u4e9aE66", "goods_number": 4, "click_count": 20,
     "shop_price": 2298.00, "add_time": 1241511871},
    {"goods_id": 10, "cat_id": 3, "goods_name": "\u7d22\u7231C702c", "goods_number": 7, "click_count": 11,
     "shop_price": 1328.00, "add_time": 1241965622},
    {"goods_id": 11, "cat_id": 3, "goods_name": "\u7d22\u7231C702c", "goods_number": 1, "click_count": 0,
     "shop_price": 1300.00, "add_time": 1241966951},
    {"goods_id": 12, "cat_id": 3, "goods_name": "\u6469\u6258\u7f57\u62c9A810", "goods_number": 8, "click_count": 13,
     "shop_price": 983.00, "add_time": 1245297652},
    {"goods_id": 13, "cat_id": 3, "goods_name": "\u8bfa\u57fa\u4e9a5320 XpressMusic", "goods_number": 8,
     "click_count": 13, "shop_price": 1311.00, "add_time": 1241967762},
    {"goods_id": 14, "cat_id": 4, "goods_name": "\u8bfa\u57fa\u4e9a5800XM", "goods_number": 1, "click_count": 6,
     "shop_price": 2625.00, "add_time": 1241968492},
    {"goods_id": 15, "cat_id": 3, "goods_name": "\u6469\u6258\u7f57\u62c9A810", "goods_number": 3, "click_count": 8,
     "shop_price": 788.00, "add_time": 1241968703},
    {"goods_id": 16, "cat_id": 2, "goods_name": "\u6052\u57fa\u4f1f\u4e1aG101", "goods_number": 0, "click_count": 3,
     "shop_price": 823.33, "add_time": 1241968949},
    {"goods_id": 17, "cat_id": 3, "goods_name": "\u590f\u65b0N7", "goods_number": 1, "click_count": 2,
     "shop_price": 2300.00, "add_time": 1241969394},
    {"goods_id": 18, "cat_id": 4, "goods_name": "\u590f\u65b0T5", "goods_number": 1, "click_count": 0,
     "shop_price": 2878.00, "add_time": 1241969533},
    {"goods_id": 19, "cat_id": 3, "goods_name": "\u4e09\u661fSGH-F258", "goods_number": 12, "click_count": 7,
     "shop_price": 858.00, "add_time": 1241970139},
    {"goods_id": 20, "cat_id": 3, "goods_name": "\u4e09\u661fBC01", "goods_number": 12, "click_count": 14,
     "shop_price": 280.00, "add_time": 1241970417},
    {"goods_id": 21, "cat_id": 3, "goods_name": "\u91d1\u7acb A30", "goods_number": 40, "click_count": 4,
     "shop_price": 2000.00, "add_time": 1241970634},
    {"goods_id": 22, "cat_id": 3, "goods_name": "\u591a\u666e\u8fbeTouch HD", "goods_number": 1, "click_count": 15,
     "shop_price": 5999.00, "add_time": 1241971076},
    {"goods_id": 23, "cat_id": 5, "goods_name": "\u8bfa\u57fa\u4e9aN96", "goods_number": 8, "click_count": 17,
     "shop_price": 3700.00, "add_time": 1241971488},
    {"goods_id": 24, "cat_id": 3, "goods_name": "P806", "goods_number": 100, "click_count": 35, "shop_price": 2000.00,
     "add_time": 1241971981},
    {"goods_id": 25, "cat_id": 13, "goods_name": "\u5c0f\u7075\u901a\/\u56fa\u8bdd50\u5143\u5145\u503c\u5361",
     "goods_number": 2, "click_count": 0, "shop_price": 48.00, "add_time": 1241972709},
    {"goods_id": 26, "cat_id": 13, "goods_name": "\u5c0f\u7075\u901a\/\u56fa\u8bdd20\u5143\u5145\u503c\u5361",
     "goods_number": 2, "click_count": 0, "shop_price": 19.00, "add_time": 1241972789},
    {"goods_id": 27, "cat_id": 15, "goods_name": "\u8054\u901a100\u5143\u5145\u503c\u5361", "goods_number": 2,
     "click_count": 0, "shop_price": 95.00, "add_time": 1241972894},
    {"goods_id": 28, "cat_id": 15, "goods_name": "\u8054\u901a50\u5143\u5145\u503c\u5361", "goods_number": 0,
     "click_count": 0, "shop_price": 45.00, "add_time": 1241972976},
    {"goods_id": 29, "cat_id": 14, "goods_name": "\u79fb\u52a8100\u5143\u5145\u503c\u5361", "goods_number": 0,
     "click_count": 0, "shop_price": 90.00, "add_time": 1241973022},
    {"goods_id": 30, "cat_id": 14, "goods_name": "\u79fb\u52a820\u5143\u5145\u503c\u5361", "goods_number": 9,
     "click_count": 1, "shop_price": 18.00, "add_time": 1241973114},
    {"goods_id": 31, "cat_id": 3, "goods_name": "\u6469\u6258\u7f57\u62c9E8 ", "goods_number": 1, "click_count": 5,
     "shop_price": 1337.00, "add_time": 1242110412},
    {"goods_id": 32, "cat_id": 3, "goods_name": "\u8bfa\u57fa\u4e9aN85", "goods_number": 4, "click_count": 9,
     "shop_price": 3010.00, "add_time": 1242110760},
    {"cat_id": 1, "cat_name": "\u624b\u673a\u7c7b\u578b"}, {"cat_id": 2, "cat_name": "CDMA\u624b\u673a"},
    {"cat_id": 3, "cat_name": "GSM\u624b\u673a"}, {"cat_id": 4, "cat_name": "3G\u624b\u673a"},
    {"cat_id": 5, "cat_name": "\u53cc\u6a21\u624b\u673a"}, {"cat_id": 6, "cat_name": "\u624b\u673a\u914d\u4ef6"},
    {"cat_id": 7, "cat_name": "\u5145\u7535\u5668"}, {"cat_id": 8, "cat_name": "\u8033\u673a"},
    {"cat_id": 9, "cat_name": "\u7535\u6c60"}, {"cat_id": 11, "cat_name": "\u8bfb\u5361\u5668\u548c\u5185\u5b58\u5361"},
    {"cat_id": 12, "cat_name": "\u5145\u503c\u5361"},
    {"cat_id": 13, "cat_name": "\u5c0f\u7075\u901a\/\u56fa\u8bdd\u5145\u503c\u5361"},
    {"cat_id": 14, "cat_name": "\u79fb\u52a8\u624b\u673a\u5145\u503c\u5361"},
    {"cat_id": 15, "cat_name": "\u8054\u901a\u624b\u673a\u5145\u503c\u5361"}
]

send_db = tab.insert_many(datas)
send_db.inserted_ids

