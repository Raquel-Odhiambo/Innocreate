from core import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/lecturer/', views.LecSignUpView.as_view(), name='lec_signup'),
]

admin.site.site_header = "InnoCreate"
admin.site.index_title = "Admin Panel"
admin.site.site_title = "Admin Page"