from flask import Flask, request, jsonify
import datetime
import pymysql

#增加等待時間，為了整合的需要所新增的 
#import time
#time.sleep( 100 )

#呼叫出Flask
app = Flask(__name__)


#建立與mysql的連線
conn = pymysql.connect(host='db', port=3306, user='root', passwd='iii', db='chatbot_db',charset='utf8mb4')

#方便用來跟mysql互動
cur = conn.cursor()


# 存入新聞
@app.route('/news',methods=['POST'])
def add_news():
    
    # 取得新聞資料
    news = request.get_json()
    
    # 定義錯誤資訊
    error = None
    
    # 檢查新聞是否重複
    cur.execute('SELECT title_id FROM chatbot_db.News WHERE url = ("%s")' % (news['url']))
    title_id = cur.fetchone() 
    if not title_id == None :
        error = 'News {} is exist.'.format(news['url'])
    
    
    #若無重複
    if error == None:
    
        # 定義儲存時間
        store_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 從DB取出來源id
        cur.execute('SELECT origin_id FROM chatbot_db.Origin WHERE origin = ("%s")' % (news['source']))
        origin_id = cur.fetchone() 
        
        # 確認新聞來源是否存在，若不存在存入新聞來源
        if origin_id == None:
        
            # 存入來源
            insertsql ='INSERT INTO chatbot_db.Origin (origin) VALUES (%s)'
            value = (news['source'])
            cur.execute(insertsql , value)
            conn.commit()
            
            # 取出剛存入的新聞來源
            cur.execute('SELECT origin_id FROM chatbot_db.Origin WHERE origin = ("%s")' % (news['source']))
            origin_id = cur.fetchone() 
        
        # 從DB取出標籤id
        cur.execute('SELECT label_id FROM chatbot_db.Label WHERE label = ("%s")' % (news['label']))
        label_id = cur.fetchone()
        
        # 從DB取出情緒id
        cur.execute('SELECT article_emotion_id FROM chatbot_db.Article_Emotion WHERE ariticle_emotion = ("%s")' % (news['ariticle_emotion']))
        article_emotion_id = cur.fetchone()
        
        # 存入新聞資料
        insertsql= "INSERT INTO chatbot_db.News (origin_id, label_id, article_emotion_id, title,url, release_datetime, content, abstract, img_url, store_datetime) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s )" 
        value =( origin_id, 
                 label_id, 
                 article_emotion_id,
                 news['title'],
                 news['url'],
                 news['date_'],
                 news['content'],
                 news['abstract'],
                 news['img_url'],
                 store_datetime
        )
        
        cur.execute(insertsql , value)
        #將資料送進資料庫中
        conn.commit()
        
        # 找出剛存入的新聞 title_id
        cur.execute('SELECT title_id FROM chatbot_db.News WHERE url = ("%s")' % (news['url']))
        title_id = cur.fetchone()
        
        # 存入記者資料
        if not news['author'] == []:
            author_list = news['author']
            for author in author_list:

                # 檢查記者是否存在資料庫
                cur.execute('SELECT author_id FROM chatbot_db.Author WHERE author = ("%s")' % (author))
                author_id = cur.fetchone()

                # 若不存在則先存入記者並取出 author_id
                if author_id == None:
                    insertsql= "INSERT INTO chatbot_db.Author (author) VALUES (%s)"
                    value = (author)
                    cur.execute(insertsql , value)
                    conn.commit()

                    cur.execute('SELECT author_id FROM chatbot_db.Author WHERE author = ("%s")' % (author))
                    author_id = cur.fetchone()

                # 將記者資訊存入DB
                insertsql= "INSERT INTO chatbot_db.Author_Write (title_id,author_id) VALUES (%s, %s)"
                value = (title_id,author_id)
                cur.execute(insertsql , value)
                conn.commit()

        # 存入 keyword
        if not news['kw'] == []:
        
            keyword_list = news['kw']
            for keyword in keyword_list:

                # 檢查關鍵字是否存在資料庫
                cur.execute('SELECT keyword_id FROM chatbot_db.Keyword WHERE keyword = ("%s")' % (keyword))
                keyword_id = cur.fetchone()

                # 若不存在則先存入關鍵字並取出 keyword_id
                if keyword_id == None:
                    insertsql= "INSERT INTO chatbot_db.Keyword (keyword) VALUES (%s)"
                    value = (keyword)
                    cur.execute(insertsql , value)
                    conn.commit()

                    cur.execute('SELECT keyword_id FROM chatbot_db.Keyword WHERE keyword = ("%s")' % (keyword))
                    keyword_id = cur.fetchone()

                # 將關鍵字資訊存入DB
                insertsql= "INSERT INTO chatbot_db.Article_Keyword (title_id,keyword_id) VALUES (%s, %s)"
                value = (title_id,keyword_id)
                cur.execute(insertsql , value)
                conn.commit()

        #回傳一個正確的描述
        result =  { "status_describe":"success add News"}

    # 若有重複,回傳存在資訊
    else:

         result = {"status_describe":"{}".format(error)}

    return jsonify(result)



# 存入使用者
@app.route('/users', methods = ['POST'])
def add_user():

    # 定義儲存時間
    join_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    users = request.get_json()

    error = None

    cur.execute('SELECT display_name FROM chatbot_db.Users WHERE user_id = ("%s")' % (users['user_id']))
    display_name = cur.fetchone()

    # 檢查id是否重複
    if not display_name == None:
        # 若重複給予錯誤訊息
        error = 'User {} {} is already registered.'.format(users['user_id'], display_name)

        #製作一個錯誤的描述
        result = {"status_describe":"{}".format(error)}

        #回傳一個錯誤的描述
        return jsonify(result)	
    else:
        # 建查 user_id 是否存在
        if users['user_id'] == None:
            error = 'The user_id of user is None !'
            result = {"status_describe":"{}".format(error)}

        # 檢查 display_name 是否存在
        elif users['display_name'] == None:
            error = 'The display_name of user is None !'
            result = {"status_describe":"{}".format(error)}

        else:

            # 將使用者資料存入
            insertsql=("INSERT INTO chatbot_db.Users (user_id, display_name, picture_url, status_message, join_datetime) VALUES ( %s,%s,%s,%s,%s )") 
            value = (users['user_id'],
                     users['display_name'],
                     users['picture_url'],
                     users['status_message'],
                     join_datetime)

            cur.execute(insertsql , value)

            #將資料送進資料庫中
            conn.commit()

            # 傳回正確訊息 
            result =  { "status_describe":"success add user" }

    return jsonify(result)



# 取出所有id
@app.route('/users_id', methods= ['GET'])
def get_all_users():
    
    # 取出所有user_id
    cur.execute('SELECT user_id FROM chatbot_db.Users')

    # 取出多筆資料
    all_user_id = cur.fetchall()
    print('all_user_id: ',all_user_id)
    users = []
    for user in all_user_id:
        users.append(user[0])

    return jsonify(users)


#接口功能：檢視指定使用者資訊
#接口位置：/users/<userid>，運用了url parameter，使用get的http method
@app.route('/users/<user_id>',methods=['GET'])
#特別注意這邊有打userid，url parameter就是這樣使用
def read_user(user_id):
    #找出資料庫符合userid的資料
    cur.execute(
        'SELECT * FROM chatbot_db.Users WHERE user_id = ("%s")' % (user_id)
        )
    #將剛剛execute的資料取出來
    user = cur.fetchone()
    #假如有找到符合的資料，包裝成統一格式並回傳
    if user is not None:
        user = {
            "user_id":user[0],
            "display_name":user[1],
            "picture_url" : user[2],
            "status_message" : user[3],
            "join_datetime" : user[4],
        }
        #轉成line要的json格式
        return jsonify(user)
    #假如沒有找到符合的資料，回傳一個錯誤訊息
    else:
        result = {
            "status_describe":"Please enter the right id!!"
        }
        return jsonify(result)


#接口功能：檢視所有使用者資訊
#接口位置：/users，使用get的http method
@app.route('/users',methods=['GET'])
def read_users():
    #找出資料庫內的所有user資料
    cur.execute(
        'SELECT * FROM chatbot_db.Users'
        )
    #由於是多筆，使用fetchall
    user = cur.fetchall()
    #假如一個user都沒
    if not user:
        answer = {
          "status_describe":"query string is incompatible"
        }
    else:
        #裝成矩陣格式
        answer = []
        for i in user:
            result = {
                "user_id":i[0],
                "display_name":i[1],
                "picture_url" : i[2],
                "status_message" : i[3],
                "join_datetime" : i[4]
            }
            answer.append(result)
    
        
    #轉成json格式
    return jsonify(answer)



# 利用title取出新聞關鍵字
@app.route('/keyword_title/<title>', methods= ['Get'])
def get_keyword_by_title(title):
    
    cur.execute(
        'SELECT title_id FROM chatbot_db.News WHERE title = ("%s")' % (title)
    )
    title_id = cur.fetchone()
    answer = None
    if title_id == None:
        answer = {
            "This title : {} can't find" .format(title)
        }
    else:
        cur.execute(
            'SELECT keyword FROM chatbot_db.Article_Keyword JOIN chatbot_db.Keyword ON Article_Keyword.keyword_id = Keyword.keyword_id WHERE title_id = ("%s") ' % (title_id[0])
        )
        answer = []
        all_keyword = cur.fetchall()

        for k in all_keyword:
            answer.append(k[0])

    return jsonify(answer)


# 利用url, 取出所有關鍵字
@app.route('/keyword_url/', methods= ['POST'])
def get_keyword_by_url():
    
    news_url= request.get_json()
    url = news_url['url']
    cur.execute(
        'SELECT title_id FROM chatbot_db.News WHERE url = ("%s")' % (url)
    )
    title_id = cur.fetchone()
    cur.execute(
        'SELECT keyword FROM chatbot_db.Article_Keyword JOIN chatbot_db.Keyword ON Article_Keyword.keyword_id = Keyword.keyword_id WHERE title_id = ("%s") ' % (title_id[0])
    )
    all_keyword = cur.fetchall()
    keyword = []
    for k in all_keyword:
        keyword.append(k[0])

    return jsonify(keyword)


# 利用單個關鍵字，找出相關新聞。
@app.route('/keyword/<keyword>',methods=['GET'])
def get_keyword_title(keyword):
    
    cur.execute(
        'SELECT keyword_id FROM chatbot_db.Keyword WHERE keyword = ("%s")' % (keyword)
    )
    keyword_id = cur.fetchone()

    cur.execute(
        'SELECT title FROM chatbot_db.Article_Keyword JOIN chatbot_db.News ON News.title_id = Article_Keyword.title_id WHERE keyword_id = ("%s")' % (keyword_id[0])
    )
    all_title = cur.fetchall()
    news_tltle = []
    for title in all_title:
        news_tltle.append(title[0])
    
    return jsonify(news_tltle)


# 找出近7天的所有關鍵字並依照數量排序
@app.route('/seven_days_kwyword/',methods=['GET'])
def get_seven_days_kwywords():
    
    cur.execute (
        "select title_id from chatbot_db.News where date_sub(curdate(), INTERVAL 7 DAY) <= date(release_datetime)"
    )
    all_title= cur.fetchall()
    title_list = []
    for title in all_title:
        title_list.append(title[0])

    query = '''SELECT keyword , count(title_id) as num FROM chatbot_db.Article_Keyword JOIN chatbot_db.Keyword ON Article_Keyword.keyword_id = Keyword.keyword_id 
        WHERE title_id IN (%s{}) group by keyword order by num DESC'''.format(', %s' * (len(title_list)-1))

    cur.execute(
        query % (tuple(title_list))
    )

    all_keyword= cur.fetchall()    
    keyword_list = []
    
    for keyword in all_keyword:
        keyword_list.append(keyword[0])
        
    return jsonify(keyword_list)


import logging
#參考:http://zwindr.blogspot.com/2016/08/python-logging.html
# 基礎設定
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    #製作名為my.log的檔案裝log
                    handlers = [logging.FileHandler('/home/jovyan/work/my.log', 'w', 'utf-8'),])
 
# 定義 handler 輸出 sys.stderr
console = logging.StreamHandler()
#定義要擷取的log最低等級到哪
console.setLevel(logging.DEBUG)
# 設定輸出格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# handler 設定輸出格式
console.setFormatter(formatter)
# 加入 hander 到 root logger
logging.getLogger('').addHandler(console)


#__name__ == __main__ 代表你執行這個模塊（py檔）時會成立
#假如你是被別的檔案import的話，__name__ == 檔案名稱，這個if就不會成立
if __name__=='__main__':

    #運行flask server，運行在0.0.0.0:5000
    #要特別注意假如運行在127.0.0.1的話，會變成只有本機連的到，外網無法
    app.run(host='0.0.0.0',port=5000)


