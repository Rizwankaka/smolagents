Here’s the corrected and updated `README.md` file with the accurate **Demo** section and other improvements:

---

# 🤖 AI Agent Assistant - Streamlit App

A **powerful AI assistant** powered by **Gemini** and built using the **[smolagents](https://github.com/Rizwankaka/smolagents/tree/main)** framework. This app helps you with various tasks, including **stock analysis**, **weather information**, and **general queries**. It provides an interactive and user-friendly interface to interact with an AI agent capable of performing web searches, fetching real-time stock data, and answering general questions.

---

## ✨ Features

- **🔐 Secure API Key Management**: Safely input and manage your Gemini API key through the app's sidebar.
- **💬 Interactive Chat Interface**: Engage in real-time conversations with the AI assistant.
- **📈 Real-Time Stock Information**: Fetch up-to-date stock data using **YFinance**.
- **🔍 Web Search Capabilities**: Perform web searches using **DuckDuckGo**.
- **📱 Responsive Design**: Works seamlessly on both **desktop** and **mobile** devices.
- **💾 Session-Based Chat History**: Maintains a history of your conversation during the session.
- **🚀 Powered by smolagents**: Leverages the **[smolagents](https://github.com/Rizwankaka/smolagents/tree/main)** framework for efficient AI agent creation and management.

---

## 🚀 Demo

Try the live app here: **[AI Agent Assistant](https://smolagents-rizwan.streamlit.app/)**

---

## 🛠️ Installation

Follow these steps to set up and run the AI Agent Assistant on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rizwankaka/smolagents.git
   cd smolagents
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Unix/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Gemini API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey).
   - Create a new API key.
   - Copy the API key for later use.

---

## 🎮 Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Enter your Gemini API key** in the sidebar.

4. **Start chatting** with the AI assistant!

---

## 📝 Example Queries

Here are some examples of what you can ask the AI assistant:

- **Stock Information**:  
  `"What's the current stock price of NVIDIA?"`
  
- **Weather Updates**:  
  `"How's the weather in New York right now?"`
  
- **General Knowledge**:  
  `"Tell me about the latest developments in AI."`

---

## 🔧 Configuration

The app uses the following **environment variables**:

- `GEMINI_API_KEY`: Your Gemini API key (can be entered through the UI).
- `TF_ENABLE_ONEDNN_OPTS`: Set to `'0'` to disable TensorFlow warnings.

---

## 🤝 Contributing

We welcome contributions to the **[smolagents](https://github.com/Rizwankaka/smolagents/tree/main)** project! Here’s how you can contribute:

1. **Fork the repository**.
2. **Create your feature branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE.md](https://github.com/Rizwankaka/smolagents/blob/main/LICENSE.md) file for details.

---

## 🙏 Acknowledgments

- **[Streamlit](https://streamlit.io/)**: For the amazing web app framework.
- **[Gemini](https://deepmind.google/technologies/gemini/)**: For the powerful AI model.
- **[smolagents](https://github.com/Rizwankaka/smolagents/tree/main)**: For the lightweight and efficient AI agent framework.
- **[YFinance](https://github.com/ranaroussi/yfinance)**: For stock data.
- **[DuckDuckGo](https://duckduckgo.com/)**: For search capabilities.

---

## 📞 Support

If you have any questions or run into issues, please **open an issue** in the [GitHub repository](https://github.com/Rizwankaka/smolagents/issues).

---

## 🌟 Show Your Support

If you find this project helpful, please give it a ⭐️ on [GitHub](https://github.com/Rizwankaka/smolagents)! Your support is greatly appreciated.

---

**Happy Chatting!** 🚀

---

This version now includes the correct **Demo** link to your live app: **[https://smolagents-rizwan.streamlit.app/](https://smolagents-rizwan.streamlit.app/)**. Let me know if you need further adjustments!
