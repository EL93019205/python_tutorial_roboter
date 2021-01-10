# import
import os
import csv

# 変数宣言
restaurants=[]
is_find_fav=False
is_find_already_restaurant_name=False
person_name=''
is_find_already_restaurant_name=''

# restaurant.csvが存在する？
if os.path.exists('restaurants.csv'):
	# restaurants.csvファイルを読み込む
	with open('restaurants.csv', 'r') as c:
		r=csv.DictReader(c)
		# csvから読み取った値をリスト型辞書に置き換える
		restaurants=[restaurant for restaurant in r]
		# リスト型辞書をCountでソートする
		restaurants=sorted(restaurants, key=lambda x:x['Count'], reverse=True)

# 名前を入力して貰う
print('名前を入力してください')
person_name=input()

#restaurantsが空でない？
if any(restaurants):
	for i, restaurant in enumerate(restaurants):
		print(restaurant['Name']+'は好きですか？[y/n]')
		while True:
			yn=input()
			if yn == 'y':
				break
			if yn == 'yes':
				yn='y'
				break
			if yn == 'Yes':
				yn='y'
				break
			if yn == 'Y':
				yn='y'
				break
			if yn == 'n':
				break
			if yn == 'no':
				break
			if yn == 'No':
				break
		if yn=='y':
			restaurants[i]['Count']=str(int(restaurants[i]['Count'])+1)
			is_find_fav=True
			break

# お気に入りのレストランが無い場合はお気に入りのレストランを聞く
if not is_find_fav:
	print("どこのレストランが好きですか？")
	restaurant_name=input()
	restaurant_name=restaurant_name.title()
	# 既にあるレストラン名であればカウントを1増やす
	for	i, restaurant in enumerate(restaurants):
		if restaurant['Name'] == restaurant_name:
			restaurants[i]['Count']=str(int(restaurants[i]['Count'])+1)
			is_find_already_restaurant_name = True
			break
	# 新規レストラン名であれば追加する
	if not is_find_already_restaurant_name:
		restaurants.append({'Name':restaurant_name, 'Count':'1'})	
# レストランのお気に入り順にソートする
restaurants=sorted(restaurants, key=lambda x:x['Count'], reverse=True)

# 結果を保存
with open('restaurants.csv', 'w') as c:
	fieldnames=['Name','Count']
	w=csv.DictWriter(c,fieldnames=fieldnames)
	w.writeheader()
	for restaurant in restaurants:
		w.writerow(restaurant)

# お礼
print(person_name+'さんありがとうございました！')



