from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.timezone import now

from .utils import get_file_path


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_valid=True)


class CommonModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(verbose_name='创建时间',
                                   default=now)
    updated = models.DateTimeField(verbose_name='修改时间',
                                   default=None, blank=True,
                                   null=True)
    is_valid = models.BooleanField(verbose_name='是否有效',
                                   default=True)

    objects = models.Manager()
    query_objects = BaseManager()

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id:
            self.updated = now()
        return super().save(force_insert, force_update,
                            using, update_fields)


class Category(CommonModel):
    category_text = models.CharField(verbose_name='分类名称',
                                     max_length=20)

    # 分类1是 安全文章收集  分类2是漏洞相关  分类3是安全工具相关 分类4是自己编写
    sub_category = models.SmallIntegerField(verbose_name='自分类',
                                            default=1)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'
        ordering = ('-created',)

    def __str__(self):
        return self.category_text


class Author(CommonModel):
    name = models.CharField(verbose_name='作者名称', max_length=100)
    url = models.CharField(verbose_name='作者链接', max_length=200)
    avatar = models.ImageField(verbose_name='作者头像',
                               blank=True, null=True, upload_to=get_file_path)
    now = now()
    directory_string_var = 'avatars/%s/%s/%s/' % (now.year, now.month,
                                                  now.day)

    def avatar_tag(self):
        img_path = settings.MEDIA_URL + '{}'.format(self.avatar)
        return '<img src= "{}" style="width:150px; height:150px;"/>'.format(
            img_path)

    avatar_tag.short_description = '头像预览'
    avatar_tag.allow_tags = True

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Article(CommonModel):
    title = models.CharField(verbose_name='文章标题', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name='作者')
    categories = models.ManyToManyField(Category,
                                        verbose_name='文章分类')
    url = models.TextField(verbose_name='链接', blank=True, null=True)
    url_md5 = models.CharField(verbose_name='链接的MD5', blank=True, null=True,
                               max_length=100, db_index=True)
    issue_time = models.DateTimeField(verbose_name='发表时间',
                                      blank=True, null=True)

    tread = models.BigIntegerField(default=0, verbose_name='踩')
    support = models.BigIntegerField(default=0, verbose_name='赞')
    views = models.BigIntegerField(default=0, verbose_name='浏览数')
    content = RichTextUploadingField(verbose_name='文章内容')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ('-created',)

    def __str__(self):
        return self.title
