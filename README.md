python -m venv env
source env/Scripts/activate
which python3

### To install fastapi
pip install fastapi

### To install uvicorn
pip install "uvicorn[standard]"

### To runserver
uvicorn main:app --reload