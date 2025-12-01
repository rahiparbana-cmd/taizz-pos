// Taizz POS — Enhanced Starter (HTML + CSS + JS)

/*
index.html
*/

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Taizz POS - Starter</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div id="app">
    <header>
      <h1>Taizz POS</h1>
      <div class="small">Simple offline POS — localStorage powered</div>
    </header>

    <section class="two-col">
      <div class="card">
        <h2>Menu / Items</h2>

        <div class="row">
          <input id="menuName" placeholder="Item name" />
          <input id="menuPrice" placeholder="Price" type="number" />
          <button id="addMenuBtn">Add to Menu</button>
        </div>

        <ul id="menuList"></ul>
        <button id="clearMenu">Clear Menu</button>
      </div>

      <div class="card">
        <h2>Cart</h2>
        <ul id="cartList"></ul>

        <div class="summary">
          <label>Discount (₹): <input id="discount" type="number" value="0" /></label>
          <label>GST (%): <input id="gst" type="number" value="5" /></label>
        </div>

        <p>Subtotal: ₹<span id="subtotal">0</span></p>
        <p>Discount: -₹<span id="discountVal">0</span></p>
        <p>GST: ₹<span id="gstVal">0</span></p>
        <p class="total">TOTAL: ₹<span id="total">0</span></p>

        <div class="row">
          <button id="saveBillBtn">Save Bill</button>
          <button id="printBtn">Print / PDF</button>
        </div>

        <div class="row">
          <button id="clearCart">Clear Cart</button>
        </div>

        <small>Saved bills: <span id="billsCount">0</span></small>
      </div>
    </section>

    <section class="card">
      <h2>Admin (simple)</h2>
      <div class="row">
        <input id="adminPass" type="password" placeholder="password" />
        <button id="loginBtn">Login</button>
        <button id="logoutBtn" style="display:none">Logout</button>
      </div>
      <div id="adminArea" style="display:none; margin-top:10px;">
        <button id="exportMenu">Export Menu (JSON)</button>
        <button id="importMenu">Import Menu (Paste JSON)</button>
      </div>
    </section>

  </div>

  <script src="app.js"></script>
</body>
</html>

/*
style.css
*/

body{font-family:Inter,Roboto,Arial;background:#f3f4f6;color:#111;margin:0;padding:18px}
#app{max-width:980px;margin:0 auto}
header{display:flex;align-items:baseline;gap:12px}
header h1{margin:0}
.small{color:#666;font-size:13px}
.card{background:#fff;padding:14px;border-radius:10px;box-shadow:0 6px 18px rgba(15,23,42,0.06);margin:12px 0}
.two-col{display:grid;grid-template-columns:1fr 420px;gap:16px}
.row{display:flex;gap:8px;margin-top:8px}
input{padding:8px;border:1px solid #ddd;border-radius:8px}
button{padding:8px 12px;border-radius:8px;border:0;background:#0f172a;color:#fff;cursor:pointer}
ul{list-style:none;padding:0}
li{padding:8px;border-bottom:1px dashed #eee;display:flex;justify-content:space-between;align-items:center}
.summary label{display:block;margin-top:8px}
.total{font-weight:700}

/* mobile */
@media(max-width:820px){.two-col{grid-template-columns:1fr}}

/*
app.js
*/

// Simple Taizz POS behavior — no external libs required
let menu = [];
let cart = [];

// --- Storage helpers ---
const LS_MENU = 'taizz_menu_v1';
const LS_BILLS = 'taizz_bills_v1';

function saveMenuToStorage(){ localStorage.setItem(LS_MENU, JSON.stringify(menu)); }
function loadMenuFromStorage(){ try{ menu = JSON.parse(localStorage.getItem(LS_MENU)) || []; }catch(e){ menu = []; } }
function saveBillToStorage(bill){ const bills = JSON.parse(localStorage.getItem(LS_BILLS) || '[]'); bills.unshift(bill); localStorage.setItem(LS_BILLS, JSON.stringify(bills)); }
function countBills(){ const bills = JSON.parse(localStorage.getItem(LS_BILLS) || '[]'); return bills.length }

// --- UI refs ---
const menuList = document.getElementById('menuList');
const cartList = document.getElementById('cartList');
const subtotalEl = document.getElementById('subtotal');
const discountInput = document.getElementById('discount');
const gstInput = document.getElementById('gst');
const discountValEl = document.getElementById('discountVal');
const gstValEl = document.getElementById('gstVal');
const totalEl = document.getElementById('total');
const billsCountEl = document.getElementById('billsCount');

// --- Load initial ---
loadMenuFromStorage(); renderMenu(); renderCart(); updateBillsCount();

// --- Menu functions ---
document.getElementById('addMenuBtn').addEventListener('click', ()=>{
  const name = document.getElementById('menuName').value.trim();
  const price = parseFloat(document.getElementById('menuPrice').value);
  if(!name || !price) return alert('Enter name + price');
  const id = Date.now();
  menu.push({ id, name, price });
  saveMenuToStorage();
  renderMenu();
  document.getElementById('menuName').value=''; document.getElementById('menuPrice').value='';
});

function renderMenu(){
  menuList.innerHTML='';
  if(menu.length===0) menuList.innerHTML='<li><em>No items. Add menu items.</em></li>';
  menu.forEach(it=>{
    const li = document.createElement('li');
    li.innerHTML = `<div>${it.name} — ₹${it.price.toFixed(2)}</div><div><button onclick="addToCart(${it.id})">Add</button></div>`;
    menuList.appendChild(li);
  })
}

document.getElementById('clearMenu').addEventListener('click', ()=>{ if(confirm('Clear all menu?')){ menu=[]; saveMenuToStorage(); renderMenu(); } });

// --- Cart functions ---
function addToCart(id){
  const item = menu.find(m=>m.id===id);
  if(!item) return;
  const existing = cart.find(c=>c.id===id);
  if(existing) existing.qty++;
  else cart.push({ ...item, qty:1 });
  renderCart();
}

function changeQty(id, delta){
  const it = cart.find(c=>c.id===id);
  if(!it) return;
  it.qty += delta;
  if(it.qty<=0) cart = cart.filter(c=>c.id!==id);
  renderCart();
}

function removeFromCart(id){ cart = cart.filter(c=>c.id!==id); renderCart(); }

function renderCart(){
  cartList.innerHTML='';
  if(cart.length===0) cartList.innerHTML='<li><em>Cart empty</em></li>';
  let subtotal = 0;
  cart.forEach(c=>{
    subtotal += c.price * c.qty;
    const li = document.createElement('li');
    li.innerHTML = `<div>${c.name} x ${c.qty} — ₹${(c.price*c.qty).toFixed(2)}</div>
      <div style="display:flex;gap:6px"><button onclick="changeQty(${c.id},1)">+</button><button onclick="changeQty(${c.id},-1)">-</button><button onclick="removeFromCart(${c.id})">✕</button></div>`;
    cartList.appendChild(li);
  })

  const discount = parseFloat(discountInput.value) || 0;
  const gstPerc = parseFloat(gstInput.value) || 0;
  const gstAmount = Math.max(0, (subtotal - discount) * gstPerc / 100);
  const total = Math.max(0, subtotal - discount + gstAmount);

  subtotalEl.textContent = subtotal.toFixed(2);
  discountValEl.textContent = discount.toFixed(2);
  gstValEl.textContent = gstAmount.toFixed(2);
  totalEl.textContent = total.toFixed(2);
}

discountInput.addEventListener('input', renderCart);
gstInput.addEventListener('input', renderCart);

document.getElementById('clearCart').addEventListener('click', ()=>{ if(confirm('Clear cart?')){ cart=[]; renderCart(); } });

// --- Save / Print ---
document.getElementById('saveBillBtn').addEventListener('click', ()=>{
  if(cart.length===0) return alert('Cart empty');
  const bill = buildBill();
  saveBillToStorage(bill);
  updateBillsCount();
  alert('Bill saved locally');
});

document.getElementById('printBtn').addEventListener('click', ()=>{
  if(cart.length===0) return alert('Cart empty');
  const bill = buildBill();
  openInvoiceWindow(bill);
});

function buildBill(){
  const subtotal = parseFloat(subtotalEl.textContent) || 0;
  const discount = parseFloat(discountInput.value) || 0;
  const gst = parseFloat(gstValEl.textContent) || 0;
  const total = parseFloat(totalEl.textContent) || 0;
  const timestamp = new Date().toISOString();
  return { id: 'B'+Date.now(), items: cart.map(c=>({name:c.name, qty:c.qty, price:c.price})), subtotal, discount, gst, total, timestamp };
}

function openInvoiceWindow(bill){
  const w = window.open('', '_blank');
  const html = `<!doctype html><html><head><meta charset="utf-8"><title>Invoice ${bill.id}</title>
  <style>body{font-family:Arial;padding:24px}table{width:100%;border-collapse:collapse}th,td{padding:8px;border-bottom:1px solid #ddd;text-align:left}</style>
  </head><body>
  <h2>Taizz POS</h2>
  <div>Invoice: ${bill.id}</div>
  <div>Date: ${new Date(bill.timestamp).toLocaleString()}</div>
  <hr />
  <table>
    <tr><th>Item</th><th>Qty</th><th>Rate</th><th>Amount</th></tr>
    ${bill.items.map(i=>`<tr><td>${i.name}</td><td>${i.qty}</td><td>₹${i.price.toFixed(2)}</td><td>₹${(i.qty*i.price).toFixed(2)}</td></tr>`).join('')}
  </table>
  <hr />
  <div>Subtotal: ₹${bill.subtotal.toFixed(2)}</div>
  <div>Discount: -₹${bill.discount.toFixed(2)}</div>
  <div>GST: ₹${bill.gst.toFixed(2)}</div>
  <h3>Total: ₹${bill.total.toFixed(2)}</h3>
  <hr />
  <button onclick="window.print()">Print / Save as PDF</button>
  </body></html>`;
  w.document.write(html);
  w.document.close();
}

function updateBillsCount(){ billsCountEl.textContent = countBills(); }

// --- Admin simple auth ---
const ADMIN_PASSWORD = 'admin123'; // change as needed

document.getElementById('loginBtn').addEventListener('click', ()=>{
  const pass = document.getElementById('adminPass').value;
  if(pass===ADMIN_PASSWORD){
    document.getElementById('adminArea').style.display='block';
    document.getElementById('logoutBtn').style.display='inline-block';
    document.getElementById('loginBtn').style.display='none';
    alert('Admin logged in');
  } else alert('Wrong password');
});

document.getElementById('logoutBtn').addEventListener('click', ()=>{
  document.getElementById('adminArea').style.display='none';
  document.getElementById('logoutBtn').style.display='none';
  document.getElementById('loginBtn').style.display='inline-block';
});

// Export / Import menu (admin)
document.getElementById('exportMenu').addEventListener('click', ()=>{
  const json = JSON.stringify(menu, null, 2);
  prompt('Copy menu JSON:', json);
});

document.getElementById('importMenu').addEventListener('click', ()=>{
  const txt = prompt('Paste menu JSON to import:');
  if(!txt) return;
  try{ const parsed = JSON.parse(txt); if(Array.isArray(parsed)){ menu = parsed; saveMenuToStorage(); renderMenu(); alert('Imported'); } else alert('Invalid format'); }catch(e){ alert('Invalid JSON') }
});

// Expose some functions to HTML inline handlers
window.addToCart = addToCart;
window.changeQty = changeQty;
window.removeFromCart = removeFromCart;

/*
--- Firebase Integration (Realtime Database) ---

// 1. Add Firebase SDK in index.html <head>
// <script src="https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js"></script>
// <script src="https://www.gstatic.com/firebasejs/11.0.1/firebase-database.js"></script>

// 2. Add your Firebase Config below:
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT-default-rtdb.firebaseio.com",
  projectId: "YOUR_PROJECT",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID"
};

firebase.initializeApp(firebaseConfig);
const db = firebase.database();

// --- Firebase Sync Functions ---
function syncMenuToFirebase(){ db.ref('menu').set(menu); }
function loadMenuFromFirebase(){ db.ref('menu').once('value', snap=>{ menu = snap.val() || []; saveMenuToStorage(); renderMenu(); }); }
function pushBillToFirebase(bill){ db.ref('bills/'+bill.id).set(bill); }

// Call once when app loads
loadMenuFromFirebase();

// Override menu save to sync online
function saveMenuToStorage(){ localStorage.setItem(LS_MENU, JSON.stringify(menu)); syncMenuToFirebase(); }

// Override bill save to sync online
function saveBillToStorage(bill){
  const bills = JSON.parse(localStorage.getItem(LS_BILLS) || '[]');
  bills.unshift(bill);
  localStorage.setItem(LS_BILLS, JSON.stringify(bills));
  pushBillToFirebase(bill);
}

How to use
1) Save three files (index.html, style.css, app.js) with the above content.
2) Open index.html in browser (works offline).
3) Add menu items, add to cart, set discount/GST, Save bill or Print to produce PDF.

Next features I can add on your request:
- Firebase persistence (online sync)
- Generate proper PDF using jsPDF
- Payment gateway integration
- Inventory tracking with alerts
- Multi-branch / user roles
- Barcodes & thermal-print friendly layout
*/

// --- PRINT INVOICE FEATURE ---
function printBill() {
  if (cart.length === 0) return alert('Cart empty');

  let invoiceHTML = `
    <div style='font-family:Arial;padding:20px;width:280px;'>
      <h2 style='text-align:center'>Taizz POS Bill</h2>
      <hr>
      <table style='width:100%;font-size:14px;'>
        ${cart.map(i => `<tr><td>${i.name}</td><td style='text-align:right'>₹${i.price}</td></tr>`).join('')}
      </table>
      <hr>
      <p style='font-size:16px'><b>Total: ₹${document.getElementById('total').textContent}</b></p>
      <p style='text-align:center;font-size:12px;'>Thank you!</p>
    </div>`;

  let w = window.open('', '', 'width=400,height=600');
  w.document.write(invoiceHTML);
  w.document.close();
  w.focus();
  w.print();
  w.close();
}


// --- KOT (Kitchen Order Ticket) PRINT ---
function printKOT() {
  if (cart.length === 0) return alert('Cart empty');

  let kotHTML = `
    <div style='font-family:Arial;padding:10px;width:240px;'>
      <h3 style='text-align:center;margin:0;'>KOT</h3>
      <p style='font-size:12px;margin:4px 0;'>Time: ${new Date().toLocaleTimeString()}</p>
      <hr>
      <table style='width:100%;font-size:14px;'>
        ${cart.map(i => `<tr><td>${i.name}</td><td style='text-align:right'>x${i.qty || 1}</td></tr>`).join('')}
      </table>
      <hr>
      <p style='font-size:12px;text-align:center;margin-top:6px;'>KITCHEN COPY</p>
    </div>`;

  let w = window.open('', '', 'width=300,height=500');
  w.document.write(kotHTML);
  w.document.close();
  w.focus();
  w.print();
  w.close();
}

