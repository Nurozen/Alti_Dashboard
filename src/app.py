import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import pika
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
import sys, os, logging, threading


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rande.sqlite3'
app.config['SECRET_KEY'] = "random string"
metrics = PrometheusMetrics(app)
metrics.info("exam", "test_app", version="1.0.0")

db = SQLAlchemy(app)

name = "<users>"

"""def rabbit_receiver(self):
    global db
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='telemetry')

    def new(ch, method, properties, body):
        with app.app_context():
         rand_int = int(body)
         logging.info(f" [x] Received {rand_int}")
         randonee = Randonee(rand_int)
         
         db.session.add(randonee)
         db.session.commit()
        logging.info(f"{rand_int} added to db")
        
    channel.basic_consume(queue='telemetry', on_message_callback=new, auto_ack=True)

    logging.info('Waiting for messages...')
    channel.start_consuming()
receiver = threading.Thread(target=rabbit_receiver, args=(1,))
receiver.start()"""


class Randonee(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    random_int = db.Column(db.String(100))

    def __init__(self, random_int):
        self.random_int = random_int

@app.route('/analysis')
def show_all():
      rand_ints = Randonee.query.all()
      intes = []
      for inte in rand_ints:
          intes.append(inte.random_int)
      
      x = intes
      y = sorted(intes)

      plt.plot(x, y)
      plt.title(f"{name}'s Telemetry Signal")
      img = io.BytesIO()
      plt.savefig(img, format='png')
      img.seek(0)

      img_b64 = base64.b64encode(img.getvalue()).decode()
      html = f'<img src="data:image/png;base64,{img_b64}" class="blog-image">'
      return render_template_string(html)
   

@app.route('/health', methods = ['GET'])
def health_check():
    return 200

@app.route('/new', methods = ['GET'])
def new():
   rand_int=str(random.randint(0, 99))
   """connection = pika.BlockingConnection(
   pika.ConnectionParameters(host='localhost'))
   channel = connection.channel()

   channel.queue_declare(queue='telemetry')

   channel.basic_publish(exchange='', routing_key='telemetry', body=rand_int)
   print(" [x] Sent 'Telemetry Sent'")
   connection.close()
   return (f"Added: {rand_int} to queue")"""

   with app.app_context():
         logging.info(f" [x] Received {rand_int}")
         randonee = Randonee(rand_int)
         
         db.session.add(randonee)
         db.session.commit()
         logging.info(f"{rand_int} added to db")
   return (f"Added: {rand_int} to queue")

@app.route("/form")
def home():
    return """
              <label>Input Username</label>
              <form action='/user_input' method='POST'>
              <input name="input">
              <input type="submit" value="Send">
              </form>
    
            """

@app.route("/user_input", methods=["POST"])
def input():
   global name
   
   if "input" not in request.form:
      return(404, "input not found")
   name = request.form['input']
   return (f"Username: {request.form['input']}")

"""@app.route("/input_analysis", methods=["POST"])
def input_analysis():
   if "input_resp" not in request.form:
      return(404, "input not found")
   
   user_text = request.form['input_resp'].split(":")
   return (user_text[1:])"""

if __name__ == '__main__':
   try:
      with app.app_context():
         db.create_all()
      app.run(debug = False, port=5556, host="localhost")
   except KeyboardInterrupt:
        print('Interrupted')
        try:
            #receiver.interrupt()
            sys.exit(0)
        except SystemExit:
            os._exit(0)