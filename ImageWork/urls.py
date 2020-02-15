from django.conf.urls import url
from .views import HomepageView, CreatePostView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name="home"),
    url(r'^post/$', CreatePostView.as_view(), name='add_post') # new
]
