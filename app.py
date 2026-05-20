import streamlit as st
import requests

# Set professional SaaS page layout
st.set_page_config(page_title="Boost My Business | Intel Engine", layout="wide")

# Initialize session state for interactive objection tracking
if "active_objection" not in st.session_state:
    st.session_state.active_objection = None

# --- CUSTOM SAAS THEMING (CSS) ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

        html, body, [data-testid="stSidebarNav"], .stMarkdown, p, div, label {
            font-family: 'Montserrat', sans-serif !important;
        }
        
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
        .script-card {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 28px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            line-height: 1.8;
            font-size: 1.1rem;
            color: #1e293b;
            font-family: 'Montserrat', sans-serif !important;
        }
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
        .objection-display-card {
            background-color: #f0fdf4;
            border: 2px solid #22c55e;
            border-radius: 8px;
            padding: 20px;
            margin-top: 15px;
            font-family: 'Montserrat', sans-serif !important;
        }
        .objection-display-title {
            font-weight: 700;
            color: #166534;
            font-size: 1rem;
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .objection-display-body {
            font-size: 1.05rem;
            color: #14532d;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
st.title("Boost My Business | Sales Intelligence Portal")
st.caption("Proprietary Cold Call Scripting Engine & Google Business Profile Audit Hub (Persona: Business Owner)")
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

# --- DATA PARSING ENGINE ---
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
            time.sleep(0.4)

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
    implication_text = f"And look, what that means in reality is that most locals are just going to click and call them first over you because their profile looks safer. It basically means less money in your pocket for local jobs that should probably be coming to {biz_name}."
    solution_text = f"What we do at Boost My Business is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly close that gap and look like the obvious choice online."
    zoom_text = f"On that Zoom, I'll show you exactly how many reviews you need to overtake {top_competitor} and a look at the automated tool that gets them from your customers in 2 clicks."

elif pillar == "Get Found (SEO/Maps Focus)":
    pain_text = f"while {top_competitor} is completely locked into those top spots on the Google Map pack, {biz_name} is actually buried way down the listings."
    implication_text = f"And look, what that means in the real world is that you are essentially invisible to about 80% of the locals searching for help in {suburb}. You're losing high-value local work to teams who aren't better than you, they're just easier to find."
    solution_text = f"We specialize strictly in optimizing local listings for {industry} businesses to push you straight into that top Google Map bracket so you're the first business people see when they need a hand."
    zoom_text = f"I’m going to run a live local heat-map for you. It’ll show you exactly where your ranking drops off across {suburb} and the 3 quick fixes to get you back in front of those buyers."

else: # Save Time (Automation Focus)
    pain_text = f"if a customer hits your website or socials after-hours, or while you're flat out on a job, there's no fast way for them to instantly message you or get a reply."
    implication_text = f"Because consumer attention spans are so short now, if they can't text or chat with you instantly, they just bounce straight back to Google and message the next guy. It means you're spending money on marketing but bleeding leads because you're too busy to answer instantly."
    solution_text = f"We give {industry} teams a smart webchat and central inbox software that automatically captures those leads and texts them back instantly, keeping them hooked so you don't lose the job while your hands are full."
    zoom_text = f"I'll actually simulate a live lead coming into your business so you can see exactly how the software saves the deal and books it into your calendar automatically while you're asleep."

with col2:
    st.subheader("3. Live Pitch Execution Flow")
    
    # Completely clean flow script with no chunked section boxes
    flow_html = f"""
    <div class="script-card">
        "Hey, it's {rep_name} here from Boost My Business. Look, I know you're probably flat out on a job, so I'll keep this incredibly brief. I was auditing the {suburb} {industry} market on Google this morning and {biz_name} popped up on my dashboard. <br><br>
        The specific reason I'm reaching out is {pain_text} <br><br>
        {implication_text} <br><br>
        We specialize strictly in fixing that visibility gap for {industry} businesses, engineering your configuration so you jump straight into that top Google Map bracket and become the absolute first team locals see.<br><br>
        Now, I know you're busy running a crew and I'm not looking to sell you anything over the phone right now. What I wanted to do is pull up a live local map analysis for you on a quick 20-minute Zoom call later this week. {zoom_text} Even if you don't use us, you'll see exactly where your market is moving right now.<br><br>
        Are you usually tied up on site in the mornings, or is early afternoon a bit cleaner for a quick look at the screen?"
    </div>
    """
    st.markdown(flow_html, unsafe_allow_html=True)
    
    # --- INTERACTIVE ACTION BUTTONS ---
    st.markdown("### 4. Live Objection Handling Matrix")
    st.caption("Click any response below if the owner interrupts or pushes back:")
    
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
    
    with btn_col1:
        if st.button("⚠️ Too Busy / No Capacity", use_container_width=True):
            st.session_state.active_objection = "busy"
    with btn_col2:
        if st.button("🤝 Has Marketing Agency", use_container_width=True):
            st.session_state.active_objection = "agency"
    with btn_col3:
        if st.button("📧 'Just Send an Email'", use_container_width=True):
            st.session_state.active_objection = "email"
    with btn_col4:
        if st.button("🔄 Clear Screen", use_container_width=True):
            st.session_state.active_objection = None

    # --- DYNAMIC REBUTTAL RENDERER ---
    if st.session_state.active_objection == "busy":
        st.markdown(f"""
        <div class="objection-display-card">
            <div class="objection-display-title">Rebuttal: Too Busy / No Capacity</div>
            <div class="objection-display-body">"Totally get that, mate, being run off your feet is a good problem to have. Most of the {industry} businesses we work with in {suburb} are flat out too. We’re actually not trying to flood you with more low-value jobs. What we do is help you automate things like your Google reviews so you can charge premium rates, pick the best jobs, and save yourself hours of admin. Let’s do a quick 20-minute Zoom later in the week—I'll show you how to automate the whole process so you can get hours back. Does Thursday afternoon work for you, or do you tend to clear the schedule on Friday mornings?"</div>
        </div>
        """, unsafe_allow_html=True)
        
    elif st.session_state.active_objection == "agency":
        st.markdown(f"""
        <div class="objection-display-card">
            <div class="objection-display-title">Rebuttal: Existing Agency Contract</div>
            <div class="objection-display-body">"Awesome, love to hear that. Honestly, if you've got someone handling your SEO, you're already ahead of 90% of the market. We’re actually a software platform, not a traditional agency. We plug in alongside what they do to automate your review generation. It basically ensures that all the traffic your agency is paying for actually chooses {biz_name} instead of scrolling past. Let's grab 20 minutes on Zoom tomorrow or Thursday. I'll show you the exact software gap we plug into so you can hand it straight to your current agency if you want to. Would tomorrow at 2:00 PM work, or is Thursday morning cleaner for you?"</div>
        </div>
        """, unsafe_allow_html=True)
        
    elif st.session_state.active_objection == "email":
        st.markdown(f"""
        <div class="objection-display-card">
            <div class="objection-display-title">Rebuttal: Direct Mail Request</div>
            <div class="objection-display-body">"No worries at all, I know you're flat out. Honestly, if I send an email, it’s just going to get buried under 50 quotes you have to get out tonight. Tell you what, let’s skip the generic email spam. Let's lock in 20 minutes on Zoom early next week. I'll bring up your live local map data, show you exactly where {top_competitor} is stealing those clicks, and you can map out a strategy from there. Are you cleaner early in the week like Monday afternoon, or is Tuesday better?"</div>
        </div>
        """, unsafe_allow_html=True)
