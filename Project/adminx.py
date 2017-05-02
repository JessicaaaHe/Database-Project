_author_ = 'Jessica'
_date_ = '5/1/17 5:26 PM'

import xadmin

from .models import Project,Sample


class ProjectAdmin(object):
    list_display = ['pname', 'pdescription', 'tag', 'mingoal', 'maxgoal', 'actualamount', 'posttime', 'endtime', 'completetime','pstate','likesnum','image']
    search_fields = ['pname', 'pdescription', 'tag', 'mingoal', 'maxgoal', 'actualamount']
    list_filter = ['pname', 'pdescription', 'tag', 'mingoal', 'maxgoal', 'actualamount', 'posttime', 'endtime', 'completetime','pstate','likesnum','image']


class SampleAdmin(object):
    list_display = ['pname','stitle', 'add_time', 'download']
    search_fields = ['pname','stitle', 'download']
    list_filter = ['pname','stitle', 'add_time', 'download']


xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(Sample, SampleAdmin)
