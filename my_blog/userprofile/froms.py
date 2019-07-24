from django import forms

from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ('username','email')
    #两次密码是否一致性对比
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("两次输入密码不一致")


