from django.conf.urls import include, url
from blog import views


urlpatterns = [
    url(r"up_down/",views.up_down),
    url(r"comment/",views.comment),
    url(r"comment_tree/(\d+)/",views.comment_tree),
    url(r"^(\w+)/(\w+)/article/(\d+)/$", views.article_detail),  # 文章详情
    url(r'(\w+)/$',views.home),
]