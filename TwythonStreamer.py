from twython import TwythonStreamer
#データを大域変数に格納するのは稚拙な手法ではあるが、サンプルコードを単純にできる
tweets = []
class MyStreamer(TwythonStreamer):
    #streamとやり取りを行う方法を定義するTwythonStreamerのサブクラス
    
    def on_success(self, data):
        #Twitterがデータを送ってきたらどうするか。ここでdataは投稿を表すPythonのライブラリとして渡される
        
        #えいごのTweetのみを対称とする
        if data['lang'] == 'en':
            tweets.append(data)
            print("received tweet #" , len(tweets))
            
        #十分なTweetが得られたら終了
            if len(tweets) >= 1000:
                self.disconnect()
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

stream = MyStreamer('NX1NKZj0c1tGLZ4Pqryrl39Hn', 'MRJVTQRidcRlqqtSs3UOcoKUcJOc2r5Pz8Fg42b3d5TUVj0Thc','774361264839467009-aPxDmI2ylS4QOeGSFbqQdWqoUVMBeNp', 'An5JNKy1UXhnz2mUjyZrsI4QC6dTbMk38gOFKVd451DBi')
#公開されているツイート(statuses)からキーワード'data'を持つものを収集する
stream.statuses.filter(track='data')

from collections import Counter
top_hashtags = Counter(hashtag['text'].lower()
                      for tweet in tweets
                      for hashtag in tweet["entities"]["hashtags"])
print(top_hashtags.most_common(5))

if 