# Medico Store

A medicine store chatbot and inventory dashboard built with Python and Streamlit. Customers can check stock, order medicines by chatting, and browse medicines by category and company.

## Status

The core store flow works: chat ordering, stock updates, and order history. Data is stored in plain text files, so this version is for learning and demos, not production use. Login, a real database, and payments are planned for later.

## Features

- **Chat ordering:** type a medicine name, optionally with a quantity (`Panadol 500mg x 2`). The bot checks stock and places the order.
- **Multiple strengths:** if a name matches more than one medicine (e.g. Augmentin), the bot shows a numbered list and asks the customer to choose.
- **Spelling tolerance:** close matches are found even with small spelling mistakes.
- **Stock page:** search medicines and see total and out-of-stock counts.
- **Categories and Companies pages:** filter medicines by category or company.
- **Orders page:** shows every order saved in `orders.txt`.

## Tech Stack

- Python 3.12
- Streamlit (UI)
- Standard library only for logic (`difflib` for spelling matches)

## Project Structure

```
Medico/
├── app.py            # Streamlit app: UI, chat logic, file handling
├── medicines.txt     # Medicine stock data (one medicine per line)
├── orders.txt        # Orders are appended here (created automatically)
├── .gitignore
└── README.md
```

## Data Format

Each line in `medicines.txt` looks like this:

```
Panadol 500mg - Category: Analgesics - Price: 120 - Stock: 50 - Company: GSK
```

Orders are saved in `orders.txt` in this format:

```
Panadol 500mg - Qty: 2 - Total: 240
```

## Local Setup (PowerShell)

Install Python 3.12 first.

```powershell
cd E:\Medico
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install streamlit
streamlit run app.py
```

The app opens at `http://localhost:8501`.

If PowerShell blocks the activation script, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Using the App

1. Open the **Chat** page and type a medicine name, for example `Brufen 400mg`.
2. Add a quantity with `x`, for example `Panadol 500mg x 2`. Without `x`, the quantity is 1.
3. If several strengths match, reply with the number of the one you want.
4. Check the **Inventory**, **Categories**, **Companies**, and **Orders** pages from the top menu.

## Notes

- Stock changes are written to `medicines.txt` right away, so keep the file closed in your editor while the app is running, then refresh the browser.
- The sample data in `medicines.txt` is not real pricing or stock.
- Fonts (Outfit and DM Sans) load from Google Fonts, so an internet connection is needed for the intended look.
- `orders.txt` is listed in `.gitignore` because it contains customer order data.

## Roadmap

- Gemini API for natural-language answers
- Customer accounts and order tracking by status
- Customer support form
- Move data from text files to SQLite or PostgreSQL
- Deployment to Streamlit Community Cloud
