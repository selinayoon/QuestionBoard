# from django.db import models

# # Create your models here.
# class Question(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     # 자동으로 현재시간 저장
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title
        
# class Comment(models.Model):
#     #ForeignKey: 외래키 -> 어디에 속해있는지에 대한 정보 담을 예정
#     #on_delete:포스트가 지워지면 어떻게 할거니
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.content
        
from django.db import models
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.content
    