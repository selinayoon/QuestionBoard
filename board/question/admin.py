from django.contrib import admin
from .models import Question,Comment

# Register your models here.

class QuestionModelAdmin(admin.ModelAdmin):
    # 사용자가 수정 할 수 없는 데이터 설정
    readonly_fields = ('created_at',)
admin.site.register(Comment)
admin.site.register(Question,QuestionModelAdmin)