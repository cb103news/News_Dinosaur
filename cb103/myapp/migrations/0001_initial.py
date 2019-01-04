# Generated by Django 2.1.2 on 2019-01-04 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisItem',
            fields=[
                ('analysis_item_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('analysis', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'analysis_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleEmotion',
            fields=[
                ('article_emotion_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('ariticle_emotion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'article_emotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('title_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('url', models.TextField(blank=True, null=True)),
                ('release_datetime', models.DateTimeField()),
                ('content', models.TextField()),
                ('abstract', models.TextField()),
                ('img_url', models.TextField(blank=True, null=True)),
                ('store_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsEmotionScore',
            fields=[
                ('news_emotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('emotion_score', models.IntegerField()),
                ('score_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'news_emotion_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('origin_id', models.AutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'origin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('poll_id', models.AutoField(primary_key=True, serialize=False)),
                ('poll_title', models.CharField(max_length=60)),
                ('poll_content', models.TextField()),
            ],
            options={
                'db_table': 'poll',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('poll_option_id', models.AutoField(primary_key=True, serialize=False)),
                ('poll_option_name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'poll_option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tldr',
            fields=[
                ('tldr_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tldr_name', models.CharField(max_length=60)),
                ('tldr_content', models.TextField()),
                ('heat_map_url', models.TextField()),
                ('emotion_map_url', models.TextField()),
                ('update_time', models.DateTimeField()),
                ('heat_map_content', models.TextField()),
                ('emotion_map_content', models.TextField()),
            ],
            options={
                'db_table': 'tldr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TldrComment',
            fields=[
                ('tldr_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_tldr_comment', models.TextField()),
                ('tldr_comment_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'tldr_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TldrEmotionScore',
            fields=[
                ('tldr_emotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('tldr_emotion_score', models.IntegerField()),
                ('tldr_score_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'tldr_emotion_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TldrKeyword',
            fields=[
                ('tldr_keyword_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tldr_keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TldrNews',
            fields=[
                ('tldr_news_id', models.AutoField(db_column='tldr_News_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tldr_news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('action_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('action_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_action',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserBehavior',
            fields=[
                ('user_behavior_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('searched_content', models.TextField()),
            ],
            options={
                'db_table': 'user_behavior',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserNewsComment',
            fields=[
                ('news_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_comment', models.TextField()),
                ('comment_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_news_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserNewsReviseAdvice',
            fields=[
                ('news_revise_advice_id', models.AutoField(primary_key=True, serialize=False)),
                ('advice_time', models.DateTimeField()),
                ('revise_advice', models.TextField()),
            ],
            options={
                'db_table': 'user_news_revise_advice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPollBehavior',
            fields=[
                ('poll_behavior_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_poll_behavior',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=100)),
                ('picture_url', models.TextField(blank=True, null=True)),
                ('status_message', models.TextField(blank=True, null=True)),
                ('join_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleKeyword',
            fields=[
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.News')),
            ],
            options={
                'db_table': 'article_keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthorWrite',
            fields=[
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.News')),
            ],
            options={
                'db_table': 'author_write',
                'managed': False,
            },
        ),
    ]