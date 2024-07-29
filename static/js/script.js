// home.html

// カテゴリ選択
document.addEventListener('DOMContentLoaded', function() {
    // カテゴリボタンと投稿コンテナ、すべての投稿を取得
    const categoryButtons = document.querySelectorAll('.category-btn');
    const postsContainer = document.getElementById('posts-container');
    const posts = postsContainer.querySelectorAll('.post');

    // 投稿をフィルタリングする関数
    function filterPosts(category) {
        // 投稿コンテナを一時的に透明にする
        postsContainer.style.opacity = '0';
        
        // アニメーションフレームをリクエスト
        requestAnimationFrame(() => {
            // 各投稿に対してフィルタリングを適用
            posts.forEach(post => {
                if (category === 'all' || post.dataset.category === category) {
                    post.style.display = 'block'; // カテゴリが一致する場合、表示
                } else {
                    post.style.display = 'none';  // カテゴリが一致しない場合、非表示
                }
            });

            // 投稿コンテナを再び表示する
            requestAnimationFrame(() => {
                postsContainer.style.opacity = '1';
            });
        });
    }

    // 各カテゴリボタンにクリックイベントリスナーを追加
    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            // すべてのボタンから'active'クラスを削除
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            // クリックされたボタンに'active'クラスを追加
            this.classList.add('active');
            // クリックされたボタンのカテゴリでフィルタリング関数を呼び出す
            filterPosts(this.dataset.category);
        });
    });
});

