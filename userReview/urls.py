"""userReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from todo.views import todoView, addTodo, deleteTodo
from login.views import loginPage, createUser, createUserRedirect, logoutPage
from reviews.views import home, createReview, reviewSearch, serchRedirect, schoolSearch
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('loginPage/', loginPage),
    path('home/', home),
    path('createUser/', createUser),
    path('createReview/',createReview),
    path('reviewSearch/', reviewSearch),
    path('createUserRedirect/', createUserRedirect),
    path('serchRedirect/', serchRedirect),
    path('logoutPage/', logoutPage),
    path('schoolSearch/', schoolSearch)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
