from flask import Flask, render_template_string, request, redirect, url_for
app = Flask(__name__)

# Use a global list for simplicity. In a real application, you'd use a database.
messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global messages
    if request.method == 'POST':
        if 'send' in request.form:
            message = request.form.get('message')
            messages.append({'text': message, 'sender': 'user'})
            messages.append({'text': f'Received your message: "{message}"', 'sender': 'guide'})
        
        elif 'reset' in request.form:
            messages = []
    return render_template_string("""
    <html>
        <head>
            <!-- Add Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
            <!-- Add FontAwesome -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
            <script src="./static/script.js"></script>
            <style>
                .message {
                    margin: 10px;
                    padding: 10px;
                }
                .user {
                    background-color: #d0f0d0;
                }
                .guide {
                    background-color: #d0d0f0;
                }
                .scrollable {
                    height: 300px;
                    overflow-y: auto;
                 #send-button, #speak-button {
                        border: 5px;
                        font: inherit;
                        background-color: transparent;
                        margin: 2px;
                        appearance: none;
                        padding: 10px 12px 3px 3px ;
                        cursor: pointer;
                        font-size: 24px;
                        display: flex;
                        } 

                        #reset-button {
                        border: none;
                        font: inherit;
                        background-color: transparent;
                        margin: 0;
                        appearance: none;
                        padding: 10px 12px;
                        cursor: pointer;
                        font-size: 24px;
                        display: flex;
                        }
  
                }
            </style>
           
        </head>
        <body>
         
            <div class="container">
                <h1 class="text-center">Smart Tourist</h1>
                <p>Hello there! I'm your Smart Tourist guide. I can answer anything, with up-to-date information.</p>
                <div class="scrollable">
                    {% for message in messages %}
                        <div class="message alert {{ 'alert-success' if message.sender == 'user' else 'alert-primary' }}">
                            {{ message.text }}
                        </div>
                    {% endfor %}
                </div>
                <form method="post" class="form-inline justify-content-center">
                    <input type="text" id="message-input" name="message" class="form-control mb-2 mr-sm-2" placeholder="Type your message here...">
                    
                    
                    
                    <button type="button" onclick="record()" id="speak-button"  class="btn btn-primary send"><i class="fa fa-microphone"></i></button>
                        </br>
                        <div>
                    <button  name="send" id="send-button" class="btn btn-primary send">
                            <i class='fa fa-paper-plane'></i>
                        </button>
                    <button name="reset" id="reset-button" class="btn btn-primary reset">
                            <i class="fas fa-sync"></i>
                        </button>
                        </div>
                
                </form>
                <div>
                    <select id="language" name="language">
                    <option value="English">English</option>
                    <option value="Urdu">Urdu</option>
                    <option value="Arabic">Arabic</option>
                    <option value="French">French</option>
                    <option value="Spanish">Spanish</option>
                    </select>
                </div>
            </div>

        </body>
    </html>
    """, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
