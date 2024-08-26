Set Up React Application:

    Create a new React application using create-react-app or another setup method of your choice.

    
    npx create-react-app vad-app
    cd vad-app

Install Dependencies:

    You will need axios to make HTTP requests to your backend API.

    

npm install axios

Run Flask Application:

    Start the Flask server by running:

   

python app.py

Handle Cross-Origin Requests:

    If you're running the React frontend and Flask backend on different ports, you may need to handle CORS (Cross-Origin Resource Sharing). Install and configure flask-cors.



pip install flask-cors

from flask_cors import CORS

CORS(app)
