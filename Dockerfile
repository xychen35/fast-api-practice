FROM python:3.8.3

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . app/blog

ENV PYTHONPATH=/blog-env
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0"]