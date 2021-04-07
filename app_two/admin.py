from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import recipie
# from import_export.admin import ImportExportModelAdmin
# Register your models here.
class recipieAdmin(ImportExportModelAdmin):
    list_display=['id','RecipeName','Ingredients','TranslatedIngredients','PrepTimeInMins','CookTimeInMins','TotalTimeInMins','Cuisine','Course','Diet','Instructions',
    'URL']
    pass

admin.site.register(recipie,recipieAdmin)