FROM python:3.6
LABEL maintainer="Sibonelo Ngobese, ngobese.s1@gmail.com"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip \ 
    && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD [ "app.py" ]
