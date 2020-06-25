from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from core.models import Student, Lecturer, User, reply

class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','admission_number', 'email','password1','password2' )
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

class LecSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','employment_no', 'email','password1','password2' )
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.save()
        lecturer = Lecturer.objects.create(user=user)
        return user


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden',}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password' )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['placeholder']='First Name'
        self.fields['first_name'].label=''

        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['placeholder']='Last Name'
        self.fields['last_name'].label=''

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email Address'
        self.fields['email'].label=''
        

class ReplyForm(forms.ModelForm):

    class Meta:
        model = reply
        fields = ('mess',)