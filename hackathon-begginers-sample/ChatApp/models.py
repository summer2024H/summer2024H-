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
            print(e)
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
            print(e)
        finally:
            cur.close()

    def getMovieRecords():
        try:
            # データベースに接続
            conn = DB.getConnection()
            cur = conn.cursor()
            # データを取得
            sql = "SELECT * FROM movies;"
            cur.execute(sql)
            movie_records = cur.fetchall()
            return movie_records
        except Exception as e:
            print(e)
        finally:
            # 接続を閉じる
            cur.close()
    
    def showMovieRoomAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.movie_title,mr.id FROM movierooms AS mr JOIN movies AS m ON mr.movie_id=m.id;"
            cur.execute(sql)
            movierooms_all = cur.fetchall()
            print('53',movierooms_all)
            return movierooms_all
        except Exception as e:
            print(e)
        finally:
            # 接続を閉じる
            cur.close()

    def getMovieRoomRecord(movie_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.id,m.movie_title,mr.movie_id FROM movies AS m LEFT JOIN movierooms AS mr ON m.id = mr.movie_id WHERE m.id='%s';"
            cur.execute(sql,int((movie_id)))
            movieroom_record = cur.fetchone()
            print('53',movieroom_record)
            return movieroom_record
        except Exception as e:
            print(e)
        finally:
            cur.close()

    def getMovieRoomBYId(mr_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM movierooms WHERE id=%s;"
            cur.execute(sql,(mr_id))
            movieroom= cur.fetchone()
            print('82',movieroom)
            return movieroom
        except Exception as e:
            print(e)
        finally:
            cur.close()

    def addMovieRoom(user_id,movie_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO movierooms (user_id, movie_id) VALUES (%s, %s);"
            cur.execute(sql, (user_id, int(movie_id)))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()

   #映画ルーム削除
    def deleteMovieRoom(mr_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM movierooms WHERE id=%s;"
            cur.execute(sql,(mr_id))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
