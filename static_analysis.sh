# 静的解析結果を出力するファイルを削除する
rm -rf pycodestyle.csv
rm -rf pylint.csv

# 静的解析結果を出力するファイルを新規作成
touch pycodestyle.csv
touch pylint.csv

# pycodestyleを実行
echo "line error message" > pycodestyle.csv
pycodestyle main.py 1>> pycodestyle.csv 2> pycodestyle_error.txt
if [ $(wc -l pycodestyle.csv | awk {'print $1'}) == '1' ]; then
    cp /dev/null pycodestyle.csv
fi

# pylintを実行
pylint main.py 1>> pylint.csv 2> pylint_error.txt
if [ $(wc -l pylint.csv | awk {'print $1'}) == '4' ]; then
    cp /dev/null pylint.csv
fi

# pycodestyle結果を出力
if [ ! -s pycodestyle.csv ]; then
    echo "pycodestyle success!!!"
else
    echo "pycodestyle failed. please check code."
    cat pycodestyle.csv
fi

# pylint結果を出力
if [ ! -s pylint.csv ]; then
    echo "pylint success!!!"
else
    echo "pylint failed. please check code."
    cat pylint.csv
fi


