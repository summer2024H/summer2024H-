/* DROP分は省略
DROP USER IF EXISTS 'testuser'@'%'; testuserがすでにある場合は削除して新たに作成する*/

DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'; /*データベース内の全ての権限をtestuserが持つ*/

CREATE TABLE users(
    id VARCHAR(255) PRIMARY KEY, /*idはuuid4によってos固有の世界で一意の数値となる*/
    user_name VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL
);

CREATE TABLE movies(
    id SERIAL PRIMARY KEY,
    movie_title VARCHAR(50) NOT NULL,
    releasedyear VARCHAR(10) NOT NULL,
    category VARCHAR(10) NOT NULL
);

/* CREATE TABLE movierooms(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL REFERENCES users(id),
    movie_id INTEGER NOT NULL REFERENCES movies(id)
); */

CREATE TABLE movierooms(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL REFERENCES users(id),
    movie_id INTEGER NOT NULL REFERENCES movies(id)
);

CREATE TABLE messages(
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL, 
    movierooms_id BIGINT UNSIGNED NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL default current_timestamp,
    updated_at TIMESTAMP NOT NULL default current_timestamp on update current_timestamp,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movierooms_id) REFERENCES movierooms(id) ON DELETE CASCADE
);

/* CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    movierooms_id BIGINT UNSIGNED NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_movierooms_id FOREIGN KEY (movierooms_id) REFERENCES movierooms(id) ON DELETE CASCADE
); */

CREATE TABLE message_reactions(
    user_id VARCHAR(255) NOT NULL REFERENCES users(id), 
    message_id INTEGER NOT NULL REFERENCES messages(id) ON DELETE CASCADE, 
    reaction_id INTEGER NOT NULL REFERENCES reactions(id)
);

CREATE TABLE reactions(
    id SERIAL PRIMARY KEY,
    reaction_type VARCHAR(255) NOT NULL
);

INSERT INTO movies(id, movie_title, releasedyear, category ) VALUES(1,'ローマの休日','1953年','恋愛');
INSERT INTO movies(id, movie_title, releasedyear, category ) VALUES(2,'ゴッドファーザー','1972年','その他');
INSERT INTO movies(id, movie_title, releasedyear, category ) VALUES(3,'タイタニック','1997年','恋愛');
INSERT INTO movies(id, movie_title, releasedyear, category ) VALUES(4,'英国王のスピーチ','2011年','その他');
INSERT INTO movies(id, movie_title, releasedyear, category ) VALUES(5,'パラサイト','2019年','その他');