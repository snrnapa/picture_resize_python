import os
import glob
from PIL import Image

print("""

このプログラムは、exeファイルと同フォルダに入っている画像を一括でリサイズし、フォルダを作成するプログラムです
画像が入ってなくても最後までエラーは出ませんが、動作はしておりませんのでご確認お願いします。

--------------作成するフォルダの名前を決めてください----------------------------------------

""")


folder_name = input("folder name：")

print("""


------------------Sample Date--------------------------------

----------------------Twitter----------------------------------

【対応・推奨画像】
拡張子：JPEG／GIF／PNG

推奨サイズ
・プロフィールアイコン：400px×400px
・ヘッダー：1500px×500px
※上下60pxが切れて表示されることがあります。
・投稿用：1280px×720px　または　1920px×1080px

容量
・プロフィールのアイコン／ヘッダー：2MB以下
・投稿用：5MB以下

----------------------Instagram----------------------------------


【対応・推奨画像】
拡張子：JPEG／GIF／PNG
推奨サイズ
・ プロフィールアイコン：300～400px程度の正方形
・投稿用

正方形：1080px×1080px
横長：1080px×566px
縦長：1080px×1350px


----------------------Facebook----------------------------------


【対応・推奨画像】
拡張子：JPEG／GIF／PNG ／BPM／TIFF
推奨サイズ
・ プロフィールアイコン ：170px×170px以上の正方形(PNG推奨)
・カバー： 851px×315px
・投稿用：幅2048px以内
容量
・ プロフィールアイコン ：100KB以下なら読み込みが速い
・投稿用：15MB以内、PNGは1MB未満推奨



""")



print("""

--------------------------横のサイズを決めてください：：：元画像と同じ比率でリサイズします-------------------


""")

width = input("picture width：")
os.mkdir(str(folder_name))
files = glob.glob('*.jpg')




for f in files:
    img = Image.open(f)
    height = round(int(img.height) * int(width) / int(img.width))
    # img.resize((width, height))
    # img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
    img_resize = img.resize((int(width), int(height)))
    title, ext = os.path.splitext(f)#パスからファイル名を取得
    img_resize.save("./" + folder_name + "/" + title + str(width) + "×" + str(height) + ext)

