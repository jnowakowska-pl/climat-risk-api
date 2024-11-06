""" Database models"""

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, \
    PermissionsMixin)
from django.contrib.auth.hashers import make_password


class AttachedFiles(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100, blank=True, null=True)
    file_size = models.BigIntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'attached_files'
        db_table_comment = 'Stores user attached files and feautures'


class AuditLogs(models.Model):
    audit_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=255)
    target_table = models.CharField(max_length=100, blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey('SessionLogs', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'audit_logs'
        db_table_comment = 'Stores user activity logs'


class ErrorLogs(models.Model):
    error_id = models.AutoField(primary_key=True)
    error_message = models.TextField()
    error_code = models.IntegerField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    stack_trace = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey('SessionLogs', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'error_logs'
        db_table_comment = 'Stores errors during the users session'


class FavoriteContent(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    content_type = models.CharField(max_length=50)
    content_id = models.IntegerField()
    saved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'favorite_content'
        db_table_comment = 'Stores user favorite content on the platform'


class MapQueries(models.Model):
    query_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    query_text = models.TextField()
    query_type = models.IntegerField()
    session = models.ForeignKey('SessionLogs', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'map_queries'


class MapViews(models.Model):
    map_view_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    zoom_level = models.IntegerField(blank=True, null=True)
    layers = models.TextField()  # This field type is a guess.
    viewed_at = models.DateTimeField(blank=True, null=True)
    query = models.ForeignKey(MapQueries, models.DO_NOTHING, blank=True, null=True)
    session = models.ForeignKey('SessionLogs', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'map_views'
        db_table_comment = 'Stores map feautures in the user log session: center coordinate, zoom details, current added layers and queries.'


class MetadataLogs(models.Model):
    metadata_id = models.AutoField(primary_key=True)
    log_id = models.IntegerField(blank=True, null=True)
    browser_info = models.TextField(blank=True, null=True)
    os_info = models.TextField(blank=True, null=True)
    device_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey('SessionLogs', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metadata_logs'
        db_table_comment = 'Stores logging events features'


class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    notification_message = models.TextField()
    notification_type = models.CharField(max_length=50, blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notifications'
        db_table_comment = 'Stores notifications to the user according with the data updating'


class Permissions(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permissions'


class SessionLogs(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    session_duration = models.DurationField(blank=True, null=True)
    session_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'session_logs'
        db_table_comment = 'Tracks user sessions: logged in, logged out, session expired'


class UiLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255)
    action_details = models.TextField(blank=True, null=True)
    page_url = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    session = models.ForeignKey(SessionLogs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ui_logs'
        db_table_comment = 'Stores detailed user actions logs'


class UserGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    group_description = models.TextField(blank=True, null=True)
#    created_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation

    permission = models.ForeignKey(Permissions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_groups'
        db_table_comment = 'Stores user groups and their descriptions'

class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
       # user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# class User(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that supports using email instead of username"""

#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     is_staff = models.BooleanField(default=False)


#     # def save(self, *args, **kwargs):
#     #     if self.password:
#     #         self.password = make_password(self.password)
#     #     super(User, self).save(*args, **kwargs)


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
   # is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)
    permission_group = models.ForeignKey('UserGroups', models.DO_NOTHING, db_column='permission_group', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        managed = True
        db_table = 'users'
        db_table_comment = 'Stores users that log in'

    def __str__(self):
        return self.email
