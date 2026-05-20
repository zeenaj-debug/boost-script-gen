import streamlit as st

# Set page layout
st.set_page_config(page_title="Boost My Business - Script Gen", layout="wide")

st.title("🚀 Boost My Business Cold Call Script Generator")
st.caption("Down-to-earth, high-impact scripts built on the Pain → Implication → Solution framework.")
st.markdown("---")

# Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📋 1. Inputs")
    rep_name = st.text_input("Your Name", value="Alex")
    biz_name = st.text_input("Prospect Business Name", value="Apex Plumbing")
    industry = st.text_input("Industry (e.g., Plumber, Electrician)", value="Plumber")
    suburb = st.text_input("Suburb / Location", value="Richmond")
    competitor = st.text_input("Local Competitor Name", value="Tradie Central")
    
    st.markdown("---")
    st.header("🎯 2. Select the Pain Focus")
    pillar = st.radio(
        "What hook are we attacking?",
        ["Get Chosen (Reviews)", "Get Found (SEO/Maps)", "Save Time (Webchat/Automation)"]
    )

# Logic to swap script text based on selection
if pillar == "Get Chosen (Reviews)":
    pain_text = f"you guys are actually showing up right there when someone looks for a {industry} in {suburb}, but the problem is {competitor} down the road has way more 5-star reviews than you guys do."
    implication_text = f"And look, what that means in reality is that **most people are just going to click and call them first** over you. It basically means less money in your pocket for local jobs that should probably be coming to you guys."
    solution_text = f"What we do at Boost is help {industry} teams automatically get those reviews rolling in right when you finish a job, so you instantly look like the safest, most trusted team online and take back those calls."
    zoom_text = f"On that Zoom, I'll show you exactly how many reviews you need to overtake {competitor} and a look at the automated tool that gets them from your customers in 2 clicks."

elif pillar == "Get Found (SEO/Maps)":
    pain_text = f"I was looking for {industry} teams in {suburb} this morning and I noticed that while your competitors are locked into those top 3 spots on the Google Map, {biz_name} is actually buried way further down the page."
    implication_text = f"What that means in the real world is that **you are essentially invisible to about 80% of the locals** searching for help. You're losing high-value local work to teams who aren't better than you, they're just easier to find."
    solution_text = f"We specialize in optimizing local listings for {industry} businesses to push you straight into that top Google Map bracket so you're the first business people see when they need a hand."
    zoom_text = f"On that Zoom, I’m going to run a live local heat-map for you. It’ll show you exactly where your ranking drops off in {suburb} and the 3 quick fixes to get you back in front of those buyers."

else: # Save Time
    pain_text = f"I was checking out your digital setup today and I noticed that if a customer hits your website or socials after-hours, or while you're flat out on a job, there's no fast way for them to instantly message you or get a reply."
    implication_text = f"Because consumer attention spans are so short now, if they can't text or chat with you instantly, **they just bounce straight back to Google and message the next guy**. It means you're spending money on marketing but bleeding leads because you're too busy to answer instantly."
    solution_text = f"We give {industry} teams a smart webchat and central inbox software that automatically captures those leads and texts them back instantly, keeping them hooked so you don't lose the job while your hands are full."
    zoom_text = f"On that Zoom, I'll actually simulate a live lead coming into your business so you can see exactly how the software saves the deal and books it into your calendar automatically while you're asleep."

# Construct the full script
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
    st.info("Copy the script below or read it directly off the screen.")
    st.markdown(full_script)
    
    st.markdown("---")
    st.header("🛡️ 4. Quick Objection Handlers")
    
    tab1, tab2, tab3 = st.tabs(["Too Busy / Don't Need Work", "Have an Agency", "Just Send Email"])
    
    with tab1:
        st.write(f"**Rebuttal:** \"Totally get that, mate, being run off your feet is a good problem to have. Most of the {industry} businesses we work with in your area are flat out too. We’re actually not trying to flood you with more low-value jobs. What we do is help you automate things like your Google reviews and webchat so you can charge premium rates, pick the best jobs, and actually save yourself a few hours of admin every week. Let’s do a quick 20-minute Zoom later in the week—I'll show you how to automate the whole process so you can get hours back. Does Thursday afternoon work for you, or do you tend to clear the schedule on Friday mornings?\"")
    with tab2:
        st.write(f"**Rebuttal:** \"Awesome, love to hear that. Honestly, if you've got someone handling your SEO, you're already ahead of 90% of the market. We’re actually a software platform, not a traditional agency. We plug in alongside what they do to automate your review generation. It basically ensures that all the traffic your agency is paying for actually chooses {biz_name} instead of scrolling past. Tell you what, I’m not asking you to change agencies. Let's grab 20 minutes on Zoom tomorrow or Thursday. I'll show you the exact software gap we plug into so you can hand it straight to your current agency if you want to. Would tomorrow at 2:00 PM work, or is Thursday morning cleaner for you?\"")
    with tab3:
        st.write(f"**Rebuttal:** \"No worries at all, I know you're flat out. Honestly, if I send an email, it’s just going to get buried under 50 quotes you have to get out tonight. Tell you what, let’s skip the generic email spam. Let's lock in 20 minutes on Zoom early next week. I'll bring up your live local map data, show you exactly where your competitors are stealing those clicks, and you can map out a strategy from there. Are you cleaner early in the week like Monday afternoon, or is Tuesday better?\"")
