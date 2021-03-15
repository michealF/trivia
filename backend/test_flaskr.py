import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
        self.DB_USER = os.getenv('DB_USER', 'postgres')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', '06M08l2010')
        self.DB_NAME = os.getenv('DB_NAME', 'test_trivia')
        self.DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
            self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        # self.database_name = "trivia_test"
        # self.database_path = "postgresql://{}:{}@{}/{}".format(
        #     'postgres', '06M08l2010', 'localhost:5432', self.database_name)
        setup_db(self.app, self.DB_PATH)

        # Define Variable Test
        self.new_question = {
            "question": "Alberta is a province of which country?",
            "answer": "Canada",
            "category": "3",
            "difficulty": 2
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # [Test One #01 retrive all categories]

    def test_retrive_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    # [Test Two #02 if categories not exists]
    def test_404_resource_not_found(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # [Test Three #3 retrive all questions with paginate]
    def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['categories'])

    # [Test Four #4 If Resource Not Exist]
    def test_404_paginated_not_exists(self):
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # [Test Five #Deleted Question]
    def test_delete_question(self):
        res = self.client().delete('/questions/5')
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(question, None)

    # [Test Six #06 If Not Delete For any Reason]
    def test_422_error_unprocessable(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # [Test Seven #7 Search with Results]
    def test_search_with_results(self):
        res = self.client().post('/questions', json={"searchTerm": "what"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['questions']), 8)

    # [Test Eight #8 Search Without any Result]
    def test_search_without_results(self):
        res = self.client().post('/questions', json={"searchTerm": "whome"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(len(data['questions']), 0)

    # [Test Nine #9 Create New Question]
    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    # [Test Ten #10 if created question not allowed]
    def _test_405_create_new_question_not_allowed(self):
        res = self.client().post('/questions/50', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Method Not Allowed")

    # [Test Eleven #11 get questions based on categories]
    def test_get_questions_based_on_categories(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['category'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    # [Test Twelve #12 If Category Not Exists]
    def test_error_if_category_not_exists(self):
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    # [Test Thirteen #13 If test play quiz]

    def test_play_quiz_game(self):
        """Tests playing quiz game success"""

        # send post request with category and previous questions
        res = self.client().post('/quizzes',
                                 json={'previous_questions': [17, 18],
                                       'quiz_category': {'type': 'Art', 'id': '2'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that a question is returned
        self.assertTrue(data['question'])

        # check that the question returned is in correct category
        self.assertEqual(data['question']['category'], 2)

        # check that question returned is not on previous q list
        self.assertNotEqual(data['question']['id'], 17)
        self.assertNotEqual(data['question']['id'], 18)

    # [Test Fourteen #14 If play quiz failed]
    def test_play_quiz_fails(self):
        res = self.client().post('/quizzes', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
