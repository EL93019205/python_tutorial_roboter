"""This is a Roboter"""
import os
import csv

# 変数宣言
RESTAURANTS = []
IS_FIND_FAB = False
IS_FIND_ALREADY_RESTAURANT_NAME = False
PERSON_NAME = ''
RESTAURANT_NAME = ''
print(type(IS_FIND_FAB))
print(type(PERSON_NAME))

# restaurant.csvが存在する？
if os.path.exists('restaurants.csv'):
    # restaurants.csvファイルを読み込む
    with open('restaurants.csv', 'r') as c:
        # csvから読み取った値をリスト型辞書に置き換える
        RESTAURANTS = list(csv.DictReader(c))
        # リスト型辞書をCountでソートする
        RESTAURANTS = sorted(RESTAURANTS, key=lambda x: x['Count'],
                             reverse=True)

# 名前を入力して貰う
print('名前を入力してください')
PERSON_NAME = input()

# RESTAURANTSが空でなければ、お気に入りの多い順にお気に入りかどうかを聞く
if any(RESTAURANTS):
    for i, restaurant in enumerate(RESTAURANTS):
        print(restaurant['Name']+'は好きですか？[y/n]')
        while True:
            YN = input()
            if YN == 'y':
                break
            if YN == 'yes':
                YN = 'y'
                break
            if YN == 'Yes':
                YN = 'y'
                break
            if YN == 'Y':
                YN = 'y'
                break
            if YN == 'n':
                break
            if YN == 'no':
                break
            if YN == 'No':
                break
        # お気に入りのレストランが見つかれば聞くのを辞める
        if YN == 'y':
            RESTAURANTS[i]['Count'] = str(int(RESTAURANTS[i]['Count'])+1)
            IS_FIND_FAB = True
            break

# お気に入りのレストランが無い場合はお気に入りのレストランを聞く
if not IS_FIND_FAB:
    print("どこのレストランが好きですか？")
    RESTAURANT_NAME = input()
    RESTAURANT_NAME = RESTAURANT_NAME.title()
    # 既にあるレストラン名であればカウントを1増やす
    for i, restaurant in enumerate(RESTAURANTS):
        if restaurant['Name'] == RESTAURANT_NAME:
            RESTAURANTS[i]['Count'] = str(int(RESTAURANTS[i]['Count'])+1)
            IS_FIND_ALREADY_RESTAURANT_NAME = True
            break
    # 新規レストラン名であれば追加する
    if not IS_FIND_ALREADY_RESTAURANT_NAME:
        RESTAURANTS.append({'Name': RESTAURANT_NAME, 'Count': '1'})

# レストランのお気に入り順にソートする
RESTAURANTS = sorted(RESTAURANTS, key=lambda x: x['Count'], reverse=True)

# 結果をcsv形式で保存する
with open('restaurants.csv', 'w') as c:
    fieldnames = ['Name', 'Count']
    w = csv.DictWriter(c, fieldnames=fieldnames)
    w.writeheader()
    for restaurant in RESTAURANTS:
        w.writerow(restaurant)

# お礼
print(PERSON_NAME+'さんありがとうございました！')
