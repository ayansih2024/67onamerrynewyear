import streamlit as st
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Marauder's Map ⚡", page_icon="🪄", layout="centered")

# auto refresh every 1 second
st_autorefresh(interval=1000, key="refresh")

# ---------- SESSION FLAGS ----------
if "spell_cast_balloons" not in st.session_state:
    st.session_state.spell_cast_balloons = False

if "unlock_balloons" not in st.session_state:
    st.session_state.unlock_balloons = False

# ---------- MAGICAL STYLING ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

h1 {
    text-align: center;
    color: #D4AF37;
    font-family: 'Cinzel', serif;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

h2 {
    color: #8B0000;
    font-family: 'Cinzel', serif;
}

body {
    background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
    color: #E8E8E8;
}

.countdown {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: #D4AF37;
    font-family: 'Cinzel', serif;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
    margin: 20px 0;
}

.message-box {
    padding: 20px;
    border-radius: 8px;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border-left: 4px solid #D4AF37;
    font-size: 16px;
    color: #E8E8E8;
}

.spell-box {
    padding: 12px;
    background: rgba(212, 175, 55, 0.1);
    border-radius: 6px;
    border: 1px solid #D4AF37;
    color: #D4AF37;
    margin: 8px 0;
    font-family: 'Cinzel', serif;
}

.footer {
    text-align: center;
    font-size: 12px;
    color: #8B8B8B;
    margin-top: 50px;
}

.gryffindor {
    color: #8B0000;
}

.slytherin {
    color: #2d5016;
}

.input-label {
    color: #D4AF37;
    font-family: 'Cinzel', serif;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>⚡ Welcome to the Marauder's Map ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#D4AF37; font-size:16px; font-family:Cinzel;'>A Magical Message Just For You ✨</p>", unsafe_allow_html=True)

# ---------- COUNTDOWN TO MAGICAL EVENT ----------
st.markdown("<h2>🕛 Countdown to Midnight Mischief</h2>", unsafe_allow_html=True)

# Get IST (UTC + 5:30)
now = datetime.utcnow() + timedelta(hours=5, minutes=30)

# Target = Jan 1 2026 00:00:00 IST
target = datetime(2026, 1, 1, 0, 0, 0)

remaining = target - now
seconds = int(remaining.total_seconds())

if seconds <= 0:
    st.markdown("<div class='countdown'>⚡ Mischief Managed! ⚡</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#D4AF37; font-size:18px;'>A new year of magic awaits! 🪄✨</p>", unsafe_allow_html=True)

    # Balloons only once
    if not st.session_state.spell_cast_balloons:
        st.balloons()
        st.session_state.spell_cast_balloons = True

else:
    days = seconds // 86400
    hrs = (seconds % 86400) // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    st.markdown(
        f"<div class='countdown'>{days}d {hrs:02d}:{mins:02d}:{secs:02d}</div>",
        unsafe_allow_html=True
    )

st.write("")

# ---------- SECRET SPELL UNLOCK ----------
st.markdown("<h2>🔐 Speak the Secret Spell</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#D4AF37; font-size:14px;'><i>Only true Marauders know this one...</i></p>", unsafe_allow_html=True)

secret = st.text_input("Incantation:iykyk", key="spell_input")

if secret.strip().lower() in ["mischief managed", "expelliarmus", "lumos", "wingardium leviosa","alohomora","accio","expecto patronum","13", "17"]:
    st.success("✨ Spell successful! The Marauder's Map reveals its secrets! ✨")

    # Balloons only first time
    if not st.session_state.unlock_balloons:
        st.balloons()
        st.session_state.unlock_balloons = True

    st.markdown("""
    <div class='message-box'>
    <h3 style='color:#D4AF37; margin-top:0;'>🪄 A Message From the Marauder 🪄</h3>
    <p>
    Hey this is me again, I think we had a great year and i am grateful that you were a part of it. I will always remember the support you gave me during my lowest of lows and the highest of highs.
    <br><br>
    Here's to more adventures, laughter, and those unforgettable moments only we understand. May this year be filled with magic, wonder, and plenty of mischief, ily! ✨
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:#D4AF37;'>📜 Our House Moments</h3>", unsafe_allow_html=True)

    memories = [
        "⚡ 13",
        "🪄 17",
        "📍 67 on a merry new year  🗺️",
        "💀 Avg Whatsapp Voice call"
    ]

    for memory in memories:
        st.markdown(f"<div class='spell-box'>{memory}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h3 style='color:#D4AF37;'>✨ Make a Magical Wish</h3>", unsafe_allow_html=True)
    wish = st.text_area("Write your wish (as if to the Mirror of Erised)…", placeholder="May your wish come true at Hogwarts...")
    if wish:
        st.success("🔮 Your wish has been inscribed in the Marauder's Map! ✨")

elif secret != "":
    st.error("❌ Incorrect incantation... try another spell! 🪄")

st.markdown("<div class='footer'>✨ Made with magic in Python & Streamlit | Mischief Managed ✨</div>", unsafe_allow_html=True)

