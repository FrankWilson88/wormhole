from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('pads/', views.pads, name='pads'),
  path('articles/', views.articles, name='articles'),
  path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article'),
  path('shop/', views.shop, name='shop'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)