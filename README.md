# 一定間隔で自動ツイート
ツイートする文章を書いたファイルからランダムに抽出し定期的にツイートする。

# インストール
Pipenvを使っています。Pipfileはpython 3.7ですが、3.6でも動くと思います。
Pipenv install でインストール後、pipenv shellに入って動かすなり、pipenv runで動かすなり・・・です。

raspbery pi 3B+ 上で動かしています。

        Linux raspberrypi 4.19.93-v7+ #1290 SMP Fri Jan 10 16:39:50 GMT 2020 armv7l GNU/Linux


# 設定
configure.ini に twitter APIとツイートの最後に追加する文章を記載する。

        [TWITTER]
        # API
        CONSUMER_KEY =
        CONSUMER_SECRET =
        ACCESS_TOKEN =
        ACCESS_TOKEN_SECRET =
        # tweet words
        WORDS =

# コメント
色んなサイトを参考にさせていただきました。感謝。
