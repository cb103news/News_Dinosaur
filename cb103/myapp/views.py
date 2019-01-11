from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Avg
from myapp.models import PollOption,Poll,AnalysisItem,ArticleEmotion,ArticleKeyword,Author,AuthorWrite,Keyword,Label,News,NewsEmotionScore,Origin,Poll,PollOption,Tldr,TldrComment,TldrEmotionScore,TldrKeyword,TldrNews,UserAction,UserBehavior,UserNewsComment,UserNewsReviseAdvice,Users
import datetime
import requests
import json
def lazybox(request):
    return render(request,"lazybox.html")
   		
def newspaper(request):
    return render(request,"newspaper.html")
	
def KeyWord2(request):
    return render(request,"KeyWord2.html")
	
def Newcheck(request):
    return render(request,"Newcheck.html")

def post(request):
    Endpoint='http://localhost:5001/seven_days_kwyword/'
    response=requests.get(Endpoint)
    kw = response.json()
    keyword = []
    for k in kw[:5]:
      keyword.append(k)
    k1 = keyword[0]
    k2 = keyword[1]
    k3 = keyword[2]
    k4 = keyword[3]
    k5 = keyword[4]
    return render(request, "keywordsearch.html", locals())
	
def post2(request):		
    mess = request.GET['username'] #取得表單輸入資料
    news = News.objects.filter(articlekeyword__keyword__keyword__icontains=mess)
    keywords = Keyword.objects.filter(keyword__icontains=mess)
    Endpoint='http://localhost:5001/Keyword/'+ str(mess)
    response=requests.get(Endpoint)
    kw = response.json()
    return render(request, "KeyWord2.html", locals())

def post3(request,username):
    one = News.objects.get(title_id=username)
    title_id = News.objects.get(title_id=username).title_id
    time = News.objects.get(title_id=username).release_datetime
    origin = Origin.objects.get(news__title_id=username)
    pic = News.objects.get(title_id=username).img_url
    kewordss = Keyword.objects.filter(articlekeyword__title__title_id=username)
    labelc = Label.objects.get(news__title_id=username).label
    author = Author.objects.filter(authorwrite__title__title_id=username)
    colors = AnalysisItem.objects.all()
    url = News.objects.get(title_id=username).url
    avg1 = NewsEmotionScore.objects.filter(title__title_id=username).aggregate(Avg('emotion_score'))
    avg = avg1['emotion_score__avg']
    comments = UserNewsComment.objects.filter(title__title_id=username)

    if request.method == "POST" and 'button1' in request.POST:
        user = Users.objects.get(user_id='123')
        title = News.objects.get(title_id=username)
        score_time = datetime.datetime.now()
        emotion_score = request.POST['e_score']
        unit = NewsEmotionScore.objects.create(user=user, title=title, score_time=score_time, emotion_score=emotion_score) 
        unit.save()               
    if request.method == "POST" and 'button2' in request.POST:
        user = Users.objects.get(user_id='123')
        title = News.objects.get(title_id=username)
        comment_time = datetime.datetime.now()
        user_comment = request.POST['user_comment']
        unit = UserNewsComment.objects.create(user=user, title=title, comment_time=comment_time, user_comment=user_comment)
        unit.save()
    if request.method == "POST" and 'button3' in request.POST:
        user = Users.objects.get(user_id='123')
        title = News.objects.get(title_id=username)
        advice_time = datetime.datetime.now()
        revise_advice = request.POST['advice']
        choice = request.POST['choice']
        analysis_item = AnalysisItem.objects.get(analysis=choice)
        unit = UserNewsReviseAdvice.objects.create(user=user, title=title,advice_time=advice_time,revise_advice=revise_advice,analysis_item=analysis_item )
        unit.save()
    else:
	    message = "請重新輸入"
    return render(request, "newspaper.html", locals())
	
def post4(request,username):
    news = News.objects.filter(articlekeyword__keyword__keyword__icontains=username)
    keywords = Keyword.objects.filter(keyword__icontains=username)
    keywords = Keyword.objects.filter(keyword__icontains=username)
    Endpoint='http://localhost:5001/Keyword/'+ str(username)
    response=requests.get(Endpoint)
    kw = response.json()
    return render(request, "KeyWord3.html", locals())
	
def post5(request,username):
    name = Tldr.objects.get(tldr_id__contains=username).tldr_name
    content = Tldr.objects.get(tldr_id__contains=username).tldr_content
    hp = Tldr.objects.get(tldr_id__contains=username).heat_map_content
    em = Tldr.objects.get(tldr_id__contains=username).emotion_map_content
    kewordss = Keyword.objects.filter(tldrkeyword__tldr__tldr_id__contains=username)
    news = News.objects.filter(tldrnews__tldr__tldr_id__contains=username)
    avg1 = TldrEmotionScore.objects.filter(tldr__tldr_id__contains=username).aggregate(Avg('tldr_emotion_score'))
    avg = avg1['tldr_emotion_score__avg']
    comments = TldrComment.objects.filter(tldr__tldr_id__contains=username)
    heat = Tldr.objects.get(tldr_id__contains=username).heat_map_url
    emotion = Tldr.objects.get(tldr_id__contains=username).emotion_map_url
    if request.method == "POST" and 'button1' in request.POST:
        user = Users.objects.get(user_id='123')
        tldr = Tldr.objects.get(tldr_id__contains=username)
        tldr_score_time = datetime.datetime.now()
        tldr_emotion_score = request.POST['ne_score']
        unit = TldrEmotionScore.objects.create(user=user, tldr=tldr, tldr_score_time=tldr_score_time, tldr_emotion_score=tldr_emotion_score) 
        unit.save()
		
    if request.method == "POST" and 'button2' in request.POST:
        user = Users.objects.get(user_id='123')
        tldr = Tldr.objects.get(tldr_id__contains=username)
        tldr_comment_time = datetime.datetime.now()
        user_tldr_comment = request.POST['tldr_comment']
        unit = TldrComment.objects.create(user=user, tldr=tldr, tldr_comment_time=tldr_comment_time, user_tldr_comment=user_tldr_comment)
        unit.save()
    else:
        message = "請重新輸入"
    return render(request, "lazybox.html", locals())

def post6(request):
    titles = Poll.objects.all()
    return render(request, "vote.html", locals())

def post7(request,username):
    title = Poll.objects.get(poll_id=username)
    polls = PollOption.objects.filter(poll_id=username).order_by('-vote_tally')
    return render(request, "vote2.html", locals())

def post8(request):
    if request.method == "POST" and 'button2' in request.POST:
        user_comment = request.POST['user_comment']
        Endpoint='http://localhost:5001/get_elastic/'
        word = {
            'text': user_comment
        }
        Header={'Content-Type':'application/json'}
        Response=requests.post(Endpoint,headers=Header,data=json.dumps(word))            
        title_list = Response.json()
        lists = []
        for i in title_list:
            i = News.objects.get(title_id=i)
            lists.append(i)
    return render(request, "Newcheck.html", locals())

