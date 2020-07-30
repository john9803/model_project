from django.db import models

# Create your models here.

# 서버임!!!!

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField() 

    def __str__(self):
        return self.title 
        # title 을 글의 제목으로 표현시켜주는 코드임