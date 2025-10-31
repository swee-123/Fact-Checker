🧠 AI Fact Checker

AI Fact Checker is a Python-based project designed to verify factual statements using AI models and online search results.
It supports both CLI (Command-Line Interface) and Streamlit Web App modes, making it easy to use for developers, researchers, and learners.

🚀 Features

🧩 AI-powered fact validation using GROQ API

🔍 Web search integration for real-time information retrieval

💬 CLI and Streamlit modes for flexibility

⚙️ Configurable via .env for secure API key management

🧪 Automated testing with pytest

📦 Project Structure
ai-fact-checker/
│
├── main.py                  # CLI entry point
├── streamlit_app.py         # Streamlit web interface
├── examples/
│   └── example_queries.txt  # Sample fact-check queries
├── tests/
│   └── test_app.py          # Unit tests
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
└── README.md                # Project documentation

⚙️ Installation and Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-fact-checker.git
cd ai-fact-checker

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Copy the example environment file and add your API keys:

cp .env.example .env


Then open .env and fill in your credentials:

GROQ_API_KEY=your_groq_api_key_here
SEARCH_API_KEY=your_search_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here

🧭 Usage
🖥️ CLI Mode

Run a fact-check query directly from the terminal:

python main.py "Is the Great Wall of China visible from space?"

🌐 Streamlit Web App

Launch the interactive web interface:

streamlit run streamlit_app.py


Then open the displayed local URL in your browser and start querying.

📄 Example Queries

You can test the app with the included examples:

examples/example_queries.txt


Or type a question directly in Streamlit:

"Did humans land on the moon in 1969?"

🧪 Testing

Run automated tests to verify functionality:

pytest tests/

📦 Requirements

Python 3.9+

groq

streamlit

requests

python-dotenv

pyyaml

pytest

Install all dependencies via:

pip install -r requirements.txt

🧰 Tech Stack
Category	Tools / Libraries
Language	Python 3.9+
Frameworks	Streamlit, CLI
AI Model	GROQ API
Web Search	Custom Search API
Configuration	YAML, dotenv
Testing	Pytest
📝 License

This project is licensed under the MIT License.
Feel free to modify and use it for personal or commercial purposes.

🤝 Contributing

Contributions are welcome!
If you'd like to add features or fix bugs:

Fork the repository

Create a new branch (feature/your-feature)

Commit your changes

Open a pull request

For major updates, please open an issue first to discuss your ideas.

🌟 Acknowledgements

GROQ API for language model inference

Streamlit for the interactive UI

Google Custom Search API for information retrieval
