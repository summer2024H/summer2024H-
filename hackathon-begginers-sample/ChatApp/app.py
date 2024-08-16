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

# デフォルト映画情報の表示
@app.route('/movierooms')
def index():
    id = session.get("id")
    if id is None:
        return redirect('/login')
    else:
        movie_records = dbConnect.getMovieRecords()
        return render_template('/index.html', movies=movie_records)

#映画ルーム一覧ページの表示
@app.route('/', methods=['GET','POST'])
def show_Movieroom():
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    if request.method == 'GET':
        movierooms_all = dbConnect.showMovieRoomAll()
        if movierooms_all:
            movierooms_all.reverse()
        return render_template('/index.html',movierooms_all = movierooms_all,user_id = user_id)
    if request.method == 'POST':
        movie_id = request.form.get('movieId')
        movieroom_record = dbConnect.getMovieRoomRecord(movie_id)
        if movieroom_record["movie_id"] is None:
           dbConnect.addMovieRoom(user_id,movie_id)
           return redirect('/')
        else:
           flash('すでに同じ名前の映画ルームが存在しています')
           return redirect('/')
    
#映画ルームの削除
@app.route('/delete/<mr_id>',methods=['POST'])
def delete_movieroom(mr_id):
    user_id = session.get("id")
    if user_id is None:
        return redirect('/login')
    else:
        movieroom = dbConnect.getMovieRoomBYId(mr_id)
        print('app.py137',mr_id)
        if movieroom["user_id"] != user_id:
            flash('チャットルームは作成者のみ削除可能です')
            return redirect('/')
        else:
            dbConnect.deleteMovieRoom(mr_id)
            return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)