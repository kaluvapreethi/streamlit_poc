# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8002", "--server.address=0.0.0.0"]
