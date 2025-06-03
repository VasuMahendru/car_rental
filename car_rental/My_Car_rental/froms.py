
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1,6)], widget=forms.RadioSelect)

    class Meta:
        model = Feedback
        fields = ['rating', 'comments']
