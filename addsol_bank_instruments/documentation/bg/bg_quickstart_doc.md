# BG Management - Quick Start Guide

**Get up and running with BG Management in 15 minutes**

**Version:** 1.0  
**For:** ERPNext 15.x  
**Module:** BG Management  
**App:** addsol_lc

---

## Prerequisites Checklist

Before you begin, ensure you have:

- [ ] ERPNext 15.x installed and running
- [ ] Admin/System Manager access
- [ ] Custom app `addsol_lc` created (or existing)
- [ ] Bench access (terminal/SSH)
- [ ] Basic understanding of ERPNext DocTypes

**Estimated Time:** 15-20 minutes

---

## Installation Steps

### Step 1: Create Directory Structure (2 minutes)

Open your terminal and run:

```bash
# Navigate to your app
cd ~/frappe-bench/apps/addsol_lc/addsol_lc/addsol_lc/

# Create DocType directories
mkdir -p doctype/bg_management
mkdir -p doctype/bg_management_extension
mkdir -p doctype/bg_management_document

# Create Report directory
mkdir -p report/active_bg_management
```

✅ **Checkpoint:** Verify directories created:
```bash
ls -la doctype/bg_management
ls -la report/active_bg_management
```

---

### Step 2: Create DocType Files (5 minutes)

#### 2.1 Main DocType - BG Management

Create `doctype/bg_management/bg_management.json`:
```bash
nano doctype/bg_management/bg_management.json
```

**Copy the JSON from artifact:** "BG Management DocType JSON"

Create `doctype/bg_management/bg_management.py`:
```bash
nano doctype/bg_management/bg_management.py
```

**Copy the Python from artifact:** "BG Management Controller (bg_management.py)"

Create `doctype/bg_management/bg_management.js`:
```bash
nano doctype/bg_management/bg_management.js
```

**Copy the JavaScript from artifact:** "BG Management Client Script (bg_management.js)"

Create `doctype/bg_management/__init__.py`:
```bash
touch doctype/bg_management/__init__.py
```

#### 2.2 Child Tables

**BG Management Extension:**
```bash
nano doctype/bg_management_extension/bg_management_extension.json
```
Copy from artifact: "BG Management Extension Child Table"

```bash
touch doctype/bg_management_extension/__init__.py
```

**BG Management Document:**
```bash
nano doctype/bg_management_document/bg_management_document.json
```
Copy from artifact: "BG Management Document Child Table"

```bash
touch doctype/bg_management_document/__init__.py
```

✅ **Checkpoint:** Verify all files created:
```bash
ls -la doctype/bg_management/
ls -la doctype/bg_management_extension/
ls -la doctype/bg_management_document/
```

---

### Step 3: Create Report (3 minutes)

Create `report/active_bg_management/active_bg_management.json`:
```bash
nano report/active_bg_management/active_bg_management.json
```

Paste this:
```json
{
 "add_total_row": 0,
 "columns": [],
 "creation": "2025-01-24 00:00:00.000000",
 "disable_prepared_report": 0,
 "disabled": 0,
 "docstatus": 0,
 "doctype": "Report",
 "filters": [],
 "idx": 0,
 "is_standard": "Yes",
 "modified": "2025-01-24 00:00:00.000000",
 "module": "Addsol LC",
 "name": "Active BG Management",
 "owner": "Administrator",
 "prepared_report": 0,
 "ref_doctype": "BG Management",
 "report_name": "Active BG Management",
 "report_type": "Script Report",
 "roles": [
  {
   "role": "Accounts Manager"
  },
  {
   "role": "Accounts User"
  }
 ]
}
```

Create `report/active_bg_management/active_bg_management.py`:
```bash
nano report/active_bg_management/active_bg_management.py
```
Copy from artifact: "Active Bank Guarantees Report"

Create `report/active_bg_management/active_bg_management.js`:
```bash
nano report/active_bg_management/active_bg_management.js
```

Paste this:
```javascript
frappe.query_reports["Active BG Management"] = {
    "filters": [
        // Copy filters JSON from "Active Bank Guarantees Report Filters" artifact
    ]
};
```

✅ **Checkpoint:** Verify report files:
```bash
ls -la report/active_bg_management/
```

---

### Step 4: Update Hooks (2 minutes)

Edit your `hooks.py`:
```bash
nano hooks.py
```

Add these lines (or merge with existing scheduler_events):
```python
# Scheduled Tasks
scheduler_events = {
    "daily": [
        "addsol_lc.addsol_lc.doctype.bg_management.bg_management.send_expiry_notifications"
    ]
}
```

✅ **Checkpoint:** Verify hooks.py contains the scheduler event

---

### Step 5: Install and Migrate (3 minutes)

```bash
# Navigate to bench directory
cd ~/frappe-bench

# If app not installed yet
bench --site your-site.local install-app addsol_lc

# If app already installed, migrate
bench --site your-site.local migrate

# Clear cache
bench --site your-site.local clear-cache

# Build assets
bench build --app addsol_lc

# Restart bench
bench restart
```

**Expected Output:**
```
Migrating your-site.local
Executing addsol_lc.patches...
Creating tables...
✓ BG Management created
✓ BG Management Extension created
✓ BG Management Document created
Migration complete!
```

✅ **Checkpoint:** No errors in migration

---

### Step 6: Enable Scheduler (1 minute)

```bash
# Enable scheduler for notifications
bench --site your-site.local enable-scheduler

# Verify scheduler status
bench doctor
```

**Expected Output:**
```
Scheduler: Enabled
```

✅ **Checkpoint:** Scheduler is enabled

---

## First Use - Create Your First BG

### Step 1: Login to ERPNext

Open browser: `http://your-site.local`

### Step 2: Navigate to BG Management

**Method 1:** Awesomebar
- Press `Ctrl + K` (or `Cmd + K` on Mac)
- Type "BG Management"
- Press Enter

**Method 2:** Module Navigation
- Click "Addsol LC" module
- Click "BG Management"
- Click "New"

### Step 3: Fill Basic Details

**Required Fields (marked with red asterisk):**

1. **BG Number**: `BG-2025-001`
2. **Type of BG**: Select "Performance Bank Guarantee"
3. **Applicant (Company)**: Select your company
4. **Issuing Bank**: Select bank (create if doesn't exist)
5. **FD Amount**: `53,010`
6. **Maturity Amount**: `58,583`
7. **Issue Date**: Today's date (auto-filled)
8. **Expiry Date**: `29-03-2026`
9. **FD Maturity Date**: `30-05-2026`

### Step 4: Fill Optional Details

**Party Details:**
- Beneficiary Type: Customer
- Beneficiary: Select customer
- Project: Select if applicable

**FD Details:**
- FD No.: `481513000628`
- Utilized Amount: `53,010` (if already utilized)

**Charges:**
- Commission Rate: `1.5` (%)
- Processing Charges: `500`

Watch auto-calculations happen:
- Commission Amount: Auto-calculated
- Total Charges: Auto-calculated
- Available Amount: Auto-calculated
- Days to Expiry: Auto-calculated

### Step 5: Upload Documents

**Scroll to Documents section:**
1. Click "Attach" under "BG Document"
2. Upload your BG PDF/image
3. Click "Attach" under "FD Receipt"
4. Upload FD receipt

**Optional:** Add supporting documents in child table

### Step 6: Save and Submit

1. Click **Save** (top right)
2. Review all details
3. Click **Submit**

🎉 **Success!** Your first BG is now in the system!

---

## Quick Tasks

### Task 1: Extend a BG (1 minute)

1. Open any submitted BG
2. Click **Actions** dropdown
3. Click **Extend BG**
4. Fill the dialog:
   - New Expiry Date: Future date
   - Extension Charges: Amount
   - Remarks: Reason
5. Click **Extend**

✅ Status changes to "Extended"
✅ Extension added to history

### Task 2: Mark as Claimed (1 minute)

1. Open any submitted BG
2. Click **Actions** → **Mark as Claimed**
3. Fill:
   - Claim Date: When claimed
   - Claim Amount: Amount claimed
4. Click **Mark as Claimed**

✅ Status changes to "Claimed"

### Task 3: Close a BG (1 minute)

1. Open any submitted BG
2. Click **Actions** → **Close BG**
3. Enter closure remarks
4. Click **Close**

✅ Status changes to "Closed"

### Task 4: View Report (1 minute)

1. Navigate to **Reports** → **Addsol LC**
2. Click **Active BG Management**
3. Apply filters (optional):
   - Company
   - Bank
   - Expiring in Days: `30`
4. Click **Refresh**

✅ See all BGs with charts and summaries

---

## Testing Your Installation

### Test Checklist

Run through this checklist to verify everything works:

#### Basic Functionality
- [ ] Can create new BG Management document
- [ ] All required fields validate properly
- [ ] Can save draft BG
- [ ] Can submit BG
- [ ] Can amend BG
- [ ] Can cancel BG

#### Calculations
- [ ] Days to Expiry calculates correctly
- [ ] Available Amount = Maturity - Utilized
- [ ] Commission Amount = FD Amount × Rate / 100
- [ ] Total Charges = Commission + Processing

#### Extensions
- [ ] Can extend a submitted BG
- [ ] Extension history records properly
- [ ] Extension number increments
- [ ] Status changes to "Extended"

#### Status Management
- [ ] Status shows as "Active" when valid
- [ ] Status changes to "Expired" when past date
- [ ] Status changes to "Claimed" when claim date set
- [ ] Status changes to "Closed" via button

#### Notifications
- [ ] Email sent on submission (check email)
- [ ] Scheduler is running (check doctor)
- [ ] Can manually trigger notification

#### Reports
- [ ] Active BG Management report loads
- [ ] Filters work correctly
- [ ] Chart displays
- [ ] Summary shows correct totals
- [ ] Can export to Excel/PDF

#### Documents
- [ ] Can attach BG document
- [ ] Can attach FD receipt
- [ ] Can add supporting documents
- [ ] Documents download properly

---

## Troubleshooting

### Issue: DocType not appearing

**Solution:**
```bash
bench --site your-site.local migrate
bench --site your-site.local clear-cache
bench restart
```

### Issue: Permission denied

**Solution:**
1. Go to: **Setup** → **Permissions** → **Role Permission Manager**
2. Select DocType: "BG Management"
3. Add role: "Accounts User" or "Accounts Manager"
4. Grant permissions: Read, Write, Create, Submit

### Issue: Reports not loading

**Solution:**
```bash
bench build --app addsol_lc
bench --site your-site.local clear-cache
```

### Issue: Scheduler not sending emails

**Solution:**
```bash
# Check scheduler status
bench doctor

# Enable if disabled
bench --site your-site.local enable-scheduler

# Check Error Log
# Navigate to: Tools → Error Log
```

### Issue: Notifications not working

**Check:**
1. Email account configured: **Setup** → **Email** → **Email Account**
2. SMTP settings correct
3. Scheduler enabled: `bench doctor`
4. Check **Error Log** for email errors

### Issue: Import errors during migration

**Solution:**
```bash
# Check syntax errors
cd ~/frappe-bench/apps/addsol_lc
python -m py_compile addsol_lc/addsol_lc/doctype/bg_management/bg_management.py

# If errors, fix Python syntax and retry
bench --site your-site.local migrate
```

---

## Quick Reference Commands

### Common Bench Commands

```bash
# Navigate to bench
cd ~/frappe-bench

# Migrate changes
bench --site your-site.local migrate

# Clear cache
bench --site your-site.local clear-cache

# Build assets
bench build --app addsol_lc

# Restart
bench restart

# Check status
bench doctor

# View logs
bench --site your-site.local console

# Enable scheduler
bench --site your-site.local enable-scheduler

# Backup
bench --site your-site.local backup
```

### Useful ERPNext Shortcuts

- `Ctrl + K`: Awesomebar (quick search)
- `Ctrl + G`: Quick list navigation
- `Ctrl + S`: Save document
- `Ctrl + Shift + S`: Submit document

---

## Next Steps

Now that you're set up, here's what to do next:

### Immediate Actions (Today)
1. ✅ Import existing BGs from Excel
2. ✅ Set up email templates (optional)
3. ✅ Configure user permissions
4. ✅ Train team on basic operations

### This Week
1. Create custom print format
2. Set up custom fields (if needed)
3. Create additional reports
4. Link to existing LC module
5. Configure workflows (if needed)

### Ongoing
1. Monitor expiry notifications
2. Review reports weekly
3. Archive closed BGs monthly
4. Train new users as needed

---

## Data Migration from Excel

If you have existing BG data in Excel:

### Quick Import Steps

1. **Prepare Excel File**
   - Save as CSV
   - Ensure dates in YYYY-MM-DD format
   - Map column names

2. **Use Data Import**
   - Go to: **Setup** → **Data** → **Data Import**
   - Select DocType: "BG Management"
   - Upload CSV
   - Map columns to fields
   - Validate and import

### Column Mapping Example

```
Excel Column          →  Field Name
──────────────────────────────────────
FD NO.               →  fd_number
FD AMOUNT            →  fd_amount
MATURITY AMOUNT      →  maturity_amount
TYPE OF BG           →  bg_type
ISSUE DATE           →  issue_date
Expiry Date          →  expiry_date
MATURITY DATE        →  fd_maturity_date
UTILIZED AMOUNT      →  utilized_amount
```

**Note:** You'll need to submit records manually after import

---

## Getting Help

### Resources
- **Features Document**: Complete feature list
- **User Manual**: Detailed usage guide
- **Implementation Guide**: Technical details

### Support Channels
- ERPNext Forum: https://discuss.erpnext.com
- Frappe Documentation: https://frappeframework.com/docs
- ERPNext Docs: https://docs.erpnext.com

### Common Questions

**Q: Can I rename "BG Management" to something else?**  
A: Yes, but not recommended. If needed, use "Rename" feature in ERPNext.

**Q: How do I add more BG types?**  
A: Setup → Customize → Customize Form → Select "BG Management" → Find "Type of BG" field → Add options

**Q: Can I change notification days?**  
A: Yes, edit `bg_management.py` and modify the `notification_days` list

**Q: How do I backup my BG data?**  
A: Regular bench backups include BG data: `bench --site your-site.local backup`

**Q: Can I use this on mobile?**  
A: Yes! ERPNext mobile app fully supports BG Management

---

## Congratulations! 🎉

You've successfully installed and configured BG Management!

**You can now:**
- ✅ Create and manage bank guarantees
- ✅ Track FD details and utilization
- ✅ Manage extensions with full history
- ✅ Receive automatic expiry notifications
- ✅ Generate comprehensive reports
- ✅ Attach and manage documents
- ✅ Monitor financial charges

**Quick Start Complete!**

---

**Time Taken:** ~15-20 minutes  
**Difficulty Level:** Intermediate  
**Next Document:** Read the User Manual for detailed usage instructions

---

**Document Version:** 1.0  
**Last Updated:** January 2025  
**For Support:** Refer to User Manual or contact your system administrator