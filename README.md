# 🛒 AI-Enhanced Product Management System

A lightweight **Product Management System** built with [Gradio](https://www.gradio.app/), featuring full CRUD (Create, Read, Update, Delete) operations plus an **AI-powered product lookup** using the [Groq API](https://groq.com/) (`llama-3.1-8b-instant`).

## ✨ Features

- **Load Dummy Data** — populate the store with 10 sample electronics products
- **View Products** — list all products currently in memory
- **Add Product** — add a new product by ID, name, and price
- **Search Product** — look up a product by its ID
- **Update Product** — edit the name/price of an existing product
- **Delete Product** — remove a product by ID
- **🤖 AI Product Details** — type any product name and get an AI-generated description via Groq's LLM

## 🖥️ Tech Stack

| Component | Technology |
|---|---|
| UI | [Gradio](https://www.gradio.app/) (Blocks API) |
| AI backend | [Groq API](https://console.groq.com/) — `llama-3.1-8b-instant` |
| Data storage | In-memory Python dictionary (no database — data resets on restart) |
| Language | Python 3 |

## 📁 Project Structure

```
.
├── app.py              # Main Gradio application (entry point)
├── requirements.txt    # Python dependencies
└── README.md
```

## 🚀 Running Locally

1. Clone the repository:
   ```bash
   git clone https://huggingface.co/spaces/<your-username>/<your-space-name>
   cd <your-space-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Groq API key as an environment variable:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"      # macOS/Linux
   setx GROQ_API_KEY "your_groq_api_key_here"         # Windows
   ```
   Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

4. Launch the app:
   ```bash
   python app.py
   ```

5. Open the local URL Gradio prints in your terminal (typically `http://127.0.0.1:7860`).

## ☁️ Deploying on Hugging Face Spaces

This app is designed to run as a **Gradio Space**:

1. Create a new Space at [huggingface.co/new-space](https://huggingface.co/new-space) with **SDK: Gradio**.
2. Upload `app.py` and `requirements.txt` (and this `README.md`).
3. In the Space's **Settings → Variables and secrets**, add a secret named `GROQ_API_KEY` with your Groq API key. **Never commit API keys directly into code.**
4. The Space will automatically install dependencies and launch `app.py`.

## ⚠️ Notes & Limitations

- **No persistence:** products are stored in memory and reset whenever the app restarts.
- **Single shared state:** all users of the same running instance see the same product list.
- **API key required:** the AI Product Details feature will not work without a valid `GROQ_API_KEY`.

## 📄 License

Add a license of your choice (e.g., MIT) here.