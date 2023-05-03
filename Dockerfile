FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install MarkupSafe
RUN pip install tensorflow==1.15.0
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/adrianc-a/tf-slim.git@remove_contrib
COPY . /code/