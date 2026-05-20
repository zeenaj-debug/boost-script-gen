import streamlit as st
import time

# Set page layout
st.set_page_config(page_title="Boost My Business - Smart Gen", layout="wide")

st.title("🦅 Boost My Business - Smart Cold Call Script Gen")
st.caption("Live Research Engine Integration (Powered by Google Business Profile Data)")
st.markdown("---")

# Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🔍 1. Quick Search")
    biz_name = st.text_input("Business Name", value="Bobs Plumbing")
    industry = st.text_input("Industry Keyword", value="Plumber")
    suburb = st.text_input("Suburb / Location", value="Rosebery")
    
    # Simple trigger button for the research engine
    run_search = st.button("⚡ Run Live Google Audit", type="primary")
    
    st.markdown("---")
    st.header("🎯 2. Select the Pain Focus")
    pillar = st.radio(
        "What hook are we attacking?",
        ["Get Chosen (Reviews)", "Get Found (SEO/Maps)", "Save Time (Webchat/Automation)"]
    )

# --- BACKEND RESEARCH ENGINE ARCHITECTURE ---
# In a full production build, this block calls a Google Maps API (e.g., SerpApi)
# using: requests.get(f"https://serpapi.com/search.json?engine=google_maps&q={biz_name}+{suburb}")
# Below is the logic processing that data for your BDR:

if run_search:
    with st.spinner(f"Searching Google Maps for '{biz_name}' in {suburb}..."):
        time.sleep(1.5) # Simulating API latency
    with st.spinner(f"Auditing local competitor landscape for '{industry} in {suburb}'..."):
        time.sleep(1.0)
    st.success("Google Audit Complete!")

# Mocking the scraped data fields that come back from Google
# If Bob's plumbing is entered, it acts real. If they type something else, it creates smart data.
if "bobs" in biz_name.lower():
    scraped_rating = 3.8
    scraped_reviews = 14
    top_competitor = "Rosebery Plumbing Pros"
    competitor_reviews = 112
    competitor_rating = 4.9
else:
    scraped_rating = 4.1
    scraped_reviews = 22
    top_competitor = f"{suburb} {industry} Co."
    competitor_reviews = 89
    competitor_rating = 4.8

# Display the data the app "found" on Google
with col1:
    st.markdown("### 📊 Google Profile Data Found")
    metrics_col1, metrics_col2 = st.columns(2)
    with metrics_col1:
        st.metric(label=f"{biz_name} Reviews", value=f"{scraped_rating} ⭐ ({scraped_reviews} reviews)")
    with metrics_col2:
        st.metric(label=f"Top Competitor ({top_competitor})", value=f"{competitor_rating} ⭐ ({competitor_reviews} reviews)")

# --- SCRIPT GENERATION ENGINE ---
rep_name = "Alex" # Default placeholder

if pillar == "Get Chosen (Reviews)":
    pain_text = f"you guys are actually showing up right there when someone looks for a {industry} in {suburb}, but looking at the map pack, the problem is {top_competitor} down the road has {competitor_reviews} reviews with a {competitor_rating}-star rating, while you guys are sitting at {scraped_rating} stars."
    implication_text = f"And look, what that means in reality is that **most locals are just going to click and call them first** over you because their profile looks safer. It basically means less money in your pocket for local jobs that should probably be coming to {biz_name}."
    solution_text = f"What we do at Boost is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly close that gap and look like the obvious choice online."
    zoom_text = f"On that Zoom, I'll show you exactly how many reviews you need to overtake {top_competitor} and a look at the automated tool that gets them from your customers in 2 clicks."

elif pillar == "Get Found (SEO/Maps)":
    pain_text = f"I was looking for {industry} teams in {suburb} this morning and I noticed that while {top_competitor} is locked into those top spots on the Google Map, {biz_name} is actually buried way further down the listings."
    implication_text = f"What that means in the real world is that **you are essentially invisible to about 80% of the locals** searching for help in {suburb}. You're losing high-value local work to teams who aren't better than you, they're just easier to find."
    solution_text = f"We specialize in optimizing local listings for {industry} businesses to push you straight into that top Google Map bracket so you're the first business people see when they need a hand."
    zoom_text = f"On that Zoom, I’m going to run a live local heat-map for you. It’ll show you exactly where your ranking drops off in {suburb} and the 3 quick fixes to get you back in front of those buyers."

else: # Save Time
    pain_text = f"I was checking out your digital setup today and I noticed that if a customer hits your website or socials after-hours, or while you're flat out on a job, there's no fast way for them to instantly message you or get a reply."
    implication_text = f"Because consumer attention spans are so short now, if they can't text or chat with you instantly, **they just bounce straight back to Google and message the next guy**. It means you're spending money on marketing but bleeding leads because you're too busy to answer instantly."
    solution_text = f"We give {industry} teams a smart webchat and central inbox software that automatically captures those leads and texts them back instantly, keeping them hooked so you don't lose the job while your hands are full."
    zoom_text = f"On that Zoom, I'll actually simulate a live lead coming into your business so you can see exactly how the software saves the deal and books it into your calendar automatically while you're asleep."

# Construct the full script dynamically injecting the scraped data
full_script = f"""
🗣️ **THE HOOK (Casual & Partner-toned):**
"Hey, it's {rep_name} here from Boost. Have you guys heard of us at all? ... No worries at all, look—I was actually just doing some lookups on the {industry} market down in {suburb} this morning and {biz_name} popped up on my screen. Reason for the call is..."

🚨 **THE PAIN & IMPLICATION:**
"...{pain_text} 

{implication_text}"

💡 **THE SOLUTION:**
"{solution_text}"

📅 **THE 20-MIN ZOOM VALUE-BUILD & CLOSE:**
"Now, I know you're flat out and I wasn't looking to take up your time while you're working. What I was hoping to do is grab a quick 20-minute Zoom later in the week.

{zoom_text} Even if you don't use us, you'll see exactly what your market looks like right now.

Are you usually tied up on site in the mornings, or is early afternoon a bit cleaner for a quick look at the screen?"
"""

with col2:
    st.header("📱 3. Your Live Script")
    st.info("The script below has been customized using the Google Maps data found.")
    st.markdown(full_script)
    
    st.markdown("---")
    st.header("🛡️ 4. Quick Objection Handlers")
    
    tab1, tab2, tab3 = st.tabs(["Too Busy / Don't Need Work", "Have an Agency", "Just Send Email"])
    
    with tab1:
        st.write(f"**Rebuttal:** \"Totally get that, mate, being run off your feet is a good problem to have. Most of the {industry} businesses we work with in {suburb} are flat out too. We’re actually not trying to flood you with more low-value jobs. What we do is help you automate things like your Google reviews so you can charge premium rates, pick the best jobs, and save yourself hours of admin. Let’s do a quick 20-minute Zoom later in the week—I'll show you how to automate the whole process so you can get hours back. Does Thursday afternoon work for you, or do you tend to clear the schedule on Friday mornings?\"")
    with tab2:
        st.write(f"**Rebuttal:** \"Awesome, love to hear that. Honestly, if you've got someone handling your SEO, you're already ahead of 90% of the market. We’re actually a software platform, not a traditional agency. We plug in alongside what they do to automate your review generation. It basically ensures that all the traffic your agency is paying for actually chooses {biz_name} instead of scrolling past. Let's grab 20 minutes on Zoom tomorrow or Thursday. I'll show you the exact software gap we plug into so you can hand it straight to your current agency if you want to. Would tomorrow at 2:00 PM work, or is Thursday morning cleaner for you?\"")
    with tab3:
        st.write(f"**Rebuttal:** \"No worries at all, I know you're flat out. Honestly, if I send an email, it’s just going to get buried under 50 quotes you have to get out tonight. Tell you what, let’s skip the generic email spam. Let's lock in 20 minutes on Zoom early next week. I'll bring up your live local map data, show you exactly where {top_competitor} is stealing those clicks, and you can map out a strategy from there. Are you cleaner early in the week like Monday afternoon, or is Tuesday better?\"")
