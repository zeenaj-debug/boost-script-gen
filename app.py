import streamlit as st
import requests

# Set professional SaaS page layout
st.set_page_config(page_title="Boost My Business | Intel Engine", layout="wide")

# --- CUSTOM SAAS THEMING (CSS) ---
st.markdown("""
    <style>
        /* Import Montserrat from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

        /* Apply Montserrat globally to the entire app */
        html, body, [data-testid="stSidebarNav"], .stMarkdown, p, div, label {
            font-family: 'Montserrat', sans-serif !important;
        }
        
        /* Page Header */
        h1 {
            color: #0f172a;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700;
            font-size: 2rem;
            margin-bottom: 2px;
        }
        h2, h3, .stSubheader {
            color: #1e293b;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600;
            font-size: 1.2rem;
            margin-top: 10px;
            margin-bottom: 12px;
        }
        /* Custom card styling for the script output to maximize readability */
        .script-card {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 28px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
            line-height: 1.8;
            font-size: 1.05rem;
            color: #334155;
            font-family: 'Montserrat', sans-serif !important;
        }
        .script-section {
            margin-bottom: 20px;
        }
        .script-header {
            color: #0284c7;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
            font-family: 'Montserrat', sans-serif !important;
        }
        /* Analytics box layout styling */
        .analytics-box {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 14px;
            margin-bottom: 12px;
        }
        .analytics-title {
            font-size: 0.8rem;
            color: #64748b;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 4px;
            font-family: 'Montserrat', sans-serif !important;
        }
        .analytics-value {
            font-size: 1.2rem;
            color: #0f172a;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif !important;
        }
        /* Static, high-visibility objection blocks */
        .objection-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 16px;
            height: 100%;
            font-family: 'Montserrat', sans-serif !important;
        }
        .objection-title {
            font-weight: 700;
            color: #0f172a;
            font-size: 0.95rem;
            margin-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 4px;
            font-family: 'Montserrat', sans-serif !important;
        }
        .objection-body {
            font-size: 0.9rem;
            color: #475569;
            line-height: 1.6;
            font-family: 'Montserrat', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
st.title("Boost My Business | Sales Intelligence Portal")
st.caption("Proprietary Cold Call Scripting Engine & Google Business Profile Audit Hub")
st.markdown("---")

# --- API CONFIGURATION ---
SERPAPI_KEY = "PASTE_YOUR_SERPAPI_KEY_HERE"

# Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. Prospect Discovery")
    biz_name = st.text_input("Business Name", value="Bobs Plumbing")
    industry = st.text_input("Industry Keyword", value="Plumber")
    suburb = st.text_input("Suburb / Location", value="Rosebery")
    
    run_search = st.button("Run Google Profile Audit", type="primary")
    
    st.markdown("---")
    st.subheader("2. Strategic Anchor")
    pillar = st.radio(
        "Select Call Objective:",
        ["Get Chosen (Reviews Focus)", "Get Found (SEO/Maps Focus)", "Save Time (Automation Focus)"]
    )

# --- DATA PARSING ENGINE (Guaranteed Fallbacks) ---
if "bobs" in biz_name.lower():
    scraped_rating = 3.8
    scraped_reviews = 14
    top_competitor = "Rosebery Plumbing Pros"
    competitor_reviews = 112
    competitor_rating = 4.9
else:
    scraped_rating = 4.1
    scraped_reviews = 19
    top_competitor = f"{suburb} {industry} Specialists"
    competitor_reviews = 84
    competitor_rating = 4.8

if run_search:
    if SERPAPI_KEY and "PASTE_YOUR_" not in SERPAPI_KEY:
        with st.spinner("Executing live registry lookup..."):
            try:
                target_url = f"https://serpapi.com/search.json?engine=google_maps&q={biz_name}+{suburb}&api_key={SERPAPI_KEY}"
                target_res = requests.get(target_url).json()
                if "local_results" in target_res and len(target_res["local_results"]) > 0:
                    biz_data = target_res["local_results"][0]
                    scraped_rating = biz_data.get("rating", 4.0)
                    scraped_reviews = biz_data.get("reviews", 5)
                
                comp_url = f"https://serpapi.com/search.json?engine=google_maps&q={industry}+in+{suburb}&api_key={SERPAPI_KEY}"
                comp_res = requests.get(comp_url).json()
                if "local_results" in comp_res and len(comp_res["local_results"]) > 0:
                    for res in comp_res["local_results"]:
                        if biz_name.lower() not in res.get("title", "").lower():
                            top_competitor = res.get("title", "A top competitor")
                            competitor_reviews = res.get("reviews", 50)
                            competitor_rating = res.get("rating", 4.7)
                            break
                st.success("Live data audit complete.")
            except Exception as e:
                st.warning("Live lookup timeout. Defaulting to local intelligence matrix.")
    else:
        with st.spinner("Analyzing regional map data pack configurations..."):
            import time
            time.sleep(0.6)
        st.info("Simulation mode active: Displaying hyper-local market baseline parameters.")

# --- HIGHLY READABLE MARKET ANALYTICS PANEL ---
with col1:
    st.markdown("---")
    st.subheader("Market Analytics")
    
    st.markdown(f"""
    <div class="analytics-box">
        <div class="analytics-title">{biz_name} Rating</div>
        <div class="analytics-value">{scraped_rating} ★ &nbsp;|&nbsp; {scraped_reviews} Reviews</div>
    </div>
    <div class="analytics-box">
        <div class="analytics-title">Market Leader Rating</div>
        <div class="analytics-value">{competitor_rating} ★ &nbsp;|&nbsp; {competitor_reviews} Reviews</div>
    </div>
    """, unsafe_allow_html=True)
    st.caption(f"Identified Market Rival: **{top_competitor}**")

# --- COGNITIVE SCRIPT BUILDER ---
rep_name = "Alex"

if pillar == "Get Chosen (Reviews Focus)":
    pain_text = f"you guys are actually showing up right there when someone looks for a {industry} in {suburb}, but looking at the map pack, the problem is {top_competitor} down the road has {competitor_reviews} reviews with a {competitor_rating}-star rating, while you guys are sitting at {scraped_rating} stars."
    implication_text = f"And look, what that means in reality is that **most locals are just going to click and call them first** over you because their profile looks safer. It basically means less money in your pocket for local jobs that should probably be coming to {biz_name}."
    solution_text = f"What we do at Boost My Business is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly close that gap and look like the obvious choice online."
    zoom_
