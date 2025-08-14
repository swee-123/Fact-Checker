# AI Fact Checker with Groq API & Streamlit

An AI-powered fact-checking application built with **Groq API**, **Streamlit**, and optional **web search integration**.  
It uses structured prompts and external search tools to verify facts in real-time.

---

## 📂 Project Structure

project/
│
├── main.py # CLI entry point
├── streamlit_app.py # Streamlit web UI
├── .env.example # Example environment variables
├── requirements.txt # Python dependencies
│
├── config/
│ ├── prompts.yaml # Prompt templates
│ └── settings.py # Configuration loader
│
├── src/
│ ├── init.py
│ ├── fact_checker.py # Main fact-checking logic
│ ├── prompt_chains.py # Prompt templates and chains
│ ├── search_tools.py # Web search integration
│ ├── utils.py # Helper functions
│
├── tests/
│ ├── test_fact_checker.py
│ └── test_search_tools.py
│
├── examples/
│ ├── example_queries.txt
│ └── demo_notebook.ipynb

yaml
Copy
Edit

---

## ⚙️ Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ai-fact-checker.git
cd ai-fact-checker
2️⃣ Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure environment variables
Copy .env.example to .env and add your keys:

bash
Copy
Edit
cp .env.example .env
Edit .env:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
SEARCH_API_KEY=your_search_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here
🚀 Running the App
CLI Mode
bash
Copy
Edit
python main.py "Is the Great Wall of China visible from space?"
Streamlit Mode
bash
Copy
Edit
streamlit run streamlit_app.py
📄 Example Query
You can test example queries from:

bash
Copy
Edit
examples/example_queries.txt
Or in Streamlit by typing:

arduino
Copy
Edit
"Did humans land on the moon in 1969?"
🧪 Testing
Run the tests with:

bash
Copy
Edit
pytest tests/
📦 Requirements
Python 3.9+

groq

streamlit

requests

python-dotenv

pyyaml

pytest

📝 License
This project is licensed under the MIT License.
Feel free to modify and use for personal or commercial projects.

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

yaml
Copy
Edit

---

Do you want me to now **merge all your `.py`, `.yaml`, and `.env.example` files into a single master code block** so you can copy your entire project in one go.