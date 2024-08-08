from util.DB import DB

class dbConnect:
    def createUser(id, name, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (id, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (id, name, email, password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
        finally:
            cur.close()


    def getMoviesAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM movies;"
            #execute()でsqlの実行
            cur.execute(sql)
            #fetchallで全件取得
            movies = cur.fetchall()
            #保存する
            # conn.commit()
            return movies
        
        except Exception as e:
            print(e +'が発生しています')
        finally:
            cur.close()
