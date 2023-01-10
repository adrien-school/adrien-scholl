from django import forms
class login_forms(forms.Form):
   username =forms.CharField(label ="nom utilisateur ",widget=forms.TextInput(attrs={'class':'form-control'}))
   pwd =forms.CharField(label ="mot de passe ",widget=forms.PasswordInput(attrs= {'class':'form-control'}))
class login_register(forms.Form):
    username =forms.CharField(label="nom utilisateur " ,widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd =forms.CharField(label ="mot de passe " ,widget=forms.PasswordInput(attrs= {'class':'form-control'}))
    pwd_confirm =forms.CharField(label="mot de passe de confirmation",widget=forms.TextInput(attrs={'class':'form-control'}))