from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

class Advertisment(models.Model):
    title=models.CharField('Название',max_length=128)
    description=models.TextField('Описание')
    price=models.DecimalField('Цена',max_digits=10,decimal_places=3)
    auction = models.BooleanField('Торг',help_text='Укажите,если возможен торг')
    create_at= models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create_at.date()==timezone.now().date():
            created_time=self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green;font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.create_at.strftime('%d.%m.%Y')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.updated_at.date()==timezone.now().date():
            updated_time =self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green;font-weight: bold;">Сегодня в {}</span>',updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y')



    def __str__(self):
        return f'Advertisement(id={self.id},title={self.title},price={self.price})'

    class Meta:
        db_table='advertisements'





























