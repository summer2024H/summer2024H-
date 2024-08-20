const loadMovieRooms = () => {
  const ul = document.querySelector('.channel-box');
  movierooms.forEach((movieroom) => {
    /* const a_title = document.createElement('a'); */
    const a_img = document.createElement('a');
    const li = document.createElement('li');
    const movieroomURL = `/chat/${movieroom['mr.id']}`;

    // movieroomのmovie_idと同じ属性と同じ属性値を持つ要素の画像パスを変更する
    const imgElement = document.getElementById(movieroom.id);
    const parentDiv = imgElement.parentElement;
    imgElement.src = `/static/img/${movieroom.id}.jpg`; // 新しい画像パスを指定

    a_img.setAttribute('href', movieroomURL);
    // imgタグの要素をクローンしてaタグの子要素に追加
    a_img.appendChild(imgElement.cloneNode(true));
    // imgタグを削除
    parentDiv.removeChild(imgElement);
    // 削除したimgタグの親要素に子要素としてaタグを追加
    parentDiv.appendChild(a_img);

    // もしチャンネル作成者user_idと自分のuser_idが同じだった場合は削除ボタンを追加
    if (user_id === movieroom.user_id) {
      const a_button = document.createElement('a');
      const deleteButton = document.createElement('button');
      const movieroomURL = `/delete/${movieroom.id}`;
      deleteButton.innerHTML = '削除';
      deleteButton.classList.add('delete-button');
      a_button.setAttribute('href', movieroomURL);
      parentDiv.appendChild(a_button);
      a_button.appendChild(deleteButton);
    }
  });
};

loadMovieRooms();
