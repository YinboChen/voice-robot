
from flask import Flask, request,jsonify,render_template, make_response
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# initialize the flask app
app = Flask(__name__)
#new thread
# def pic():
#     lena = mpimg.imread('1.png')
#     plt.imshow(lena)
#     plt.show()

respond = "Vacuum Robot"

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # return a fulfillment response
    if action == 'poweron':      
        respond = "power on! hello! Nice to see you again!"     
        return {'fulfillmentText': respond }

    elif action =='poweroff':
        respond = "power off! I am going to sleep."
        return {'fulfillmentText': respond}

    elif action =='return':
        respond = "Okay! I will go back soon!"
        return {'fulfillmentText': respond}

    elif action =='startclean':
        respond = "Okay! Clean is start!"
        return {'fulfillmentText': respond}

    elif action =='stopclean':
        respond = "All right! I am stopping!"
        return {'fulfillmentText': respond}

@app.route('/index',methods =['GET','POST'])
def index():
     return '<iframe allow="microphone;" width="350" height="430" src="https://console.dialogflow.com/api-client/demo/embedded/e4605fb2-a4e4-43b4-b224-e3eb874f4048"> </iframe>'


    
# create a route for webhook
@app.route('/webhook', methods=['GET','POST'])
def webhook():

    # return response
    return jsonify(results())
    #return jsonify({'fulfillmentText': results()})

    

    

    # run the app
if __name__ == '__main__':
   app.run()
   