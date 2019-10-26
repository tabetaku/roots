import os
from uuid import uuid4

from django.db import models

from apps.domains.metadata.constants import GenderType
from libs.django.db.models.base_model import BaseModel

_MAX_PROFILE_IMG_FOLDER = 1024


def profile_img_upload_to(instance, filename):
    uuid = uuid4()
    prefix = int(uuid) % _MAX_PROFILE_IMG_FOLDER
    extension = os.path.splitext(filename)[-1].lower()

    return f'profile/{prefix}/{uuid.hex}{extension}'


class People(BaseModel):
    name_kor = models.CharField(max_length=32, null=False, blank=False, verbose_name='한글이름', )
    name_foreign = models.CharField(max_length=32, null=True, blank=True, verbose_name='외국이름', )

    name_original_kor = models.CharField(max_length=32, null=False, blank=True, verbose_name='본명-한글', )
    name_original_foreign = models.CharField(max_length=32, null=False, blank=True, verbose_name='본명-외국어', )

    gender = models.IntegerField(null=False, blank=False, choices=GenderType.get_choices(), verbose_name='성별')

    profile_img = models.ImageField(null=True, blank=True, upload_to=profile_img_upload_to, verbose_name='사진', )

    birth_date = models.DateField(null=True, blank=True, verbose_name='생년월일', )
    death_date = models.DateField(null=True, blank=True, verbose_name='사망날짜', )

    class Meta:
        db_table = 'people'
        verbose_name = '인물'
        verbose_name_plural = '인물목록'
