from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id','title','url') # 사이트에서 출력할 컬럼 목록
