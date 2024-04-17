FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && rm requirements.txt
RUN pip install gunicorn

EXPOSE 5050

CMD ["gunicorn", "-b", "0.0.0.0:5050", "app:app"]
