from django.forms import ModelForm
from .models import Vote, Aspirant, Seat, Upload
from django.db import models
from django.forms import ModelChoiceField
from django import forms

#lass VoteForm(ModelForm):
#     class Meta:
 #        model = Vote
  #       fields = ['aspirant', 'station', 'vcast']

# class MenuModelChoiceField(ModelChoiceField):
#     def label_from_instance(self, aspirant):
#         return "Vote #%s) %s" % (aspirant.name,aspirant.seat)
    
# class VoteForm(ModelForm):
#     aspirant = MenuModelChoiceField(queryset=Vote.objects.all())
#     class Meta:      
#         model = Vote
#         #fields = '__all__'
#         fields = ['aspirant', 'station', 'vcast']


class VoteForm(forms.ModelForm):
	aspirant = forms.ModelMultipleChoiceField(queryset=Aspirant.objects.all())
	station = forms.ModelMultipleChoiceField(queryset=Upload.objects.all())
	vcast = forms.IntegerField()
	class Meta:
		model = Vote
		fields = ['aspirant', 'station', 'vcast']

    # # def __init__(self, *args, **kwargs):
    # #     super().__init__(*args, **kwargs)
    # #     self.fields['station'].queryset = Vote.objects.none()

    # #     if 'aspirant' in self.data:
    # #         try:
    # #             aspirant_id = int(self.data.get('aspirant'))
    # #             self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
    # #         except (ValueError, TypeError):
    # #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    # #     elif self.instance.pk:
    # #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')