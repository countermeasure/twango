from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'tasks.views.home'),
    url(r'^(view|project)/(\w+)/tasks/$', 'tasks.views.list_tasks',
        name='list-tasks'),
    url(r'^task/add/$', 'tasks.views.add_task', name='add-task'),
    url(r'^task/edit/(\d+)/$', 'tasks.views.edit_task', name='edit-task'),
    url(r'^task/postpone/(\d+)/(\d+)/$', 'tasks.views.postpone_task',
        name='postpone-task'),
    url(r'^task/complete/(\d+)/$', 'tasks.views.complete_task',
        name='complete-task'),
    url(r'^task/complete-with-followup/(\d+)/$',
        'tasks.views.complete_task',
        {'follow_up': True},
        name='complete-with-followup'),
    url(r'^task/complete-and-duplicate/(\d+)/$',
        'tasks.views.complete_task',
        {'duplicate': True},
        name='complete-and-duplicate'),
    url(r'^task/rubbish/empty/$', 'tasks.views.empty_rubbish',
        name='empty-rubbish'),
    url(r'^task/rubbish/(\d+)/$', 'tasks.views.rubbish_task',
        name='rubbish-task'),
    url(r'^task/toggle-underway/(\d+)/$',
        'tasks.views.toggle_task_underway'),
    url(r'^(context|priority|project)/list/$', 'tasks.views.attribute_list',
        name='attribute-list'),
    url(r'^(context|priority|project)/add/$', 'tasks.views.attribute_add_edit',
        name='attribute-add'),
    url(r'^(context|priority|project)/edit/(\d+)$',
        'tasks.views.attribute_add_edit',
        name='attribute-edit'),
    url(r'^(context|priority|project)/delete/(\d+)$',
        'tasks.views.attribute_delete',
        name='attribute-delete'),
    url(r'^documentation/$', 'tasks.views.documentation', name='documentation'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
