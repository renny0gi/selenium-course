# Page Object in use repo
Important! use python version 3.8 otherwise fix the code like this f'{var=}'
install:
- git clone https://github.com/renny0gi/selenium-course
- cd selenium-course
- git checkout final_project
- activate venv(or create for Windows: python -m venv venv; .\venv\Scripts\activate)
- pip install -r requirements.txt
- pytest -vs --tb=line --language=en -m need_review