import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ahmad Sufi | Cloud Portfolio",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* GLOBAL THEME */
    .stApp {
        background: linear-gradient(to bottom right, #0f172a, #1e293b);
        color: #e2e8f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* CUSTOM HEADERS WITH GRADIENT */
    h1 {
        background: -webkit-linear-gradient(45deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        padding-bottom: 10px;
    }
    
    h2, h3 {
        color: #38bdf8;
        font-weight: 600;
    }

    /* CARD STYLE (Glassmorphism) */
    .css-card {
        background-color: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* LINK STYLING */
    a {
        color: #38bdf8 !important;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }

    /* SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }

    /* PROGRESS BAR COLOR */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #38bdf8, #818cf8);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: PROFILE & CONTACT ---
with st.sidebar:
    # Profile Image Handling
    try:
        image = Image.open("profile.png")
        st.image(image, width=200) 
    except FileNotFoundError:
        st.warning("⚠️ Please save your photo as 'profile.png'")

    st.markdown("## Ahmad Sufi bin Khairul Azha")
    st.write("📍 **Melaka Tengah, Melaka**")
    st.write("📧 [sufiazha1812@gmail.com](mailto:sufiazha1812@gmail.com)")
    st.write("📞 **017-605 7914**")
    
    # --- SOCIAL LINKS (FIXED) ---
    # 1. LinkedIn (Note: The URL is long, keep it on ONE line)
    st.markdown("[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg) LinkedIn Profile](https://www.linkedin.com/in/ahmad-sufi-khairul-azha-0630813a5/)")
    
    # 2. GitHub (Note: I changed the icon color to FFFFFF (White) so it is visible)
    st.markdown("[![GitHub](https://img.icons8.com/material-outlined/24/FFFFFF/github.png) GitHub Profile](https://github.com/sufzha)")

    st.markdown("---")
    
    st.subheader("Soft Skills")
    soft_skills = ["Leadership", "Communication", "Problem-solving", "Teamwork", "Adaptability"]
    for skill in soft_skills:
        st.markdown(f"✅ {skill}")

    st.markdown("---")
    
    # Resume Download Button
    with open("portfolio.py", "rb") as file: 
        st.download_button(
            label="📄 Download Full CV",
            data=file,
            file_name="Ahmad_Sufi_Resume.pdf",
            mime="application/pdf"
        )

# --- MAIN CONTENT ---

# HERO SECTION
st.markdown('<div class="css-card">', unsafe_allow_html=True)
st.title("Cloud Computing Enthusiast & Innovator")
st.write("""
A curious and adaptable Diploma student in Cloud Computing with strong hands-on experience in server setup, virtualization, web development, and AI prompting. Skilled in Linux and Windows server administration, container-based deployment, and full-stack development. An international STEM innovation gold medalist with proven leadership, problem-solving ability, and a calm approach under pressure. Passionate about continuous learning and building a strong foundation for a successful career in IT and cloud computing.
""")
st.markdown('</div>', unsafe_allow_html=True)

# TECHNICAL SKILLS SECTION
st.markdown("## 🛠 Technical Proficiency")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.subheader("☁️ Cloud & Virtualization")
    st.markdown("""
    *   **Server Admin:** Linux (Ubuntu/Debian) & Windows Server
    *   **Virtualization:** Proxmox, VirtualBox, VMware
    *   **Containers:** Docker (Basic Deployment)
    *   **Hardware:** Raspberry Pi Server, ESP32, Basic Soldering
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.subheader("💻 Dev & AI")
    st.markdown("""
    *   **Languages:** Python (Intermediate), Java (Intermediate), Arduino
    *   **Web:** Full Stack (HTML/CSS, Backend Deployment)
    *   **AI:** Prompt Engineering & Tool Integration
    *   **Tools:** Linux CLI, Nextcloud Self-Hosting
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# EXPERIENCE & PROJECTS
st.markdown("## 🚀 Key Projects & Experience")

tab1, tab2, tab3 = st.tabs(["Virtualization & Servers", "Web & AI Dev", "Cloud Hosting"])

with tab1:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.markdown("### Virtualization & Server Administration")
    st.write("""
    - **Infrastructure:** Set up and managed Linux and Windows servers in virtualized environments.
    - **Configuration:** Performed system configuration, service deployment, and maintenance.
    - **Troubleshooting:** Gained hands-on experience in server management and error resolution.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.markdown("### Web Development & AI")
    st.write("""
    - **Full-Stack:** Developed web applications handling both frontend (HTML/CSS) and backend logic.
    - **AI Integration:** Applied AI Prompt Engineering to improve productivity, content structuring, and coding workflows.
    - **Workflow:** Experienced in development, testing, and deployment cycles.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.markdown("### Cloud & Self-Hosted Services")
    st.write("""
    - **Nextcloud:** Deployed personal cloud storage for collaboration and data management.
    - **IoT Server:** Configured Raspberry Pi running services via Docker and Streamlit.
    - **Containerization:** Practiced lightweight infrastructure hosting.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ACHIEVEMENTS & EDUCATION
col_ach, col_edu = st.columns([1.5, 1])

with col_ach:
    st.markdown("## 🏆 Achievements")
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    
    st.markdown("### 🥇 International STEM Innovation Competition")
    st.info("**Gold Medalist**")
    st.write("Awarded for innovation and problem-solving at the international level. Demonstrated creativity and technical thinking.")
    
    st.divider()
    
    st.markdown("### 🇲🇾 WorldSkills Malaysia Belia (WSMB) 2025")
    st.warning("**Competitor - Cloud Computing**")
    st.write("Selected attendee and competitor in the national level Cloud Computing skill category.")
    
    st.divider()
    
    st.markdown("### ☁️ CloudHunt Competition")
    st.write("Participated in cloud computing competition against institutions across Malaysia.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_edu:
    st.markdown("## 🎓 Education")
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.markdown("**Diploma in Computer Technology**")
    st.markdown("*(Cloud Computing)*")
    st.write("🏫 **TVETMARA Campus Besut**")
    st.caption("July 2024 – July 2027 (Expected)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("## 📜 Certifications")
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.write("🔹 **Cisco Networking & Data Communication** (Beginner & Intermediate)")
    st.write("🔹 **Self-Learning:** GitHub-based courses & Online Resources")
    st.markdown('</div>', unsafe_allow_html=True)

# PERSONAL VALUES & FOOTER
st.markdown("## ❤️ Personal Values")
col_q1, col_q2 = st.columns(2)

with col_q1:
    st.info("“Opportunities don't happen. You create them.”")
with col_q2:
    st.info("“Quality means doing it right when no one is looking.”")

st.markdown("---")
st.caption("References available upon request. | Built with Python & Streamlit.")