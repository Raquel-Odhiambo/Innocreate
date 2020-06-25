from django.contrib import admin
from .models import Student, Lecturer, Project, User, Comm, reply
from django.contrib.auth.models import Group

# class AdminPage(admin.ModelAdmin):
# 	list_display=('admission_number')
# 	list_editable=('admission_number',)
# 	search_fields=('admission_number',)
# 	list_per_page=5
    
	
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Project)
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Comm)
admin.site.register(reply)
