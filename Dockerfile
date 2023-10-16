FROM python:3.11

WORKDIR /root

#Copys
COPY ./src /root/src/
COPY ./requirements.txt /root/requirements.txt
COPY ./tests /root/tests/
COPY ./rabbit_install_script.sh /root/rabbit_install_script.sh

#Runs
RUN pip3 install -r /root/requirements.txt
RUN sh /root/rabbit_install_script.sh

#Config
EXPOSE 5005:5005

#Startup
#CMD [ "python3", "-m" , "flask", "--app", "/home/runner/work/Alti_Dashboard/Alti_Dashboard", "run", "--port=5005","--host=0.0.0.0"]
CMD [ "python3", "/home/runner/work/Alti_Dashboard/Alti_Dashboard/app.py"]