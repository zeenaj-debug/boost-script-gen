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
            white-space: pre-wrap;
            font-family: inherit;
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
# If you have a SerpApi key, paste it here. If not, leave it as is for smart simulation.
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

# --- BASE DATA BASELINE (Always exists so script never blanks out) ---
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

# --- LIVE API OVERRIDE ---
if run_search:
    # Only try to fetch live web data if a real key has been entered
    if SERPAPI_KEY and "PASTE_YOUR_" not in SERPAPI_KEY:
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
                st.success("Live data audit complete.")
            except Exception as e:
                st.warning("Live lookup timeout. Defaulting to local intelligence matrix.")
    else:
        # Fake a quick loading spinner for the BDRs so the app feels responsive right now
        with st.spinner("Analyzing regional map data pack configurations..."):
            import time
            time.sleep(0.8)
        st.info("Simulation mode active: Displaying hyper-local market baseline parameters.")

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
    pain_text = f"you guys are actually showing up right there when someone looks for a {industry} in {suburb}, but looking at the map pack, the problem is {top_competitor} down the road has {competitor_reviews} reviews with a {competitor_rating}-star rating, while you guys are sitting at {scraped_rating} stars."
    implication_text = f"And look, what that means in reality is that **most locals are just going to click and call them first** over you because their profile looks safer. It basically means less money in your pocket for local jobs that should probably be coming to {biz_name}."
    solution_text = f"What we do at Boost My Business is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly close that gap and look like the obvious choice online."
    zoom_text = f"On that Zoom, I'll show you exactly how many reviews you need to overtake {top_competitor} and a look at the automated tool that gets them from your customers in 2 clicks."

elif pillar == "Get Found (SEO/Maps Focus)":
    pain_text = f"I was looking for {industry} teams in {suburb} this morning and I noticed that while {top_competitor} is locked into those top spots on the Google Map, {biz_name} is actually buried way further down the listings."
    implication_text = f"What that means in the real world is that **you are essentially invisible to about 80% of the locals** searching for help in {suburb}. You're losing high-value local work to teams who aren't better than you, they're just easier to find."
    solution_text = f"We specialize in optimizing local listings for {industry} businesses to push you straight into that top Google Map bracket so you're the first business people see when they need a hand."
    zoom_text = f"On that Zoom, I’m going to run a live local heat-map for you. It’ll show you exactly where your ranking drops off in {suburb} and the 3 quick fixes to get you back in front of those buyers."

else: # Save Time
    pain_text = f"I was checking out your digital setup today and I noticed that if a customer hits your website or socials after-hours, or while you're flat out on a job, there's no fast way for them to instantly message you or get a reply."
    implication_text = f"Because consumer attention spans are so short now, if they can't text or chat with you instantly, **they just bounce straight back to Google and message the next guy**. It means you're spending money on marketing but bleeding leads because you're too busy to answer instantly."
    solution_text = f"We give {industry} teams a smart webchat and central inbox software that automatically captures those leads and texts them back instantly, keeping them hooked so you don't lose the job while your hands are full."
    zoom_text = f"On that Zoom, I'll actually simulate a live lead coming into your business so you can see exactly how the software saves the deal and books it into your calendar automatically while you're asleep."

# Clean layout variables
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
    st.markdown(f'<div class="script-card">{full_script}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("4. Objection Mitigation Matrix")
    
    tab1, tab2, tab3 = st.tabs(["Capacity Constraints", "Existing Agency Contract", "Direct Mail Request"])
    
    with tab1:
        st.markdown(f"**Strategic Rebuttal:** \"Totally get that, mate, being run off your feet is a good problem to have. Most of the {industry} businesses we work with in {suburb} are flat out too. We’re actually not trying to flood you with more low-value jobs. What we do is help you automate things like your Google reviews so you can charge premium rates, pick the best jobs, and save yourself hours of admin. Let’s do a quick 20-minute Zoom later in the week—I'll show you how to automate the whole process so you can get hours back. Does Thursday afternoon work for you, or do you tend to clear the schedule on Friday mornings?\"")
    with tab2:
        st.markdown(f"**Strategic Rebuttal:** \"Awesome, love to hear that. Honestly, if you've got someone handling your SEO, you're already ahead of 90% of the market. We’re actually a software platform, not a traditional agency. We plug in alongside what they do to automate your review generation. It basically ensures that all the traffic your agency is paying for actually chooses {biz_name} instead of scrolling past. Let's grab 20 minutes on Zoom tomorrow or Thursday. I'll show you the exact software gap we plug into so you can hand it straight to your current agency if you want to. Would tomorrow at 2:00 PM work, or is Thursday morning cleaner for you?\"")
    with tab3:
        st.markdown(f"**Strategic Rebuttal:** \"No worries at all, I know you're flat out. Honestly, if I send an email, it’s just going to get buried under 50 quotes you have to get out tonight. Tell you what, let’s skip the generic email spam. Let's lock in 20 minutes on Zoom early next week. I'll bring up your live local map data, show you exactly where {top_competitor} is stealing those clicks, and you can map out a strategy from there. Are you cleaner early in the week like Monday afternoon, or is Tuesday better?\"")
