# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnalysisItem(models.Model):
    analysis_item_id = models.CharField(primary_key=True, max_length=30)
    analysis = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'Analysis_Item'


class ArticleEmotion(models.Model):
    article_emotion_id = models.CharField(primary_key=True, max_length=30)
    ariticle_emotion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Article_Emotion'


class ArticleKeyword(models.Model):
    title = models.ForeignKey('News', models.DO_NOTHING, primary_key=True)
    keyword = models.ForeignKey('Keyword', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Article_Keyword'
        unique_together = (('title', 'keyword'),)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Author'


class AuthorWrite(models.Model):
    title = models.ForeignKey('News', models.DO_NOTHING, primary_key=True)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Author_Write'
        unique_together = (('title', 'author'),)


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Keyword'


class Label(models.Model):
    label_id = models.CharField(primary_key=True, max_length=30)
    label = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Label'


class News(models.Model):
    title_id = models.AutoField(primary_key=True)
    origin = models.ForeignKey('Origin', models.DO_NOTHING)
    label = models.ForeignKey(Label, models.DO_NOTHING)
    article_emotion = models.ForeignKey(ArticleEmotion, models.DO_NOTHING)
    title = models.CharField(max_length=150)
    url = models.TextField(blank=True, null=True)
    release_datetime = models.DateTimeField()
    content = models.TextField()
    abstract = models.TextField()
    img_url = models.TextField(blank=True, null=True)
    store_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'News'


class NewsEmotionScore(models.Model):
    news_emotion_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.ForeignKey(News, models.DO_NOTHING)
    emotion_score = models.IntegerField()
    score_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'News_Emotion_Score'


class Origin(models.Model):
    origin_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Origin'


class Poll(models.Model):
    poll_id = models.AutoField(primary_key=True)
    poll_title = models.CharField(max_length=60)
    poll_img = models.TextField()

    class Meta:
        managed = False
        db_table = 'Poll'


class PollOption(models.Model):
    poll_option_id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll, models.DO_NOTHING)
    option_title = models.CharField(max_length=60)
    vote_tally = models.IntegerField()
    option_img = models.TextField()

    class Meta:
        managed = False
        db_table = 'Poll_Option'


class Tldr(models.Model):
    tldr_id = models.CharField(primary_key=True, max_length=30)
    tldr_name = models.CharField(max_length=60)
    tldr_content = models.TextField()
    heat_map_url = models.TextField()
    emotion_map_url = models.TextField()
    update_time = models.DateTimeField()
    heat_map_content = models.TextField()
    emotion_map_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'TLDR'


class TldrComment(models.Model):
    tldr_comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    tldr = models.ForeignKey(Tldr, models.DO_NOTHING)
    user_tldr_comment = models.TextField()
    tldr_comment_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TLDR_Comment'


class TldrEmotionScore(models.Model):
    tldr_emotion_id = models.AutoField(primary_key=True)
    tldr = models.ForeignKey(Tldr, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    tldr_emotion_score = models.IntegerField()
    tldr_score_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TLDR_Emotion_Score'


class TldrKeyword(models.Model):
    tldr_keyword_id = models.AutoField(primary_key=True)
    tldr = models.ForeignKey(Tldr, models.DO_NOTHING)
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TLDR_Keyword'


class TldrNews(models.Model):
    tldr_news_id = models.AutoField(db_column='tldr_News_id', primary_key=True)  # Field name made lowercase.
    tldr = models.ForeignKey(Tldr, models.DO_NOTHING)
    title = models.ForeignKey(News, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TLDR_News'


class UserAction(models.Model):
    action_id = models.CharField(primary_key=True, max_length=30)
    action_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'User_Action'


class UserBehavior(models.Model):
    user_behavior_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    action = models.ForeignKey(UserAction, models.DO_NOTHING)
    action_time = models.DateTimeField()
    searched_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'User_Behavior'


class UserNewsComment(models.Model):
    news_comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.ForeignKey(News, models.DO_NOTHING)
    user_comment = models.TextField()
    comment_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'User_News_Comment'


class UserNewsReviseAdvice(models.Model):
    news_revise_advice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.ForeignKey(News, models.DO_NOTHING)
    analysis_item = models.ForeignKey(AnalysisItem, models.DO_NOTHING)
    advice_time = models.DateTimeField()
    revise_advice = models.TextField()

    class Meta:
        managed = False
        db_table = 'User_News_Revise_Advice'



class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=60)
    display_name = models.CharField(max_length=100)
    picture_url = models.TextField(blank=True, null=True)
    status_message = models.TextField(blank=True, null=True)
    join_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Users'
