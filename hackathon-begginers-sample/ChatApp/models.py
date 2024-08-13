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

    def getMovieroomsAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.movie_title,mr.id,mr.user_id FROM movies AS m JOIN movierooms AS mr ON m.id = mr.movie_id;"
            cur.execute(sql)
            movieroom_records = cur.fetchall()
            return movieroom_records
        except Exception as e:
            print(e)
        finally:
            cur.close()

    def getMovieRoomRecordsById(movieroom_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM movierooms WHERE id=%s;"
            cur.execute(sql, (movieroom_id))
            movieroom_record = cur.fetchone()
            return movieroom_record
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

    def deleteChannel(movieroom_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM movierooms WHERE id=%s;"
            cur.execute(sql, (movieroom_id))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()