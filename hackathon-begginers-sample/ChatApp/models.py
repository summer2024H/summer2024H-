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

    def getMovieRoomRecord(movie_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.id,m.movie_title,mr.movie_id FROM movies AS m LEFT JOIN movierooms AS mr ON m.id = mr.movie_id WHERE m.id='%s';"
            cur.execute(sql,int((movie_id)))
            movieroom_record = cur.fetchone()
            return movieroom_record
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
