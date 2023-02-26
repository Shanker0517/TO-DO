from django.urls import path,include
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,UserLogin,UserRegistration
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register',UserRegistration.as_view(),name='register'),
    path('login',UserLogin.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('item/<int:pk>',TaskDetail.as_view(),name='items'),
    path('create-task/',TaskCreate.as_view(),name='create-task'),
    path('update-task/<int:pk>',TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>',TaskDelete.as_view(),name='delete-task'),
]