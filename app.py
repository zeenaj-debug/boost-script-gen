import streamlit as st
import requests

# Set professional SaaS page layout
st.set_page_config(page_title="Boost My Business | Intel Engine", layout="wide")

# --- CUSTOM SAAS THEMING (CSS) ---
st.markdown("""
    <style>
        /* Main page background refinement */
        .reportview-container {
            background: #f8f9fa;
        }
        /* Clean corporate headers */
        h1 {
            color: #1e293b;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-weight: 700;
        }
        h2, h3 {
            color: #334155;
            font-weight: 600;
        }
        /* Custom card styling for the script output */
        .script-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            margin-bottom: 16px;
        }
        /* Analytics box layout styling */
        .analytics-box {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 12px;
            margin-bottom: 10px;
        }
        .analytics-title {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 2px;
        }
        .analytics-value {
            font-size: 1.15rem;
            color: #0f172a;
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
st.title("Boost My Business | Sales Intelligence Portal")
st.caption("Proprietary Cold Call Scripting Engine & Google Business Profile Audit Hub")
st.markdown("---")

# --- API CONFIGURATION ---
# Paste your SerpApi key between the quotes below:
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

# --- DATA PARSING ENGINE ---
# Default fallback data if no search has been executed
scraped_rating = 4.0
scraped_reviews = 10
top_competitor = f"Local {industry} Competitor"
competitor_reviews = 75
competitor_rating = 4.8

if run_search:
    with st.spinner("Executing live registry lookup..."):
        try:
            # 1. Target Data Fetch
            target_url = f"https://serpapi.com/search.json?engine=google_maps&q={biz_name}+{suburb}&api_key={SERPAPI_KEY}"
            target_res = requests.get(target_url).json()
            
            if "local_results" in target_res and len(target_res["local_results"]) > 0:
                biz_data = target_res["local_results"][0]
                scraped_rating = biz_data.get("rating", 4.0)
                scraped_reviews = biz_data.get("reviews", 5)
            
            # 2. Competitor Data Fetch
            comp_url = f"https://serpapi.com/search.json?engine=google_maps&q={industry}+in+{suburb}&api_key={SERPAPI_KEY}"
            comp_res = requests.get(comp_url).json()
            
            if "local_results" in comp_res and len(comp_res["local_results"]) > 0:
                for res in comp_res["local_results"]:
                    if biz_name.lower() not in res.get("title", "").lower():
                        top_competitor = res.get("title", "A top competitor")
                        competitor_reviews = res.get("reviews", 50)
                        competitor_rating = res.get("rating", 4.7)
                        break
            st.success("Audit log compiled successfully.")
        except Exception as e:
            st.error("Live lookup timeout. Utilizing local semantic framework.")

# --- HIGHLY READABLE MARKET ANALYTICS PANEL ---
with col1:
    st.markdown("---")
    st.subheader("Market Analytics")
    
    # Prospect Box
    st.markdown(f"""
    <div class="analytics-box">
        <div class="analytics-title">{biz_name} Rating</div>
        <div class="analytics-value">{scraped_rating} ★ | {scraped_reviews} Reviews</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Competitor Box
    st.markdown(f"""
    <div class="analytics-box">
        <div class="analytics-title">Market Leader Rating</div>
        <div class="analytics-value">{competitor_rating} ★ | {competitor_reviews} Reviews</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"Identified Market Rival: **{top_competitor}**")

# --- COGNITIVE SCRIPT BUILDER ---
rep_name = "Alex"

if pillar == "Get Chosen (Reviews Focus)":
    pain_text = f"""you guys are actually showing up right there when someone looks for a {industry} in {suburb}, but looking at the map pack, the problem is {top_competitor} down the road has {competitor_reviews} reviews with a {competitor_rating}-star rating, while you guys are sitting at {scraped_rating} stars."""
    implication_text = f"""And look, what that means in reality is that **most locals are just going to click and call them first** over you because their profile looks safer. It basically means less money in your pocket for local jobs that should probably be coming to {biz_name}."""
    solution_text = f"""What we do at Boost My Business is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly close that gap and look like the obvious choice online."""
    zoom_text = f"""On that Zoom, I'll show you exactly how many reviews you need to overtake {top_competitor} and a look at the automated tool that gets them from your customers in 2 clicks."""

elif pillar == "Get Found (SEO/Maps Focus)":
    pain_text = f"""I was looking for {industry} teams in {suburb} this morning and I noticed that while {top_competitor} is locked into those top spots on the Google Map, {biz_name} is actually buried way further down the listings."""
    implication_text = f"""What that means in the real world is that **you are essentially invisible to about 80% of the locals** searching for help in {suburb}. You're losing high-value local work to teams who aren't better than you, they're just easier to find."""
    solution_text = f"""We specialize in optimizing local listings for {industry} businesses to push you straight into that top Google Map bracket so you're the first business people see when they need a hand."""
    zoom_text = f"""On that Zoom, I’m going to run a live local heat-map for you. It’ll show you exactly where your ranking drops off in {suburb} and the 3 quick fixes to get you back in front of those buyers."""

else: # Save Time
    pain_text = f"""I was checking out your digital setup today and I noticed that if a customer hits your website or socials after-hours, or while you're flat out on a job, there's no fast way for them to instantly message you or get a reply."""
    implication_text = f"""Because consumer attention spans are so short now, if they can't text or chat with you instantly, **they just bounce straight back to Google and message the next guy**. It means you're spending money on marketing but bleeding leads because you're too busy to answer instantly."""
    solution_text = f"""We give {industry} teams a smart webchat and central inbox software that automatically captures those leads and texts them back instantly, keeping them hooked so you don't lose the job while your hands are full."""
    zoom_text = f"""On that Zoom, I'll actually simulate a live lead coming into your business so you can see exactly how the software saves the deal and books it into your calendar automatically while you're asleep."""

# Clean, markdown execution layout
full_script = f"""
**THE HOOK**
"Hey, it's {rep_name} here from Boost My Business. Have you guys heard of us at all? ... No worries at all, look—I was actually just doing some lookups on the {industry} market down in {suburb} this morning and {biz_name} popped up on my screen. Reason for the call is..."

**THE PAIN & IMPLICATION**
"...{pain_text} 

{implication_text}"

**THE SOLUTION**
"{solution_text}"

**THE 20-MINUTE ZOOM VALUE BUILD**
"Now, I know you're flat out and I wasn't looking to take up your time while you're working. What I was hoping to do is grab a quick 20-minute Zoom later in the week.

{zoom_text} Even if you don't use us, you'll see exactly what your market looks like right now.

Are you usually tied up on site in the mornings, or is early afternoon a bit cleaner for a quick look at the screen?"
"""

with col2:
    st.subheader("3. Tailored Delivery Script")
    
    # Styled Card Wrapper via Markdown Container
    st.markdown(f'<div class="script-card">{full_script}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("4. Objection Mitigation Matrix")
    
    tab1, tab2, tab3 = st.tabs(["Capacity Constraints", "Existing Agency Contract", "Direct Mail Request"])
    
    with tab1:
        st.markdown(
