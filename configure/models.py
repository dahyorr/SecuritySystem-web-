from django.db import models


# Create your models here.


class RfidId(models.Model):
    entryid = models.AutoField(primary_key=True)
    ownername = models.CharField(max_length=70)
    code = models.CharField(max_length=20)
    datecreated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rfid_id'

    def __str__(self):
        return self.ownername

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('Manage:Index')


class Pininput(models.Model):
    pin = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pininput'

    def __str__(self):
        return self.pin


class Pincode(models.Model):
    code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincode'

    def __str__(self):
        return str(self.code)


class Armstate(models.Model):
    state = models.CharField(max_length=1, blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'armstate'

    def __str__(self):
        return str(self.state)


class Gui(models.Model):
    page = models.CharField(max_length=50, blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'gui'

    def __str__(self):
        return self.page


class Lockstate(models.Model):
    state = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lockstate'

    def __str__(self):
        return str(self.state)
