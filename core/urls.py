from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('student/dashboard', views.student, name = 's_dashboard'),
    path('lecturers/dashboard', views.lecturer, name = 'l_dashboard'),
    path('project/add', views.ProjectCreate.as_view(), name = 'add_proj'),
    path('messages/s/add', views.StudentMessage.as_view(), name = 's_messages'),
    path('messages/',views.communicate, name= 'communicate'),
    path('chatscreen/<int:pk>/', views.chat, name = 'chat')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)