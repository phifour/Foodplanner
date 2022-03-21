from django import forms

DEMO_CHOICES =(
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)


TIME_HORIZON =(
    ("7", "1 Week"),
    ("14", "2 Weeks"),
    ("21", "3 Weeks"),
    ("28", "4 Weeks"),
)


COOKINGTIME_CHOICES =(
    (15, 15),
    (30, 30),
    (60, 60)
)
  
MAX_INCREDIENTS_CHOICES =(
    (5, 5),
    (10, 10),
    (20, 20)
)

class RecipieSearchForm(forms.Form):
    recipename = forms.CharField(label='Recipe name', max_length=100)
    cooktime = forms.ChoiceField(choices = COOKINGTIME_CHOICES, label='Max Cookingtime')
    nosalt = forms.BooleanField(label='No salt',required = False)
    nosugar = forms.BooleanField(label='No sugar',required = False)
    number_of_incredients_max = forms.ChoiceField(choices = MAX_INCREDIENTS_CHOICES, label='Max Incredients')
    #xxx = forms.MultipleChoiceField(required=False, choices=DEMO_CHOICES)
    #geeks_field = forms.ChoiceField(choices = COOKINGTIME_CHOICES)


class FoodplanForm(forms.Form):
    timehorizoin = forms.ChoiceField(choices = TIME_HORIZON, label='How Long?')
    cooktime = forms.ChoiceField(choices = COOKINGTIME_CHOICES, label='Max Cookingtime')
    number_of_incredients_max = forms.ChoiceField(choices = MAX_INCREDIENTS_CHOICES, label='Max Incredients')
    vegetarian = forms.BooleanField(label='Vegetarian',required = False)


    #xxx = forms.MultipleChoiceField(required=False, choices=DEMO_CHOICES)
    #geeks_field = forms.ChoiceField(choices = COOKINGTIME_CHOICES)
            