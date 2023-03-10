from django.urls import path
from news.api.views import (
    ArticleListCreateAPIView,
    ArticleDetailAPIView,
    JournalistListCreateAPIView,
    # article_list_create_api_view,
    article_detail_api_view,)


urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article_list"),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article_detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list"),
    # path("articles/", article_list_create_api_view, name="article_list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article_detail"),
]