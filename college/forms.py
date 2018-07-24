from django import forms
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField

from college.models import Student


class StudentForm(forms.ModelForm):
    skills = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skills'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone No'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}))
    myimg = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'My Image'}))
    captcha = CaptchaField()
    class Meta:
        model = Student
        fields = ['skills', 'phone_no', 'email']
