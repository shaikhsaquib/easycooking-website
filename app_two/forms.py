from django import forms
from .models import recipie

class RecipeForm(forms.ModelForm):
    
    class meta:
        model = recipie
        fields=['RecipeName','TranslatedRecipeName','Ingredients','TranslatedIngredients','PrepTimeInMins','CookTimeInMins','TotalTimeInMins','Cuisine','Course','Diet','Instructions','TranslatedInstructions','UR']