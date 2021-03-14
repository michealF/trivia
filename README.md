# Full Stack Trivia API Project

This project is a game where users can test their knowledge answering trivia questions. The task for the project was to create an API and test suite for implementing the following functionality:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

## Getting Started

### Installing Dependencies

Developers using this project should already have Python3, pip, node, and npm installed.

#### Frontend Dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

#### Backend Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

## Running the Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Running the Server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

Omit the dropdb command the first time you run tests.

## API Reference

### Getting Started

- Base URL: Currently this application is only hosted locally. The backend is hosted at `http://127.0.0.1:5000/`
- Authentication: This version does not require authentication or API keys.

### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return three types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 405 - method not allowed

### Endpoints

#### GET /categories

- General: Returns a list of categories.
- Sample: `curl http://127.0.0.1:5000/categories`<br>

        {
            "categories": {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            },
            "success": true
        }

#### GET /questions

- General:
  - Returns a list of questions.
  - Results are paginated in groups of 10.
  - Also returns list of categories and total number of questions.
- Sample: `curl http://127.0.0.1:5000/questions`<br>

        {
            "categories": {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            },
            "questions": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
                {
                    "answer": "Tom Cruise",
                    "category": 5,
                    "difficulty": 4,
                    "id": 4,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                },
                {
                    "answer": "Maya Angelou",
                    "category": 4,
                    "difficulty": 2,
                    "id": 5,
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                },
                {
                    "answer": "Edward Scissorhands",
                    "category": 5,
                    "difficulty": 3,
                    "id": 6,
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                },
                {
                    "answer": "Muhammad Ali",
                    "category": 4,
                    "difficulty": 1,
                    "id": 9,
                    "question": "What boxer's original name is Cassius Clay?"
                },
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                    "answer": "George Washington Carver",
                    "category": 4,
                    "difficulty": 2,
                    "id": 12,
                    "question": "Who invented Peanut Butter?"
                },
                {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                },
                {
                    "answer": "Agra",
                    "category": 3,
                    "difficulty": 2,
                    "id": 15,
                    "question": "The Taj Mahal is located in which Indian city?"
                }
        ],
            "success": true,
            "total_questions": 21
        }

#### DELETE /questions/\<int:id\>

- General:
  - Deletes a question by id using url parameters.
  - Returns id of deleted question upon success.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/25`<br>

        {
            "deleted": 25,
            "questions": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
                {
                    "answer": "Tom Cruise",
                    "category": 5,
                    "difficulty": 4,
                    "id": 4,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                },
                {
                    "answer": "Maya Angelou",
                    "category": 4,
                    "difficulty": 2,
                    "id": 5,
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                },
                {
                    "answer": "Edward Scissorhands",
                    "category": 5,
                    "difficulty": 3,
                    "id": 6,
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                },
                {
                    "answer": "Muhammad Ali",
                    "category": 4,
                    "difficulty": 1,
                    "id": 9,
                    "question": "What boxer's original name is Cassius Clay?"
                },
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                    "answer": "George Washington Carver",
                    "category": 4,
                    "difficulty": 2,
                    "id": 12,
                    "question": "Who invented Peanut Butter?"
                },
                {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                },
                {
                    "answer": "Agra",
                    "category": 3,
                    "difficulty": 2,
                    "id": 15,
                    "question": "The Taj Mahal is located in which Indian city?"
                }
            ],
            "success": true,
            "total_questions": 20

  }

#### POST /questions

This endpoint either creates a new question or returns search results.

1. If <strong>no</strong> search term is included in request:

- General:
  - Creates a new question using JSON request parameters.
  - Returns JSON object with newly created question, as well as paginated questions.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": "How Many Countries Have Still The Shilling As Currency", "answer": "Four Tanzania, Somalia, Kenya, Uganda ", "difficulty": 3, "category": "2" }'`<br>

        {
            "created": 27,
            "questions": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
                {
                    "answer": "Tom Cruise",
                    "category": 5,
                    "difficulty": 4,
                    "id": 4,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                },
                {
                    "answer": "Muhammad Ali",
                    "category": 4,
                    "difficulty": 1,
                    "id": 9,
                    "question": "What boxer's original name is Cassius Clay?"
                },
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                    "answer": "George Washington Carver",
                    "category": 4,
                    "difficulty": 2,
                    "id": 12,
                    "question": "Who invented Peanut Butter?"
                },
                {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                },
                {
                    "answer": "The Palace of Versailles",
                    "category": 3,
                    "difficulty": 3,
                    "id": 14,
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                },
                {
                    "answer": "Agra",
                    "category": 3,
                    "difficulty": 2,
                    "id": 15,
                    "question": "The Taj Mahal is located in which Indian city?"
                },
                {
                    "answer": "Escher",
                    "category": 2,
                    "difficulty": 1,
                    "id": 16,
                    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
                }
            ],
            "success": true,
            "total_questions": 21
        }

2. If search term <strong>is</strong> included in request:

- General:
  - Searches for questions using search term in JSON request parameters.
  - Returns JSON object with paginated matching questions.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "what"}'`<br>
  {
  "questions": [
  {
  "answer": "Apollo 13",
  "category": 5,
  "difficulty": 4,
  "id": 2,
  "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  },
  {
  "answer": "Tom Cruise",
  "category": 5,
  "difficulty": 4,
  "id": 4,
  "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  },
  {
  "answer": "Edward Scissorhands",
  "category": 5,
  "difficulty": 3,
  "id": 6,
  "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  },
  {
  "answer": "Muhammad Ali",
  "category": 4,
  "difficulty": 1,
  "id": 9,
  "question": "What boxer's original name is Cassius Clay?"
  },
  {
  "answer": "Lake Victoria",
  "category": 3,
  "difficulty": 2,
  "id": 13,
  "question": "What is the largest lake in Africa?"
  },
  {
  "answer": "Mona Lisa",
  "category": 2,
  "difficulty": 3,
  "id": 17,
  "question": "La Giaconda is better known as what?"
  },
  {
  "answer": "The Liver",
  "category": 1,
  "difficulty": 4,
  "id": 20,
  "question": "What is the heaviest organ in the human body?"
  },
  {
  "answer": "Blood",
  "category": 1,
  "difficulty": 4,
  "id": 22,
  "question": "Hematology is a branch of medicine involving the study of what?"
  },
  {
  "answer": "Lake Naser",
  "category": 3,
  "difficulty": 2,
  "id": 24,
  "question": "What Is Smallest Lake In Africa"
  }
  ],
  "success": true,
  "total_questions": 9
  }

#### GET /categories/\<int:category_id\>/questions

- General:
  - Gets questions by category id using url parameters.
  - Returns JSON object with paginated matching questions.
- Sample: `curl http://127.0.0.1:5000/categories/4/questions`<br>
  {
  "category": "History",
  "questions": [
  {
  "answer": "Maya Angelou",
  "category": 4,
  "difficulty": 2,
  "id": 5,
  "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
  },
  {
  "answer": "Muhammad Ali",
  "category": 4,
  "difficulty": 1,
  "id": 9,
  "question": "What boxer's original name is Cassius Clay?"
  },
  {
  "answer": "George Washington Carver",
  "category": 4,
  "difficulty": 2,
  "id": 12,
  "question": "Who invented Peanut Butter?"
  }
  ],
  "success": true,
  "total_questions": 20
  }

#### POST /quizzes

- General:
  - Allows users to play the quiz game.
  - Uses JSON request parameters of category and previous questions.
  - Returns JSON object with random question not among previous questions.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [17, 18], "quiz_category": {"type": "Art", "id": "2"}}'`<br>

        {
            "question": {
                    "answer": "Jackson Pollock",
                    "category": 2,
                    "difficulty": 2,
                    "id": 19,
                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            },
            "success": true
        }

## Authors

Michael Saad authored the API (`__init__.py`), test suite (`test_flaskr.py`), and this README.<br>
All other project files, including the models and frontend, were created by [Udacity](https://www.udacity.com/) as a project template for the [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).
