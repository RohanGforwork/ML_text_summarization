

# ML TEXT Summarization and sentiment analysis for X tweets 

This project allows users to input their tweets, which are processed through multiple steps in the backend to provide translated, slang-checked, and summarized text, followed by an optional short inference of the content. The flow includes user input, translation via Google Translate, slang detection, and text summarization. This tool is aimed at simplifying and summarizing complex or slang-heavy tweets for better understanding.

## Features

- **Frontend:**
  - Accepts input from users in the form of Twitter tweets.
  
- **Backend:**
  - **Translation:** Translates the tweet content using Google Translate.
  - **Slang Detection:** Detects slang in the tweet using advanced slang detection models.
  - **Summarization:** Summarizes the translated tweet to give a more concise version.
  - **Inference:** Provides a short inference or sentiment analysis based on the content (optional).

## Technologies Used

- **Frontend:**
  - HTML/CSS/JavaScript (or any JS framework like React or Angular)
  
- **Backend:**
  - Python (Flask/Django)
  - Google Translate API
  - Slang Detection Library (e.g., custom model or pre-existing library)
  - Text Summarization Model (e.g., Hugging Face Transformers, BART)
  - Sentiment Analysis/Inference (using NLP models)

## Requirements

To run this project locally, you will need to set up the following:

### Frontend

- A web server that can serve the frontend (e.g., using `npm` or `webpack`).
  
### Backend

- Python 3.7 or later.
- Required libraries:
  - Flask or Django
  - googletrans (for Google Translate)
  - Text summarization and slang detection models (e.g., Hugging Face transformers)
  - Requests, Flask-CORS (for frontend-backend communication)

```bash
pip install googletrans==4.0.0-rc1
pip install transformers
pip install requests
pip install flask
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/twitter-sentiment-summary.git
   cd twitter-sentiment-summary
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up and run the backend server:

   ```bash
   python app.py
   ```

4. Open the frontend (in your browser) to interact with the app. 

---

## Usage

1. Open the application in your browser (once the backend and frontend are running).
2. Enter a tweet into the input field.
3. After submitting, the backend will:
   - Translate the tweet into English.
   - Detect and correct any slang words.
   - Summarize the text for a more concise version.
4. After receiving the summary, the user can optionally request a short inference or sentiment analysis of the tweet.

## Example Flow:

1. **User Input:**
   - *"Yo! This party was lit, so much fun!"*

2. **Backend Processing:**
   - Translation: "Yo! This party was fun, so much enjoyment!"
   - Slang Detection: Recognizes "lit" as slang for fun or exciting.
   - Summarization: "The party was fun!"

3. **User Request:**
   - **Optional Inference:** "The tweet reflects excitement and positive emotions regarding a party."

---

## Contributing

We welcome contributions! If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or further inquiries, feel free to open an issue or reach out to the maintainers at `sathwiknh@gmail.com`.

