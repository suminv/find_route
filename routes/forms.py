from cities.models import City
from django import forms

from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From',
                                       queryset=City.objects.all(),
                                       widget=forms.Select(
                                           attrs={
                                               'class':
                                                   'form-control'
                                           }))

    to_city = forms.ModelChoiceField(label='To',
                                     queryset=City.objects.all(),
                                     widget=forms.Select(
                                         attrs={
                                             'class':
                                                 'form-control'
                                         }))

    cities_through = forms.ModelMultipleChoiceField(label='Through cities',
                                                    queryset=City.objects.all(),
                                                    required=False,
                                                    widget=forms.SelectMultiple(
                                                        attrs={
                                                            'class': 'form-control'
                                                        }))

    travelling_time = forms.IntegerField(label='Travel time',
                                         widget=forms.NumberInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Travelling time'
                                             }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Name of route', widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the name of route'
        }))
    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )
    travel_time = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
