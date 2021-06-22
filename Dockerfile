FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/blog/.local/bin:${PATH}"
RUN mkdir /blog
WORKDIR /blog
#COPY blog/ /blog/
COPY requirements.txt /blog/
RUN useradd -ms /bin/bash blog
RUN chown -R blog:blog /blog
USER blog
RUN pip install -r requirements.txt
