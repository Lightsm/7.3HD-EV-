FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pytest bandit

EXPOSE 5000

CMD ["python", "app.py"]