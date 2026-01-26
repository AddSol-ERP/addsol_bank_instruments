# Letter of Credit Management - Quick Start Guide

**Get up and running with LC management in 5 minutes!**

---

## 🚀 What This App Does

Manage your complete Letter of Credit lifecycle:
- ✅ Create and track Import/Export LCs
- ✅ Monitor shipments and utilization
- ✅ Track documents and submissions
- ✅ Manage amendments
- ✅ Analyze costs and performance
- ✅ Get expiry alerts

---

## 📍 Step 1: Access the LC Workspace (30 seconds)

1. **Login** to your ERPNext site
2. **Click** the workspace icon (☰) in the left sidebar
3. **Find** and **click** "Letter of Credit"
4. **You're in!** See the dashboard with shortcuts and reports

---

## 📝 Step 2: Create Your First LC (3 minutes)

### Quick Method (If you have a Purchase/Sales Order)

1. **Click** the blue **"Letter of Credit"** button
2. **Fill essential fields:**

```
LC Number: [Bank's LC number]          Example: LC/2026/001
LC Type: [Select type]                 Example: Sight LC
Transaction Type: [Import or Export]   Example: Import
LC Date: [Opening date]                Example: 15-Jan-2026
Expiry Date: [Expiry date]             Example: 31-Mar-2026
```

3. **Link your order:**
   - **Import:** Select Purchase Order
   - **Export:** Select Sales Order
   - **Magic!** Supplier, Amount, Currency auto-fill

4. **Review bank details:**
   - Issuing Bank: [Your bank or customer's bank]

5. **Add required documents** (click "Add Row"):
   - Commercial Invoice
   - Bill of Lading
   - Certificate of Origin
   - (Add others as per LC terms)

6. **Save** → **Submit**

**Done!** Your LC is now active and being tracked.

---

## 📦 Step 3: Track Shipments (1 minute)

**When goods are shipped:**

1. **Open your LC**
2. **Scroll to "Shipments"** section
3. **Click "Add Row"**
4. **Fill in:**

```
Shipment Date: [When shipped]          Example: 10-Mar-2026
B/L or AWB Number: [Shipping doc no.]  Example: MAEU123456
Shipped Value: [Value shipped]         Example: 25000
```

5. **Save**

**Watch:** Utilized Amount updates automatically!

---

## 📄 Step 4: Manage Documents (1 minute)

**As documents are prepared:**

1. **Open your LC**
2. **Go to "Required Documents"** table
3. **For each document:**
   - Change **Status** to "Submitted"
   - Enter **Submitted Date**
   - **Attach** document file (optional)
   - Add **Remarks** if needed

4. **Save**

**Track:** All documents in one place!

---

## 📊 Step 5: Use Reports (30 seconds)

### Daily Check: LC Expiry Report

1. **From workspace**, click **"LC Expiry Report"** (red button)
2. **See:** LCs expiring soon
3. **Take action** on urgent items

### Weekly Review: LC Register

1. **From workspace**, click **"LC Register"**
2. **See:** All your LCs with status
3. **Filter** by date, type, or status as needed

---

## 🔧 Quick Tips for Success

### ✅ DO:
- **Always link** to Purchase/Sales Orders (saves time!)
- **Set expiry dates** with 15-30 day buffer
- **Update shipments** immediately
- **Check expiry report** daily
- **Record all charges** for accurate costing

### ❌ DON'T:
- Don't submit LC until bank actually opens it
- Don't set unrealistic expiry dates
- Don't forget to update document status
- Don't ignore the expiry report alerts
- Don't skip recording charges

---

## 🎯 Common Scenarios

### Scenario 1: Import LC for Raw Materials

```
1. Supplier sends Proforma Invoice
2. Create Purchase Order in ERPNext
3. Create LC (Import type)
4. Link to Purchase Order
5. Bank opens LC → Update LC Number
6. Submit LC
7. Track shipment when goods dispatched
8. Update documents when received
9. Make payment
10. Close LC when settled
```

### Scenario 2: Export LC from Customer

```
1. Customer's bank opens LC
2. Create Sales Order in ERPNext
3. Create LC (Export type)
4. Link to Sales Order
5. Enter LC details from bank advice
6. Submit LC
7. Ship goods → Add shipment
8. Prepare documents → Update status
9. Submit documents to bank
10. Receive payment → Close LC
```

### Scenario 3: LC Amendment (Date Extension)

```
1. Shipment delayed - need more time
2. Open the LC
3. Click "Actions" → "Create Amendment"
4. Enter new expiry date
5. Enter reason: "Delay in Shipment"
6. Save as draft
7. Contact bank for amendment
8. After bank confirms → Submit amendment
9. LC automatically updates with new date
```

---

## 🆘 Quick Troubleshooting

### Problem: Can't submit LC
**Solution:** Check all required fields (marked with *) are filled

### Problem: Utilized amount not updating
**Solution:** Click Save after adding/editing shipments

### Problem: Can't find my LC
**Solution:** Check it's submitted (Draft LCs don't show in some reports)

### Problem: Need to change submitted LC
**Solution:** Create an Amendment instead (can't edit submitted LCs)

---

## 📱 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Search | `/` (forward slash) |
| Create New | `Ctrl + K` |
| Save | `Ctrl + S` |
| Submit | `Ctrl + Enter` |

---

## 🎓 Next Steps

### Learn More:
1. **Read full User Manual** for detailed field explanations
2. **Review Best Practices** section
3. **Watch** (upcoming video tutorials)

### Customize:
1. **Set up** your document templates
2. **Create** LC amount thresholds
3. **Configure** email alerts for expiry

### Optimize:
1. **Run monthly** cost analysis reports
2. **Compare** bank charges
3. **Negotiate** better rates based on data

---

## 🔗 Quick Reference

### Essential Fields

**Creating LC:**
- LC Number *(Bank reference)*
- LC Type *(Sight, Usance, etc.)*
- Transaction Type *(Import/Export)*
- Dates *(Opening, Expiry, Shipment)*
- Parties *(Applicant, Beneficiary)*
- Bank *(Issuing Bank)*
- Amount *(LC value)*
- Currency *(USD, EUR, etc.)*

**Adding Shipment:**
- Shipment Date
- B/L or AWB Number
- Shipped Value

**Tracking Documents:**
- Document Type
- Status *(Pending/Submitted/Accepted)*
- Submitted Date

**Recording Charges:**
- Charge Type
- Amount
- Currency
- Date

### Report Purpose

| Report | Use For |
|--------|---------|
| **LC Register** | Overview of all LCs |
| **LC Expiry** | Daily expiry monitoring |
| **LC Utilization** | Working capital analysis |
| **LC Charges** | Cost tracking & budgeting |

### Status Flow

```
Draft → Opened → Documents Submitted → 
Documents Accepted → Payment Made → Settled
```

---

## 💡 Pro Tips

**Tip 1: Use Tolerance Wisely**
```
Set 5-10% tolerance for flexibility
Example: LC $100,000 + 5% = $105,000 max
Prevents minor quantity variations from causing issues
```

**Tip 2: Create Document Checklist**
```
As soon as LC opens, list ALL required documents
Assign someone to prepare each
Set internal deadlines (before LC expiry)
```

**Tip 3: Monitor Expiry Daily**
```
Make it part of morning routine:
- Open LC Expiry Report
- Check "Expiring This Week"
- Take immediate action
- Never let LC expire unused
```

**Tip 4: Link Everything**
```
Link LC to:
- Purchase/Sales Order (auto-fills data)
- Delivery Note (auto-fills shipment)
- Payment Entry (tracks payments)
- Charges (complete cost picture)
```

**Tip 5: Export Reports**
```
Export to Excel for:
- Custom analysis
- Charts and graphs
- Management presentations
- Year-end reviews
```

---

## 📞 Getting Help

**In-App Help:**
- Hover over field labels for tooltips
- Click "?" icon for field descriptions

**Documentation:**
- Full User Manual (detailed guide)
- Features Document (what app does)

**Support:**
- ERPNext Community Forums
- Email: support@addsol.com

---

## ✅ Quick Start Checklist

Before you begin:
- [ ] ERPNext 15 installed
- [ ] LC app installed
- [ ] Have Accounts Manager/User role
- [ ] Have first LC details ready

Your first LC:
- [ ] Accessed LC workspace
- [ ] Created Purchase/Sales Order
- [ ] Created LC document
- [ ] Filled all required fields
- [ ] Added required documents
- [ ] Saved and submitted

After submission:
- [ ] Added shipment details
- [ ] Updated document status
- [ ] Recorded charges
- [ ] Checked expiry report

---

## 🎯 Success Metrics

**After your first week:**
- ✅ All LCs created in system
- ✅ Daily expiry check routine established
- ✅ Team trained on basics
- ✅ Documents tracked properly

**After first month:**
- ✅ All shipments updated real-time
- ✅ All charges recorded
- ✅ Monthly reports generated
- ✅ Cost analysis completed

**After first quarter:**
- ✅ Process optimizations identified
- ✅ Bank negotiations based on data
- ✅ Team fully proficient
- ✅ System integrated in daily workflow

---

## 🚀 You're Ready!

You now know enough to:
- Create and manage LCs
- Track shipments and documents
- Monitor expiry dates
- Use reports for insights
- Record costs accurately

**Start with one LC and build from there!**

---

*For detailed explanations of every field and advanced features, refer to the complete User Manual.*

**Welcome to efficient LC management! 🎉**