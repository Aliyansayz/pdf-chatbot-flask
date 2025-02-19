<!DOCTYPE html>
<html>
        <head>
            <!-- Add Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
            <!-- Add FontAwesome -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://code.jquery.com/ui/1.13.0/jquery-ui.min.js"></script>
            <script src="./static/script.js"></script>
           
            
            <style>

                body {
                    font-family: 'Roboto', sans-serif;
                }

                .container {
                    width: 100%;
                }

                .row {
                    margin: 0;
                }

                .display-4 {
                    font-weight: 700; /* Bold */
                }

                .lead {
                    font-weight: 400; /* Regular */
                }


                .container {
                    width: 100%;
                }

                .row {
                    margin: 0;
                }

                .chat-element {
                    height: 200px;
                    overflow-y: auto;
                    padding: 10px;
                    display: flex;
                    flex-direction: column;
                }

                .message-box {
                    border-radius: 10px;
                    margin-bottom: 10px;
                    padding: 10px;
                    color: white;
                    word-wrap: break-word; /* This will prevent long text from overflowing */
                    display: inline-block; /* This will make the width of the box adjust to the text */
                }

                .sender {
                    background-color: #008000; /* Emerald Green */
                    align-self: flex-end; /* This will align the sender's messages to the right */
                }

                .bot {
                    background-color: #808080; /* Gray */
                    align-self: flex-start; /* This will align the bot's responses to the left */
                }

                
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

                    #upload-button {
                    color: white;
                    background-color: #007bff;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                    font-size: 14px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                    margin-top: 12px;
                    }

                    #message-input {
                    bottom: 0;
                    width: 100%;
                    flex-grow: 1;
                    font-size: 16px;
                    box-sizing: border-box;
                    border: none;
                    padding: 10px 0 10px 12px;
                    border-radius: 40px 0 0 40px;
                    background-color: transparent;
                    height: auto;
                    }

                    .input-group {
                    position: relative;
                    display: flex;
                    flex-wrap: nowrap;
                    align-items: stretch;
                    width: 100%;
                    border-radius: 40px;
                    border: 1px solid #2d2d2d;
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
            <script>

        // Define an object that maps each location to an array of questions
        const locationQuestions = {
            Makkah: [
                "What are the other must-visit places in Makkah ?",
                "Where can I perform Tawaf around the Kaaba ?",
                "What is the significance of the Kaaba"
            ],
            Mina: [
                "How can I travel back to Makkah from Mina ?",
                "What is the purpose of staying in Mina during Hajj ?",
                "What facilities are available in Mina ?",
                "How can I travel back to Makkah from Mina ?"
            ],
            Arfat: [
                "Where can I stay in Arafat during Hajj ?",
                "What happens on the Day of Arafat, the most important day of Hajj ?"
            
            ],
        };

        function loadlocationQuestions() {
            const location = document.getElementById("location").value;
            let questions = "<ul>";
            // Loop through the questions array for the selected location and create a list item for each question
            for (let question of locationQuestions[location]) {
                questions += `<li onclick="copytextLocation('${question}')">${question}</li>`;
            }
            questions += "</ul>";
            document.getElementById("locquestions").innerHTML = questions;
        }

        function copytextLocation(text) {
            document.getElementById("message-input").value = text;
        }

        //______________________________________________

        // Define an object that maps each food preference to an array of questions
        const foodQuestions = {
            NonGluten: [
                "Enlist some egg non Gluten breakfast and deserts in Saudi Arabia ?"
            ],
            EggFree: [
                "Enlist some egg free top dishes  in Saudi Arabia ?"
            ],
            NonDairy: [
                "What are top  non dairy products in Saudi Arabia ?"
            ],
        };

        function loadQuestions() {
            const food = document.getElementById("food").value;
            let questions = "<ul>";
            // Loop through the questions array for the selected food and create a list item for each question
            for (let question of foodQuestions[food]) {
                questions += `<li onclick="copyText('${question}')">${question}</li>`;
            }
            questions += "</ul>";
            document.getElementById("foodquestions").innerHTML = questions;
        }

        function copyText(text) {
            document.getElementById("message-input").value = text;
        }
    </script>

         


            <div class="container-main">
                <div class="row">
                <!-- Heading -->
                <div class="col-12">
                    <h1 class="display-4">Smart Tourist</h1>
                </div>

                <!-- Description -->
                <div class="col-12">
                    <p class="lead">Hello there! I'm your SmarTourist guide. How can I assist you ?</p>
                </div>
                </div>
            </div>
            <div>
    
    
</div>    

            <div class="container">
    <div class="row">
       
        <!-- Chat Element -->
        <div class="col-12">
            <div class="chat-element" style="height: 500px; overflow-y: auto;">
                {% for message in messages %}
                    <div class="message-box sender" style="text-align: right;">
                        <div class="me">{{ message.sender }}</div>
                    </div>
                    <div class="message-box bot" style="text-align: left;">
                        <div class="message-line">{{ message.response }}</div>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
</div>


                    
                </div>
    

                <form method="post" class="form-inline justify-content-center"  >
                    <input type="text" id="message-input" name="message"  class="form-control mb-2 mr-sm-2" style="width: 80%;" placeholder="Type your message here...">
                    
                    <button  name="send" id="send-button" class="btn btn-primary send">
                            <i class='fa fa-paper-plane'></i>
                        </button>
                    <button type="button" onclick="record()" id="speak-button"  class="btn btn-primary send"><i class="fa fa-microphone"></i></button>
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

        <div>
            <h4>FAQs</h4>

            <label for="location">Select your location:</label>
                <select id="location" onchange="loadlocationQuestions()">
                    <option value="Makkah">Makkah</option>
                    <option value="Mina">Mina</option>
                    <option value="Arfat">Arfat</option>
                </select>
                <br><br>
                <div id="locquestions"></div>


            <label for="food">Select your food preference:</label>
                 <select id="food" onchange="loadQuestions()">
                   <option value="NonGluten">Non Gluten</option>
                   <option value="EggFree">Egg Free</option>
                   <option value="NonDairy">Non Dairy</option>
                    </select>
                    <br><br>
                    
                <div id="foodquestions"></div>

            

        </div> 
    
        </body>
    </html>

