"""
URL configuration for empproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empapp import views
from rest_framework.authtoken import views as authview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.EmployeeCreateList.as_view()),
    path('emp/details/<int:pk>', views.EmployeeRetrieveUpdateDelete.as_view()),
    path('task', views.TaskCreateList.as_view()),
    path('task/details/<int:pk>', views.TaskRetrieveUpdateDelete.as_view()),
    path('token',authview.obtain_auth_token),
    path('pending/<int:id>',views.PendingTask.as_view()),

]

