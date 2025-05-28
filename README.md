python -m venv env
source env/Scripts/activate
which python3

### To install fastapi
pip install fastapi

### To install uvicorn
pip install "uvicorn[standard]"

### To runserver
uvicorn main:app --reload

When you need to receive form fields instead of JSON, you can use Form.
# To use forms, first install python-multipart.
pip install python-multipart.