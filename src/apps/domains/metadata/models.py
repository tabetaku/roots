import os
from uuid import uuid4

from django.db import models

from apps.domains.metadata.constants import ContentType, GenderType, ParticipantType
from libs.django.db.models.base_model import BaseModel

_MAX_PROFILE_IMG_FOLDER = 1024


def _img_upload_to(prefix: str, filename: str) -> str:
    uuid = uuid4()
    # 하나의 디렉토리내 파일이 많이 생기지 않게 하기 위함이다. 이렇게 하면 100만개(1024*1024) 까지는 괜찮다.
    # 그 이상 많아지면 다른 대응이 필요하다.
    sub_folder = int(uuid) % _MAX_PROFILE_IMG_FOLDER
    extension = os.path.splitext(filename)[-1].lower()

    return f'{prefix}/{sub_folder}/{uuid.hex}{extension}'


def _people_profile_img_upload_to(instance, filename):
    return _img_upload_to('profile', filename)


def _content_cover_img_upload_to(instance, filename):
    return _img_upload_to('profile', filename)


class Content(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='제목', )
    title_kor = models.CharField(max_length=255, null=False, blank=False, verbose_name='한국제목', )

    content_type = models.IntegerField(null=False, blank=False, choices=ContentType.get_choices(), verbose_name='작품 종류')

    cover_img = models.ImageField(null=True, blank=True, upload_to=_content_cover_img_upload_to, verbose_name='작품사진', )

    start_date = models.DateField(null=True, blank=True, verbose_name='방송시작날짜', )
    end_date = models.DateField(null=True, blank=True, verbose_name='방송종료날짜', )

    class Meta:
        db_table = 'content'
        verbose_name = '작품'
        verbose_name_plural = '작품목록'


class Video(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.PROTECT, related_name='video_list', verbose_name='작품')

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='제목', )
    title_kor = models.CharField(max_length=255, null=False, blank=False, verbose_name='한글제목', )

    order = models.IntegerField(
        null=False, blank=False, default=1, verbose_name='순서', help_text='이 숫자를 바탕으로 volume 을 노출한다. 단편의 경우 1이다.'
    )

    broadcast_date = models.DateField(null=True, blank=True, verbose_name='방송월일', )
    viewer_ratings = models.IntegerField(null=True, blank=True, verbose_name='시청률')

    class Meta:
        db_table = 'video'
        verbose_name = '영상'
        verbose_name_plural = '영상목록'


class People(BaseModel):
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name='이름', )
    name_kor = models.CharField(max_length=32, null=False, blank=False, verbose_name='한글이름', )

    name_original_kor = models.CharField(max_length=32, null=False, blank=True, verbose_name='본명-한글', )
    name_original_foreign = models.CharField(max_length=32, null=False, blank=True, verbose_name='본명-외국어', )

    gender = models.IntegerField(null=False, blank=False, choices=GenderType.get_choices(), verbose_name='성별')

    profile_img = models.ImageField(null=True, blank=True, upload_to=_people_profile_img_upload_to, verbose_name='사진', )

    birth_date = models.DateField(null=True, blank=True, verbose_name='생년월일', )
    death_date = models.DateField(null=True, blank=True, verbose_name='사망날짜', )

    class Meta:
        db_table = 'people'
        verbose_name = '인물'
        verbose_name_plural = '인물목록'


class Participation(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.PROTECT, related_name='video', verbose_name='영상')
    people = models.ForeignKey(People, on_delete=models.PROTECT, related_name='people', verbose_name='인물')
    participant_type = models.IntegerField(null=False, blank=False, choices=ParticipantType.get_choices(), verbose_name='참여 종류')

    class Meta:
        db_table = 'participation'
        verbose_name = '참여정보'
        verbose_name_plural = '참여정보목록'



