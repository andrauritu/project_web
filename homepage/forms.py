from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
    class Meta:
        model = PersonalInfo
        fields = ['first_name', 'last_name', 'group', 'your_project_title', 'your_colleagues_for_the_project', 'email', 'project_link']
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your last name'
            }),
            'group': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., 1241EB'
            }),
            'your_project_title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your project title'
            }),
            'your_colleagues_for_the_project': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Enter your project colleagues',
                'rows': 3
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your.email@example.com'
            }),
            'project_link': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://example.com/project'
            }),
        }
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'group': 'Group',
            'your_project_title': 'Project Title',
            'your_colleagues_for_the_project': 'Project Colleagues',
            'email': 'Email',
            'project_link': 'Project Link',
        }