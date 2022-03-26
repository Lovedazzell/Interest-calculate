from django import forms



class InterestCalForm(forms.Form):
    amount = forms.IntegerField( label_suffix="" ,widget=forms.TextInput(attrs={'class':'form1','placeholder':'Enter your loan ammount'}))
    release_date = forms.DateField( label_suffix="",widget=forms.SelectDateWidget(attrs={'class':'form2'}))
    