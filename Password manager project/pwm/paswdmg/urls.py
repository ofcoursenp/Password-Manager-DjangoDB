from django.contrib import admin
from django.urls import path,include
from paswdmg import views


admin.site.site_header = "Password Manager Login"
admin.site.site_title = "Password Manager"
admin.site.index_title = "Password Manager"

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('database',views.database,name='database'),
    path('return',views.returnin,name='return')
]
