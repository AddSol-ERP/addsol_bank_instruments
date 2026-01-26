# BG Management - User Manual

**Complete Guide to Using BG Management Module**

**Version:** 1.0  
**Module:** BG Management  
**App:** addsol_lc  
**For:** ERPNext 15.x  
**Last Updated:** January 2025

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Creating a Bank Guarantee](#creating-a-bank-guarantee)
4. [Managing Bank Guarantees](#managing-bank-guarantees)
5. [Extensions and Renewals](#extensions-and-renewals)
6. [Claims and Closures](#claims-and-closures)
7. [Document Management](#document-management)
8. [Reports and Analytics](#reports-and-analytics)
9. [Notifications and Alerts](#notifications-and-alerts)
10. [Advanced Features](#advanced-features)
11. [Best Practices](#best-practices)
12. [Troubleshooting](#troubleshooting)
13. [FAQs](#faqs)

---

## Introduction

### What is BG Management?

BG Management is a comprehensive Bank Guarantee management module for ERPNext 15 that helps organizations:
- Track bank guarantees throughout their lifecycle
- Manage Fixed Deposit (FD) details and utilization
- Handle extensions with complete history
- Monitor expiry dates with automatic alerts
- Generate comprehensive reports
- Maintain complete documentation

### Why "BG Management" and not "Bank Guarantee"?

ERPNext 15 already includes a standard "Bank Guarantee" DocType in the Accounts module. To avoid naming conflicts and provide enhanced functionality, this custom module is named "BG Management".

### Who Should Use This Manual?

This manual is designed for:
- **Accounts Managers**: Full access to all features
- **Accounts Users**: Day-to-day BG operations
- **Project Managers**: Monitoring project-related BGs
- **Finance Team**: Financial tracking and reporting
- **Auditors**: Reviewing BG history and compliance

### Key Benefits

- ✅ **Centralized Management**: All BG information in one place
- ✅ **Automated Alerts**: Never miss an expiry date (30, 15, 7, 3, 1 days before)
- ✅ **Complete Audit Trail**: Every change is tracked with version history
- ✅ **Financial Visibility**: Real-time FD and utilization tracking
- ✅ **Extension History**: Full audit trail of all extensions
- ✅ **Compliance Ready**: Complete documentation and history
- ✅ **Time Saving**: Automated calculations and notifications

---

## Getting Started

### Accessing BG Management

#### Method 1: Using Awesomebar (Fastest)
1. Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac)
2. Type "BG Management"
3. Press Enter

#### Method 2: Through Modules
1. Click on **Modules** in top navigation bar
2. Select **Addsol LC**
3. Click **BG Management**

#### Method 3: Using Search
1. Click the search icon in top right corner
2. Search for "BG Management"
3. Click on the result

### Understanding the Interface

#### List View
When you first open BG Management, you'll see the list view displaying:

**Columns:**
- **BG Number**: Unique identifier (clickable to open)
- **Type**: Category of guarantee
- **Status**: Current state with color indicator
- **FD Number**: Fixed deposit reference

**List View Actions:**
- Click any row to open the document
- Use filters (left sidebar) to find specific BGs
- Use search box for quick lookup
- Click "New" button to create a BG
- Select multiple rows for bulk actions

**Status Colors:**
- 🟢 Green: Active
- 🔵 Blue: Extended
- 🔴 Red: Expired
- 🟠 Orange: Claimed
- ⚪ Gray: Closed
- ⚫ Dark Gray: Cancelled

#### Form View
When you open a BG document, you'll see organized sections:

1. **Basic Details**
   - BG Number, Type, Status
   
2. **Party Details**
   - Beneficiary information
   - Company and project links
   
3. **Financial Details**
   - Bank, FD details, amounts
   
4. **Date Details**
   - Issue, expiry, maturity dates
   - Days to expiry calculation
   
5. **Extension Details** (Collapsible)
   - Extension history
   - Extension dates and charges
   
6. **Charges & Commission**
   - Commission calculation
   - Processing charges
   
7. **Documents & Attachments**
   - BG document, FD receipt
   - Supporting documents table
   
8. **Remarks**
   - Notes and internal comments

---

## Creating a Bank Guarantee

### Step-by-Step Guide

#### Step 1: Start New BG

1. Navigate to BG Management list view
2. Click **New** button (top right corner)
3. A new blank form opens

#### Step 2: Fill Basic Details

**BG Number** ⭐ (Required)
- Enter unique BG number
- Examples: 
  - `BG-2025-001`
  - `BG/HDFC/2025/001`
  - `481513000628` (FD number as reference)
- This becomes the document name
- Must be unique across all BGs
- System will show error if duplicate

**Type of BG** ⭐ (Required)
- Click dropdown to select
- Available types:
  - **Performance Bank Guarantee**: Most common, ensures contract performance
  - **Bid Bond Guarantee**: Submitted with tender/bid
  - **Advance Payment Guarantee**: For advance payments received
  - **Retention Money Guarantee**: In lieu of retention money
  - **Financial Guarantee**: General financial obligations
  - **Payment Guarantee**: Ensures payment obligations
  - **Warranty Guarantee**: For warranty period
- Select the appropriate type

**Status** (Auto-set)
- Automatically set to "Active"
- Don't change manually
- System manages status automatically

#### Step 3: Fill Party Details

**Beneficiary Type** (Optional but recommended)
- Select party type from dropdown
- Options: Customer, Supplier, Employee, etc.
- Determines what appears in Beneficiary dropdown

**Beneficiary** (Optional but recommended)
- Select specific party
- Dropdown shows parties of selected type
- Example: Select "ABC Corporation" from Customer list
- Name auto-fetches in next field

**Beneficiary Name** (Auto-fetched)
- Automatically filled from party master
- Read-only field
- Shows for reference

**Applicant (Company)** ⭐ (Required)
- Your company name
- Auto-filled with user's default company
- Change if managing multiple companies
- Example: "Your Company Pvt Ltd"

**Project** (Optional)
- Link to specific project
- Dropdown shows all active projects
- Useful for project-wise BG tracking
- Example: "Metro Line 3 Construction"

**Purchase Order** (Optional)
- Link to specific PO
- For supplier BGs
- Example: "PO-2025-001"

**Sales Order** (Optional)
- Link to specific SO
- For customer BGs
- Example: "SO-2025-042"

#### Step 4: Fill Financial Details

**Issuing Bank** ⭐ (Required)
- Select bank from master
- Click dropdown to see available banks
- If bank not in list:
  1. Type bank name
  2. Click "Create a new Bank"
  3. Enter bank details
  4. Save and return
- Example: "HDFC Bank", "State Bank of India"

**Bank Account** (Optional)
- Select specific bank account
- Dropdown automatically filters to show only accounts of selected bank
- Useful for tracking which account is blocked
- Example: "HDFC Current Account - 12345"

**FD Number** (Required before submission)
- Enter Fixed Deposit number
- Can be alphanumeric
- Example: `481513000628`
- This is your reference to bank FD

**FD Amount** ⭐ (Required)
- Enter fixed deposit amount
- This is the amount blocked with bank
- Example: `53,010.00`
- Use proper currency format

**Maturity Amount** ⭐ (Required)
- Enter FD maturity value
- Usually higher than FD amount (includes interest)
- Example: `58,583.00`
- This is what you'll receive at maturity

**Utilized Amount** (Optional, defaults to 0)
- Enter if already partially utilized
- Example: `53,010.00` if fully utilized
- Updates automatically when claimed
- Cannot exceed maturity amount

**Available Amount** (Auto-calculated, Read-only)
- System calculates automatically
- Formula: Maturity Amount - Utilized Amount
- Example: If Maturity = 58,583 and Utilized = 53,010, then Available = 5,573
- Updates in real-time

#### Step 5: Fill Date Details

**Issue Date** ⭐ (Required)
- Date when BG was issued by bank
- Auto-filled with today's date
- Change if BG was issued earlier
- Format: DD-MM-YYYY
- Example: `08-01-2025`

**Expiry Date** ⭐ (Required)
- Original expiry date of BG
- Must be after issue date
- Example: `29-03-2026`
- System validates this

**FD Maturity Date** ⭐ (Required)
- When the Fixed Deposit matures
- Should be on or after BG expiry date
- Example: `30-05-2026`
- System validates this

**Days to Expiry** (Auto-calculated, Read-only)
- System calculates remaining days
- Based on current date vs expiry date
- If extended, uses extension expiry date
- Updates automatically
- Example: `64` (days remaining)

**Claim Date** (Leave blank initially)
- Fill only when BG is actually claimed
- Leave empty for active BGs
- Will be filled when marking as claimed

#### Step 6: Extension Details (Initially Collapsed)

**Is Extended** (Checkbox)
- Leave unchecked when creating new BG
- Will be automatically checked when you extend
- Don't manually check

**Extension Expiry Date**
- Shows only when extended
- Automatically filled during extension process

**Extension Claim Date**
- For reference if extension period has separate claim date
- Optional field

**Extension History** (Child Table)
- Empty initially
- Automatically populated when you extend BG
- Shows complete extension audit trail

#### Step 7: Charges & Commission (Optional)

**Commission Rate** (Optional)
- Enter bank's commission rate as percentage
- Example: `1.5` for 1.5%
- Decimal allowed: `0.75` for 0.75%

**Commission Amount** (Auto-calculated, Read-only)
- System calculates automatically
- Formula: (FD Amount × Commission Rate) / 100
- Example: If FD = 53,010 and Rate = 1.5%, then Commission = 795.15
- Updates when FD amount or rate changes

**Processing Charges** (Optional)
- Enter any one-time or recurring charges
- Example: `500` for ₹500 processing fee
- Bank charges, documentation charges, etc.

**Total Charges** (Auto-calculated, Read-only)
- Sum of commission and processing charges
- Example: Commission 795.15 + Processing 500 = Total 1,295.15
- Updates automatically

#### Step 8: Upload Documents

**BG Document** ⭐ (Required before submission)
- Click "Attach" button
- Browse and select BG document file
- Supported formats: PDF (recommended), JPG, PNG, Word
- File should be clear and readable
- Example: Original BG letter from bank
- Upload completes and shows filename

**FD Receipt** (Recommended)
- Click "Attach" button
- Select FD receipt/certificate
- Proof of fixed deposit
- Same supported formats as above

**Supporting Documents** (Optional, see detailed section below)
- Multiple documents can be added via child table
- See [Document Management](#document-management) for details

#### Step 9: Add Remarks

**Remarks** (Optional)
- Rich text editor available
- Add any relevant notes about the BG
- Examples:
  - "Performance guarantee for Metro project Phase 2"
  - "Beneficiary: ABC Corporation for contract #12345"
  - "Valid for 12 months from project start date"
- Visible to all users with access
- Can format text (bold, italic, bullets, etc.)

**Internal Notes** (Optional)
- Plain text area
- For internal team reference only
- Can include sensitive information
- Examples:
  - "Bank contact: Mr. Sharma, 98765-43210"
  - "Renewal reminder set for 15 days before expiry"
  - "Related to LC-2025-001"

#### Step 10: Save and Submit

**Option 1: Save as Draft**
1. Click **Save** button (top right)
2. Document is saved but not submitted
3. Status shows "Draft" in orange
4. Can edit freely anytime
5. Not locked, no notifications sent
6. Good for partial completion

**When to Save as Draft:**
- Information is incomplete
- Waiting for BG document from bank
- Need to verify details
- Want to come back later

**Option 2: Submit**
1. Review all details carefully
2. Ensure all required fields are filled
3. Verify BG document is attached
4. Verify FD number is entered
5. Click **Submit** button
6. Confirmation dialog appears
7. Click "Yes" to confirm
8. Document is now submitted

**After Submission:**
- Status changes to "Active" (green)
- Document is locked (cannot edit directly)
- Action buttons appear (Extend, Claim, Close)
- Email notification sent to Accounts Managers
- To make changes, use "Amend" button
- Can view but not edit

### Validation Checks

Before submission, system automatically validates:

✅ **BG Number is unique** - No duplicate BG numbers allowed  
✅ **Required fields filled** - All fields marked with ⭐  
✅ **Expiry after issue** - Expiry date must be after issue date  
✅ **FD maturity valid** - FD maturity on or after BG expiry  
✅ **Utilized ≤ Maturity** - Utilized cannot exceed maturity amount  
✅ **BG document attached** - Main BG document is required  
✅ **FD number entered** - FD reference is mandatory  

If any validation fails:
- Error message appears in red
- Specific issue is highlighted
- Fix the issue and try again

### What Happens After Submission

Once successfully submitted:

✅ **Document is locked** - Cannot edit directly  
✅ **Status becomes Active** - Green indicator  
✅ **Notifications sent** - Emails to Accounts Managers  
✅ **Action buttons appear** - Extend, Claim, Close options  
✅ **Audit trail starts** - All changes tracked  
✅ **Can amend** - Use Amend to make changes  
✅ **Can cancel** - If needed, can cancel document  
✅ **Scheduler monitors** - System watches for expiry  

---

## Managing Bank Guarantees

### Viewing BG Details

#### Opening a BG Document

**From List View:**
1. Navigate to BG Management list
2. Find the BG you want to view
3. Click on the BG Number (clickable link)
4. Document opens in form view

**Using Awesomebar:**
1. Press `Ctrl + K`
2. Type BG number (e.g., "BG-2025-001")
3. Select from results
4. Document opens

**From Reports:**
1. Run Active BG Management report
2. Click on BG Number in report
3. Document opens

#### Reading the Form

**Status Indicator** (Top right corner)
- Large colored badge shows current status
- **Green "Active"**: BG is valid and active
- **Blue "Extended"**: BG has been extended
- **Red "Expired"**: Past expiry date
- **Orange "Claimed"**: Beneficiary has invoked
- **Gray "Closed"**: Normally closed
- **Dark Gray "Cancelled"**: Cancelled document

**Alert Messages** (Below toolbar, above form)
- **Red Banner**: "This Bank Guarantee has expired"
- **Red Alert**: "Expiring in 7 days" (or less)
- **Orange Alert**: "Expiring in 15 days" (8-15 days)
- **Yellow Alert**: "Expiring in 30 days" (16-30 days)
- No alert if more than 30 days remaining

**Section Navigation**
- Form is divided into clear sections
- Each section has a heading
- Collapsible sections (Extension Details) can be clicked to expand/collapse
- Scroll down to view all sections
- Key information is at the top

**Read-Only Fields**
- Grayed out fields cannot be edited
- These are auto-calculated or system-managed:
  - Status
  - Available Amount
  - Days to Expiry
  - Commission Amount
  - Total Charges
  - Extension Number
  - Extension Days

**Editable Fields** (if not submitted)
- White background
- Can click and type/select
- Shows cursor when hovering

### Searching and Filtering

#### Quick Search (In List View)

**Basic Search:**
1. In list view, locate search box at top
2. Type search term:
   - BG Number: "BG-2025-001"
   - Beneficiary name: "ABC Corp"
   - FD Number: "481513"
   - Status: "Active"
3. Press Enter or click search icon
4. Results filter immediately

**Search Tips:**
- Partial matches work ("BG-2025" finds all 2025 BGs)
- Case-insensitive
- Searches multiple fields automatically
- Clear search to see all records

#### Using Filters (Left Sidebar)

**Standard Filters:**
Available by default:
- **BG Number**: Exact match filter
- **Type**: Dropdown of BG types
- **Status**: Dropdown of statuses
- **Beneficiary**: Text match on beneficiary

**How to Use Standard Filters:**
1. Click on filter field in left sidebar
2. Enter value or select from dropdown
3. List updates automatically
4. Multiple filters combine (AND logic)

**Custom Filters:**

**Adding Custom Filter:**
1. Click **"+ Add Filter"** button (above standard filters)
2. **Step 1**: Select field name from dropdown
   - Example: "Bank", "Project", "FD Amount", "Days to Expiry"
3. **Step 2**: Select operator:
   - `=` (equals)
   - `!=` (not equals)
   - `>` (greater than)
   - `<` (less than)
   - `>=` (greater than or equal)
   - `<=` (less than or equal)
   - `like` (contains text)
   - `not like` (doesn't contain)
   - `in` (in list)
   - `is` (for null values)
4. **Step 3**: Enter value
   - For text: type value
   - For numbers: enter number
   - For dates: use date picker
   - For links: select from dropdown
5. Click **"Apply"** or press Enter
6. Filter applies immediately

**Example Custom Filters:**

**Find BGs expiring in next 30 days:**
- Field: "Days to Expiry"
- Operator: `<=`
- Value: `30`

**Find high-value BGs:**
- Field: "FD Amount"
- Operator: `>`
- Value: `100000`

**Find specific bank's BGs:**
- Field: "Bank"
- Operator: `=`
- Value: Select "HDFC Bank"

**Find unclaimed BGs:**
- Field: "Claim Date"
- Operator: `is`
- Value: "not set"

**Multiple Filters:**
- Add multiple filters for complex queries
- All conditions must be met (AND logic)
- Example: Bank = "HDFC" AND Days to Expiry < 30
- Filters stack on left sidebar
- Remove by clicking X on filter

**Clearing Filters:**
1. Click **"Clear Filters"** button at top of filter sidebar
2. All filters removed
3. Full list shows again

**Saving Filter Sets:**

**Save Your Filters:**
1. Set up your desired filters
2. Click **"Save Filters"** button
3. Enter a descriptive name
   - Example: "Expiring This Month", "HDFC Active BGs"
4. Click Save
5. Filter set is saved for reuse

**Using Saved Filters:**
1. Click **"Saved Filters"** dropdown
2. Select your saved filter set
3. Filters apply automatically
4. Edit or delete saved filters as needed

#### Sorting Data

**Single Column Sort:**
1. Click on column header in list view
2. List sorts ascending by that column
3. Click again to sort descending
4. Arrow icon shows sort direction (↑ or ↓)
5. Example: Click "Expiry Date" to see earliest expiring first

**Multi-Column Sort:**
1. Sort by first column (click header)
2. Hold **Shift** key
3. Click second column header while holding Shift
4. Both sorts apply
5. Example: Sort by Status, then by Expiry Date within each status

**Default Sort:**
- By default, sorted by "Modified" (most recent first)
- Can change default via List Settings

### Viewing History and Audit Trail

#### Version History (Change Log)

**Accessing Version History:**
1. Open any submitted BG document
2. Click **"View"** menu in toolbar
3. Select **"Version History"** from dropdown
4. Version history page opens

**What You See:**
- Complete list of all changes
- Chronological order (newest first)
- For each change:
  - **Date & Time**: When change was made
  - **User**: Who made the change
  - **Field Changed**: What was modified
  - **Old Value**: Previous value
  - **New Value**: New value

**Example Version History:**
```
Version 3 - 2025-01-15 14:30 by john@company.com
  Status: Extended → Claimed
  Claim Date: (not set) → 2025-01-15
  Utilized Amount: 0 → 53,010

Version 2 - 2025-01-10 10:15 by admin@company.com
  Extension Expiry Date: (not set) → 2025-06-29
  Status: Active → Extended

Version 1 - 2025-01-08 09:00 by admin@company.com
  Document Created
```

**Use Cases:**
- Audit compliance
- Tracking who made changes
- Understanding document evolution
- Resolving disputes
- Compliance requirements

#### Extension History

**Viewing Extension History:**
1. Open BG document (submitted and extended)
2. Scroll to **"Extension Details"** section
3. Click section header to expand (if collapsed)
4. View **"Extension History"** child table
5. Table shows all extensions chronologically

**Extension History Columns:**
- **Extension #**: Sequential number (1, 2, 3...)
- **Previous Expiry Date**: Expiry before this extension
- **New Expiry Date**: Updated expiry after extension
- **Extension Days**: Calculated days added
- **Extension Date**: When extension was processed
- **Extension Charges**: Cost of this extension
- **Approved By**: User who approved/processed
- **Remarks**: Notes about why extended

**Example Extension History:**

| Ext # | Previous Expiry | New Expiry | Days | Extension Date | Charges | Approved By | Remarks |
|-------|----------------|------------|------|----------------|---------|-------------|---------|
| 1 | 2025-03-29 | 2025-06-29 | 92 | 2025-03-15 | 1,000 | admin@co.com | Project delay |
| 2 | 2025-06-29 | 2025-09-29 | 92 | 2025-06-20 | 1,200 | admin@co.com | Additional scope |

**Benefits:**
- Complete audit trail of extensions
- Track total extension costs
- Know who approved each extension
- Compliance documentation
- Historical reference

### Printing and Exporting

#### Standard Print

**Printing a BG:**
1. Open the BG document
2. Click **"Print"** icon in toolbar (printer icon)
3. Print dialog opens
4. Select print format from dropdown:
   - Standard format (default)
   - Custom formats (if created)
5. Print preview shows
6. Options:
   - **Print**: Send to printer
   - **Download PDF**: Save as PDF file
   - **Email**: Send via email

**Print Settings:**
- Letter head (if configured)
- Company details
- BG details formatted
- Terms and conditions (if added)

#### Exporting Document

**Export Single BG:**
1. Open BG document
2. Click **"Menu"** (three dots) in toolbar
3. Select **"Export"**
4. Choose format:
   - **JSON**: For data import/backup
   - **Excel**: Spreadsheet format
5. File downloads
6. Can be re-imported if needed

**Bulk Export:**
See [Reports and Analytics](#reports-and-analytics) section

---

## Extensions and Renewals

### Understanding Extensions

**What is an Extension?**
- Extending the expiry date of an existing BG
- New expiry date set beyond original expiry
- Original BG continues (no new BG created)
- Complete history maintained

**When to Extend:**
- Project duration increased
- Beneficiary requests extension
- Contract extended
- Original expiry approaching but work ongoing
- Performance period needs more time
- Mutual agreement with beneficiary

**Extension vs New BG:**
- **Extension**: Same BG, new expiry, history maintained
- **New BG**: Cancel old, create new, separate records

### Extension Process

#### Step 1: Check Eligibility

**BG Must Be:**
- ✅ Submitted (not draft)
- ✅ Status: Active or Extended (not Claimed, Closed, or Cancelled)
- ✅ You have permission to extend

**If Eligibility Not Met:**
- Draft BG: Submit first
- Claimed BG: Cannot extend claimed BGs
- Closed BG: Cannot extend closed BGs
- Cancelled BG: Create new BG instead

#### Step 2: Open BG and Launch Extension

1. Navigate to the BG document
2. Ensure document is open in form view
3. Locate **"Actions"** dropdown button (top right area of toolbar)
4. Click **"Actions"**
5. From dropdown menu, select **"Extend BG"**
6. Extension dialog window opens

**If "Extend BG" Not Visible:**
- Check BG is submitted
- Check status is Active/Extended
- Check you have permissions
- Refresh page and try again

#### Step 3: Fill Extension Dialog

Dialog contains fields:

**Current Expiry Date** (Read-only, for reference)
- Shows the current expiry date
- If not extended: shows original expiry date
- If already extended: shows last extension expiry date
- Example: `29-03-2026`
- Cannot be changed (for reference only)

**New Expiry Date** ⭐ (Required)
- Enter the new expiry date
- **Must be after current expiry date**
- Use date picker (click calendar icon)
- Example: If current is `29-03-2026`, new could be `29-06-2026`
- System validates this field

**Extension Charges** (Optional, defaults to 0)
- Enter any charges for this extension
- Bank may charge for extension
- Example: `1,000` for ₹1,000
- Can be 0 if no charges
- Will be recorded in extension history

**Remarks** (Optional but recommended)
- Add reason for extension
- Good for audit trail
- Examples:
  - "Project deadline extended by 3 months due to monsoon delays"
  - "Additional scope added to contract"
  - "Beneficiary requested extension for final performance review"
  - "Contract extended as per amendment dated 15-Jan-2025"
- Shows in extension history
- Can be multi-line

#### Step 4: Submit Extension

1. Review all entered details carefully
2. Verify new expiry date is correct
3. Click **"Extend"** button in dialog
4. System processes the extension
5. Success message appears
6. Dialog closes
7. Document reloads with updates

**Processing:**
- Usually instant (< 1 second)
- If delay, please wait
- Don't click multiple times

#### What Happens After Extension

**Automatic Updates to Main Document:**

✅ **Status Changes:**
- Old: "Active"
- New: "Extended" (blue badge)

✅ **Extension Expiry Date:**
- Updated with new expiry date you entered
- Example: `29-06-2026`

✅ **Days to Expiry:**
- Recalculated based on new expiry
- Example: If today is 01-Jan-2026 and new expiry is 29-06-2026, shows `179` days

✅ **Is Extended Checkbox:**
- Automatically checked
- Shows document has been extended

**New Row Added to Extension History:**

✅ **Extension Number:**
- Auto-assigned sequentially
- First extension: #1
- Second extension: #2
- And so on...

✅ **Previous Expiry Date:**
- Records what expiry was before this extension
- Example: `29-03-2026`

✅ **New Expiry Date:**
- The new expiry date you entered
- Example: `29-06-2026`

✅ **Extension Days:**
- Auto-calculated
- Formula: New Expiry Date - Previous Expiry Date
- Example: `92` days

✅ **Extension Date:**
- Date when extension was processed
- Auto-set to today
- Example: `15-01-2026`

✅ **Extension Charges:**
- The charges you entered
- Example: `1,000`
- Can be 0

✅ **Approved By:**
- Auto-set to current user
- Your user ID
- Example: `admin@company.com`

✅ **Remarks:**
- The remarks you entered
- Saved for audit trail

**Document Saved:**
- All changes saved automatically
- No need to click Save
- Document remains submitted

**Visual Confirmation:**
- Status badge changes to blue "Extended"
- Extension Details section shows "Is Extended" checked
- Extension History table has new row
- Days to Expiry updated

### Multiple Extensions

**Unlimited Extensions Allowed:**
- No system limit on number of extensions
- Can extend as many times as needed
- Each extension tracked separately
- Complete history maintained

**Example Scenario:**

**Original BG:**
- Issue Date: 08-Jan-2025
- Expiry Date: 29-Mar-2026

**First Extension (15-Mar-2026):**
- Previous Expiry: 29-Mar-2026
- New Expiry: 29-Jun-2026
- Extension Days: 92
- Charges: 1,000

**Second Extension (20-Jun-2026):**
- Previous Expiry: 29-Jun-2026
- New Expiry: 29-Sep-2026
- Extension Days: 92
- Charges: 1,200

**Third Extension (25-Sep-2026):**
- Previous Expiry: 29-Sep-2026
- New Expiry: 29-Dec-2026
- Extension Days: 91
- Charges: 1,500

**Result:**
- Extension History shows 3 rows
- Extensions numbered #1, #2, #3
- Total extension: 275 days (92+92+91)
- Total extension charges: 3,700 (1000+1200+1500)
- Current expiry: 29-Dec-2026
- Status: Extended

### Extension Best Practices

**Before Extending:**
1. ✅ Check with beneficiary (get approval)
2. ✅ Coordinate with bank (may need FD extension too)
3. ✅ Verify project timeline
4. ✅ Get necessary internal approvals
5. ✅ Document reason clearly

**During Extension:**
1. ✅ Enter correct new expiry date
2. ✅ Record accurate charges
3. ✅ Write clear remarks explaining why
4. ✅ Verify dates before submitting

**After Extension:**
1. ✅ Inform stakeholders (beneficiary, bank, project team)
2. ✅ Update physical BG document (if required by bank)
3. ✅ Extend FD if needed to cover new expiry
4. ✅ Update project documentation
5. ✅ Calendar reminder for new expiry date

**Documentation:**
- Keep extension approval emails
- Attach extension letters to Supporting Documents
- Maintain correspondence
- Record in project files

### Extension Financial Tracking

**Per Extension Charges:**
- Recorded individually in extension history
- Each extension has its own charge field
- Separate from main document charges
- Easy to track extension-specific costs

**Total Extension Cost:**
- Sum all charges from extension history rows
- Example: Ext#1: 1000 + Ext#2: 1200 + Ext#3: 1500 = Total 3,700
- Use for budgeting and cost analysis
- Can be exported to reports

**Overall BG Cost:**
- Main processing charges
- Main commission
- Plus: All extension charges
- Total cost of maintaining the BG

**Financial Reporting:**
- Extension costs can be analyzed separately
- Bank-wise extension charges
- Time-based extension analysis
- Budget variance reporting

---

## Claims and Closures

### Understanding Claims

**What is a Claim?**
- Beneficiary invokes the bank guarantee
- Bank pays the beneficiary
- Amount deducted from your FD
- Represents a loss/expense to your company

**When Claims Happen:**
- Contract breach or non-performance
- Failure to meet obligations
- Delays beyond acceptable limits
- Quality issues
- Other contractual defaults

**Types of Claims:**
- **Full Claim**: Entire BG amount claimed
- **Partial Claim**: Only part of BG claimed
- **Progressive Claims**: Multiple partial claims over time

### Marking a BG as Claimed

#### When to Mark as Claimed

**Mark as Claimed when:**
- ✅ Received claim letter/notice from beneficiary
- ✅ Bank has processed the claim
- ✅ Amount deducted from FD
- ✅ Claim is confirmed and final

**Don't Mark as Claimed if:**
- ❌ Only received claim threat/warning
- ❌ Claim is under dispute
- ❌ No formal claim letter received
- ❌ Bank hasn't confirmed

#### Claim Process - Step by Step

**Step 1: Verify Claim**
- Receive claim letter from beneficiary
- Verify with bank
- Get claim amount confirmation
- Check claim validity

**Step 2: Open BG Document**
1. Navigate to the claimed BG
2. Open in form view
3. Verify status is Active or Extended
4. Cannot claim if already Closed or Cancelled

**Step 3: Launch Claim Dialog**
1. Click **"Actions"** dropdown (top right)
2. Select **"Mark as Claimed"**
3. Claim dialog opens

**If "Mark as Claimed" Not Visible:**
- Status might be Closed/Cancelled
- BG might not be submitted
- Check permissions
- Refresh and try again

**Step 4: Enter Claim Details**

**Dialog Fields:**

**Claim Date** ⭐ (Required)
- Date when claim was made/processed
- Use date picker
- Defaults to today's date
- Change if claim was processed earlier
- Example: `15-01-2026`
- This is the official claim date

**Claim Amount** (Optional but recommended)
- Enter the amount that was claimed
- This will be added to "Utilized Amount"
- Example: `10,000` for partial claim
- Example: `53,010` for full claim
- Can be 0 if you only want to mark status
- Validates: Won't exceed Maturity Amount

**Remarks** (Optional but recommended)
- Reason for claim
- Reference to claim letter
- Dispute status if any
- Examples:
  - "Performance shortfall as per clause 5.2, Claim Letter Ref: CLM/2025/001"
  - "Delay in delivery beyond grace period"
  - "Quality issues - final inspection failed"
  - "Claim under dispute, legal action initiated"
- Important for records and future reference

**Step 5: Submit Claim**
1. Review all entered details
2. Verify claim amount is correct
3. Click **"Mark as Claimed"** button
4. System processes
5. Success message shows
6. Dialog closes
7. Document reloads

#### What Happens After Marking as Claimed

**Automatic Updates:**

✅ **Status Changes:**
- Old: Active/Extended
- New: Claimed (orange badge)
- Very visible indicator

✅ **Claim Date:**
- Set to date you entered
- Permanent record
- Cannot be cleared

✅ **Utilized Amount:**
- If claim amount entered: Utilized Amount increases by claim amount
- Example: Was 0, claimed 10,000 → Now 10,000
- If multiple claims: Amounts accumulate
- Validates: Cannot exceed Maturity Amount

✅ **Available Amount:**
- Auto-recalculates
- Formula: Maturity Amount - Utilized Amount
- Example: Maturity 58,583 - Utilized 10,000 = Available 48,583
- Shows remaining FD value

✅ **Document Saved:**
- All changes saved automatically
- No additional save needed
- Document remains submitted

**Restrictions After Claimed:**
- ❌ Cannot extend (extensions not allowed after claim)
- ❌ Cannot close (use Cancel if needed)
- ✅ Can amend if claim details wrong
- ✅ Can add more claim amount via amend
- ✅ Can cancel document if needed

**Financial Impact:**
- Expense/loss recorded
- FD reduced
- Available amount decreased
- May trigger accounting entries

### Partial vs Full Claims

**Partial Claim:**
- Only part of BG amount claimed
- Example: BG for 50,000, claimed 10,000
- Available amount still positive
- Remaining FD still locked
- Status: Claimed
- May have further claims later

**Full Claim:**
- Entire BG amount claimed
- Example: BG for 50,000, claimed 50,000
- Available amount = 0
- Entire FD utilized
- Status: Claimed
- No further claims possible

**Progressive Claims:**
- Multiple partial claims over time
- Each time: Amend document → Add to utilized amount
- Track each claim in version history
- Utilized amount accumulates
- Example:
  - Claim 1: 10,000 (Total utilized: 10,000)
  - Claim 2: 5,000 (Total utilized: 15,000)
  - Claim 3: 8,000 (Total utilized: 23,000)

### Normal Closure (No Claim)

#### When to Close Normally

**Close a BG when:**
- ✅ BG expired without claim
- ✅ Project completed successfully
- ✅ Contract fulfilled satisfactorily
- ✅ Beneficiary released the BG
- ✅ Performance period over
- ✅ FD can be released

**Perfect Scenario for Closure:**
- Project done well
- No claims made
- Beneficiary satisfied
- All obligations met
- BG no longer required

#### Closure Process

**Step 1: Verify Closure Eligibility**

**Must Meet:**
- ✅ BG is submitted
- ✅ Status is Active or Extended (NOT Claimed)
- ❌ Cannot close if Claimed
- ✅ Preferably expired or near expiry
- ✅ Have beneficiary's release (if required)

**Step 2: Open BG Document**
1. Navigate to BG
2. Open in form view
3. Verify status

**Step 3: Initiate Closure**
1. Click **"Actions"** dropdown
2. Select **"Close BG"**
3. Confirmation dialog appears

**If "Close BG" Not Visible:**
- Might be Claimed (cannot close claimed BGs)
- Check permissions
- Refresh page

**Step 4: Enter Closure Details**

**Closure Remarks Dialog:**
- Single text area for remarks
- Enter detailed closure reason
- Examples:
  - "Project completed successfully on 29-Mar-2026. BG expired without claim. FD released on 01-Apr-2026."
  - "Contract fulfilled as per terms. Beneficiary satisfied. Performance certificate received."
  - "Warranty period completed. No defects found. BG closure approved."
- These remarks will be appended to Internal Notes
- Important for audit and compliance

**Step 5: Confirm Closure**
1. Review your remarks
2. Click **"Close"** button in dialog
3. System processes closure
4. Success message appears
5. Dialog closes
6. Document reloads

#### What Happens After Closure

**Automatic Updates:**

✅ **Status Changes:**
- Old: Active/Extended
- New: Closed (gray badge)
- Clear visual indicator

✅ **Internal Notes Updated:**
- Your closure remarks appended
- Timestamp and user added automatically
- Example format:
  ```
  [2026-01-15 14:30 by admin@company.com]
  Project completed successfully...
  ```
- Permanent record maintained

✅ **Document Saved:**
- Changes saved automatically
- Document remains submitted

**What You Can Do After Closure:**
- ✅ View the document
- ✅ Print/export
- ✅ Reference in reports
- ❌ Cannot reopen
- ❌ Cannot extend
- ❌ Cannot claim
- ✅ Can cancel if truly necessary (rare)

**What to Do After Closure:**
1. Inform bank to release FD
2. Collect FD amount + interest
3. Update accounting records
4. File physical BG document
5. Update project closure documents
6. Archive electronically

### Cancelling a BG

#### When to Cancel

**Valid Reasons to Cancel:**
- BG created in error (wrong details)
- Contract cancelled before BG expiry
- BG replaced with new BG
- Beneficiary waived BG requirement
- Project terminated
- Duplicate entry
- Need to correct major errors (then create fresh)

**Invalid Reasons:**
- Simple errors (use Amend instead)
- Want to change dates (use Extend instead)
- Normal completion (use Close instead)

#### Cancellation Process

**Step 1: Open BG**
1. Navigate to BG document
2. Must be in submitted state
3. Can be any status (Active, Extended, Claimed, Closed)

**Step 2: Click Cancel**
1. Locate **"Cancel"** button in toolbar
2. Click Cancel
3. Cancellation dialog appears

**Step 3: Enter Cancellation Reason**
- Dialog asks for reason
- Enter detailed explanation
- Required field
- Examples:
  - "BG created with wrong beneficiary. Correct BG created as BG-2025-045"
  - "Contract cancelled before project start"
  - "Duplicate entry. Original BG is BG-2025-020"
- Reason saved in document

**Step 4: Confirm Cancellation**
1. Click "Yes" or "Confirm" button
2. System processes cancellation
3. Document updates

#### After Cancellation

**Changes:**
- ✅ Status → Cancelled (dark gray)
- ✅ Red "Cancelled" stamp appears
- ✅ Document is locked (cannot amend)
- ✅ Cancellation notification sent (if configured)
- ✅ Kept in system for audit trail
- ❌ Cannot be re-submitted
- ❌ Cannot be amended
- ✅ Can be viewed
- ✅ Shows in reports (if filtered to show cancelled)

**Next Steps:**
- Create correct BG if needed
- Inform stakeholders
- Release FD with bank (if applicable)
- Update records

### Amending a BG

#### When to Amend

**Use Amend for:**
- Correcting errors in submitted BG
- Updating information
- Changing beneficiary details
- Correcting amounts
- Updating dates (minor corrections)
- Fixing FD number
- Any edit to submitted document

**Don't Use Amend for:**
- Extensions (use Extend BG button)
- Claims (use Mark as Claimed)
- Closure (use Close BG)
- Cancellation (use Cancel)

#### Amendment Process

**Step 1: Open Original BG**
1. Navigate to BG to be amended
2. Document must be submitted
3. Cannot amend cancelled documents

**Step 2: Click Amend**
1. Locate **"Amend"** button in toolbar
2. Click Amend
3. System creates amendment

**What Happens:**
- New document created
- Same BG number with "-1" suffix
- Example: "BG-2025-001-1"
- Original document linked
- Status resets to Draft

**Step 3: Make Changes**
1. Edit required fields
2. All fields become editable
3. Update as needed
4. Examples:
  - Fix beneficiary name
  - Correct FD amount
  - Update bank details
  - Change commission rate

**Step 4: Document Changes**
- Add remarks explaining what was changed
- Important for audit trail
- Example: "Amended to correct beneficiary name from 'ABC Corp' to 'ABC Corporation Ltd'"

**Step 5: Submit Amendment**
1. Review all changes
2. Click **"Submit"** button
3. Amendment is now active

**After Amendment:**
- New version (BG-2025-001-1) is active
- Original (BG-2025-001) is superseded
- "Amended From" field links to original
- Original shows "Amended By" link to new version
- Complete version trail maintained

**Version Chain:**
- BG-2025-001 (Original - superseded)
- BG-2025-001-1 (First amendment - active)
- BG-2025-001-2 (Second amendment - if needed)
- And so on...

---

## Document Management

### Primary Documents

#### BG Document (Main Attachment)

**What is BG Document?**
- The official bank guarantee letter/certificate
- Issued by bank
- Legal document
- Required before submission

**What to Attach:**
- Original BG letter from bank (PDF preferred)
- Bank guarantee certificate
- Scanned copy if physical original
- Clear and readable
- All pages if multi-page

**File Formats Supported:**
- **PDF** (Recommended) - Best for official documents
- **Images**: JPG, JPEG, PNG
- **Word**: DOC, DOCX
- **Other**: Most common formats

**How to Attach:**
1. In BG form, scroll to "Documents & Attachments" section
2. Locate "BG Document" field
3. Click **"Attach"** button
4. File browser opens
5. Navigate to file location
6. Select BG document file
7. Click Open
8. File uploads (progress bar shows)
9. Upload completes
10. Filename displays in field
11. Click filename to open/view

**File Naming Best Practice:**
```
Format: [BG-Number]_BG-Original_[Date].pdf
Example: BG-2025-001_BG-Original_2025-01-08.pdf
```

**File Size:**
- Keep under 5 MB if possible
- Compress large scans
- Use PDF instead of images for better size

**Replacing Attached File:**
1. Click existing filename
2. Click Remove/Delete
3. Attach new file following steps above

#### FD Receipt

**What is FD Receipt?**
- Proof of fixed deposit
- FD certificate from bank
- Shows FD blocked for BG

**What to Attach:**
- FD receipt/certificate
- FD allocation letter
- Bank confirmation of FD
- FD maturity details

**Same process as BG Document:**
- Click "Attach" under "FD Receipt"
- Select file
- Upload

**Recommended but Not Mandatory:**
- Can submit BG without FD receipt
- But highly recommended for records

### Supporting Documents (Child Table)

#### Purpose of Supporting Documents

**Why Use Supporting Documents Table?**
- Attach multiple related documents
- Organize by document type
- Better than single attachment
- Easy to manage and track
- Each document separately categorized

**What to Attach Here:**
- BG application form
- Bank approval letters
- Extension letters and approvals
- Correspondence with beneficiary
- Renewal notices
- Project documents
- Contract references
- Claim letters (if any)
- Closure certificates
- Any other related documents

#### Adding Supporting Documents

**Step 1: Scroll to Supporting Documents**
- In form, find "Documents & Attachments" section
- Below primary attachments
- Child table titled "Supporting Documents"

**Step 2: Add New Row**
1. Click **"Add Row"** button (below table)
2. New blank row appears in table
3. Row is editable

**Step 3: Fill Row Details**

**Document Type** ⭐ (Required)
- Click dropdown in row
- Select appropriate type:
  - **BG Application**: Initial application to bank
  - **BG Approval Letter**: Bank's approval
  - **FD Certificate**: Additional FD documents
  - **Renewal Letter**: Extension/renewal letters
  - **Closure Letter**: BG closure/release letter
  - **Claim Letter**: Beneficiary's claim letter
  - **Other**: Anything else
- Choose most appropriate type

**Document Name** (Optional but recommended)
- Descriptive name for the document
- Click in field and type
- Examples:
  - "Extension Approval - March 2026"
  - "Beneficiary Acknowledgment Letter"
  - "Bank FD Certificate - Original"
  - "Project Completion Certificate"
- Helps in quick identification

**Document File (Attachment)** (Required)
1. In the row, find attachment column
2. Click **"Attach"** button
3. File browser opens
4. Select your file
5. Upload completes
6. Filename shows in cell
7. Click to view/download later

**Upload Date** (Auto-filled)
- Automatically set to today's date
- Can change if document dated earlier
- Click to use date picker
- Example: If letter dated 15-Jan-2026, set upload date to that

**Remarks** (Optional)
- Any notes about this document
- Click in field and type
- Examples:
  - "Original copy filed in cabinet A-23"
  - "Received via email from bank on 15-Jan-2026"
  - "Supersedes earlier approval dated 10-Jan-2026"
- Helpful context

**Step 4: Save Row**
- Click outside the row OR
- Click **"Update"** button (if editing existing BG) OR
- Will save when you save main document

**Step 5: Add More Documents**
- Repeat process for each document
- Click "Add Row" again
- Fill next row
- No limit on number of documents

#### Managing Supporting Documents

**Editing Existing Document Row:**
1. Click anywhere in the row
2. Fields become editable
3. Make changes
4. Click outside or Update to save

**Removing Document Row:**
1. Hover over row
2. X button appears on right
3. Click X to delete row
4. Confirm deletion
5. Row removed

**Replacing Attached File:**
1. Click on filename in row
2. Option to remove/delete
3. Remove old file
4. Click "Attach" again
5. Upload new file

**Viewing Document:**
1. Click on filename in table
2. Document opens in new tab/window
3. Can view, download, print

**Downloading Document:**
1. Click filename
2. File opens
3. Use browser's download option
4. Or right-click → Save As

### Example Supporting Documents Table

| Document Type | Document Name | Attachment | Upload Date | Remarks |
|--------------|---------------|------------|-------------|---------|
| BG Application | Initial BG Application | application.pdf | 05-01-2025 | Submitted to HDFC |
| BG Approval Letter | Bank Approval | approval.pdf | 07-01-2025 | Approved on 07-Jan |
| FD Certificate | FD Certificate Original | fd_cert.pdf | 08-01-2025 | FD No. 481513000628 |
| Renewal Letter | First Extension Approval | ext1.pdf | 15-03-2026 | 3 month extension |
| Closure Letter | Release Letter from Beneficiary | release.pdf | 30-03-2026 | Project completed |

### Document Attachment Best Practices

**File Naming Convention:**
```
Recommended Format:
[BG-Number]_[Document-Type]_[Date].extension

Examples:
BG-2025-001_Application_2025-01-05.pdf
BG-2025-001_Approval_2025-01-07.pdf
BG-2025-001_Extension-1_2025-03-15.pdf
BG-2025-001_Closure_2025-03-30.pdf
```

**Benefits:**
- Easy to identify which BG
- Chronological sorting
- Document type clear
- Professional organization
- Easy searching

**File Organization:**
- One document per attachment
- Don't combine multiple documents in one PDF (unless naturally together)
- If document has multiple pages, keep as one file
- Separate correspondence should be separate attachments

**Quality:**
- Use PDF for official documents (best quality, smallest size)
- Scan at 150-300 DPI (readable but not huge)
- Ensure text is readable
- Include all pages
- No handwritten scribbles if possible

**Security:**
- Sensitive documents: Check file permissions
- Password-protected PDFs: Note password in remarks
- Confidential info: Mark in Document Name or Remarks

**Maintenance:**
- Review documents quarterly
- Remove duplicates
- Update if replacements received
- Archive old versions if needed

---

## Reports and Analytics

### Active BG Management Report

#### Overview

**Purpose:**
- View all active and extended BGs
- Filter by various criteria
- Analyze BG exposure
- Monitor expiring BGs
- Export data for further analysis

**Access:** Reports → Addsol LC → Active BG Management

#### Accessing the Report

**Method 1: Through Reports Menu**
1. Click **"Reports"** in top navigation
2. Navigate to **"Addsol LC"** section
3. Click **"Active BG Management"**
4. Report opens

**Method 2: Through Awesomebar**
1. Press `Ctrl + K`
2. Type "Active BG Management"
3. Select from results
4. Report opens

**Method 3: Direct URL**
- Bookmark report URL for quick access

#### Understanding Report Layout

**Report Sections:**

**1. Filters (Top Section)**
- Multiple filter options
- Set criteria to narrow results
- Covered in detail below

**2. Report Table (Middle Section)**
- Tabular data display
- Multiple columns
- Sortable columns
- Clickable BG numbers

**3. Chart (Right Side or Below)**
- Visual representation
- Donut chart by default
- Shows status distribution

**4. Summary Cards (Top)**
- Key metrics at a glance
- Total counts and amounts
- Color-coded indicators

#### Report Columns

**Default Columns Displayed:**

1. **BG Number** (Link)
   - Clickable to open BG
   - Example: BG-2025-001

2. **Type**
   - BG type
   - Example: Performance Bank Guarantee

3. **Beneficiary**
   - Party name
   - Example: ABC Corporation

4. **Status**
   - Current status
   - Color-coded

5. **Issue Date**
   - When BG was issued
   - Format: DD-MM-YYYY

6. **Expiry Date**
   - Effective expiry (considers extension)
   - Format: DD-MM-YYYY

7. **Days to Expiry**
   - Remaining days
   - Negative if expired

8. **FD Amount**
   - Original FD amount
   - Currency formatted

9. **Maturity Amount**
   - FD maturity value
   - Currency formatted

10. **Utilized Amount**
    - Amount claimed/used
    - Currency formatted

11. **Available Amount**
    - Remaining available
    - Currency formatted

12. **Bank**
    - Issuing bank name
    - Example: HDFC Bank

13. **Project**
    - Linked project
    - Blank if no project

**Column Features:**
- Click header to sort
- Hover for full value (if truncated)
- Some columns are clickable links

#### Using Filters

**Available Filter Options:**

**1. Company**
- **Purpose**: Filter by your company
- **Type**: Dropdown
- **Default**: Your default company
- **Use Case**: Multi-company setups
- **Example**: Select "ABC Pvt Ltd"

**2. From Date**
- **Purpose**: Start of date range
- **Field**: Issue Date
- **Type**: Date picker
- **Example**: 01-01-2025
- **Use Case**: See BGs issued from this date onwards

**3. To Date**
- **Purpose**: End of date range
- **Field**: Issue Date
- **Type**: Date picker
- **Example**: 31-12-2025
- **Use Case**: See BGs issued up to this date

**4. Bank**
- **Purpose**: Filter by issuing bank
- **Type**: Dropdown (Link field)
- **Example**: HDFC Bank
- **Use Case**: Bank-wise BG analysis

**5. BG Type**
- **Purpose**: Filter by guarantee type
- **Type**: Dropdown
- **Options**: All BG types
- **Example**: Performance Bank Guarantee
- **Use Case**: Type-specific reports

**6. Status**
- **Purpose**: Filter by current status
- **Type**: Dropdown
- **Options**: Active, Extended, Expired, Claimed, Closed, Cancelled
- **Default**: Shows Active and Extended only
- **Use Case**: Focus on specific status
- **Tip**: Clear this to see all statuses

**7. Beneficiary**
- **Purpose**: Filter by party
- **Type**: Text field
- **Matching**: Contains (partial match works)
- **Example**: "ABC" finds "ABC Corp", "ABC Ltd"
- **Use Case**: Party-wise BG exposure

**8. Project**
- **Purpose**: Filter by project
- **Type**: Dropdown (Link field)
- **Example**: Metro Line 3
- **Use Case**: Project-wise BG tracking

**9. Expiring in Days** (Special Filter)
- **Purpose**: Find BGs expiring soon
- **Type**: Number input
- **Logic**: Shows BGs expiring within entered days
- **Example**: Enter `30` to see BGs expiring in next 30 days
- **Use Case**: Urgent action items, renewal planning
- **Very Useful**: Priority monitoring

#### How to Apply Filters

**Single Filter:**
1. Select/enter value in filter field
2. Click **"Refresh"** button OR
3. Press Enter
4. Report updates with filtered data

**Multiple Filters:**
1. Set first filter
2. Set second filter
3. Set third filter (and so on)
4. All filters apply together (AND logic)
5. Click "Refresh"
6. Report shows only records matching ALL filters

**Example Multi-Filter:**
- Bank = "HDFC Bank"
- Status = "Active"
- Expiring in Days = 30
- Result: Active HDFC BGs expiring in next 30 days

**Clearing Filters:**
1. Click **"Clear Filters"** button
2. All filter values reset
3. Report shows all data (based on default status filter)

**Refreshing Data:**
- Click "Refresh" anytime to reload
- Use if data changed since report opened
- Reapplies current filters

#### Understanding the Chart

**Chart Type: Donut Chart**

**What it Shows:**
- Distribution of BGs by Status
- Pie segments for each status
- Color-coded
- Percentage and count

**Chart Elements:**

**Segments (Colored Sections):**
- Green: Active BGs
- Blue: Extended BGs
- Orange: Expired BGs
- Red: Claimed BGs
- Gray: Closed BGs

**Legend:**
- Right side or below chart
- Lists each status with color
- Click to toggle visibility

**Hover Interaction:**
- Hover over segment
- Tooltip shows:
  - Status name
  - Count
  - Percentage

**Example Chart Data:**
```
Active: 15 BGs (50%)
Extended: 8 BGs (27%)
Expired: 5 BGs (17%)
Claimed: 2 BGs (6%)
```

**No Chart?**
- If no data matches filters, no chart shown
- Adjust filters to see data

#### Report Summary (Key Metrics)

**Summary Cards at Top:**

**1. Total BGs**
- **What**: Count of BGs in current filter
- **Color**: Green indicator
- **Example**: 30
- **Use**: Know how many BGs you're looking at

**2. Total FD Amount**
- **What**: Sum of all FD amounts
- **Color**: Blue indicator
- **Format**: Currency
- **Example**: ₹15,30,000
- **Use**: Total FD exposure

**3. Total Maturity Amount**
- **What**: Sum of all maturity amounts
- **Color**: Blue indicator
- **Format**: Currency
- **Example**: ₹16,85,000
- **Use**: Expected total maturity value

**4. Total Utilized**
- **What**: Sum of utilized amounts
- **Color**: Orange indicator
- **Format**: Currency
- **Example**: ₹2,50,000
- **Use**: How much has been claimed/used

**5. Total Available**
- **What**: Sum of available amounts
- **Color**: Green indicator
- **Format**: Currency
- **Example**: ₹14,35,000
- **Use**: How much is still available

**6. Expiring in 30 Days**
- **What**: Count of BGs expiring within 30 days
- **Color**: Red if > 0, Green if 0
- **Example**: 5
- **Use**: Urgent attention needed
- **Action**: Click to filter (if implemented)

**Summary Updates:**
- Recalculates with each filter change
- Based on visible/filtered data only
- Instant updates

#### Sorting and Organizing

**Column Sorting:**
1. Click any column header
2. Data sorts ascending (A-Z, 0-9, Old-New)
3. Click again for descending (Z-A, 9-0, New-Old)
4. Arrow indicates sort direction (↑↓)

**Common Sorts:**
- Expiry Date (earliest first) - See expiring soon
- Days to Expiry (lowest first) - Urgent items
- FD Amount (highest first) - High-value BGs
- Status (alphabetical) - Group by status

**Multi-Column Sort:**
- Sort by Status first
- Then Shift+Click Expiry Date
- Groups by status, sorted by expiry within each

#### Exporting Report Data

**Export to Excel:**
1. Click **"Export"** or **"Menu"** button (top right of report)
2. Select **"Export"** → **"Excel"**
3. Excel file downloads
4. Open in Excel, Google Sheets, etc.
5. All visible columns exported
6. Filtered data only (not all BGs)

**Export to PDF:**
1. Click "Export" → "PDF"
2. PDF generates with current view
3. Includes chart
4. Download or print

**Export to CSV:**
1. Click "Export" → "CSV"
2. Comma-separated values file
3. Import into other systems
4. Use for data analysis tools

**Print:**
1. Click "Print" button or icon
2. Print preview opens
3. Select printer or save as PDF
4. Includes report data and chart

**What Gets Exported:**
- Current filtered data only
- All visible columns
- Summary metrics
- Chart (PDF only)
- Date range and filter info (PDF)

#### Report Use Cases

**Weekly BG Review:**
1. Filter: Expiring in Days = 30
2. Sort: Days to Expiry (ascending)
3. Export to Excel
4. Identify renewals needed
5. Plan extensions

**Monthly Financial Reporting:**
1. Filter: From Date = 01-Feb-2026, To Date = 28-Feb-2026
2. View Summary: Total FD Amount
3. Export to Excel
4. Include in financial report

**Bank-Wise Analysis:**
1. Filter: Bank = "HDFC Bank"
2. View Summary Totals
3. Repeat for each bank
4. Compare bank exposure

**Project Tracking:**
1. Filter: Project = "Metro Line 3"
2. See all project BGs
3. Monitor project BG exposure
4. Track expirations

**Audit Preparation:**
1. Clear all filters (show all)
2. Export complete data
3. Provide to auditors
4. Include chart for visualization

**Claimed BGs Analysis:**
1. Filter: Status = "Claimed"
2. Review all claimed BGs
3. Calculate total loss
4. Analyze claim patterns

### Creating Custom Reports

While detailed custom report creation requires technical knowledge, here's an overview:

#### Using Report Builder (Simple)

**For Non-Programmers:**

1. **Access Report Builder**
   - Go to: Setup → Report Builder
   - Click "New Report"

2. **Basic Configuration**
   - Report Name: "My BG Report"
   - Reference DocType: "BG Management"
   - Report Type: "Report Builder"

3. **Add Columns**
   - Click "Add Column"
   - Select fields to display
   - Arrange order
   - Set column widths

4. **Add Filters**
   - Standard filters
   - User can change at runtime

5. **Save and Use**
   - Save report
   - Run anytime
   - Share with team

**Example Simple Reports:**
- BGs by Status
- High Value BGs (FD Amount > 100000)
- BGs Expiring This Month
- Project-wise BG Summary

#### Script Reports (Advanced - Requires Programming)

For custom calculations, complex logic, charts - requires Python knowledge. Contact your system administrator.

---

## Notifications and Alerts

### Automatic Email Notifications

#### Expiry Alerts

**How It Works:**
- Daily scheduler runs in background
- Checks all active/extended BGs
- Identifies BGs approaching expiry
- Sends email alerts at specific thresholds

**Notification Thresholds:**
- **30 days before expiry**: First warning
- **15 days before expiry**: Second warning
- **7 days before expiry**: Urgent warning
- **3 days before expiry**: Critical warning
- **1 day before expiry**: Final warning

**Who Receives Alerts:**
- All users with "Accounts Manager" role
- Configured in system automatically
- No manual subscription needed

**Email Content Includes:**
- Subject: "BG Management [BG-Number] expiring in X days"
- BG Number (clickable link)
- BG Type
- Beneficiary name
- Expiry Date (or Extension Expiry if extended)
- Days Remaining
- FD Amount
- Call to action

**Email Timing:**
- Daily scheduler runs (usually early morning)
- Checks at configured time
- Emails sent immediately when threshold matched
- One email per BG per threshold

**Example Email:**
```
Subject: BG Management BG-2025-001 expiring in 7 days

Dear Team,

This is to inform you that the following Bank Guarantee is expiring soon:

BG Number: BG-2025-001
Type: Performance Bank Guarantee
Beneficiary: ABC Corporation
Expiry Date: 29-Mar-2026
Days Remaining: 7
FD Amount: ₹53,010.00

Please take necessary action.

View BG: [Link to BG document]

Regards,
ERPNext System
```

**No Spam:**
- Each threshold triggers only once
- Won't send multiple emails for same threshold
- Example: At 7 days, you get one email, not daily emails

#### Submission Notifications

**When Sent:**
- Immediately after BG is submitted
- Real-time notification

**Who Receives:**
- Users with Accounts Manager role
- Can be customized

**Email Content:**
- New BG submitted notification
- BG Number and key details
- Link to view document
- Submitted by user info

**Purpose:**
- Inform team of new BG
- Immediate awareness
- Team coordination

#### Cancellation Notifications

**When Sent:**
- When BG is cancelled

**Who Receives:**
- Accounts Managers
- Document owner

**Email Content:**
- BG has been cancelled
- Cancellation reason
- Cancelled by user
- Link to document

### In-App Notifications

#### Dashboard Alerts (On BG Form)

**Visible Directly on Document:**

**Red Alert Banner:**
- **"This Bank Guarantee has expired"**
- Shows when expiry date has passed
- Very prominent red background
- Cannot be missed

**Red Alert Comment:**
- **"This Bank Guarantee is expiring in X days"**
- Shows when 7 days or less remaining
- Red color
- Above form

**Orange Alert Comment:**
- **"This Bank Guarantee is expiring in X days"**
- Shows when 8-15 days remaining
- Orange/amber color

**Yellow Alert Comment:**
- **"This Bank Guarantee is expiring in X days"**
- Shows when 16-30 days remaining
- Yellow color

**No Alert:**
- When more than 30 days remaining
- Or already closed/claimed

**Benefits:**
- Immediate visual feedback
- See status at a glance
- No need to check dates manually

#### Status Indicators

**Page Indicator (Top Right):**
- Large colored badge
- Shows current status
- Color-coded for quick recognition

**Status Colors:**
- 🟢 **Green - Active**: All good, BG is valid
- 🔵 **Blue - Extended**: Has been extended
- 🔴 **Red - Expired**: Past expiry date
- 🟠 **Orange - Claimed**: Has been claimed
- ⚪ **Gray - Closed**: Normally closed
- ⚫ **Dark Gray - Cancelled**: Cancelled

**Always Visible:**
- Top right corner of form
- Visible while scrolling
- Instant status check

### Configuring Notifications

#### Checking Email Configuration

**Prerequisites for Emails to Work:**
1. Email account configured in ERPNext
2. SMTP settings correct
3. Test email successful
4. Scheduler enabled

**Verify Email Setup:**
1. Go to: **Setup** → **Email** → **Email Account**
2. Check your email account
3. Verify fields:
   - Email ID
   - SMTP Server
   - Port (usually 587 or 465)
   - Use TLS/SSL
   - Login/Password
4. Scroll down
5. Click **"Send Test Email"**
6. Enter your email
7. Click Send
8. Check if you receive test email

**If Test Fails:**
- Check SMTP credentials
- Verify network/firewall
- Check spam folder
- Contact IT support

#### Ensuring Scheduler is Enabled

**Check Scheduler Status:**
```bash
# SSH/Terminal access needed
cd ~/frappe-bench
bench doctor
```

**Look for Line:**
```
Scheduler: Enabled  ✓
```

**If Shows Disabled:**
```bash
bench --site your-site.local enable-scheduler
```

**Verify:**
```bash
bench doctor
```

Should now show "Enabled"

**What Scheduler Does:**
- Runs background jobs
- Checks BG expiries daily
- Sends notification emails
- Other automated tasks

**If Scheduler Not Running:**
- Notifications won't be sent
- Must be enabled
- Contact system administrator

#### Customizing Notification Days

**Current Thresholds:**
- 30, 15, 7, 3, 1 days

**To Change (Requires Code Access):**
1. Access server/code
2. Edit file: `bg_management.py`
3. Find function: `send_expiry_notifications()`
4. Find line: `notification_days = [30, 15, 7, 3, 1]`
5. Modify array:
   - Example: `[60, 30, 7]` for 60, 30, 7 days only
   - Example: `[45, 30, 15, 7, 3, 1, 0]` for more alerts
6. Save file
7. Run: `bench --site your-site.local migrate`
8. Restart: `bench restart`

**Note:** Requires technical knowledge. Ask system administrator.

#### Adding More Recipients

**Default:** Accounts Manager role receives all emails

**Option 1: Add Users to Role**
1. Go to: **Setup** → **Users** → select user
2. Add role: "Accounts Manager"
3. Save
4. User now receives notifications

**Option 2: Customize Code (Advanced)**
- Modify `get_notification_recipients()` function
- Add specific email addresses
- Or add different roles
- Requires programming knowledge

### Managing Notification Overload

**If Receiving Too Many Emails:**

**Solution 1: Adjust Thresholds**
- Reduce number of notification days
- Example: Only 15 and 3 days (instead of 30, 15, 7, 3, 1)
- Fewer emails, still enough warning

**Solution 2: Email Filtering**
- Set up email filter/rule
- Move BG notifications to specific folder
- Review folder daily/weekly
- Keeps inbox clean

**Solution 3: Digest Emails (Future Enhancement)**
- Compile all notifications into one daily email
- Requires customization
- Contact administrator

**Solution 4: Role-Based Distribution**
- Create specific roles for different BG types
- Example: "BG Manager - HDFC", "BG Manager - SBI"
- Distribute responsibility
- Each person gets fewer emails

**Solution 5: Dashboard/Report Review**
- Disable/reduce email notifications
- Instead, check "Active BG Management" report daily
- Filter: Expiring in Days = 30
- More control, less email

---

## Advanced Features

### Linking to Other DocTypes

#### Project Linking

**Benefits of Project Link:**
- Track project-wise BG exposure
- See all BGs for a project
- Financial planning per project
- Project closure verification

**How to Link:**
1. In BG form, find "Project" field
2. Click dropdown
3. Select project from list
4. Save

**Viewing Project BGs:**
- Open Project document
- View connections/links
- See all linked BGs
- Or use BG report filtered by project

**Use Cases:**
- Infrastructure projects with multiple BGs
- Client projects requiring performance guarantees
- Long-term contracts
- Multi-phase projects

#### Purchase Order Linking

**For Supplier BGs:**
When BG is issued in favor of supplier (reverse BG):

1. Set Beneficiary Type: Supplier
2. Select Supplier
3. Link to Purchase Order
4. Track PO-wise guarantee obligations

**Benefits:**
- PO-specific tracking
- Procurement compliance
- Supplier relationship management
- Audit trail

#### Sales Order Linking

**For Customer BGs:**
When customer gives you BG (received BG):

1. Set Beneficiary Type: Customer
2. Select Customer
3. Link to Sales Order
4. Track sales order guarantees

**Benefits:**
- Order fulfillment tracking
- Revenue assurance
- Customer credit management

#### Multiple Links

**Can Link:**
- Project + PO (project procurement)
- Project + SO (project sales)
- Any combination as needed

**Cannot Link:**
- Both PO and SO on same BG (choose one)
- One BG → one of each type

### Integration with Accounting

#### Commission Accounting (Manual)

**Creating Journal Entry for Commission:**

1. Open BG with commission
2. Click "Create" dropdown (if available)
3. Select "Journal Entry"
4. Or create JE manually:

**Manual JE Steps:**
1. Go to: Accounting → Journal Entry → New
2. Entry Type: Journal Entry
3. Add Row 1:
   - Account: Commission Expense
   - Debit: Commission Amount
4. Add Row 2:
   - Account: Bank Account
   - Credit: Commission Amount
5. Reference: BG Number in remarks
6. Save and Submit

**Accounts to Use:**
- **Debit**: Commission Expense (P&L account)
- **Credit**: Bank Account (Asset account)

#### FD Accounting

**When FD is Blocked:**

**Journal Entry:**
1. Entry Type: Journal Entry
2. Row 1:
   - Account: Fixed Deposit (Asset)
   - Debit: FD Amount
3. Row 2:
   - Account: Bank Current Account
   - Credit: FD Amount
4. Remarks: "FD blocked for BG-2025-001"
5. Submit

**On FD Maturity:**

**Journal Entry:**
1. Row 1:
   - Account: Bank Account
   - Debit: Maturity Amount
2. Row 2:
   - Account: Fixed Deposit
   - Credit: FD Amount
3. Row 3:
   - Account: Interest Income
   - Credit: (Maturity Amount - FD Amount)
4. Submit

**On Claim:**

**Journal Entry:**
1. Row 1:
   - Account: BG Claim Expense/Loss
   - Debit: Claim Amount
2. Row 2:
   - Account: Fixed Deposit
   - Credit: Claim Amount
3. Remarks: "Claim against BG-2025-001"
4. Submit

**Note:** Accounting integration can be customized for auto-JE creation. Contact administrator.

### Bulk Operations

#### Bulk Update Fields

**Updating Multiple BGs at Once:**

**Use Case:** Change project for 10 BGs

**Steps:**
1. Go to BG Management list view
2. Use filters to get desired BGs
3. Select BGs:
   - Click checkbox for each BG, or
   - Click top checkbox to select all visible
4. Click "Actions" dropdown (above list)
5. Select "Update"
6. Dialog opens
7. Select field to update (e.g., "Project")
8. Enter new value
9. Click "Update"
10. All selected BGs updated

**Supported for:**
- Dropdown fields
- Link fields
- Some data fields

**Not Supported for:**
- Amounts (for safety)
- Dates (for safety)
- Status (system managed)

**Be Careful:**
- Cannot undo bulk update easily
- Verify selection before updating
- Consider backing up first

#### Bulk Export

**Exporting Many BGs:**

**Method 1: From List**
1. Apply filters to get desired BGs
2. Click "Menu" → "Export"
3. Select format (Excel/CSV)
4. All filtered BGs export
5. Download file

**Method 2: From Report**
1. Run "Active BG Management" report
2. Apply filters
3. Click "Export"
4. Choose format
5. Download

**Uses:**
- Year-end reporting
- Audit preparation
- Data analysis
- Backup
- Migration

### Custom Fields (Admin)

**What are Custom Fields?**
- Additional fields added to standard BG Management form
- Without modifying core code
- Preserved during updates

**When to Add Custom Fields:**
- Company-specific requirements
- Additional tracking needed
- Integration requirements
- Extra categorization

**How to Add (Admin only):**
1. Go to: **Setup** → **Customize** → **Customize Form**
2. Enter DocType: "BG Management"
3. Click "Customize"
4. Scroll to "Fields" section
5. Click "Add Row"
6. Configure field:
   - Label: Field name to display
   - Field Type: Data, Link, Select, etc.
   - Options: For dropdowns
   - Insert After: Where to place field
7. Set properties:
   - Mandatory
   - Read Only
   - In List View
   - etc.
8. Click "Update"
9. Field added to form

**Example Custom Fields:**
- Internal Reference Number
- Department
- Cost Center
- Insurance Policy Number
- Guarantor Name
- Approval Authority
- Risk Rating

**Note:** Added fields persist even after app updates.

### Workflows (Admin)

**What are Workflows?**
- Define approval process
- Multiple states and transitions
- Role-based approvals
- Automated routing

**When to Use:**
- Multi-level approvals needed
- Compliance requirements
- Segregation of duties
- Controlled access

**Basic Workflow Example:**

**States:**
1. Draft (creator)
2. Pending Approval (approver)
3. Approved (final)

**Transitions:**
- Draft → Pending (Submit for Approval)
- Pending → Approved (Approve)
- Pending → Draft (Reject)

**Roles:**
- Accounts User: Can create, submit for approval
- Accounts Manager: Can approve/reject

**Setting Up (Admin):**
1. Create Workflow States
2. Create Workflow
3. Add Transitions
4. Assign Roles
5. Apply to BG Management DocType

**Using Workflow:**
- User creates BG (Draft state)
- User clicks "Submit for Approval" (→ Pending)
- Manager receives notification
- Manager reviews and approves/rejects
- On approval, BG moves to Approved state
- System submits document

**Benefits:**
- Controlled submission
- Audit trail of approvals
- Compliance
- Risk management

---

## Best Practices

### Data Entry Best Practices

#### BG Numbering Conventions

**Recommended Formats:**

**Format 1: Sequential**
```
BG-[YEAR]-[SEQUENCE]

Examples:
BG-2025-001
BG-2025-002
BG-2026-001
```

**Format 2: Bank-Based**
```
BG/[BANK-CODE]/[YEAR]/[SEQUENCE]

Examples:
BG/HDFC/2025/001
BG/SBI/2025/001
```

**Format 3: Project-Based**
```
BG-[PROJECT-CODE]-[SEQUENCE]

Examples:
BG-METRO-001
BG-HIGHWAY-001
```

**Benefits of Good Numbering:**
- Easy identification
- Chronological sorting
- Quick reference
- Professional appearance
- Audit-friendly

**Avoid:**
- Special characters (except - and /)
- Spaces
- Very long numbers
- Confusing formats

#### Document Naming Standards

**For Attached Files:**
```
Format: [BG-Number]_[Doc-Type]_[Date].extension

Examples:
BG-2025-001_Original_2025-01-15.pdf
BG-2025-001_FD-Receipt_2025-01-15.pdf
BG-2025-001_Extension-1_2025-04-20.pdf
```

**Benefits:**
- Easy to find
- Clear identification
- Professional
- Sortable

#### Consistent Master Data

**Beneficiary Names:**
- Always select from master (don't type manually)
- Use standard party name
- Avoid abbreviations if full name available
- Example: Use "ABC Corporation Limited" not "ABC Corp"

**Bank Names:**
- Use bank master
- Don't create duplicate banks
- Standard naming: "HDFC Bank", "State Bank of India"
- Include branch if multiple branches

**Date Entry:**
- Use date picker (click calendar icon)
- Format handled automatically
- Double-check dates before saving
- Verify expiry > issue date

### Maintenance Best Practices

#### Regular Reviews

**Weekly Tasks:**
1. **Monday Morning:**
   - Run "Active BG Management" report
   - Filter: Expiring in Days = 30
   - Review list
   - Identify action items

2. **Check Notifications:**
   - Review expiry alert emails
   - Plan extensions if needed
   - Contact banks for renewals

3. **Update Status:**
   - Mark any claimed BGs
   - Close completed BGs
   - Update utilized amounts

**Monthly Tasks:**
1. **First Week:**
   - Run full BG report (all statuses)
   - Export to Excel
   - Reconcile with bank statements

2. **FD Reconciliation:**
   - Match FD amounts with bank records
   - Verify interest calculations
   - Check FD maturity dates

3. **Document Check:**
   - Ensure all BGs have documents attached
   - Upload missing documents
   - Organize physical files

4. **Review Claimed BGs:**
   - List all claimed BGs
   - Calculate total losses
   - Analyze claim reasons
   - Identify patterns

**Quarterly Tasks:**
1. **Comprehensive Audit:**
   - Review all active BGs
   - Verify beneficiary details still correct
   - Check project status alignment
   - Ensure extensions are valid

2. **Archive Old BGs:**
   - Closed BGs > 2 years old
   - Export data
   - Maintain for compliance period
   - Clear from active list (if allowed)

3. **Training:**
   - Train new team members
   - Refresh existing users
   - Update procedures
   - Share best practices

**Annual Tasks:**
1. **Year-End Reporting:**
   - Export all BG data
   - Include in annual report
   - Financial statements
   - Audit preparation

2. **Process Review:**
   - Review BG management process
   - Identify improvements
   - Update procedures
   - System enhancements

#### Backup Strategy

**Automatic Backups:**
- ERPNext does daily backups automatically
- Includes all BG data
- Includes all attachments
- Verify backups are running

**Check Backup Status:**
```bash
# Terminal/SSH access
cd ~/frappe-bench
bench --site your-site.local backup
```

**Manual Backups:**

**Before Major Changes:**
- Before bulk updates
- Before system upgrades
- Before customizations
- Monthly manual backup

**How to Backup:**
1. Go to: **Settings** → **System Settings**
2. Click "Download Backup"
3. Select "With Files" (includes attachments)
4. Download
5. Store securely offsite

**What to Backup:**
- Database (includes all BG data)
- Files (includes all attachments)
- Custom configurations

**Backup Storage:**
- Keep multiple versions
- Store offsite (cloud/different location)
- Test restore periodically
- Minimum 3 months retention

#### Data Cleanup

**Quarterly Cleanup:**

1. **Remove Draft BGs:**
   - Old draft BGs (> 6 months)
   - Created by mistake
   - No longer needed
   - Delete carefully

2. **Check Duplicate Documents:**
   - Multiple attachments of same file
   - Remove older versions
   - Keep latest only

3. **Archive Closed BGs:**
   - Export closed BGs data
   - Keep for compliance
   - Mark as archived (if feature available)

4. **Review Cancelled BGs:**
   - Understand why cancelled
   - Learn from mistakes
   - Keep for audit trail

**Don't Delete:**
- Submitted documents (keep for audit)
- Claimed BGs (legal/compliance)
- Any BG less than 3 years old
- Active or Extended BGs

### Security Best Practices

#### Access Control

**Role Assignment:**

**Principle of Least Privilege:**
- Give minimum access needed
- Don't make everyone Accounts Manager
- Use Accounts User for operators
- Reserve Manager for approvers

**Quarterly Review:**
- Review all user permissions
- Remove access for transferred employees
- Update roles based on current responsibilities
- Document access levels

**Sensitive Information:**

**Internal Notes Field:**
- Use for confidential info
- Bank contact details
- Sensitive remarks
- Not visible in prints (if configured correctly)

**Document Attachments:**
- Check file permissions
- Password-protect sensitive PDFs
- Note passwords in Internal Notes
- Don't share unnecessarily

#### Audit Trail Maintenance

**Version History:**
- System automatically maintains
- Review for important BGs
- Use in case of disputes
- Compliance documentation

**Extension History:**
- Never delete rows
- Complete audit trail
- Shows all approvals
- Compliance proof

**Regular Audit Reviews:**

**Monthly:**
- Review changes to high-value BGs
- Check who approved extensions
- Verify claim entries
- Look for anomalies

**Quarterly:**
- Comprehensive audit
- Cross-check with bank records
- Verify all approvals proper
- Document findings

### Financial Best Practices

#### FD Tracking and Reconciliation

**Monthly Reconciliation:**

**Steps:**
1. **Export BG Data:**
   - Run Active BG Management report
   - Export to Excel
   - Get total FD amounts

2. **Get Bank Statement:**
   - FD statement from bank
   - List all FDs
   - Check blocked status

3. **Match:**
   - Match FD numbers
   - Match FD amounts
   - Match maturity amounts
   - Identify discrepancies

4. **Investigate Differences:**
   - Missing FDs in system
   - Extra FDs in bank (not in system)
   - Amount mismatches
   - Resolve and update

**FD Maturity Tracking:**

**Create Reminder System:**
1. **Calendar Entries:**
   - Add FD maturity dates to calendar
   - Set reminders 30 days before
   - Plan renewals

2. **Report:**
   - Filter: FD Maturity Date <= 30 days from now
   - Review monthly
   - Action on maturities

**Interest Calculation:**

**Track Expected Interest:**
- Maturity Amount - FD Amount = Interest
- Compare with bank's interest
- Verify calculations
- Account for TDS if applicable

**FD Renewal:**
- When BG extended, extend FD too
- Ensure FD maturity >= BG expiry
- Update FD details in BG
- Upload new FD receipt

#### Charge Management

**Recording All Charges:**

**Types of Charges:**
1. **Initial Charges:**
   - Commission (in main form)
   - Processing fees (in main form)

2. **Extension Charges:**
   - Record in Extension History
   - Each extension separately

3. **Other Charges:**
   - Add as custom field if frequent
   - Or document in remarks

**Financial Reporting:**

**Monthly Charge Summary:**
1. Export all BGs
2. Sum commission amounts
3. Sum processing charges
4. Sum extension charges
5. Calculate total BG cost
6. Compare to budget
7. Variance analysis

**Bank-Wise Analysis:**
1. Group BGs by bank
2. Calculate charges per bank
3. Negotiate better rates
4. Optimize bank relationships

**Budget vs Actual:**
- Set annual BG budget
- Track monthly spend
- Forecast year-end
- Report variances

### Communication Best Practices

#### Stakeholder Communication

**Regular Updates:**

**To Beneficiaries:**
- Inform of extensions (share extension letter)
- Confirm BG details at start
- Update contact details if changed
- Professional communication

**To Banks:**
- Coordinate FD renewals
- Inform of BG cancellations
- Update contact persons
- Maintain good relationship

**To Project Managers:**
- Share BG status for their projects
- Alert of upcoming expiries
- Coordinate extensions with project timeline
- Include in project reports

**To Finance Team:**
- Monthly BG report
- Total exposure updates
- Claim notifications
- Budget variance reports

**Documentation:**

**Keep Email Trail:**
- Save important correspondence
- Attach to Supporting Documents
- Reference in remarks
- Easy retrieval

**File Physical Documents:**
- Original BG letters
- FD certificates
- Correspondence
- Organized filing system

#### Internal Team Communication

**Regular Meetings:**

**Weekly BG Review:**
- 15-minute standup
- Review expiring BGs
- Assign action items
- Follow-up on previous items

**Monthly Review:**
- Detailed BG report
- Financial impact
- Lessons learned (claims)
- Process improvements

**Meeting Agenda:**
1. BGs expiring in next 30 days
2. Extension status
3. Claims (if any)
4. New BGs submitted
5. Action items from last meeting
6. Any other business

**Knowledge Sharing:**

**Document Procedures:**
- Standard operating procedures (SOPs)
- Flowcharts
- Templates
- Training materials

**Training:**
- New employees
- System updates
- Best practices
- Quarterly refreshers

**Lessons Learned:**
- Document claims and reasons
- Process failures
- Improvements made
- Share with team

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Cannot Save BG

**Symptoms:**
- Save button grayed out or does nothing
- Error message appears
- Changes not saving

**Possible Causes & Solutions:**

**1. Required Fields Missing:**
- **Solution**: Look for fields marked with red asterisk (⭐)
- Fill all required fields
- Red asterisk disappears when filled
- Try saving again

**2. Validation Errors:**
- **Error**: "Expiry Date must be after Issue Date"
  - **Solution**: Make expiry date later than issue date
- **Error**: "FD Maturity Date should be on or after BG Expiry Date"
  - **Solution**: FD maturity must be >= BG expiry
- **Error**: "Utilized Amount cannot exceed Maturity Amount"
  - **Solution**: Reduce utilized amount or increase maturity amount

**3. Unique Constraint:**
- **Error**: "BG Number already exists"
  - **Solution**: Choose a different, unique BG number
  - Check if BG already created
  - Don't duplicate numbers

**4. Permission Issues:**
- **Solution**: Check you have "Write" permission
- Contact administrator
- Login with correct account

**5. Network/Connection:**
- **Solution**: Check internet connection
- Refresh page (F5)
- Try again

**Still Not Working?**
- Check Error Log: **Tools** → **Error Log**
- Contact system administrator
- Provide error message details

#### Issue 2: Cannot Submit BG

**Symptoms:**
- Submit button disabled
- Validation error on submit
- Submit fails

**Possible Causes & Solutions:**

**1. BG Document Not Attached:**
- **Error**: "Please attach BG Document before submission"
- **Solution**: Scroll to Documents section
- Attach BG document
- Try submitting again

**2. FD Number Missing:**
- **Error**: "FD Number is mandatory before submission"
- **Solution**: Enter FD number in Financial Details
- Save and submit

**3. Validation Errors:**
- Same as save issues above
- Fix validation errors
- Try submitting

**4. Permission:**
- **Error**: "You don't have permission to Submit"
- **Solution**: Check you have "Submit" permission
- Contact administrator
- You may only have "Write" permission

**5. Document in Wrong State:**
- Already submitted: Shows "Submitted" in status bar
- Already cancelled: Cannot resubmit
- **Solution**: Check document state

#### Issue 3: Extension Not Working

**Symptoms:**
- "Extend BG" button not visible
- Extension fails with error
- Extension button grayed out

**Possible Causes & Solutions:**

**1. Document Not Submitted:**
- **Solution**: Submit the BG first
- Extensions only work on submitted BGs
- Save → Submit → Then Extend

**2. Wrong Status:**
- **Error**: BG is Claimed, Closed, or Cancelled
- **Solution**: Cannot extend these statuses
- Only Active/Extended can be extended
- If mistakenly closed, amend document

**3. New Date Not After Current:**
- **Error**: "New Expiry Date must be after current expiry date"
- **Solution**: Enter date that's later than current expiry
- Check if extended (uses extension expiry, not original)

**4. Permission Issues:**
- **Solution**: Check you have permission to extend
- May need Accounts Manager role
- Contact administrator

**5. Page Not Refreshed:**
- **Solution**: Refresh page (F5)
- Reopen document
- Try again

#### Issue 4: Reports Not Loading

**Symptoms:**
- Blank report screen
- Error message in report
- Report takes too long
- "No data" message

**Possible Causes & Solutions:**

**1. Filters Too Restrictive:**
- **Solution**: Clear all filters
- Click "Clear Filters"
- Refresh report
- Gradually add filters back

**2. No Data Exists:**
- **Message**: "No data to show"
- **Solution**: Create some BG records first
- Or adjust filters to match existing data

**3. Permission Issues:**
- **Solution**: Check you have "Read" permission for BG Management
- Contact administrator

**4. Browser Cache:**
- **Solution**: Clear browser cache
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Try different browser

**5. System Issue:**
- **Command Line Fix** (Admin):
```bash
bench --site your-site.local clear-cache
bench build --app addsol_lc
```

#### Issue 5: Notifications Not Received

**Symptoms:**
- No expiry alert emails
- Submission notifications missing
- Expected emails not arriving

**Possible Causes & Solutions:**

**1. Email Configuration:**
- **Check**: Setup → Email → Email Account
- Verify SMTP settings correct
- Test email: Click "Send Test Email"
- If test fails, fix SMTP settings

**2. Scheduler Not Enabled:**
- **Check Scheduler:**
```bash
bench doctor
```
- Look for "Scheduler: Enabled"
- **If Disabled:**
```bash
bench --site your-site.local enable-scheduler
```

**3. Wrong Role:**
- Notifications go to "Accounts Manager" role
- **Solution**: Check you have this role
- Go to: User Settings or ask admin

**4. Spam Folder:**
- **Solution**: Check email spam/junk folder
- Add sender to contacts
- Mark as "Not Spam"

**5. Email Address Wrong:**
- **Solution**: Check your email in User profile
- Update if incorrect
- Save and wait for next notification

**6. No BGs Expiring:**
- **Solution**: Notifications only sent when BGs approaching expiry
- Check if any BGs within threshold days
- Create test BG expiring soon to verify

**7. Error Log:**
- **Check**: Tools → Error Log
- Look for email-related errors
- Share with administrator

#### Issue 6: Attachments Not Opening

**Symptoms:**
- Click filename but nothing happens
- Download fails
- "File not found" error

**Possible Causes & Solutions:**

**1. File Was Deleted:**
- **Solution**: Check if file exists in system
- Re-upload if necessary
- Contact administrator

**2. Browser Pop-up Blocked:**
- **Solution**: Allow pop-ups for this site
- Check browser settings
- Click filename again

**3. File Permission:**
- **Solution**: Check file permissions
- Administrator may need to fix
- Re-upload file

**4. Large File Timeout:**
- **Solution**: If file very large (>10MB)
- Download may timeout
- Try with better internet connection
- Compress and re-upload

**5. Browser Cache:**
- **Solution**: Clear browser cache
- Try different browser
- Hard refresh page

#### Issue 7: Auto-Calculations Wrong

**Symptoms:**
- Days to expiry showing wrong number
- Available amount incorrect
- Commission not calculating

**Possible Causes & Solutions:**

**1. Page Not Refreshed:**
- **Solution**: Save document
- Refresh page (F5)
- Calculations recalculate

**2. Extended But Using Original Dates:**
- **Solution**: Check "Is Extended" checkbox
- System uses extension expiry if extended
- Verify extension expiry date filled

**3. Fields Manually Edited:**
- Read-only fields should not be edited directly
- **Solution**: Clear the field
- Save document
- System will recalculate

**4. Date Issue:**
- **Solution**: Check dates are valid
- Ensure not in future if shouldn't be
- Save and refresh

**If Persists:**
- Contact system administrator
- May be a bug
- Provide specific details

---

## FAQs (Frequently Asked Questions)

### General Questions

**Q1: What is the difference between "Bank Guarantee" and "BG Management"?**

**A:** "Bank Guarantee" is ERPNext's standard DocType with basic features in the Accounts module. "BG Management" is our custom module with advanced features including:
- Complete FD tracking (amount, maturity, utilization)
- Extension history with child table
- Automatic expiry notifications (30, 15, 7, 3, 1 days)
- Multiple document attachments
- Advanced reporting with charts
- Auto-calculations

Both can coexist. Use "BG Management" for advanced needs.

---

**Q2: Can I delete a submitted BG?**

**A:** No. Submitted documents cannot be deleted for audit trail and compliance reasons. 

**Options:**
- **Cancel** the document if created in error
- **Amend** if you need to correct details
- Cancelled documents remain in system for audit

---

**Q3: How do I correct a mistake in a submitted BG?**

**A:** Use the **Amend** function:
1. Open the submitted BG
2. Click "Amend" button
3. Make corrections
4. Submit the amendment
5. New version created, original preserved

---

**Q4: Can I have unlimited BG numbers?**

**A:** Yes, no limit on number of BGs. System scales well for thousands of BG records.

---

### Financial Questions

**Q5: How is Available Amount calculated?**

**A:** Formula: `Available Amount = Maturity Amount - Utilized Amount`

It updates automatically when either value changes. Shows how much FD value is still available.

---

**Q6: Can utilized amount exceed maturity amount?**

**A:** No. System validates and prevents this. You'll get error message if you try.

**Why:** You cannot utilize more than the FD maturity value.

---

**Q7: How are commission charges calculated?**

**A:** Formula: `Commission Amount = (FD Amount × Commission Rate) / 100`

Example:
- FD Amount: 50,000
- Commission Rate: 1.5%
- Commission: (50,000 × 1.5) / 100 = 750

Calculates automatically when you enter FD amount or rate.

---

**Q8: What if extension has separate charges?**

**A:** Extension charges are recorded separately:
- Enter in Extension dialog when extending
- Stored in Extension History child table
- Each extension has own charge field
- Separate from main commission/processing charges

Sum all extension charges for total extension cost.

---

### Extension Questions

**Q9: How many times can I extend a BG?**

**A:** Unlimited. No system restriction on number of extensions.

Each extension is tracked in Extension History with:
- Extension number (1, 2, 3...)
- Previous and new expiry dates
- Extension charges
- Approval details

---

**Q10: Can I extend an expired BG?**

**A:** Technically yes (system allows it), but you should:
1. Extend BEFORE expiry (best practice)
2. If already expired, check with beneficiary and bank first
3. May need special approvals
4. Update expiry date to future date

---

**Q11: What happens to the original expiry date when I extend?**

**A:** Original expiry is preserved:
- "Expiry Date" field keeps original date
- "Extension Expiry Date" field shows new expiry
- Extension History shows all dates
- System uses extension expiry for calculations and alerts

Complete audit trail maintained.

---

**Q12: Can I cancel an extension?**

**A:** No direct "undo extension" feature.

**Options:**
1. **Amend** the document
2. Remove extension history row (if just added)
3. Change extension expiry back
4. Or keep as-is (accurate audit trail)

Best practice: Don't extend unless sure.

---

### Document Questions

**Q13: What file formats are supported for attachments?**

**A:** Commonly supported formats:
- **PDF** (recommended for official documents)
- **Images**: JPG, JPEG, PNG, GIF
- **Documents**: DOC, DOCX, XLS, XLSX
- **Text**: TXT, CSV
- **Others**: Most common formats

PDF recommended for BG documents (best quality, universal).

---

**Q14: Is there a file size limit?**

**A:** Yes, ERPNext has default limits:
- Usually 10 MB per file (admin can change)
- Large files slow down system
- **Recommendation**: Keep under 5 MB
- Compress large scans if needed

---

**Q15: Can I attach multiple versions of the same document?**

**A:** Yes, use Supporting Documents child table:
- Add multiple rows
- Each row = one document
- Different versions, updates, or related documents
- Example: Original BG, Amendment 1, Amendment 2

---

**Q16: What if I attached the wrong file?**

**A:**
1. Click on the filename/attachment
2. Click "Remove" or "Delete" button
3. Confirm deletion
4. Upload correct file
5. Save document

If already submitted, need to amend to change attachment.

---

### Report Questions

**Q17: Why doesn't the report show my BG?**

**A:** Check filters:
- **Default filter**: Shows only Active and Extended BGs
- **Solution**: Clear "Status" filter to see all
- Or select specific status you want

Other reasons:
- BG might be draft (not submitted)
- Dates outside filter range
- Wrong company selected

---

**Q18: Can I export report to Excel?**

**A:** Yes:
1. Run the report
2. Apply filters if needed
3. Click "Export" button
4. Select "Excel"
5. File downloads
6. Open in Excel/Google Sheets

Also available: PDF, CSV formats.

---

**Q19: How do I save my filter settings?**

**A:**
1. Apply your desired filters
2. Click "Save Filters" button
3. Give it a descriptive name (e.g., "Expiring This Month")
4. Click Save

**To Use Later:**
1. Open report
2. Click "Saved Filters" dropdown
3. Select your saved filter
4. Filters apply automatically

---

**Q20: Can I create my own custom report?**

**A:** Yes, two methods:

**1. Report Builder (Simple - No coding):**
- Setup → Report Builder → New
- Select fields, filters
- Save and use

**2. Script Report (Advanced - Requires Python):**
- For complex calculations
- Custom layouts
- Charts
- Contact administrator

---

### Notification Questions

**Q21: When do expiry notifications go out?**

**A:** Daily scheduler sends emails at these thresholds:
- 30 days before expiry
- 15 days before expiry
- 7 days before expiry
- 3 days before expiry
- 1 day before expiry

One email per threshold per BG.
Usually sent in early morning.

---

**Q22: Who receives notifications?**

**A:** All users with **"Accounts Manager"** role.

**To Receive:**
- Ask administrator to add you to this role
- OR administrator can customize to add specific users

---

**Q23: Can I change notification days?**

**A:** Yes, but requires code change:
- Edit `bg_management.py` file
- Modify `notification_days` array
- Example: Change `[30, 15, 7, 3, 1]` to `[60, 30, 7]`
- Requires technical knowledge
- Ask system administrator

---

**Q24: Why am I not receiving notifications?**

**A:** Check:
1. You have "Accounts Manager" role?
2. Email configured in system?
3. Scheduler enabled? (Run `bench doctor`)
4. Email address correct in your User profile?
5. Check spam/junk folder
6. Any BGs actually expiring within threshold days?
7. Check Error Log for email errors

---

### Status Questions

**Q25: When does status change to "Expired"?**

**A:** Automatically when:
- Current date passes the expiry date, OR
- If extended, current date passes extension expiry date

Happens on document save/view.
No manual action needed.

---

**Q26: Can I manually change the status?**

**A:** No, status is system-managed for accuracy.

**Status Changes By:**
- **System automatically**: Based on dates and conditions
- **Action buttons**: Extend BG, Mark as Claimed, Close BG

Don't edit status field directly (it's read-only).

---

**Q27: What's the difference between "Closed" and "Cancelled"?**

**A:**

**Closed:**
- BG completed normally
- No claim made
- Successful completion
- Use "Close BG" button
- Can happen after expiry

**Cancelled:**
- BG terminated/cancelled
- Created in error, or
- Contract cancelled, or
- Being replaced
- Use "Cancel" button
- Document marked cancelled

---

**Q28: Can I reopen a closed BG?**

**A:** No, once closed cannot be reopened.

**If Closed by Mistake:**
- Amend the document
- Change status back (if allowed), OR
- Create new BG if truly needed

Best practice: Only close when certain.

---

### Workflow Questions

**Q29: Can I set up multi-level approvals?**

**A:** Yes, using ERPNext Workflow feature:
- Define states (Draft, Pending, Approved)
- Create transitions
- Assign roles to each transition
- Apply to BG Management DocType

Requires administrator setup.

---

**Q30: Who can submit a BG?**

**A:** Users with either:
- "Accounts User" role, OR
- "Accounts Manager" role

These have "Submit" permission by default.

---

**Q31: Who can cancel a BG?**

**A:** Only users with **"Accounts Manager"** role.

Accounts Users cannot cancel (only create/submit).

---

**Q32: Can I limit who can extend BGs?**

**A:** Yes, through:
- Custom permission rules
- Workflow (require approval for extension)
- Role-based access

Contact administrator to set up.

---

### Integration Questions

**Q33: Can BG Management integrate with LC module?**

**A:** Yes, easy to link:
1. Add a Link field to BG Management
2. Link to your LC DocType
3. Now you can reference LC from BG

Or vice versa (add BG link field to LC).

---

**Q34: Does it work with ERPNext Projects?**

**A:** Yes, full integration:
- Link BGs to projects via Project field
- View project → see linked BGs
- Filter reports by project
- Track project-wise BG exposure

---

**Q35: Can I link to Purchase/Sales Orders?**

**A:** Yes, fields available:
- **Purchase Order**: For supplier BGs
- **Sales Order**: For customer BGs
- Link during BG creation
- Track order-wise guarantees

---

**Q36: Can it create accounting entries automatically?**

**A:** Partial automation available:
- Can create Journal Entry from BG (manual completion needed)
- Accounts must be configured by administrator
- Full automation possible with customization

Contact administrator for accounting integration setup.

---

### Mobile Questions

**Q37: Can I use BG Management on mobile?**

**A:** Yes! Fully supported:
- ERPNext mobile app (iOS/Android)
- Mobile browser (responsive design)
- All features work on mobile
- Create, view, edit BGs
- Upload documents from phone camera

---

**Q38: Can I receive notifications on mobile?**

**A:** Yes:
- ERPNext mobile app: Push notifications
- Email: Notification emails to your phone
- Enable notifications in app settings

---

**Q39: Can I attach documents from mobile?**

**A:** Yes:
- Take photo with camera
- Select from photo gallery
- Choose files from phone storage
- Upload to BG document

Same as desktop, just mobile interface.

---

## Glossary of Terms

**BG** - Bank Guarantee

**FD** - Fixed Deposit (money blocked with bank as security for BG)

**Beneficiary** - The party in whose favor the BG is issued (who can claim the BG)

**Applicant** - The party applying for the BG (usually your company)

**Maturity Amount** - The amount the FD will be worth at maturity (including interest)

**Utilized Amount** - Portion of BG/FD amount that has been claimed or used

**Available Amount** - Maturity Amount minus Utilized Amount (what's left)

**Extension** - Extending the expiry date of an existing BG beyond original expiry

**Amendment** - Creating a new version of a submitted document with corrections

**Claim** - Beneficiary invoking/using the guarantee (demanding payment)

**Commission** - Fee/percentage charged by bank for issuing BG

**DocType** - Document type in ERPNext (like BG Management, Customer, Invoice, etc.)

**Child Table** - Table within a document that can have multiple rows (like Extension History)

**Scheduler** - Background process that runs automated tasks (like sending notifications)

**SMTP** - Email sending protocol/server

**Awesomebar** - ERPNext's quick search feature (Ctrl+K or Cmd+K)

**Submittable DocType** - Document type that can be submitted (locked after submission)

**Workflow** - Defined approval process with states and transitions

**Master Data** - Core reference data like Customer, Supplier, Bank (used across system)

---

## Keyboard Shortcuts

### Global Shortcuts

- `Ctrl + K` (Windows/Linux) / `Cmd + K` (Mac): **Awesomebar** - Quick search
- `Ctrl + G`: **Go to List** - Navigate to module list
- `Ctrl + S`: **Save document**
- `Ctrl + Shift + S`: **Submit document**
- `Esc`: **Close dialog** or go back
- `Tab`: **Next field**
- `Shift + Tab`: **Previous field**

### List View Shortcuts

- `/`: **Focus search** box
- `Arrow keys`: **Navigate** through rows
- `Enter`: **Open** selected document
- `Ctrl + Click`: **Open in new tab**

### Form View Shortcuts

- `Ctrl + S`: **Save**
- `Ctrl + Shift + S`: **Submit**
- `Esc`: **Go back** to list

---

## Status Color Reference

Quick visual guide to status colors:

- 🟢 **Green (Active)**: BG is currently valid and active
- 🔵 **Blue (Extended)**: BG has been extended beyond original expiry
- 🔴 **Red (Expired)**: BG has passed its expiry date
- 🟠 **Orange (Claimed)**: BG has been invoked/claimed by beneficiary
- ⚪ **Gray (Closed)**: BG completed normally without claim
- ⚫ **Dark Gray (Cancelled)**: BG was cancelled before completion

---

## Contact Information

### For Technical Support

**System Administrator**
- Email: admin@yourcompany.com
- Phone: +91-XXX-XXX-XXXX
- Hours: 9:00 AM - 6:00 PM IST

**IT Help Desk**
- Email: helpdesk@yourcompany.com
- Ticket System: http://helpdesk.yourcompany.com
- Phone: +91-XXX-XXX-XXXX

### For Process Questions

**Accounts Manager**
- Email: accounts@yourcompany.com
- Phone: +91-XXX-XXX-XXXX

**Finance Team**
- Email: finance@yourcompany.com
- Phone: +91-XXX-XXX-XXXX

### For Training

**Training Coordinator**
- Email: training@yourcompany.com
- Schedule: Monthly training sessions

---

## Additional Resources

### External Documentation

**ERPNext Documentation**
- Website: https://docs.erpnext.com
- User Manual: https://docs.erpnext.com/docs/user/manual
- API Documentation: https://frappeframework.com/docs

**Community Forums**
- ERPNext Forum: https://discuss.erpnext.com
- Search for solutions
- Ask questions
- Share experiences

**Video Tutorials**
- YouTube: Search "ERPNext tutorials"
- Frappe School: https://frappe.school

### Internal Documentation

**Related Documents**
- BG Management - Features.md (complete feature list)
- BG Management - Quick Start Guide.md (installation guide)
- BG Management - Implementation Guide.md (technical details)

**Standard Operating Procedures (SOPs)**
- BG Creation SOP
- BG Extension SOP
- BG Closure SOP
- Monthly Reconciliation SOP

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | January 2025 | Implementation Team | Initial user manual created |
| | | | |

---

## Feedback and Improvements

We continuously improve this manual based on user feedback.

**How to Provide Feedback:**
1. Email: documentation@yourcompany.com
2. Subject: "BG Management User Manual Feedback"
3. Include:
   - Section that needs improvement
   - What's unclear or missing
   - Suggestions for improvement
   - Screenshots if applicable

**Thank You!**

Your feedback helps us improve the documentation for everyone.

---

## Conclusion

Congratulations! You've completed the BG Management User Manual.

**You Now Know How To:**
- ✅ Create and manage bank guarantees
- ✅ Track FD details and utilization
- ✅ Handle extensions with complete history
- ✅ Process claims and closures
- ✅ Manage documents efficiently
- ✅ Generate comprehensive reports
- ✅ Set up and use notifications
- ✅ Apply best practices
- ✅ Troubleshoot common issues

**Next Steps:**
1. Practice creating a test BG
2. Explore the reports
3. Set up your filters
4. Import your existing BG data
5. Train your team
6. Start using in production

**Remember:**
- Refer back to this manual anytime
- Check FAQs for quick answers
- Contact support when needed
- Keep learning and improving

---

**Happy BG Managing!**

---

**End of User Manual**

**Document Version:** 1.0  
**Last Updated:** January 2025  
**Total Pages:** [As displayed]  
**For:** BG Management Module, ERPNext 15.x

---

**Copyright © 2025 Your Company**  
All rights reserved.

This document is for internal use only. Do not distribute without permission.