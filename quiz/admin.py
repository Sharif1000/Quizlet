from django.contrib import admin
from .models import QuizCategory, Quiz, Question, QuizAttempt, Rating, UserProgress 
# Register your models here.

class QuizCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'average_rating']

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['first_name','title', 'score']
    
    def first_name(self,obj): 
        return obj.user.first_name 
    
    def title(self,obj): 
        return obj.quiz.title 
    
class UserprogressAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'title', 'score']
    
    def first_name(self,obj): 
        return obj.user.first_name 
    
    def last_name(self,obj): 
        return obj.user.last_name 
    
    def title(self,obj): 
        return obj.quiz.title 

class RatingAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'title', 'rating']
    
    def first_name(self,obj): 
        return obj.reviewer.user.first_name 
    
    def last_name(self,obj): 
        return obj.reviewer.user.last_name 
    
    def title(self,obj): 
        return obj.quiz.title 

admin.site.register(QuizCategory, QuizCategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(UserProgress, UserprogressAdmin)
