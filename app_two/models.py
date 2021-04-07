from django.db import models


# Create your models here.
class recipie(models.Model):
    # Srno=models.IntegerField(null=True)
    RecipeName=models.CharField(max_length=155,null=True)
    # TranslatedRecipeName=models.CharField(max_length=155,null=True)
    Ingredients=models.CharField(max_length=155,null=True)
    TranslatedIngredients=models.CharField(max_length=155,null=True)
    PrepTimeInMins=models.IntegerField(null=True)
    CookTimeInMins=models.IntegerField(null=True)
    TotalTimeInMins=models.IntegerField(null=True)
    # Servings=models.IntegerField(null=True)
    Cuisine=models.CharField(max_length=155,null=True)
    Course=models.CharField(max_length=155,null=True)
    Diet=models.CharField(max_length=155,null=True)
    Instructions=models.CharField(max_length=155,null=True)
    # TranslatedInstructions=models.CharField(max_length=256,null=True)
    URL=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.RecipeName
    