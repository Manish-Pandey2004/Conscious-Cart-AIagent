import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# --- Setup Streamlit UI ---
st.set_page_config(page_title="Conscious Cart AI", layout="centered")
st.title("Conscious Cart AI Agent 🛒")
st.write("by Code Craft")

# --- Image ---
image_url = "https://pbs.twimg.com/media/GxV9tYzX0AAPL2W.jpg"  # Ensure this is a valid image URL
st.image(image_url, caption="Conscious Cart AI", use_container_width=True)  # use_container_width instead of use_column_width
# --- Image ---
image_url = "https://preview.redd.it/how-did-the-hakla-meme-even-start-v0-yo1essir8fgf1.jpeg?width=1051&format=pjpg&auto=webp&s=ef70f63703efe3a90b51e5b4e9ead939a2e4bf89"  # Ensure this is a valid image URL
st.image(image_url, caption="Conscious Cart AI", use_container_width=True)  # use_container_width instead of use_column_width
# --- Image ---
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhBA4T_BrpjbjhLr1yAdUDnJgME2ebJQ40qw&s"  # Ensure this is a valid image URL
st.image(image_url, caption="Conscious Cart AI", use_container_width=True)  # use_container_width instead of use_column_width
# --- Session State Initialization ---
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "api_validated" not in st.session_state:
    st.session_state.api_validated = False

# --- Function to Load LLM (only once) ---
@st.cache_resource(show_spinner=False)
def load_llm(api_key):
    return ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash-latest",
        temperature=0,
        google_api_key=api_key,
    )

# --- API Key Input ---
if not st.session_state.api_validated:
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    if api_key:
        try:
            # Try initializing the LLM to validate the key
            llm = load_llm(api_key)
            # ACTUALLY INVOKE A TEST PROMPT TO VALIDATE KEY
            _ = llm.invoke([HumanMessage(content="Say hello")])

            st.session_state.api_key = api_key
            st.session_state.api_validated = True
            st.success("API key validated successfully!")
        except Exception as e:
            import traceback
            st.error(f"API validation failed: {str(e)}")
            st.exception(e)  # Optional: shows full traceback in Streamlit
            st.stop()

# --- Proceed if API is validated ---
if st.session_state.api_validated:
    llm = load_llm(st.session_state.api_key)

    # --- Input: Product Name or URL ---
    product_input = st.text_input("Enter a Product NAME or URL:")

    # --- Function: Scrape Product Details ---
    def scrape_product_details(url):
        try:
            resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "Unknown Product"
            return title
        except Exception as e:
            return f"Error scraping: {e}"

    # --- Function: Generate Product Description ---
    def generate_details_from_name(name):
        try:
            response = llm.invoke([HumanMessage(content=f"Describe the product: {name}")])
            return response.content
        except Exception as e:
            return f"Error generating details: {e}"

    # --- Function: Analyze Environmental Impact ---
    def analyze_environmental_impact(details):
        try:
            response = llm.invoke([HumanMessage(content=f"Analyze the environmental impact of this product: {details}")])
            return response.content
        except Exception as e:
            return f"Error analyzing impact: {e}"

    # --- Function: Generate Recommendation ---
    def generate_recommendation(impact):
        try:
            response = llm.invoke([HumanMessage(content=f"Based on this environmental impact, what would you recommend?: {impact}")])
            return response.content
        except Exception as e:
            return f"Error generating recommendation: {e}"

    # --- Analyze Button ---
    if st.button("Analyze"):
        if not product_input:
            st.warning("Please enter a product URL or name.")
        else:
            with st.spinner("Processing..."):
                if product_input.lower().startswith("http"):
                    details = scrape_product_details(product_input)
                else:
                    details = generate_details_from_name(product_input)

                st.markdown("### 📦 Product Description")
                st.markdown(details)

                impact = analyze_environmental_impact(details)
                st.markdown("### 🌍 Environmental Impact")
                st.markdown(impact)

                recommendation = generate_recommendation(impact)
                st.markdown("### 📝 Final Recommendation")
                st.markdown(recommendation)


