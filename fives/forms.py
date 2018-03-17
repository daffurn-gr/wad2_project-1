from django import forms
from django.contrib.auth.models import User
from fives.models import Player, Game
import datetime


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class PlayerForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=Player.GENDER_CHOICES, label="Gender")

    class Meta:
        model=Player
        fields = ('gender',)


class GameForm(forms.ModelForm):

    game_type = forms.ChoiceField(choices=Game.GAME_CHOICES, initial=Game.MENS_CP, label="Game type", widget=forms.Select(attrs={'class':'form-control'}))

    date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'class':'form-control'}))
    duration = forms.ChoiceField(choices=Game.DURATION_CHOICES, initial=Game.ONE_HOUR, label="Duration", widget=forms.Select(attrs={'class':'form-control'}))

    street = forms.CharField(max_length=128, label="Street & number", widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=128, label="City/Town", widget=forms.TextInput(attrs={'class':'form-control'}))
    postcode = forms.CharField(max_length=128, label="Postcode", widget=forms.TextInput(attrs={'class':'form-control'}))

    price = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Price/person")
    booked = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control form-check-input', 'type':'checkbox'}), initial=False, required=False, label="Pitch booked?")

    field_order=['game_type','date','time','duration','street','city','postcode', 'price', 'booked']

    class Meta:
        model = Game
        exclude = ('game_id', 'free_slots', 'host', 'latitude', 'longitude', 'end', 'custom_slug', 'start')

class RatingForm(forms.ModelForm):
    skill = forms.ChoiceField(choices=Player.RATINGS, initial=Player.THREE)
    likeability = forms.ChoiceField(choices=Player.RATINGS, initial=Player.THREE)
    punctuality = forms.ChoiceField(choices=Player.RATINGS, initial=Player.THREE)

    class Meta:
        model = Player
        fields = ('skill', 'likeability', 'punctuality')

class RateHostForm(forms.ModelForm):
    host_rating = forms.ChoiceField(choices=Player.RATINGS, initial=Player.THREE)

    class Meta:
        model = Player
        fields = ('host_rating',)

class FilterForm(forms.ModelForm):

    game_type = forms.ChoiceField(choices=Game.GAME_CHOICES, initial=Game.MENS_CP)

    class Meta:
        model = Game
        fields = ('game_type', )
