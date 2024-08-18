from flask import Flask, request, redirect, render_template, session, flash
from datetime import timedelta
import hashlib
import uuid
import re

from models import dbConnect

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)

# サインアップページの表示
@app.route('/signup')
def signup():
    return render_template('/signup.html')

# サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        id = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(id, name, email, password)
            UserId = str(id)
            session['id'] = UserId
            return redirect('/')
    return redirect('/signup')

# ログインページの表示
@app.route('/login')
def login():
    return render_template('/login.html')

# ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['id'] = user["id"]
                return redirect('/')
    return redirect('/login')


# ログアウト処理
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# 映画ルーム一覧ページの表示
@app.route('/')
def index():
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    else:
        movie_records = dbConnect.getMovieRecords()
        movieroom_records = dbConnect.getMovieroomsAll()
        if movieroom_records:
            movieroom_records.reverse()
        print("app.py92",movieroom_records)
        return render_template('index.html', movies=movie_records, movierooms=movieroom_records, user_id=user_id)

# 映画ルームの作成
@app.route('/', methods=['POST'])
def addMovieroom():
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    movie_id = request.form.get('movieId')
    movieroom_record = dbConnect.getMovieRoomRecord(movie_id)
    print(102,movieroom_record)
    if movieroom_record:
        if movieroom_record["movie_id"] is None:
            dbConnect.addMovieRoom(user_id,movie_id)
        else:
            flash('すでに同じ名前の映画ルームが存在しています')
        return redirect('/')
    else:
        flash('タイトルを選択してください')
        return redirect('/')

# 映画ルームの削除
@app.route('/delete/<cid>')
def delete_channel(cid):
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    else:
        movieroom = dbConnect.getMovieRoomRecordsById(cid)
        if movieroom["user_id"] != user_id:
            flash(' 映画ルームは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            return redirect('/')
        
#メッセージ投稿画面の表示
@app.route('/chat/<cid>')
def home(cid):
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    else: 
       cid= cid
       movieroom_record = dbConnect.getMovieRoomRecordsByName(cid)
       message_records = dbConnect.getMessageAll(cid)
       print('app.py138',movieroom_record)
       print('app.py139',message_records)
       return render_template('chat.html',messages = message_records,movieroom= movieroom_record) 

#メッセージの投稿
@app.route('/message',methods=['POST'])
def addMessage():
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')

    else:
        message = request.form.get('message')
        movieroom_id = request.form.get('movieroom_id')

    # if not message or message.isspace():
    #     flash('メッセージが空です。') 
    if message:
        dbConnect.createMessage(user_id,movieroom_id,message)


    # else:
    #     dbConnect.createMessage(user_id, cid, message)
       
    return redirect('/chat/{movieroom_id}'.format(movieroom_id = movieroom_id))

#メッセージの削除
@app.route('/delete_message',methods =['POST'])
def delete_message():
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    
    message_id = request.form.get('message_id')
    movieroom_id = request.form.get('movieroom_id')
    if message_id:
        dbConnect.deleteMessage(message_id)

    return redirect('/chat/{movieroom_id}'.format(movieroom_id=movieroom_id)) 
    



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)