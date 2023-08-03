from django.db import models

class Advertisment(models.Model):
    title=models.CharField('Название',max_length=128)
    description=models.TextField('Описание')
    price=models.DecimalField('Цена',max_digits=10,decimal_places=3)
    auction = models.BooleanField('Торг',help_text='Укажите,если возможен торг')
    create_at= models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Advertisement(id={self.id},title={self.title},price={self.price})'

    class Meta:
        db_table='advertisements'





























