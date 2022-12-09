from django import forms 
from .models import Thing

"""Forms of the project."""

class ThingForm(forms.ModelForm):
    name = forms.CharField(label= "name")
    description = forms.Textarea(label="description")
    quantity = forms.NumberInput(
        label = "quantity"
    )
    def save(self): 
                super().save(commit=False) 
                thing =  Thing.objects.create_thing(
                        self.cleaned_data.get ('name'),
                        first_name = self.cleaned_data.get ('description'),
                        last_name = self.cleaned_data.get ('quantity'),
                )
                return thing
        
        
                