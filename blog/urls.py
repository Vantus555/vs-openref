from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', index.as_view(), name="blog_url"),
    path('ajaxAddPost', ajaxAddPost.as_view(), name="ajaxAddPost_url"),
    path('ajaxDeletePost', ajaxDeletePost.as_view(), name="ajaxDeletePost_url"),
    path('ajaxGetPostText', ajaxGetPostText.as_view(), name="ajaxGetPostText_url"),
    path('ajaxGetDir', ajaxGetDir.as_view(), name="ajaxGetDir_url"),
    path('ajaxPublicationPost', ajaxPublicationPost.as_view(), name="ajaxPublicationPost_url"),
    path('ajaxSavePost', ajaxSavePost.as_view(), name="ajaxSavePost_url"),
    path('ajaxAddToBasket', ajaxAddToBasket.as_view(), name="ajaxAddToBasket_url"),
]