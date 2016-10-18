from django.test import TestCase, Client

from django.core.urlresolvers import reverse
from rolepermissions.shortcuts import assign_role

from users.models import User
from courses.models import CourseCategory, Course, Subject, Topic
from forum.models import Forum, Post, PostAnswer

class ForumViewTestCase (TestCase):

	def setUp(self):

		self.user = User.objects.create_user(
			username = 'test',
			email = 'testing@amadeus.com',
			is_staff = True,
			is_active = True,
			password = 'testing'
		)
		assign_role(self.user, 'system_admin')

		self.user_professor = User.objects.create_user(
            username = 'professor',
            email = 'professor@amadeus.com',
            is_staff = False,
            is_active = True,
            password = 'testing',
            type_profile = 1
        )
		assign_role(self.user_professor, 'professor')

		self.user_student = User.objects.create_user(
            username = 'student',
            email = 'student@amadeus.com',
            is_staff = False,
            is_active = True,
            password = 'testing',
            type_profile = 2
        )
		assign_role(self.user_student, 'student')

		self.category = CourseCategory.objects.create(
			name = 'Category test',
			slug = 'category_test'
		)
		self.category.save()

		self.course = Course.objects.create(
			name = 'Course Test',
			slug = 'course_test',
			max_students = 50,
			init_register_date = '2016-08-26',
			end_register_date = '2016-10-01',
			init_date = '2016-10-05',
			end_date = '2017-10-05',
			category = self.category
		)
		self.course.save()

		self.subject = Subject.objects.create(
            name = 'Subject Test',
            slug='subject-test',
            description = "description of the subject test",
            visible = True,
            course = self.course,
            init_date = '2016-10-05',
            end_date = '2017-10-05',
        )
		self.subject.save()

		self.topic = Topic.objects.create(
            name = 'Topic Test',
            description = "description of the topic test",
            subject = self.subject,
            owner = self.user,
        )
		self.topic.save()

		self.forum = Forum.objects.create(
        	topic=self.topic,
        	name = 'forum test',
        	slug='forum-test',
        	description = 'description of the forum test',
        	create_date = '2016-10-02',
        	modification_date = '2016-10-03',
        	limit_date = '2017-10-05',
        )
		self.forum.save()

		self.post = Post.objects.create(
            user = self.user,
            message = 'posting a test',
            modification_date = '2016-11-09',
            post_date = '2016-10-03',
            forum = self.forum,
        )
		self.post.save()

		self.answer = PostAnswer.objects.create(
            user = self.user,
            post = self.post,
            message = 'testing a post answer',
            modification_date = '2016-10-05',
            answer_date = '2016-10-04',
        )
		self.answer.save()

		self.client = Client()
		self.client.login(username='test', password='testing')
		
		self.client_professor = Client()
		self.client_professor.login (username='professor', password='testing')

		self.client_student = Client()
		self.client_student.login (username='student', password='testing')

		


		self.update_url = reverse('course:forum:update', kwargs={'pk':self.forum.pk})

		self.createPost_url = reverse('course:forum:create_post')
		self.updatePost_url = reverse('course:forum:update_post', kwargs={'pk':self.post.pk})

######################### ForumDetailView #########################

	def test_ForumDetail_view_ok (self):
		url = reverse('course:forum:view', kwargs={'slug':self.forum.slug})
        
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
		response = self.client_professor.get(url)
		self.assertEquals(response.status_code, 200)

		response = self.client_student.get(url)
		self.assertEquals(response.status_code, 200)

	def test_ForumDetail_context(self):
		url = reverse('course:forum:view', kwargs={'slug':self.forum.slug})

		response = self.client.get(url)
		self.assertTrue('forum' in response.context)

		response = self.client_professor.get(url)
		self.assertTrue('forum' in response.context)

		response = self.client_student.get(url)
		self.assertTrue('forum' in response.context)


######################### CreateForumView #########################

	def test_CreateForum_view_ok (self):
		url = reverse('course:forum:create')

		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		
		response = self.client_professor.get(url)
		self.assertEquals(response.status_code, 200)

		response = self.client_student.get(url)
		self.assertEquals(response.status_code, 200)
		
	def test_CreateForum_context(self):
		url = reverse('course:forum:create')		
		
		response = self.client.get(url)
		self.assertTrue('form' in response.context)

		response = self.client_professor.get(url)
		self.assertTrue('form' in response.context)

		response = self.client_student.get(url)
		self.assertTrue('form' in response.context)

	def test_CreateForum_form_error (self):
		url = reverse('course:forum:create')
		data = {'name':'', 'limit_date': '', 'description':'', 'topic':''}
		list_forum = Forum.objects.all().count()

		response = self.client.post(url, data)
		self.assertEquals (response.status_code, 400)
		self.assertEquals(list_forum, Forum.objects.all().count())

		response = self.client_professor.post(url, data)
		self.assertEquals (response.status_code, 400)
		self.assertEquals(list_forum, Forum.objects.all().count())

		response = self.client_student.post(url, data)
		self.assertEquals (response.status_code, 400)
		self.assertEquals(list_forum, Forum.objects.all().count())

	def test_CreateForum_form_ok (self):
		url = reverse('course:forum:create')
		data = {
		'name':'Forum Test2', 
		'limit_date': '2017-10-05', 
		'description':'Test', 
		'topic':str(self.topic.id)
		}
		list_forum = Forum.objects.all().count()

		response = self.client.post(url, data)
		self.assertEquals (response.status_code, 302)
		self.assertEquals(list_forum+1, Forum.objects.all().count())

		response = self.client_professor.post(url, data)
		self.assertEquals (response.status_code, 302)
		self.assertEquals(list_forum+2, Forum.objects.all().count())

		response = self.client_student.post(url, data)
		self.assertEquals (response.status_code, 302)
		self.assertEquals(list_forum+3, Forum.objects.all().count())

######################### UpdateForumView #########################

	def test_UpdateForum_view_ok (self):
		response = self.client.get(self.update_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'forum/forum_form.html')

	def test_UpdateForum_context(self):		
		response = self.client.get(self.update_url)
		self.assertTrue('form' in response.context)

	def test_UpdateForum_form_error (self):
		data = {'name':'', 'limit_date': '', 'description':''}

		response = self.client.post(self.update_url, data)
		self.assertEquals (response.status_code, 400)

	def test_UpdateForum_form_ok (self):
		data = {
		'name':'Forum Updated', 
		'limit_date': '2017-10-05', 
		'description':'Test', 
		'topic':str(self.topic.id)
		}

		response = self.client.post(self.update_url, data)
		self.assertEquals (response.status_code, 302)

		forum = Forum.objects.get(name='Forum Updated')

######################### CreatePostView #########################

	def test_CreatePost_form_error (self):
		data = {'message': '', 'forum': ''}
		
		#response = self.client.post(self.createPost_url, data)
		#self.assertEquals (response.status_code, 400)

	def test_CreatePost_form_ok (self):
		data = {
		'forum': str(self.forum.id),
		'message':'posting a test2'		
		}

		response = self.client.post(self.createPost_url, data)
		self.assertEquals (response.status_code, 302)

		post = Post.objects.get(message='posting a test2')

######################### UpdatePostView #########################

	def test_UpdatePost_form_error (self):
		data = {'message': ''}

		response = self.client.post(self.updatePost_url, data)
		self.assertFormError (response, 'form', 'message', 'Este campo é obrigatório.')

	def test_UpdatePost_form_ok (self):
		data = {'message':'updating a post'}

		response = self.client.post(self.updatePost_url, data)
		#self.assertEquals (response.status_code, 302)

		#self.assertEquals(self.post.message, 'updating a post')



