import difflib
import html
import streamlit as st

st.set_page_config(page_title="Medico Everyday Care", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

    .stApp {background: #faf8f2; font-family: 'DM Sans', sans-serif; color: #252743;}
    #MainMenu, footer, header[data-testid="stHeader"] {visibility: hidden;}
    .block-container {max-width: 1440px; padding-top: 1.2rem; padding-bottom: 0;}
    h1, h2, h3, .outfit {font-family: 'Outfit', sans-serif;}

    .topbar {
        background: #ffffff; border-radius: 20px; padding: 14px 26px;
        display: flex; align-items: center; justify-content: space-between;
        box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05); margin-bottom: 14px;
    }
    .brand {display: flex; align-items: center; gap: 10px;}
    .brand-symbol {
        background: #5040c9; color: #ffffff; width: 40px; height: 40px;
        border-radius: 14px; display: flex; align-items: center; justify-content: center;
        font-size: 24px; font-weight: 700;
    }
    .brand-name {font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 27px; color: #252743;}
    .brand-sub {font-size: 12px; color: #66677c;}
    .profile {display: flex; align-items: center; gap: 10px; font-size: 13px; color: #252743;}
    .avatar {
        background: #f6e99c; width: 38px; height: 38px; border-radius: 100px;
        display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;
    }

    div[role="radiogroup"] {
        background: #ffffff; border-radius: 100px; padding: 6px; gap: 4px;
        box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05); width: fit-content; margin-bottom: 22px;
    }
    div[role="radiogroup"] > label {border-radius: 100px; padding: 8px 16px; margin: 0;}
    div[role="radiogroup"] > label > div:first-child {display: none;}
    div[role="radiogroup"] > label p {font-size: 14px; font-weight: 500; margin: 0; color: #252743;}
    div[role="radiogroup"] > label:has(input:checked) {background: #ede9ff;}
    div[role="radiogroup"] > label:has(input:checked) p {color: #5040c9; font-weight: 700;}

    div[data-testid="stHorizontalBlock"]:has(> div[data-testid="stColumn"]:nth-child(2)) > div[data-testid="stColumn"]:nth-child(1) {
        background: #ffd6be; border-radius: 24px; padding: 30px 30px 26px 30px;
    }

    .care-title {font-family: 'Outfit', sans-serif; font-size: 46px; line-height: 1.05; font-weight: 500; margin: 0;}
    .seal-row {display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;}
    .seal {
        background: #f6e99c; width: 72px; height: 72px; border-radius: 100px;
        display: flex; align-items: center; justify-content: center; font-size: 30px; transform: rotate(10deg);
    }
    .illustration {
        background: #fff3ea; border-radius: 24px; height: 170px; margin: 18px 0;
        display: flex; align-items: center; justify-content: center; font-size: 80px;
    }

    .card {background: #ffffff; border-radius: 24px; padding: 20px; box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05); margin-bottom: 12px;}
    .card-head {display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;}
    .card-title {font-family: 'Outfit', sans-serif; font-size: 23px; font-weight: 500; margin: 0;}
    .muted {font-size: 12px; color: #66677c;}

    .med-list {max-height: 300px; overflow-y: auto;}
    .med-row {display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid #e5e2ed;}
    .med-row:last-child {border-bottom: none;}
    .med-icon {background: #ede9ff; width: 36px; height: 36px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 17px;}
    .med-name {font-weight: 600; font-size: 14px;}
    .med-meta {font-size: 11px; color: #66677c;}
    .pill-in {background: #e7f2d9; color: #296248; font-size: 11px; font-weight: 600; padding: 5px 10px; border-radius: 100px; margin-left: auto; white-space: nowrap;}
    .pill-out {background: #faf8f2; color: #66677c; font-size: 11px; font-weight: 600; padding: 5px 10px; border-radius: 100px; margin-left: auto; white-space: nowrap;}

    .chat-head {display: flex; align-items: center; gap: 14px; padding-bottom: 18px; border-bottom: 1px solid #e5e2ed; margin-bottom: 20px;}
    .spark {background: #ede9ff; width: 52px; height: 52px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-size: 26px;}
    .chat-title {font-family: 'Outfit', sans-serif; font-size: 25px; font-weight: 500; margin: 0;}
    .online {font-size: 12px; color: #66677c;}
    .online::before {content: "● "; color: #4caf50;}

    .msg-meta {font-size: 11px; color: #66677c; font-weight: 500; margin: 0 0 6px 0;}
    .bubble-bot {background: #ffffff; color: #252743; padding: 18px 20px; border-radius: 4px 22px 22px 22px; box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05); font-size: 15px; line-height: 1.5; margin-bottom: 18px; max-width: 92%;}
    .bubble-bot b {font-family: 'DM Sans', sans-serif; font-weight: 700;}
    .bubble-user {background: #5040c9; color: #ffffff; padding: 14px 20px; border-radius: 22px 22px 4px 22px; font-size: 15px; line-height: 1.5; margin-bottom: 18px; max-width: 70%; margin-left: auto; width: fit-content;}
    .user-wrap {display: flex; flex-direction: column; align-items: flex-end;}

    .order-card {background: #ffffff; border-radius: 24px; padding: 22px; box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05); margin-bottom: 18px;}
    .order-head {display: flex; align-items: center; gap: 12px; margin-bottom: 10px;}
    .check {background: #e7f2d9; width: 36px; height: 36px; border-radius: 100px; display: flex; align-items: center; justify-content: center; font-size: 18px; color: #296248;}
    .order-title {font-family: 'Outfit', sans-serif; font-size: 24px; font-weight: 500; margin: 0;}
    .order-sum {background: #ede9ff; border-radius: 16px; padding: 14px 16px; display: flex; align-items: center; gap: 14px; margin-top: 12px;}
    .order-sum-name {font-weight: 700; font-size: 14px;}
    .order-sum-meta {font-size: 12px; color: #66677c;}
    .order-total {margin-left: auto; font-weight: 700; font-size: 21px; color: #5040c9;}

    [data-testid="stForm"] {background: #ffffff; border: 1px solid #e5e2ed; border-radius: 24px; padding: 10px 14px; box-shadow: 0 6px 24px rgba(48, 34, 100, 0.05);}
    [data-testid="stForm"] button {background: #5040c9; color: #ffffff; border: none; border-radius: 14px; font-weight: 700;}
    [data-testid="stForm"] button:hover {background: #4032a8; color: #ffffff;}
    .disclaimer {font-size: 11px; color: #66677c; text-align: center; margin-top: 8px;}
</style>
""", unsafe_allow_html=True)

def load_medicines(filename):
    medicines = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(" - ")
            name = parts[0]
            category = parts[1].replace("Category: ", "")
            price = int(parts[2].replace("Price: ", ""))
            stock = int(parts[3].replace("Stock: ", ""))
            company = parts[4].replace("Company: ", "")
            medicines.append({
                "name": name,
                "category": category,
                "price": price,
                "stock": stock,
                "company": company,
            })
    return medicines

def save_medicines(filename, medicines):
    with open(filename, "w") as f:
        for med in medicines:
            f.write(
                f"{med['name']} - Category: {med['category']} - Price: {med['price']} "
                f"- Stock: {med['stock']} - Company: {med['company']}\n"
            )

def save_order(filename, name, qty, price):
    with open(filename, "a") as f:
        f.write(f"{name} - Qty: {qty} - Total: {qty * price}\n")

def load_orders(filename):
    orders = []
    try:
        with open(filename) as f:
            for line in f:
                parts = line.strip().split(" - ")
                if len(parts) == 3:
                    orders.append({
                        "Medicine": parts[0],
                        "Quantity": parts[1].replace("Qty: ", ""),
                        "Total": parts[2].replace("Total: ", ""),
                    })
    except FileNotFoundError:
        pass
    return orders

def find_matches(query, medicines):
    query = query.lower().strip()
    return [med for med in medicines if query in med["name"].lower()]

def find_medicine(query, medicines):
    query = query.lower().strip()

    for med in medicines:
        if query in med["name"].lower():
            return med

    names = [med["name"].lower() for med in medicines]
    close = difflib.get_close_matches(query, names, n=1, cutoff=0.6)
    if close:
        for med in medicines:
            if med["name"].lower() == close[0]:
                return med

    return None

if "medicines" not in st.session_state:
    st.session_state.medicines = load_medicines("medicines.txt")

medicines = st.session_state.medicines

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending" not in st.session_state:
    st.session_state.pending = None

def bot(text):
    return {"role": "assistant", "text": text}

def place_order(med, qty):
    if med["stock"] >= qty:
        med["stock"] -= qty
        save_medicines("medicines.txt", medicines)
        save_order("orders.txt", med["name"], qty, med["price"])
        return {
            "role": "assistant",
            "text": f"{qty} x {med['name']} ka order ho gaya. Baaki stock: {med['stock']}",
            "order": {"name": med["name"], "qty": qty, "total": qty * med["price"], "company": med["company"]},
        }
    return bot(f"Maafi chahte hain, {med['name']} ka stock kaafi nahi. Abhi sirf {med['stock']} available hain.")

def handle_order(order):
    if " x " in order:
        name, qty_text = order.split(" x ", 1)
        try:
            qty = int(qty_text.strip())
        except ValueError:
            return bot("Quantity number mein likhein, jaise Panadol 500mg x 2")
    else:
        name = order
        qty = 1

    name = name.strip()
    matches = find_matches(name, medicines)

    if len(matches) > 1:
        st.session_state.pending = {"qty": qty, "matches": matches}
        text = "Is naam ki kai medicines hain. Kaunsi chahiye? Number likhein:"
        for i, m in enumerate(matches, 1):
            text += f"\n{i}. {m['name']} - Price: {m['price']} - Stock: {m['stock']}"
        return bot(text)

    if len(matches) == 1:
        med = matches[0]
    else:
        med = find_medicine(name, medicines)

    if med is None:
        return bot("Yeh medicine humare paas nahi hai.")

    return place_order(med, qty)

def process_message(text):
    st.session_state.messages.append({"role": "user", "text": text})

    pending = st.session_state.pending
    if pending and text.isdigit():
        choice = int(text)
        matches = pending["matches"]
        qty = pending["qty"]
        st.session_state.pending = None
        if 1 <= choice <= len(matches):
            reply = place_order(matches[choice - 1], qty)
        else:
            reply = bot("Galat number hai.")
    else:
        st.session_state.pending = None
        reply = handle_order(text)

    st.session_state.messages.append(reply)

def bubble_text(text):
    return html.escape(text).replace("\n", "<br>")

total_count = len(medicines)
sold_out_count = len([m for m in medicines if m["stock"] == 0])

st.markdown("""
<div class="topbar">
    <div class="brand">
        <div class="brand-symbol">+</div>
        <span class="brand-name">medico</span>
        <span class="brand-sub">everyday care</span>
    </div>
    <div class="profile">
        <span>Hi, Ghilman</span>
        <div class="avatar">GT</div>
    </div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "Menu",
    ["Chat", "Inventory", "Categories", "Companies", "Orders"],
    horizontal=True,
    label_visibility="collapsed",
)

if page == "Chat":
    left, right = st.columns([0.41, 0.59], gap="large")

    with left:
        st.markdown(f"""
        <div class="seal-row">
            <div class="care-title">A little care,<br>a lot easier.</div>
            <div class="seal">❤️</div>
        </div>
        <div class="illustration">💊</div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
            <div class="card-head">
                <p class="card-title">On our shelves</p>
                <span class="muted">{total_count} medicines · {sold_out_count} sold out</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        search = st.text_input("Find a medicine", placeholder="Find a medicine", label_visibility="collapsed")
        categories = ["All categories"] + sorted({m["category"] for m in medicines})
        chosen_cat = st.selectbox("Category", categories, label_visibility="collapsed")

        shown = [
            m for m in medicines
            if search.lower() in m["name"].lower()
            and (chosen_cat == "All categories" or m["category"] == chosen_cat)
        ]

        rows_html = ""
        for m in shown[:25]:
            if m["stock"] > 0:
                pill = f'<span class="pill-in">{m["stock"]} available</span>'
            else:
                pill = '<span class="pill-out">Sold out</span>'
            rows_html += (
                '<div class="med-row">'
                '<div class="med-icon">💊</div>'
                '<div>'
                f'<div class="med-name">{html.escape(m["name"])}</div>'
                f'<div class="med-meta">{html.escape(m["company"])} · {html.escape(m["category"])} · Rs {m["price"]} / pack</div>'
                '</div>'
                f'{pill}'
                '</div>'
            )

        if rows_html:
            st.markdown(f'<div class="card"><div class="med-list">{rows_html}</div></div>', unsafe_allow_html=True)
        else:
            st.info("Koi medicine nahi mili.")

    with right:
        st.markdown("""
        <div class="chat-head">
            <div class="spark">✨</div>
            <div>
                <p class="chat-title">Your care companion</p>
                <span class="online">Here to help you find &amp; order</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p class="msg-meta">MEDICO</p>
        <div class="bubble-bot">
            <b>Hello, Ghilman! Let's tick one thing off your list.</b><br>
            Tell me the medicine, strength and how many packs you need, like "Panadol 500mg x 2". I'll take care of the stock check.
        </div>
        """, unsafe_allow_html=True)

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(
                    f'<div class="user-wrap"><div class="bubble-user">{bubble_text(msg["text"])}</div></div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<p class="msg-meta">MEDICO</p><div class="bubble-bot">{bubble_text(msg["text"])}</div>',
                    unsafe_allow_html=True,
                )
                if msg.get("order"):
                    o = msg["order"]
                    st.markdown(f"""
                    <div class="order-card">
                        <div class="order-head">
                            <div class="check">✓</div>
                            <p class="order-title">All sorted. Your order is in!</p>
                        </div>
                        <div class="order-sum">
                            <div>🛍️</div>
                            <div>
                                <div class="order-sum-name">{html.escape(o["name"])} × {o["qty"]}</div>
                                <div class="order-sum-meta">{html.escape(o["company"])}</div>
                            </div>
                            <div class="order-total">Rs {o["total"]}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        with st.form("order_form", clear_on_submit=True):
            c1, c2 = st.columns([6, 1])
            user_input = c1.text_input(
                "Message",
                placeholder="What can we find for you?",
                label_visibility="collapsed",
            )
            submitted = c2.form_submit_button("Send")

        if submitted and user_input.strip():
            process_message(user_input.strip())
            st.rerun()

        st.markdown(
            '<p class="disclaimer">For ordering, not medical advice. Your pharmacist can help with medicine questions.</p>',
            unsafe_allow_html=True,
        )

elif page == "Inventory":
    st.markdown('<h1 class="care-title">Inventory</h1>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.markdown(f'<div class="card"><div class="muted">Total medicines</div><div class="card-title">{total_count}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="card"><div class="muted">Out of stock</div><div class="card-title">{sold_out_count}</div></div>', unsafe_allow_html=True)

    search = st.text_input("Medicine dhoondhein", key="inv_search")
    rows = [
        {"Medicine": m["name"], "Category": m["category"], "Price": m["price"], "Stock": m["stock"], "Company": m["company"]}
        for m in medicines
        if search.lower() in m["name"].lower()
    ]
    if rows:
        st.dataframe(rows, hide_index=True)
    else:
        st.info("Koi medicine nahi mili.")

elif page == "Categories":
    st.markdown('<h1 class="care-title">Categories</h1>', unsafe_allow_html=True)

    categories = sorted({m["category"] for m in medicines})
    chosen = st.selectbox("Category chunein", categories)

    rows = [
        {"Medicine": m["name"], "Price": m["price"], "Stock": m["stock"], "Company": m["company"]}
        for m in medicines
        if m["category"] == chosen
    ]
    st.write(f"{len(rows)} medicines mili")
    st.dataframe(rows, hide_index=True)

elif page == "Companies":
    st.markdown('<h1 class="care-title">Companies</h1>', unsafe_allow_html=True)

    companies = sorted({m["company"] for m in medicines})
    chosen = st.selectbox("Company chunein", companies)

    rows = [
        {"Medicine": m["name"], "Category": m["category"], "Price": m["price"], "Stock": m["stock"]}
        for m in medicines
        if m["company"] == chosen
    ]
    st.write(f"{len(rows)} medicines mili")
    st.dataframe(rows, hide_index=True)

elif page == "Orders":
    st.markdown('<h1 class="care-title">Orders</h1>', unsafe_allow_html=True)

    orders = load_orders("orders.txt")
    if orders:
        st.dataframe(orders, hide_index=True)
    else:
        st.info("Abhi tak koi order nahi hua.")