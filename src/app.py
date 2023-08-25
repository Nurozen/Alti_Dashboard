from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
              <form action='/user_input' method='POST'>
              <input name="input">
              <input type="submit" value="Send">
              </form>
    
            """

@app.route("/user_input", methods=["POST"])
def input():
   
   if "input" not in request.form:
      return(404, "input not found")
   return (f"Input: {request.form['input']}")

if __name__ == "__main__":
  app.run(debug = True)