_author_ = 'Jessica'
_date_ = '5/1/17 5:36 PM'

import xadmin

from .models import ProjectComment, ProjectRate, UserFavourite, UserMessage, UserProject, Charge


class ProjectCommentAdmin(object):
    list_display = ['logname', 'pname', 'comments', 'add_time']
    search_fields = ['logname', 'pname', 'comments']
    list_filter = ['logname', 'pname', 'comments', 'add_time']


class ProjectRateAdmin(object):
    list_display = ['logname', 'pname', 'ratelevel', 'add_time']
    search_fields = ['logname', 'pname', 'ratelevel']
    list_filter = ['logname', 'pname', 'ratelevel', 'add_time']


class UserFavouriteAdmin(object):
    list_display = ['logname', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['logname', 'fav_id', 'fav_type']
    list_filter = ['logname', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserProjectAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class ChargeAdmin(object):
    list_display = ['logname', 'pname', 'creditnum', 'charamount', 'charstate', 'chartime']
    search_fields = ['logname', 'pname', 'creditnum', 'charamount', 'charstate']
    list_filter = ['logname', 'pname', 'creditnum', 'charamount', 'charstate', 'chartime']





xadmin.site.register(ProjectComment, ProjectCommentAdmin)
xadmin.site.register(ProjectRate, ProjectRateAdmin)
xadmin.site.register(UserFavourite, UserFavouriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserProject, UserProjectAdmin)
xadmin.site.register(Charge, ChargeAdmin)


