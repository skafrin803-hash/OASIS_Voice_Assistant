# TASK 1 - Voice Assistant | Oasis Infobyte

## Completion Rule: Advanced Tier Implemented

### Beginner Features:
- Voice input via speech_recognition
- Greeting on "hello"
- Time/Date on request
- Web search
- Error handling
- pyttsx3 TTS

### Advanced Features Implemented:
- [x] Natural Language Understanding: Intent parsing from free-form sentences
- [x] Send email via voice using smtplib
- [x] Timed reminder with audible alert
- [x] Live weather via OpenWeatherMap API
- [x] General knowledge QA via Wikipedia API
- [x] Custom commands via config.json

### Setup
1. Get free weather API key from https://openweathermap.org/api
2. Replace YOUR_OPENWEATHER_API_KEY_HERE in code
3. For email, create a dummy Gmail and use App Password: https://myaccount.google.com/apppasswords
4. pip install -r requirements.txt
5. python voice_assistant.py

### Privacy Consideration
- Microphone data is processed only when listening and sent to Google Speech Recognition API temporarily.
- No voice recordings are stored locally.
- Email credentials and weather API key are stored locally in code only for demo purpose.
- Weather city name and search queries are sent to respective public APIs (OpenWeatherMap, Wikipedia, Google).

### Tech Stack
Python, speech_recognition, pyttsx3, nltk concept, smtplib, OpenWeatherMap API, wikipedia