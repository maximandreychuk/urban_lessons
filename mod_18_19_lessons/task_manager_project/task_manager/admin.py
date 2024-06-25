from django.contrib import admin
from .models import Booking, ExtraService, Tour, Author, Book, Task, Comment, Page, Publisher, Warehouse, Goods, Manager, Stocktaking, Shipper, GoodsWarehouse, TechicalMachine


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title__startswith', 'author__name']
    list_filter = ['pub_date']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'birthdate']
    list_filter = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'phone__endswith']
    list_filter = ['address']


admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Page)

admin.site.register(Warehouse)
admin.site.register(Goods)
admin.site.register(Manager)
admin.site.register(Stocktaking)
admin.site.register(Shipper)
admin.site.register(GoodsWarehouse)
admin.site.register(TechicalMachine)

admin.site.register(Booking)
admin.site.register(Tour)
admin.site.register(ExtraService)
