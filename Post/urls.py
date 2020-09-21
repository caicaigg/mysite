from django.conf.urls import url
from Post import views

app_name = 'Post'   # 这里是为了url反向解析用

urlpatterns = [
    # 这里放映射的view
    url(r'^$', views.index, name="index"),
]