from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False,default=0)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

    def __str__(self):
        return self.hname


