from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', index.as_view(), name="user_url"),
    path('images', images.as_view(), name="images_url"),
    path('roles_and_roots', roles_and_roots.as_view(), name="roles_and_roots_url"),
    path('ajaxRegistration', ajaxRegistration.as_view(), name="ajaxRegistration_url"),
    path('ajaxInput', ajaxInput.as_view(), name="ajaxInput_url"),
    path('ajaxUserExit', ajaxUserExit.as_view(), name="ajaxUserExit_url"),
    path('ajaxChangeMiniTag', ajaxChangeMiniTag.as_view(), name="ajaxChangeMiniTag_url"),
    path('ajaxChangePass', ajaxChangePass.as_view(), name="ajaxChangePass_url"),
    path('ajaxAddRole', ajaxAddRole.as_view(), name="ajaxAddRole_url"),
    path('ajaxDeleteRole', ajaxDeleteRole.as_view(), name="ajaxDeleteRole_url"),
    path('ajaxAddRoot', ajaxAddRoot.as_view(), name="ajaxAddRoot_url"),
    path('ajaxUpdateRole', ajaxUpdateRole.as_view(), name="ajaxUpdateRole_url"),
    path('ajaxGetFreedoms', ajaxGetFreedoms.as_view(), name="ajaxGetFreedoms_url"),
    path('ajaxDeleteImage', ajaxDeleteImage.as_view(), name="ajaxDeleteImage_url"),
]