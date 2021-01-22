from googleapiclient.discovery import build


# APIキーとAPIで使うサービスとAPIのバージョン
DEVELOPER_KEY = "AIzaSyA9EJqdzvKnuPkIQGZcshMZDn_NTIiKRpY" 
YOUTUBE_API_SERVICE_NAME = "youtube" 
YOUTUBE_API_VERSION = "v3" 

def get_videos_search(key_word):
    youtube = build(YOUTUBE_API_SERVICE_NAME, 
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    youtube_query = youtube.search().list(q=key_word,
                                          part='id,snippet',
                                          maxResults=1)
    # print(f'*'*70)
    youtube_res = youtube_query.execute()
    # print(youtube_res)
    # print(f'*'*70)
    return youtube_res.get('items', [])


"""
要件1：欲しい分野の動画が投稿された時、その動画を取得する。
要件2：
"""
def get_latest_interesting_video(key_word):
    result = get_videos_search(key_word=key_word)
    
    for item in result:
        if item['id']['kind'] == 'youtube#video':
            print(f'*'*70)
            print(item['snippet']['title'])
            print('https://www.youtube.com/watch?v=' + item['id']['videoId'])


if __name__ == '__main__':
    key_word = 'bitcoin'
    get_latest_interesting_video(key_word)


