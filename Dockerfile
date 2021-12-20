FROM python:3.8-alpine
RUN mkdir /mcash
ADD . /mcash
WORKDIR /mcash
RUN pip install -r requirements.txt
CMD ["python", "./src/mcashd.py"]
