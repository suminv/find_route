from cities.models import City
from trains.models import Train
from django import forms


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Number of train', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter train number'
    }))
    travel_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time'
    }))

    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class':
            'form-control'
    }))
    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class':
            'form-control'
    }))

    class Meta:
        """Selected all fields from model Train"""
        model = Train
        fields = '__all__'
