# StudySync

## セットアップ手順

以下の手順に従って、プロジェクトをセットアップし、実行してください。

### 前提条件

- Python 3.7以上
- pip（Pythonパッケージマネージャー）
- 仮想環境（推奨）

### インストール

1. リポジトリをクローンするか、プロジェクトファイルをダウンロードします。

2. プロジェクトディレクトリに移動します：
   ```
   cd StudySync
   ```

3. 仮想環境を作成し、有効化します（推奨）：
   ```
   python -m venv venv
   source venv/bin/activate  # Linuxの場合
   venv\Scripts\activate  # Windowsの場合
   ```

4. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

### データベースのセットアップ

1. データベースを初期化します：
   ```
   flask db init
   ```

2. 初期マイグレーションを作成します：
   ```
   flask db migrate -m "Initial migration"
   ```

3. データベースをアップグレードします：
   ```
   flask db upgrade
   ```

### アプリケーションの実行

1. Flaskアプリケーションを起動します：
   ```
   flask run
   ```

2. ブラウザで `http://localhost:5000` にアクセスして、アプリケーションを使用します。