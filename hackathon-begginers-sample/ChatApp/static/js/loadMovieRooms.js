const loadMovieRooms = () => {
  const ul = document.querySelector('.channel-box');
  ul.innerHTML = '';
  movierooms.forEach((movieroom) => {
    const a_title = document.createElement('a');
    const li = document.createElement('li');
    const movieroomURL = `/detail/${movieroom.id}`;
    a_title.innerText = movieroom.movie_title;
    a_title.setAttribute('href', movieroomURL);
    li.appendChild(a_title);
    ul.appendChild(li);

    // もしチャンネル作成者user_idと自分のuser_idが同じだった場合は削除ボタンを追加
    if (user_id === movieroom.user_id) {
      const a_button = document.createElement('a');
      const deleteButton = document.createElement('button');
      const movieroomURL = `/delete/${movieroom.id}`;
      deleteButton.innerHTML = '削除';
      deleteButton.classList.add('delete-button');
      a_button.setAttribute('href', movieroomURL);
      li.appendChild(a_button);
      a_button.appendChild(deleteButton);
    }
  });
};

loadMovieRooms();
