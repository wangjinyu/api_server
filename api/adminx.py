import xadmin
from xadmin import *
from .models import UserInfo

class GlobalSetting(object):
    site_title = "API 管理系统"
    site_footer = "http://blog.develop-er.com/"
    menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSetting)

class UserInfoAdmin(object):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'age')
    empty_value_display = '-empty-'
xadmin.site.unregister(UserInfo)
xadmin.site.register(UserInfo, UserInfoAdmin)
