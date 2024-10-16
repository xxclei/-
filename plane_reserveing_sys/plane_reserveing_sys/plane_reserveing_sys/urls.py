
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('regist/', views.regist,name="regist"),
    path('', views.login,name="login"), 
    path('login/', views.login,name="submit_login"), 
    path('admin_index/', views.admin_index,name="admin_index"),
    path('Tours_index/', views.Tours_index,name="admin_index")
    # path('Tours_index/get_user_info/', get_user_info,name="get_user_info")
                          #绑定url和视图函数。
]