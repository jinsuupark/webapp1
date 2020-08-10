from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE',max_length=100,blank=True)
    # blank -> Null 유무
    url = models.URLField('URL',unique=True)
    # Bookmark라는 테이블에 title,url column을 만드는 과정

    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
                            # User: User의 primarykey가 해당됨
                            # delete CASCADE user가 삭제되면 bookmark도 삭제됨
                            # 널 OK 빈칸 OK
    def __str__(self):
        return self.title
