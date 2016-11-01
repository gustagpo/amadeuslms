from django.conf.urls import url, include

from . import views
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='manage'),
	url(r'^all-courses/$', views.AllCoursesView.as_view(), name='all_courses'),
	url(r'^create/$', views.CreateCourseView.as_view(), name='create'),
	url(r'^replicate_course/(?P<slug>[\w_-]+)/$', views.ReplicateCourseView.as_view(), name='replicate_course'),
	url(r'^edit/(?P<slug>[\w_-]+)/$', views.UpdateCourseView.as_view(), name='update'),
	url(r'^delete/(?P<slug>[\w_-]+)/$', views.DeleteCourseView.as_view(), name='delete'),
	url(r'^subscribe/(?P<slug>[\w_-]+)/$', views.subscribe_course, name='subscribe'),
	url(r'^category/(?P<slug>[\w_-]+)/$', views.FilteredView.as_view(), name='filter'),
	url(r'^categories/view/$', views.IndexCatView.as_view(), name='manage_cat'),
	url(r'^categories/create/$', views.CreateCatView.as_view(), name="create_cat"),
	url(r'^categories/edit/(?P<slug>[\w_-]+)/$', views.UpdateCatView.as_view(), name='update_cat'),
	url(r'^categories/delete/(?P<slug>[\w_-]+)/$', views.DeleteCatView.as_view(), name='delete_cat'),
	url(r'^subjects/(?P<slug>[\w_-]+)/$', views.SubjectsView.as_view(), name='view_subject'),
	url(r'^subjects/create/(?P<slug>[\w_-]+)/$', views.CreateSubjectView.as_view(), name='create_subject'),
	url(r'^subjects/update/(?P<slug>[\w_-]+)/$', views.UpdateSubjectView.as_view(), name='update_subject'),
	url(r'^subjects/delete/(?P<slug>[\w_-]+)/$', views.DeleteSubjectView.as_view(), name='delete_subject'),
	url(r'^subjects/subscribe/(?P<slug>[\w_-]+)/$', views.subscribe_subject, name='subscribe_subject'),
	url(r'^topics/create/(?P<slug>[\w_-]+)/$', views.CreateTopicView.as_view(), name='create_topic'),
	url(r'^topics/update/(?P<slug>[\w_-]+)/$', views.UpdateTopicView.as_view(), name='update_topic'),
	url(r'^topics/(?P<slug>[\w_-]+)/$', views.TopicsView.as_view(), name='view_topic'),
	url(r'^subjects/categories$',views.IndexSubjectCategoryView.as_view(), name='subject_category_index'),
	url(r'^forum/', include('forum.urls', namespace = 'forum')),
	url(r'^poll/', include('poll.urls', namespace = 'poll')),
	url(r'^exam/', include('exam.urls', namespace = 'exam')),
	url(r'^files/', include('files.urls', namespace = 'file')),
	url(r'^upload-material/$', views.UploadMaterialView.as_view(), name='upload_material'),
	url(r'^subjects/file-material-view/(?P<slug>[\w_-]+)/$', views.FileMaterialView.as_view(), name='file_material_view'),
	url(r'^links/',include('links.urls',namespace = 'links')),
	url(r'^(?P<slug>[\w_-]+)/', include([
		url(r'^$', views.CourseView.as_view(), name='view'),
		url(r'^(?P<category>[\w_-]+)/$', views.CourseView.as_view(), name='view_filter')
	])),
]
