const speakButton = document.getElementById('speak-button');
const messageInput = document.getElementById('message-input');
let recognition;
let isRecording = false; // Add a boolean flag

speakButton.addEventListener('click', () => {
  if ('webkitSpeechRecognition' in window) {
    // Browser supports Speech Recognition API
    startStopRecognition();
  } else {
    // Browser doesn't support Speech Recognition API
    alert('Sorry, your browser does not support speech recognition.');
  }
});

function startStopRecognition() {
  if (isRecording) {
    // Stop recording if already active
    recognition.stop();
    speakButton.textContent = 'Start Recording';
    isRecording = false;
  } else {
    // Start recording
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US'; // Adjust language as needed

    recognition.onresult = (event) => {
      const transcript = event.results
        .map((result) => result[0].transcript)
        .join('');
      messageInput.value = transcript;
    };

    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event);
      alert('Speech recognition failed. Please try again.');
      speakButton.textContent = 'Start Recording';
      isRecording = false;
    };

    recognition.onend = () => {
      recognition = null;
      speakButton.textContent = 'Start Recording';
      isRecording = false;
    };

    speakButton.textContent = 'Stop Recording';
    recognition.start();
    isRecording = true;
  }
}
