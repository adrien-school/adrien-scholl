from django.contrib import admin
from ventehabbi.models import Article ,Category ,comment
# Register your models here.
class liste(admin.ModelAdmin):
    list_display =('title','desc','create_at','update_at','category')
admin.site.register(Article,liste,)
admin.site.register(Category)
class list_comment(admin.ModelAdmin):
    list_display = ('name' ,'body','email')
admin.site.register(comment ,list_comment)