from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # foreign keyのものをIDではなく、データを表示する
    # author = serializers.StringRelatedField()
    #foreign_keyのオブジェクト全部持ってくる
    # author = JournalistSerializer(read_only=True)

    # フィールドの拡張
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        timedelta = timesince(publication_date,now)
        return timedelta

    def validate(self, data):
        """Check that description and title are different"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description must be different dorm one another"
            )
        return data

    def validate_title(Self, value):
        if len(value) < 60:
            raise serializers.ValidationError("The title has to be at least 60 characters")
        return value

    class Meta:
        # シリアライズしたいmodelを指定
        model = Article
        # id以外をシリアライズ
        exclude = ("id",)
        # 全てのフィールドをシリアライズ
        # fields = "__all__"
        # title, description, bodyをシリアライズ
        # fields = ("title", "description", "body)


class JournalistSerializer(serializers.ModelSerializer):
    # view_nameはurls.pyのnameに指定している名前
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article_detail")
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     """Article serializer"""
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self,validate_data):
#         print(validate_data)
#         return Article.objects.create(**validate_data)

#     def update(self,instance,validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.body = validated_data.get('body',instance.body)
#         instance.location = validated_data.get('location',instance.location)
#         instance.publication_date = validated_data.get('publication_date',instance.publication_date)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         """Check that description and title are different"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Title and Description must be different dorm one another"
#             )
#         return data

#     def validate_title(Self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError("The title has to be at least 60 characters")
#         return value