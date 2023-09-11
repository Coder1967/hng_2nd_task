from unittest import TestCase
from models.user import User
from api.app import app
from models import storage
import unittest
from models.user import User
url_prefix = '/api/'
name = "testing_app_name"


class TestUser(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.res  = self.app.post('{}'.format(url_prefix),
                                  json=dict(name=name))
        self.user_id = storage.get(User, name=name)[0].user_id

    def test_post_user(self):
        self.assertEqual(201, self.res.status_code)


    def test_get_user(self):
        res = self.app.get('{}{}'.format(url_prefix, name))
        self.assertEqual(200, res.status_code)

    def test_update_user(self):
        res = self.app.put('{}{}'.format(url_prefix, self.user_id), json={'name': 'john'})
        self.assertEqual(201, res.status_code)
    
    def test_delete_user(self):
        res = self.app.delete('{}{}'.format(url_prefix, self.user_id))
        self.assertEqual(200, res.status_code)


    def tearDown(self):
        user = storage.get(User, name=name)[0]
        if user:
            storage.delete(user)
            storage.save()
            storage.close()



class TestError(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.res  = self.app.post('{}'.format(url_prefix),
                                  json=dict(name=name))
        self.user_id = storage.get(User, name=name)[0].user_id


    def test_postUser_ErrorTest(self):
        res  = self.app.post('{}'.format(url_prefix)) #json not passed
        self.assertEqual(400, res.status_code)
        res  = self.app.post('{}'.format(url_prefix), json={}) #name was not passed
        self.assertEqual(400, res.status_code)


    def test_updateUser_ErrorTest(self):
        res = self.app.put('{}{}'.format(url_prefix, "hello")) #id must be int
        self.assertEqual(400, res.status_code)
        res  = self.app.put('{}{}'.format(url_prefix, self.user_id)) #json not passed
        self.assertEqual(400, res.status_code)
        res  = self.app.put('{}{}'.format(url_prefix, self.user_id), json={}) #name was not passed
        self.assertEqual(400, res.status_code)
        res = self.app.put('{}-32'.format(url_prefix, self.user_id), json={'name':name})
        self.assertEqual(404, res.status_code)


    def test_deleteUser_ErrorTest(self):
        res = self.app.put('{}{}'.format(url_prefix, -32), json={'name':name})
        self.assertEqual(404, res.status_code)

    def test_getUser_ErrorTest(self):
        res = self.app.get('{}{}'.format(url_prefix, -3))
        self.assertEqual(404, res.status_code)
        res = self.app.get('{}{}'.format(url_prefix, "None_existent_name"))
        self.assertEqual(404, res.status_code)


    def tearDown(self):
        user = storage.get(User, name=name)[0]
        if user:
            storage.delete(user)
            storage.save()
            storage.close()



if __name__ == '__main__':
    unittest.main()
