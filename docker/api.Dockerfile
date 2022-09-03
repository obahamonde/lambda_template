FROM python:3.9.11

COPY ./ /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN prisma db push
RUN prisma db pull
RUN prisma migrate deploy
RUN prisma generate


EXPOSE 8000:80

CMD ["uvicorn", "api.main:app", "--reload", "--host=0.0.0.0", "--port=80"]