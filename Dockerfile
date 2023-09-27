FROM python:3.11

WORKDIR /root

#Copys
COPY ./src /root/src/
COPY ./requirements.txt /root/requirements.txt
COPY ./tests /root/tests/

#Runs
RUN pip3 install -r /root/requirements.txt

#Config
EXPOSE 5005:5005

#Startup
CMD [ "python3", "-m" , "flask", "--app", "/root/src/app", "run", "--port=5005","--host=0.0.0.0"]