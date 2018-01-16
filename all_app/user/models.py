from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from core.models import CoreModel
from common.models import File
from utils.permission_classes import custom_model_permission

# Create your models here.


class UserManager(BaseUserManager):
    """用户管理器"""
    def create_user(self, username, password):
        if username is None:
            raise ValueError('用户名必须填写')
        if password is None:
            raise ValueError('密码必须填写')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Menu(CoreModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')
    icon = models.CharField(max_length=255, default="")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    order_num = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    class Meta:
        verbose_name = verbose_name_plural = '菜单'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])


class Role(CoreModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    menus = models.ManyToManyField('Menu')

    class Meta:
        verbose_name = verbose_name_plural = '角色'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])


class Organization(CoreModel):
    name = models.CharField(max_length=32, verbose_name='组织名称')
    parent_organization = models.ForeignKey('Organization',
                                            on_delete=models.CASCADE,
                                            null=True,
                                            default=None,
                                            limit_choices_to={'organization_type': '公司'},
                                            verbose_name="父组织")
    organization_type = models.CharField(choices=(('公司', '公司'),
                                                  ('部门', '部门')), max_length=32, verbose_name='组织类型')

    class Meta:
        unique_together = ('name', 'parent_organization',)
        verbose_name = verbose_name_plural = '组织'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])


class AbstractUser(AbstractBaseUser, PermissionsMixin, CoreModel):
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    password = models.CharField(blank=True, max_length=255, verbose_name='密码')
    telephone = models.CharField(blank=True, max_length=255, unique=True, verbose_name='电话号码')
    fullname = models.CharField(blank=True, max_length=255, verbose_name='姓名')
    avatar = models.ForeignKey(File, blank=True, null=True, verbose_name='用户头像', on_delete=models.SET_NULL)
    add_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='加入时间')
    organization = models.ForeignKey(Organization, verbose_name="组织", related_name='organization_staffs', null=True,
                                     on_delete=models.SET_NULL)
    session_id = models.CharField(default="", max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    is_admin = models.BooleanField(default=False, verbose_name='是否管理员')
    is_online = models.IntegerField(default=0)  # 是否在线
    login_times = models.IntegerField(default=0)  # 登录过的次数

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def get_username(self):
        return self.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.fullname

    def get_short_name(self):
        # The user is ident
        return self.fullname

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        abstract = True


class User(AbstractUser):

    class Meta:
        verbose_name = verbose_name_plural = '用户'
        default_permissions = ()
        permissions = [('group_manage', '权限组管理'),
                       ('role_manage', '角色管理'),
                       ('organization_manage', '组织管理')
                       ] + custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])


class OperationLog(CoreModel):
    detail = models.CharField(max_length=200, unique=True, verbose_name='操作详情')
    operator = models.ForeignKey(User, null=True, verbose_name='操作人')

    class Meta:
        verbose_name = verbose_name_plural = '操作日志'
        default_permissions = ()
        permissions = custom_model_permission('menu', verbose_name, ['read', 'add', 'delete', 'change'])
