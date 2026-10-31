import difflib

def load_medicines(filename):
    medicines = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(" - ")
            name = parts[0]
            price = int(parts[1].replace("Price: ", ""))
            stock = int(parts[2].replace("Stock: ", ""))
            medicines.append({"name": name, "price": price, "stock": stock})
    return medicines

def save_medicines(filename, medicines):
    with open(filename, "w") as f:
        for med in medicines:
            f.write(f"{med['name']} - Price: {med['price']} - Stock: {med['stock']}\n")

def save_order(filename, name, qty, price):
    with open(filename, "a") as f:
        f.write(f"{name} - Qty: {qty} - Total: {qty * price}\n")

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

medicines = load_medicines("medicines.txt")

order = input("Customer: ").strip()

# quantity alag variable mein le rahe hain
if " x " in order:
    name, qty_text = order.split(" x ", 1)
    try:
        qty = int(qty_text.strip())
    except ValueError:
        print("Bot: Quantity number mein likhein, jaise Panadol 500mg x 2")
        exit()
else:
    name = order
    qty = 1

name = name.strip()

matches = find_matches(name, medicines)

if len(matches) > 1:
    print("Bot: Is naam ki kai medicines hain:")
    for i, m in enumerate(matches, 1):
        print(f"{i}. {m['name']} - Price: {m['price']} - Stock: {m['stock']}")
    choice = input("Kaunsi medicine chahiye? Sirf number likhein: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(matches):
        med = matches[int(choice) - 1]
    else:
        print("Bot: Galat number hai.")
        exit()
elif len(matches) == 1:
    med = matches[0]
else:
    med = find_medicine(name, medicines)

if med is None:
    print("Bot: Yeh medicine humare paas nahi hai.")
elif med["stock"] >= qty:
    med["stock"] -= qty
    save_medicines("medicines.txt", medicines)
    save_order("orders.txt", med["name"], qty, med["price"])
    print(f"Bot: {qty} x {med['name']} ka order ho gaya. Baaki stock: {med['stock']}")
else:
    print(f"Bot: Maafi chahte hain, {med['name']} ka stock kaafi nahi. Abhi sirf {med['stock']} available hain.")