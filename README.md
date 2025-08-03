# 🛒 Conscious Cart – AI-Powered Eco Product Analyzer

**Conscious Cart** is an intelligent agent designed to empower consumers to make environmentally conscious shopping decisions. By simply providing a product name or a URL, users can get an instant, AI-driven analysis of the product's environmental impact, complete with recommendations for more sustainable alternatives. This tool leverages the power of **Google Gemini** to deliver insightful and actionable advice, helping you shop smarter and greener.

---

## 🚀 Live Demo

👉 **Try the app live on Streamlit:** [https://conscious-cart-ai-agent-v3.streamlit.app/](https://conscious-cart-ai-agent-v3.streamlit.app/)

---

## 🌿 Key Features

* **Dual Input System**: Accepts either a direct **product name** (e.g., "plastic water bottle") or a **URL** from e-commerce sites.
* **Intelligent Data Retrieval**:
    * For URLs, it **scrapes the product page** for details.
    * If scraping fails, it intelligently **analyzes keywords from the URL** itself as a fallback.
    * For product names, it uses Gemini to **generate a hypothetical, typical description** for analysis.
* **AI-Powered Analysis**: Utilizes **Google Gemini** for a multi-faceted evaluation:
    * **Summarizes** key product characteristics.
    * **Evaluates** the likely environmental and sustainability impact.
    * **Suggests** greener, more eco-friendly alternatives when a product is not recommended.
* **Clear & Actionable Recommendations**: Provides a final verdict to guide your purchasing decisions:
    * ✅ **RECOMMENDED**: The product has a relatively low environmental impact.
    * ⚠️ **NOT RECOMMENDED**: The product has significant environmental concerns.
    * 🤔 **NEUTRAL**: The product has a mixed or average environmental impact.

---
## 🌍 Aligning with Global Goals

This project directly contributes to **Goal 12: Responsible Consumption and Production** of the United Nations' Sustainable Development Goals. By providing transparent, AI-driven insights into the environmental impact of products, Conscious Cart equips consumers with the necessary tools to make informed and responsible choices, fostering a global shift towards more sustainable consumption patterns.

---
## 🧬 How It Works: The Agent Workflow

The Conscious Cart agent follows a logical, multi-step process to deliver its analysis:

1.  **User Input**: The agent starts by prompting the user for a product name or URL.
2.  **Input Routing**: It determines whether the input is a URL or a product name.
3.  **Data Gathering**:
    * **If URL**: Attempts to scrape the webpage. If it fails, it extracts keywords from the URL string.
    * **If Name**: Prompts Gemini to create a detailed, hypothetical product description.
4.  **Impact Analysis**: The gathered product details are sent to Gemini with a specific prompt to analyze the environmental impact and provide a verdict.
5.  **Recommendation Generation**:
    * If the verdict is **NOT RECOMMENDED**, the agent asks Gemini to suggest specific, sustainable alternatives.
    * The final analysis and any alternatives are formatted into a clear, easy-to-read report.

---

## 🧪 Sample Interaction

Here’s a sample run showing the agent's capabilities when analyzing a product name.

**User Input:**
> Gold Ornaments

**Agent Output:**

> ### 📦 Product Description
>
> Gold ornaments are decorative items made from gold, used to adorn the body. They encompass a vast range of styles, designs, and purposes... Designs range from simple, minimalist pieces to elaborate, heavily embellished items featuring gemstones, intricate carvings, filigree work, and enamel...
>
> ### 🌍 Environmental Impact
>
> The environmental impact of gold ornaments is significant and multifaceted, stemming primarily from gold mining... Mining operations, particularly open-pit mining, cause widespread habitat destruction... and release large quantities of toxic chemicals, including mercury and cyanide, into water bodies...
>
> ### 📝 Final Recommendation
>
> Based on the environmental impact, I recommend a multi-pronged approach:
>
> 1.  **Prioritize recycled gold**: Actively seek out and purchase jewelry made from recycled gold to reduce the demand for newly mined gold.
> 2.  **Choose responsibly sourced gold**: Look for certifications from reputable organizations like the Responsible Jewellery Council (RJC).
> 3.  **Value longevity and repair**: Treat your gold jewelry with care to extend its lifespan and repair damaged pieces instead of replacing them.

---

## 🚀 Installation & Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JAYANTRANJANJHA/Conscious-Cart-AI-Agent.git](https://github.com/JAYANTRANJANJHA/Conscious-Cart-AI-Agent.git)
    cd Conscious-Cart-AI-Agent
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You will need to create a `requirements.txt` file containing `streamlit`, `requests`, `beautifulsoup4`, `langchain-google-genai`)*

3.  **Set up your API Key:**
    You will need a Google Gemini API key. The application will prompt you to enter it when you first run it.

---

## 🛠️ Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
2.  **Enter your API Key** in the input field when prompted.
3.  Once validated, **enter a product name or URL** into the main input box.
4.  Click the **"Analyze"** button and wait for the AI-powered recommendation.

---

## 🤝 Contribute

Contributions are welcome! Whether it's improving the scraper, refining the prompts, or adding new features, please feel free to fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the License - see the `LICENSE` file for details.

---

**Make smarter, greener choices — one product at a time. 🌎**
