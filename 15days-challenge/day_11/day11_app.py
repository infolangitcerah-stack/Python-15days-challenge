# app.py
from datetime import datetime
from io import BytesIO

import pandas as pd
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="🍔 Restaurant Order & Billing",
    page_icon="🍔",
    layout="centered",
)

# ----------------- CUSTOM STYLE -----------------
ACCENT_DEFAULT = "#6C5CE7"
st.markdown(
    f"""
    <style>
    /* Global width control */
    .main-container {{
        max-width: 900px;
        margin: 0 auto;
    }}
    /* Narrow sections */
    .section-box {{
        max-width: 650px;
        margin: 0 auto;
        padding: 15px;
        border-radius: 12px;
        background: rgba(255,255,255,0.6);
        backdrop-filter: blur(6px);
    }}
    h1 {{
        color: #1A1A1A;
        text-shadow: 0 0 10px rgba(108,92,231,0.2);
        text-align: center;
        margin-bottom: 0.3em;
    }}
    .neon-card {{
        border-radius: 20px;
        padding: 18px;
        background: rgba(255,255,255,0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.8);
        box-shadow: 0 8px 30px rgba(108,92,231,0.15);
        text-align: center;
    }}
    .stDownloadButton > button {{
        border-radius: 12px;
        padding: 10px 16px;
        font-weight: 600;
        background: {ACCENT_DEFAULT};
        color: white;
    }}
    .dataframe tbody tr:hover {{
        background-color: rgba(108,92,231,0.08);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- WRAP EVERYTHING -----------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.markdown(
    """
    <div class="neon-card">
      <h1>🍔 Restaurant Order & Billing App — Social Eagle GenAI Architect | Day 11 | Coach Dom</h1>
      <p style="color:#444;">Futuristic, friendly, and precise — with two decimal accuracy.</p>
    </div>
    <br/>
    """,
    unsafe_allow_html=True,
)

# ----------------- SETTINGS -----------------
col1, col2 = st.columns([2, 1])
with col1:
    tax_rate = st.slider("Tax (%)", 0.0, 15.0, 6.0, 0.5)
with col2:
    accent = st.color_picker("Accent Color", ACCENT_DEFAULT)
    st.markdown(
        f"<style>.stDownloadButton > button{{background:{accent};}}</style>", unsafe_allow_html=True
    )

bill_title = st.text_input("Invoice Title", "Social Eagle — Day 11 Assignment")
customer_name = st.text_input("Customer Name (optional)", "")

# ----------------- MENU DATA -----------------
MENU = [
    {"Category": "Burgers", "Item": "Classic Burger", "Price": 12.90},
    {"Category": "Burgers", "Item": "Cheese Burger", "Price": 14.50},
    {"Category": "Burgers", "Item": "Spicy Chicken Burger", "Price": 13.90},
    {"Category": "Sides", "Item": "Fries", "Price": 5.50},
    {"Category": "Sides", "Item": "Onion Rings", "Price": 6.20},
    {"Category": "Drinks", "Item": "Iced Lemon Tea", "Price": 4.80},
    {"Category": "Drinks", "Item": "Soda", "Price": 4.50},
    {"Category": "Dessert", "Item": "Chocolate Lava Cake", "Price": 8.90},
]

# ----------------- MENU DISPLAY -----------------
st.subheader("📋 Menu")
menu_df = pd.DataFrame(MENU)
menu_df["Price (RM)"] = menu_df["Price"].map(lambda x: f"{x:.2f}")
st.dataframe(menu_df[["Category", "Item", "Price (RM)"]], use_container_width=True)

# ----------------- ITEM SELECTION -----------------
st.subheader("🛒 Select Items & Quantities")
st.markdown('<div class="section-box">', unsafe_allow_html=True)

selected_rows = []

categories = sorted(set(m["Category"] for m in MENU))
for cat in categories:
    st.markdown(f"**{cat}**")
    cat_items = [m for m in MENU if m["Category"] == cat]

    # Header row
    cols = st.columns([3, 1, 1])
    with cols[0]:
        st.caption("Item")
    with cols[1]:
        st.caption("Price (RM)")
    with cols[2]:
        st.caption("Qty")

    # Items
    for m in cat_items:
        c1, c2, c3 = st.columns([3, 1, 1])
        c1.write(m["Item"])
        c2.write(f"{m['Price']:.2f}")
        qty = c3.number_input(
            label=f"qty_{m['Item']}",
            min_value=0,
            max_value=20,
            step=1,
            value=0,
            key=f"qty_{m['Item']}",
        )
        if qty > 0:
            selected_rows.append(
                {
                    "Item": m["Item"],
                    "Unit Price (RM)": m["Price"],
                    "Quantity": qty,
                    "Line Total (RM)": m["Price"] * qty,
                }
            )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ----------------- BILL SUMMARY -----------------
if selected_rows:
    st.subheader("🧾 Bill Summary")
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    bill_df = pd.DataFrame(selected_rows)
    bill_df["Unit Price (RM)"] = bill_df["Unit Price (RM)"].map(lambda x: float(f"{x:.2f}"))
    bill_df["Line Total (RM)"] = bill_df["Line Total (RM)"].map(lambda x: float(f"{x:.2f}"))

    subtotal = float(f"{bill_df['Line Total (RM)'].sum():.2f}")
    tax_amount = float(f"{(subtotal * (tax_rate / 100)):.2f}")
    total = float(f"{(subtotal + tax_amount):.2f}")

    st.dataframe(bill_df, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Subtotal (RM)", f"{subtotal:.2f}")
    c2.metric(f"Tax {tax_rate:.1f}% (RM)", f"{tax_amount:.2f}")
    c3.metric("Total (RM)", f"{total:.2f}")

    # ---------- DOWNLOADS ----------
    def invoice_csv_bytes(df):
        out = BytesIO()
        df.to_csv(out, index=False, float_format="%.2f")
        return out.getvalue()

    def invoice_pdf_bytes(df, subtotal, tax_rate, tax_amount, total, title, customer):
        buf = BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        width, height = A4
        x_margin, y_margin = 20 * mm, 20 * mm
        y = height - y_margin

        c.setFont("Helvetica-Bold", 16)
        c.drawString(x_margin, y, title)
        y -= 12 * mm
        c.setFont("Helvetica", 10)
        c.drawString(x_margin, y, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        if customer:
            c.drawString(x_margin + 200, y, f"Customer: {customer}")
        y -= 10 * mm

        c.setFont("Helvetica-Bold", 11)
        c.drawString(x_margin, y, "Item")
        c.drawString(x_margin + 250, y, "Unit (RM)")
        c.drawString(x_margin + 330, y, "Qty")
        c.drawString(x_margin + 400, y, "Line (RM)")
        y -= 8 * mm
        c.line(x_margin, y, width - x_margin, y)
        y -= 8 * mm

        c.setFont("Helvetica", 10)
        for _, row in df.iterrows():
            c.drawString(x_margin, y, str(row["Item"]))
            c.drawRightString(x_margin + 300, y, f"{row['Unit Price (RM)']:.2f}")
            c.drawRightString(x_margin + 360, y, f"{row['Quantity']}")
            c.drawRightString(x_margin + 470, y, f"{row['Line Total (RM)']:.2f}")
            y -= 8 * mm

        y -= 10 * mm
        c.setFont("Helvetica-Bold", 12)
        c.drawRightString(x_margin + 470, y, f"Subtotal: RM {subtotal:.2f}")
        y -= 8 * mm
        c.setFont("Helvetica", 12)
        c.drawRightString(x_margin + 470, y, f"Tax ({tax_rate:.1f}%): RM {tax_amount:.2f}")
        y -= 8 * mm
        c.setFont("Helvetica-Bold", 13)
        c.drawRightString(x_margin + 470, y, f"Total: RM {total:.2f}")

        y = 20 * mm
        c.setFont("Helvetica-Oblique", 9)
        c.drawCentredString(
            width / 2, y, "Thank you for dining with us! — Social Eagle GenAI Architect"
        )
        c.showPage()
        c.save()
        pdf = buf.getvalue()
        buf.close()
        return pdf

    colA, colB = st.columns(2)
    colA.download_button(
        "⬇️ Download CSV",
        data=invoice_csv_bytes(bill_df),
        file_name=f"invoice_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv",
    )
    colB.download_button(
        "⬇️ Download PDF",
        data=invoice_pdf_bytes(
            bill_df, subtotal, tax_rate, tax_amount, total, bill_title, customer_name
        ),
        file_name=f"invoice_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
        mime="application/pdf",
    )

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("👉 Select some items to generate your bill and download invoice.")

# ----------------- CLOSE MAIN CONTAINER -----------------
st.markdown("</div>", unsafe_allow_html=True)
