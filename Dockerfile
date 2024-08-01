FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app /app/app
COPY tests /app/tests

EXPOSE 5000
CMD ["python", "app/main.py"]
