_author_ = 'Jessica'
_date_ = '5/1/17 4:42 PM'

import xadmin

from .models import EmailVerifyRecord, Banner, CreditCard


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


class CreditCardAdmin(object):
    list_display = ['creditnum', 'logname', 'realname', 'securitycode', 'add_time']
    search_fields = ['creditnum', 'logname', 'realname', 'securitycode']
    list_filter = ['creditnum', 'logname', 'realname', 'securitycode', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(CreditCard, CreditCardAdmin)


