# csvをFirestoreにインポートする
# cred:Firestoreの秘密鍵のファイル名
# csvdata:インポートするファイル名
# firestoreData:Firestoreに登録する項目。CSVの項目はdata[i]で指定する。
# db.collection~は、登録するコレクションに合わせて変更すること

import csv
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate(u'C:/Users/eby/pastQuestionDataImport/serviceAccountKey.json')  # FIrestoreの秘密鍵の設定
app = firebase_admin.initialize_app(cred)  # Firebase初期化
db = firestore.client()  # Firestore使用宣言

csvdata = 'C:/Users/eby/pastQuestionDataImport/testQuestion.csv'  # CSVファイル名の定義

with open(csvdata) as f:  # CSVファイルオープン
    reader = csv.reader(f)  # CSVから1レコード読み出し
    header = next(reader)  # Header行読み飛ばし
    
    for data in reader:  # 1レコード分の処理
        firestoreData = {  # Firestoreのドキュメントの項目セット
            u'_id': data[0],
            u'question': data[1],
            u'currentAnswer': data[2],
            u'choicesType': data[3],
            u'choicesVolume': data[4],
            u'lastCorrectDate': data[5],
            u'correctCount': data[6],
            u'incorrectCount': data[7],
            u'commentary': data[8],
            u'createdAt': data[9]
        }
        db.collection('1').document(data[0]).set(firestoreData)  # CSVの1列目をドキュメント名としてデータ登録

