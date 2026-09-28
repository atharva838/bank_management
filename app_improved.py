
import streamlit as st
from main_improved import Bank

st.set_page_config(
    page_title="NovaBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

bank = Bank()

# =========================================================
# NOVABANK - MODERN UI
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0b1220;
    --navy2: #111c33;
    --blue: #2563eb;
    --blue2: #3b82f6;
    --cyan: #06b6d4;
    --green: #10b981;
    --red: #ef4444;
    --text: #172033;
    --muted: #64748b;
    --surface: #ffffff;
    --bg: #f4f7fb;
    --border: #e6ebf2;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #000000 !important;
    color: #ffffff !important;
}
/* Global dark theme */
.stApp,
.stApp p,
.stApp label,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6,
.stApp span,
.stApp div {
    color: #ffffff !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer { visibility: hidden; }
[data-testid="stHeader"] { background: transparent; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08111f 0%, #101c31 100%);
    border-right: 1px solid rgba(255,255,255,.06);
}
[data-testid="stSidebar"] * {
    color: #e8eef9 !important;
}
[data-testid="stSidebar"] .stRadio label {
    border-radius: 12px;
    padding: 9px 12px;
    transition: all .2s ease;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.09);
    transform: translateX(3px);
}
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.10);
}
[data-testid="stSidebar"] [data-testid="stButton"] button {
    background: rgba(255,255,255,.08);
    color: white !important;
    border: 1px solid rgba(255,255,255,.13);
}
[data-testid="stSidebar"] [data-testid="stButton"] button:hover {
    background: rgba(239,68,68,.20);
    border-color: rgba(239,68,68,.45);
}

/* Main width */
.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Typography */
.hero-title {
    font-size: clamp(2rem, 4vw, 3.4rem);
    font-weight: 800;
    letter-spacing: -1.8px;
    margin: 0;
    color: #0f172a;
}
.hero-subtitle {
    color: var(--muted);
    font-size: 1rem;
    margin-top: .45rem;
}
.section-title {
    font-size: 1.35rem;
    font-weight: 750;
    color: #0f172a;
    margin: .5rem 0 1rem;
}

/* Login / create page */
.auth-shell {
    max-width: 1050px;
    margin: 3vh auto 0;
}
.brand-pill {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    padding: 9px 15px;
    border-radius: 999px;
    color: white;
    font-weight: 700;
    background: linear-gradient(135deg, #1d4ed8, #06b6d4);
    box-shadow: 0 10px 25px rgba(37,99,235,.22);
}
.auth-banner {
    background: linear-gradient(135deg, #0b1220 0%, #142746 55%, #155e75 100%);
    color: white;
    border-radius: 28px;
    padding: 34px;
    margin: 0 0 24px;
    box-shadow: 0 22px 55px rgba(15,23,42,.18);
    position: relative;
    overflow: hidden;
}
.auth-banner:after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -70px;
    top: -100px;
    border-radius: 50%;
    background: rgba(255,255,255,.08);
}
.auth-banner h1 {
    font-size: 2.6rem;
    margin: 12px 0 6px;
    letter-spacing: -1px;
}
.auth-banner p {
    color: #cbd5e1;
    margin: 0;
}

/* Cards */
.card {
    background: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,.5);
    color: #ffffff !important;
}
.metric-card {
    min-height: 142px;
    position: relative;
    overflow: hidden;
    transition: transform .2s ease, box-shadow .2s ease;
}
.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 40px rgba(15,23,42,.12);
}
.metric-icon {
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 13px;
    font-size: 22px;
    margin-bottom: 14px;
    background: #eff6ff;
}
.metric-label {
    color: var(--muted);
    font-size: .82rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .5px;
}
.metric-value {
    color: #0f172a;
    font-size: 1.55rem;
    font-weight: 800;
    margin-top: 5px;
    word-break: break-word;
}
.balance-card {
    background: linear-gradient(135deg, #0b1220 0%, #1d4ed8 65%, #06b6d4 100%);
    color: white;
    border: 0;
}
.balance-card .metric-label,
.balance-card .metric-value {
    color: white;
}
.balance-card .metric-icon {
    background: rgba(255,255,255,.15);
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    border: 0 !important;
    border-radius: 12px !important;
    min-height: 44px;
    font-weight: 700 !important;
    transition: all .2s ease !important;
}
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 22px rgba(37,99,235,.20);
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    border-radius: 11px !important;
    border: 1px solid #dbe3ef !important;
    min-height: 44px;
    background: white !important;
    color: #000000 !important;
}
.stTextInput input[type="password"] {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}
.stTextInput input::placeholder,
.stNumberInput input::placeholder {
    color: #000000 !important;
    opacity: 0.6;
}
.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,.12) !important;
}
.stTextInput input,
.stNumberInput input {
    background: #151515 !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    border: 1px solid #3a3a3a !important;
}

.stTextInput input::placeholder,
.stNumberInput input::placeholder {
    color: #aaaaaa !important;
    opacity: 1;
}
/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #eaf0f8;
    padding: 6px;
    border-radius: 14px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 9px 20px;
}
.stTabs [aria-selected="true"] {
    background: white;
    box-shadow: 0 3px 12px rgba(15,23,42,.08);
}
.stTabs [data-baseweb="tab-list"] {
    background: #111111 !important;
}

.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
}

.stTabs [aria-selected="true"] {
    background: #222222 !important;
    color: #ffffff !important;
}
/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 13px;
}

/* Tables */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
    border: 1px solid var(--border);
}

.hero-title {
    color: #ffffff !important;
}

.metric-value {
    color: #ffffff !important;
}

.section-title {
    color: #ffffff !important;
}
/* Welcome */
.welcome {
    background: linear-gradient(135deg, #ffffff, #eef6ff);
    border: 1px solid #dceafe;
    border-radius: 20px;
    padding: 22px 24px;
    margin-bottom: 22px;
}
.welcome h2 {
    margin: 0 0 5px;
    color: #0f172a;
}
.welcome p {
    margin: 0;
    color: var(--muted);
}

/* Transaction rows */
.txn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
    padding: 14px 0;
    border-bottom: 1px solid #edf1f6;
}
.txn:last-child { border-bottom: 0; }
.txn-left {
    display: flex;
    align-items: center;
    gap: 12px;
}
.txn-icon {
    width: 40px;
    height: 40px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius: 12px;
    font-weight: 800;
}
.txn-deposit { background: #dcfce7; color: #059669; }
.txn-withdraw { background: #fee2e2; color: #dc2626; }
.txn-name { font-weight: 700; color: #172033; }
.txn-date { color: #94a3b8; font-size: .78rem; margin-top: 2px; }
.txn-amount { font-weight: 800; }
.txn-green { color: #059669; }
.txn-red { color: #dc2626; }

/* Small-screen adjustments */
@media (max-width: 700px) {
    .block-container { padding: 1rem; }
    .auth-banner { padding: 24px; border-radius: 20px; }
    .auth-banner h1 { font-size: 2rem; }
    .hero-title { font-size: 2rem; }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================
def logout():
    for key in ["logged_in", "account_no"]:
        st.session_state.pop(key, None)
    st.rerun()


def money(value):
    return f"₹{value:,.2f}"


def render_metric(icon, label, value, balance=False):
    cls = "card metric-card balance-card" if balance else "card metric-card"
    st.markdown(
        f"""
        <div class="{cls}">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_transactions(transactions, limit=5):
    rows = list(reversed(transactions))
    if limit:
        rows = rows[:limit]

    if not rows:
        st.info("No transactions yet. Your activity will appear here.")
        return

    html = '<div class="card">'
    for tx in rows:
        is_deposit = tx.get("type") == "Deposit"
        icon = "↓" if is_deposit else "↑"
        icon_class = "txn-deposit" if is_deposit else "txn-withdraw"
        amount_class = "txn-green" if is_deposit else "txn-red"
        sign = "+" if is_deposit else "-"
        html += f"""
        <div class="txn">
            <div class="txn-left">
                <div class="txn-icon {icon_class}">{icon}</div>
                <div>
                    <div class="txn-name">{tx.get("type", "Transaction")}</div>
                    <div class="txn-date">{tx.get("date", "—")}</div>
                </div>
            </div>
            <div class="txn-amount {amount_class}">{sign}{money(float(tx.get("amount", 0)))}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# =========================================================
# LOGIN / CREATE ACCOUNT
# =========================================================
def login_page():
    st.markdown('<div class="auth-shell">', unsafe_allow_html=True)

    st.markdown("""
    <div class="auth-banner">
        <span class="brand-pill">🏦 NOVABANK</span>
        <h1>Banking, made simple.</h1>
        <p>Securely manage your account, balance and transactions from one modern dashboard.</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.35, 1], gap="large")

    with left:
        st.markdown('<div class="section-title">Welcome back 👋</div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="color:#64748b;margin-top:-8px;">Login to access your NovaBank account.</p>',
            unsafe_allow_html=True,
        )

        login_tab, create_tab = st.tabs(["🔐  Login", "✨  Create Account"])

        with login_tab:
            with st.form("login_form", clear_on_submit=False):
                account_no = st.text_input(
                    "Account Number",
                    placeholder="Enter your 10-digit account number",
                    max_chars=10,
                )
                pin = st.text_input(
                    "4-Digit PIN",
                    type="password",
                    max_chars=4,
                    placeholder="Enter your PIN",
                )
                submitted = st.form_submit_button("🔓  Login Securely", use_container_width=True)

            if submitted:
                account = bank.authenticate(account_no, pin)
                if account:
                    st.session_state.logged_in = True
                    st.session_state.account_no = account["account_no"]
                    st.success("Login successful! Opening your dashboard…")
                    st.rerun()
                else:
                    st.error("Invalid account number or PIN.")

        with create_tab:
            with st.form("create_account_form", clear_on_submit=True):
                name = st.text_input("Full Name", placeholder="e.g. Atharav Gurav")
                age = st.number_input("Age", min_value=1, max_value=120, value=18)
                email = st.text_input("Email", placeholder="you@example.com")
                pin = st.text_input(
                    "Create 4-Digit PIN",
                    type="password",
                    max_chars=4,
                    placeholder="Choose a secure 4-digit PIN",
                )
                submitted = st.form_submit_button(
                    "🚀  Create My Account",
                    use_container_width=True,
                )

            if submitted:
                try:
                    account = bank.create_account(name, age, email, pin)
                    st.success("Account created successfully!")
                    st.info(
                        f"Your account number is **{account['account_no']}**. "
                        "Save this number for future login."
                    )
                except ValueError as error:
                    st.error(str(error))

    with right:
        st.markdown("""
        <div class="card" style="margin-top:45px;">
            <div style="font-size:42px;margin-bottom:10px;">💳</div>
            <h2 style="margin:0 0 8px;">Your money. Your control.</h2>
            <p style="color:#64748b;line-height:1.7;">
                Track your balance, make deposits and withdrawals,
                update your profile and review your transaction history
                from a single place.
            </p>
            <hr style="border:0;border-top:1px solid #e8edf4;margin:20px 0;">
            <p style="margin:7px 0;">🔒 Secure account login</p>
            <p style="margin:7px 0;">⚡ Instant balance updates</p>
            <p style="margin:7px 0;">📊 Clear transaction history</p>
            <p style="margin:7px 0;">🎯 Simple account management</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# DASHBOARD
# =========================================================
def dashboard():
    account_no = st.session_state.account_no
    account = bank.get_account(account_no)
    transactions = account.get("transactions", [])

    # Sidebar
    with st.sidebar:
        st.markdown(
            """
            <div style="padding:8px 4px 18px;">
                <div style="font-size:25px;font-weight:800;">🏦 NovaBank</div>
                <div style="color:#94a3b8;font-size:12px;margin-top:4px;">Personal Banking</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background:rgba(255,255,255,.07);padding:14px;border-radius:14px;margin-bottom:15px;">
                <div style="font-size:12px;color:#94a3b8;">SIGNED IN AS</div>
                <div style="font-weight:700;margin-top:3px;">{account['name']}</div>
                <div style="font-size:12px;color:#94a3b8;margin-top:3px;">A/C {account['account_no']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        page = st.radio(
            "Navigation",
            ["🏠 Dashboard", "💰 Deposit", "💸 Withdraw", "👤 Profile",
             "📋 Transactions", "⚠️ Delete Account"],
            label_visibility="collapsed",
        )

        st.markdown("<div style='height:25vh'></div>", unsafe_allow_html=True)
        st.button("🚪  Logout", on_click=logout, use_container_width=True)

    # -----------------------------------------------------
    if page == "🏠 Dashboard":
        st.markdown(
            f"""
            <div class="welcome">
                <h2>Good to see you, {account['name'].split()[0]} 👋</h2>
                <p>Here is a quick overview of your NovaBank account.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        c1, c2, c3 = st.columns(3, gap="medium")
        with c1:
            render_metric("💰", "Current Balance", money(account["balance"]), True)
        with c2:
            render_metric("🏦", "Account Number", account["account_no"])
        with c3:
            render_metric("↔️", "Total Transactions", len(transactions))

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        left, right = st.columns([1.35, 1], gap="large")

        with left:
            st.markdown('<div class="section-title">Recent Activity</div>', unsafe_allow_html=True)
            render_transactions(transactions, limit=5)

        with right:
            st.markdown('<div class="section-title">Account Overview</div>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="card">
                    <p><span style="color:#64748b;">👤 Name</span><br><b>{account['name']}</b></p>
                    <p><span style="color:#64748b;">✉️ Email</span><br><b>{account['email']}</b></p>
                    <p><span style="color:#64748b;">🎂 Age</span><br><b>{account['age']} years</b></p>
                    <p style="margin-bottom:0;"><span style="color:#64748b;">🆔 Account</span><br><b>{account['account_no']}</b></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # -----------------------------------------------------
    elif page == "💰 Deposit":
        st.markdown('<div class="hero-title">Deposit Money</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Add money safely to your NovaBank account.</p>', unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        left, right = st.columns([1.1, .9], gap="large")
        with left:
            with st.form("deposit_form"):
                amount = st.number_input(
                    "Amount (₹)",
                    min_value=1.0,
                    max_value=100000.0,
                    step=100.0,
                    value=1000.0,
                    help="Maximum single deposit: ₹1,00,000",
                )
                st.caption(f"After deposit: **{money(account['balance'] + amount)}**")
                submitted = st.form_submit_button("💰  Deposit Now", use_container_width=True)

            if submitted:
                try:
                    balance = bank.deposit(account_no, amount)
                    st.success(f"{money(amount)} deposited successfully.")
                    st.metric("Updated Balance", money(balance))
                    st.balloons()
                except ValueError as error:
                    st.error(str(error))

        with right:
            render_metric("💰", "Current Balance", money(account["balance"]), True)
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
            st.info("💡 Deposits are recorded automatically in your transaction history.")

    # -----------------------------------------------------
    elif page == "💸 Withdraw":
        st.markdown('<div class="hero-title">Withdraw Money</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Withdraw funds from your available balance.</p>', unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        left, right = st.columns([1.1, .9], gap="large")
        with left:
            with st.form("withdraw_form"):
                amount = st.number_input(
                    "Amount (₹)",
                    min_value=1.0,
                    max_value=max(1.0, float(account["balance"])),
                    step=100.0,
                    value=min(1000.0, max(1.0, float(account["balance"]))),
                )
                st.caption(f"Remaining after withdrawal: **{money(account['balance'] - amount)}**")
                submitted = st.form_submit_button("💸  Withdraw Now", use_container_width=True)

            if submitted:
                try:
                    balance = bank.withdraw(account_no, amount)
                    st.success(f"{money(amount)} withdrawn successfully.")
                    st.metric("Remaining Balance", money(balance))
                except ValueError as error:
                    st.error(str(error))

        with right:
            render_metric("💳", "Available Balance", money(account["balance"]), True)
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
            st.warning("⚠️ You cannot withdraw more than your current balance.")

    # -----------------------------------------------------
    elif page == "👤 Profile":
        st.markdown('<div class="hero-title">Profile Settings</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Keep your personal account details up to date.</p>', unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        left, right = st.columns([1.15, .85], gap="large")

        with left:
            with st.form("update_profile"):
                name = st.text_input("Full Name", value=account["name"])
                email = st.text_input("Email Address", value=account["email"])
                pin = st.text_input(
                    "New 4-Digit PIN",
                    type="password",
                    max_chars=4,
                    placeholder="Leave blank to keep current PIN",
                )
                submitted = st.form_submit_button("💾  Save Changes", use_container_width=True)

            if submitted:
                try:
                    bank.update_account(
                        account_no,
                        name=name,
                        email=email,
                        pin=pin or None,
                    )
                    st.success("Profile updated successfully.")
                    st.rerun()
                except ValueError as error:
                    st.error(str(error))

        with right:
            st.markdown(
                f"""
                <div class="card">
                    <div style="font-size:40px;">👤</div>
                    <h3 style="margin:8px 0;">{account['name']}</h3>
                    <p style="color:#64748b;margin:5px 0;">{account['email']}</p>
                    <p style="color:#64748b;margin:5px 0;">Account: <b>{account['account_no']}</b></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # -----------------------------------------------------
    elif page == "📋 Transactions":
        st.markdown('<div class="hero-title">Transaction History</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">A complete record of your account activity.</p>', unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        if transactions:
            total_deposits = sum(float(t["amount"]) for t in transactions if t["type"] == "Deposit")
            total_withdrawals = sum(float(t["amount"]) for t in transactions if t["type"] == "Withdrawal")

            a, b, c = st.columns(3)
            with a:
                render_metric("↘️", "Total Deposited", money(total_deposits))
            with b:
                render_metric("↗️", "Total Withdrawn", money(total_withdrawals))
            with c:
                render_metric("🔢", "Transactions", len(transactions))

            st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
            render_transactions(transactions)
        else:
            st.info("No transactions yet.")

    # -----------------------------------------------------
    elif page == "⚠️ Delete Account":
        st.markdown('<div class="hero-title">Delete Account</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">This action permanently removes your account and its stored data.</p>', unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.error(
            "⚠️ Permanent action\n\n"
            "Your account information, balance and transaction history will be removed."
        )

        confirm = st.checkbox("I understand that this action cannot be undone.")

        if confirm:
            if st.button("🗑️  Delete My Account", type="primary", use_container_width=True):
                try:
                    bank.delete_account(account_no)
                    st.success("Account deleted successfully.")
                    logout()
                except ValueError as error:
                    st.error(str(error))


# =========================================================
# APP ENTRY
# =========================================================
if st.session_state.get("logged_in"):
    dashboard()
else:
    login_page()
