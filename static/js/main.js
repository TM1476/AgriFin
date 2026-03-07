document.addEventListener('DOMContentLoaded', () => {
    
    // 4a: Voice NLP Module
    const micBtn = document.getElementById('mic-btn');
    const voiceOutput = document.getElementById('voice-output');

    if (micBtn) {
        micBtn.onclick = () => {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {
                alert("Browser does not support Speech Recognition.");
                return;
            }

            const recognition = new SpeechRecognition();
            recognition.start();
            micBtn.innerText = "Listening...";

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                voiceOutput.innerText = `Extracted Metadata: ${transcript}`;
                micBtn.innerText = "🎤 Start Voice Intake";
            };

            recognition.onerror = () => {
                micBtn.innerText = "🎤 Error (Try Again)";
            };
        };
    }

    // 3a: Neural Scorecard Module
    const scoreBtn = document.getElementById('score-btn');
    const scoreVal = document.getElementById('score-val');
    const statusText = document.getElementById('status-text');

    if (scoreBtn) {
        scoreBtn.onclick = async () => {
            scoreBtn.innerText = "Analyzing Satellite Data...";
            
            try {
                const response = await fetch('/api/score', { method: 'POST' });
                const data = await response.json();
                
                // Update the UI with data from Python
                scoreVal.innerText = data.score;
                statusText.innerText = `${data.status}: ${data.details}`;
                scoreBtn.innerText = "Analysis Complete";
            } catch (error) {
                console.error("Error fetching score:", error);
                statusText.innerText = "Connection Error";
            }
        };
    }
});
