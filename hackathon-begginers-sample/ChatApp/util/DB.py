import pymysql

#pythonとmysqlを繋げるインターフェイス.pymysqlを使用してinit.sqlとを繋げてる
class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host ="db",
            db ="chatapp",
            user ="testuser",
            password ="testuser",
            port =3306,  #ポート番号追加
            charset ="utf8",
            #辞書形式で結果を取得するようにするオプション。
            cursorclass =pymysql.cursors.DictCursor
            )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
