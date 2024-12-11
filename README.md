# Poems Api Automation

This project was created as part of the interview process for **Sporty**.

## Project Overview

The task was to create arbitrary **REST API** tests for the application:
[PoetryDB GitHub Repository](https://github.com/thundercomb/poetrydb#readme)

The main tools used for solving this task were **Python**, **Pytest** as the test runner, and the **requests** library for API communication.

## How to Run the Tests
After cloning the project, execute the following commands to run the tests:

**Linux/Mac Environment:**\
python3 -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
pytest test_poems.py

**Windows Environment:**\
python3 -m venv venv\
venv\Scripts\activate\
pip install -r requirements.txt\
pytest test_poems.py

## Test Cases
The table below contains the test cases for the implemented API tests:

| Test Case ID | Test Description                                           | Input Parameters                                                                                 | Expected Output                                                                                 | Pass Criteria                                                                                   |
|--------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| TC_01        | Verify that the API returns status 200 and the correct line count for all poems by the author. | author: "Adam Lindsay Gordon"                                                                    | - API response status: 200                                                                      | Line count matches the number of non-empty lines in the poem.                                   |
|              |                                                           |                                                                                                  | - Correct line count matches the actual number of lines in the poems.                          |                                                                                                 |
| TC_02        | Verify that the API returns status 200 and the correct line count for all poems by the author. | author: "Alan Seeger"                                                                            | - API response status: 200                                                                      | Line count matches the number of non-empty lines in the poem.                                   |
|              |                                                           |                                                                                                  | - Correct line count matches the actual number of lines in the poems.                          |                                                                                                 |
| TC_03        | Verify that the API returns status 200 and the correct line count for all poems by the author. | author: "Alexander Pope"                                                                         | - API response status: 200                                                                      | Line count matches the number of non-empty lines in the poem.                                   |
|              |                                                           |                                                                                                  | - Correct line count matches the actual number of lines in the poems.                          |                                                                                                 |
| TC_04        | Verify that the API returns status 200 and the correct author for a given poem title.          | title: "Thoughts On The Works Of Providence", expected_author: "Phillis Wheatley"               | - API response status: 200                                                                      | The author in the API response matches the expected_author.                                     |
|              |                                                           |                                                                                                  | - The author matches the expected author for the poem title.                                   |                                                                                                 |
| TC_05        | Verify that the API returns status 200 and the correct author for a given poem title.          | title: ""All Is Vanity, Saith the Preacher"", expected_author: "George Gordon, Lord Byron"       | - API response status: 200                                                                      | The author in the API response matches the expected_author.                                     |
|              |                                                           |                                                                                                  | - The author matches the expected author for the poem title.                                   |                                                                                                 |
| TC_06        | Verify that the API returns status 200 and the correct author for a given poem title.          | title: ""And the sins of the fathers shall be"", expected_author: "Stephen Crane"               | - API response status: 200                                                                      | The author in the API response matches the expected_author.                                     |
|              |                                                           |                                                                                                  | - The author matches the expected author for the poem title.                                   |                                                                                                 |
