# Letter of Credit Management App - Complete User Manual

## Table of Contents

1. [Getting Started](#getting-started)
2. [Creating a Letter of Credit](#creating-a-letter-of-credit)
3. [Managing LC Amendments](#managing-lc-amendments)
4. [Document Management](#document-management)
5. [Shipment Tracking](#shipment-tracking)
6. [Charges Management](#charges-management)
7. [Using Reports](#using-reports)
8. [Workspace Navigation](#workspace-navigation)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Accessing the LC Module

1. **Login** to your ERPNext site
2. **Click** on the workspace icon (☰) in the left sidebar
3. **Find and click** "Letter of Credit" workspace
4. You'll see the LC dashboard with shortcuts and reports

### Understanding User Roles

**Your access depends on your role:**

- **Accounts Manager:** Full access - create, edit, submit, amend, cancel LCs
- **Accounts User:** Can create, edit, and submit LCs (cannot cancel)
- **Purchase Manager:** View-only access to LCs and reports
- **Sales Manager:** View-only access to LCs and reports

---

## Creating a Letter of Credit

### When to Create an LC

**Import LC:** When purchasing goods from international supplier  
**Export LC:** When receiving LC from international customer

### Step-by-Step Guide

#### Step 1: Navigate to New LC

**Method 1:** Click "New Letter of Credit" shortcut in workspace  
**Method 2:** Search bar → Type "Letter of Credit" → Click "+ Add Letter of Credit"  
**Method 3:** Go to Letter of Credit list → Click "New" button

---

#### Step 2: Basic Information

**Series (Auto-filled):**
- `LC-IMP-.YYYY.-` for Import LCs
- `LC-EXP-.YYYY.-` for Export LCs
- System automatically assigns the next number

**LC Number:** *(Required)*
```
Enter the bank-provided LC number
Example: LC/2024/001234
Purpose: Official bank reference number for this LC
```

**LC Type:** *(Required)*
```
Options:
- Sight LC: Payment on presentation of documents
- Usance LC: Payment after specified period (30, 60, 90 days)
- Deferred Payment LC: Payment at future date without draft
- Revolving LC: Can be used multiple times up to limit
- Transferable LC: Can be transferred to third party
- Back-to-Back LC: LC opened against another LC as collateral
- Standby LC: Guarantee payment if buyer defaults

Choose based on your agreement with bank/supplier
```

**Transaction Type:** *(Required)*
```
Options:
- Import: You are buying goods (supplier is beneficiary)
- Export: You are selling goods (customer is beneficiary)

Important: This automatically sets applicant/beneficiary types
```

**LC Opening Date:** *(Required)*
```
Date when bank opens/issues the LC
Usually the date on bank's LC opening advice
Cannot be in the future
```

**Expiry Date:** *(Required)*
```
Last date for document submission
Must be after LC Opening Date
Bank will not accept documents after this date
Example: If LC opened on 01-Jan-2024, expiry might be 31-Mar-2024
```

**Latest Shipment Date:** *(Optional)*
```
Last date when goods can be shipped
Must be before or equal to Expiry Date
Ensures time for document preparation after shipment
Example: If expiry is 31-Mar-2024, shipment date might be 15-Mar-2024
```

**Status:** *(Auto-managed)*
```
System automatically manages status:
- Draft: Being created
- Opened: Submitted and bank has opened LC
- Amended: LC has been modified
- Documents Submitted: Required documents given to bank
- Documents Accepted: Bank has accepted documents
- Payment Made: Payment processed
- Settled: LC fully completed
- Cancelled: LC cancelled
- Expired: Expiry date has passed

You can manually change some statuses using action buttons
```

---

#### Step 3: Party Details

**Applicant Type:** *(Auto-filled based on Transaction Type)*
```
Import LC: Your company
Export LC: Supplier (overseas buyer)
System fills this automatically - don't change unless necessary
```

**Applicant:** *(Required)*
```
Applicant: The party who OPENS/APPLIES for the LC at their bank (and ultimately pays)
For Import: Select your company
For Export: Select the overseas buyer
```

**Applicant Name:** *(Auto-filled)*
```
Automatically populated from selected applicant
Read-only field for display
```

**Beneficiary Type:** *(Auto-filled based on Transaction Type)*
```
Import LC: Supplier (overseas seller)
Export LC: Your company
System fills this automatically
```

**Beneficiary:** *(Required)*
```
Beneficiary: The party who RECEIVES payment under the LC (after fulfilling conditions)
For Import: Select the overseas supplier
For Export: Select your company
This is who receives payment under the LC
```

**Beneficiary Name:** *(Auto-filled)*
```
Automatically populated from selected beneficiary
Read-only field for display
```

---

#### Step 4: Bank Details

**Issuing Bank:** *(Required)*
```
Bank that issues/opens the LC
For Import: Your bank
For Export: Customer's bank
Enter full bank name and branch
Example: HDFC Bank, Marine Lines Branch, Mumbai
```

**Advising Bank:** *(Optional)*
```
Bank that advises/notifies the beneficiary about LC
Usually a bank in beneficiary's country
For Export: Your bank (advises you about LC received)
Example: State Bank of India, International Division
```

**Confirming Bank:** *(Optional)*
```
Bank that guarantees payment (for confirmed LCs)
Provides additional security to beneficiary
Charges extra fees
Example: Citibank Singapore
```

**Reimbursing Bank:** *(Optional)*
```
Bank that will reimburse the advising/confirming bank
Usually specified in LC terms
Example: JP Morgan Chase, New York
```

---

#### Step 5: Financial Details

**Currency:** *(Required)*
```
Currency in which LC is denominated
Select from dropdown: USD, EUR, GBP, JPY, etc.
Must match Purchase/Sales Order currency
Example: USD
```

**LC Amount:** *(Required)*
```
Total value of the LC
Enter numeric value in selected currency
Example: 50000 (for USD 50,000)
This is the maximum amount that can be drawn
```

**Tolerance (%):** *(Optional, Default: 0)*
```
Acceptable percentage variance in value/quantity
Common values: 5%, 10%
Allows flexibility in shipment
Example: If LC Amount is 50,000 with 5% tolerance:
- Maximum drawable: 52,500 (50,000 + 2,500)
- Minimum acceptable: 47,500 (50,000 - 2,500)
```

**Utilized Amount:** *(Auto-calculated, Read-only)*
```
Total value of shipments made against this LC
Automatically calculated from Shipments table
Updates when you add/remove shipments
Shows how much of LC has been used
```

**Balance Amount:** *(Auto-calculated, Read-only)*
```
Remaining LC value available for shipments
Formula: (LC Amount + Tolerance Amount) - Utilized Amount
Example: If LC Amount is 50,000, Tolerance 5%, Utilized 30,000:
Balance = (50,000 + 2,500) - 30,000 = 22,500
```

---

#### Step 6: Reference Documents

**Purchase Order:** *(Optional but Recommended)*
```
Link to ERPNext Purchase Order (for Import LC)
Auto-fills: Supplier, Currency, Amount, Incoterms
Makes LC creation faster and accurate
Click "..." to search and select PO
```

**Sales Order:** *(Optional but Recommended)*
```
Link to ERPNext Sales Order (for Export LC)
Auto-fills: Customer, Currency, Amount, Incoterms
Click "..." to search and select SO
```

**Incoterms:** *(Optional)*
```
International Commercial Terms defining responsibilities
Common options:
- FOB (Free on Board): Buyer pays shipping from port
- CIF (Cost, Insurance & Freight): Seller pays to destination
- CFR (Cost and Freight): Like CIF but no insurance
- EXW (Ex Works): Buyer collects from seller's premises
- DDP (Delivered Duty Paid): Seller pays everything to destination
```

**Port of Loading:** *(Optional)*
```
Where goods will be loaded onto ship/plane
Example: Nhava Sheva Port, Mumbai
Important for tracking and compliance
```

**Port of Discharge:** *(Optional)*
```
Where goods will be unloaded
Example: Los Angeles Port, USA
Customer's receiving location
```

---

#### Step 7: Shipment & Payment Terms

**Partial Shipment:** *(Checkbox)*
```
☑ Allowed: Can ship goods in multiple lots
☐ Not Allowed: Must ship all goods at once

Example: If allowed, you can ship:
- Shipment 1: $20,000 worth
- Shipment 2: $30,000 worth
Total: $50,000
```

**Transhipment:** *(Checkbox)*
```
☑ Allowed: Goods can be transferred between ships/planes
☐ Not Allowed: Direct shipment only

Affects routing and shipping costs
```

**Payment Terms:** *(Required)*
```
Options:
- At Sight: Pay immediately on document presentation
- Usance: Pay after X days (30, 60, 90, 120 days)
- Deferred Payment: Pay on specific future date
- Acceptance: Pay on draft acceptance

Auto-filled based on LC Type but can be changed
```

**Usance Days:** *(Conditional - appears if Payment Terms = Usance)*
```
Number of days after document presentation for payment
Common values: 30, 60, 90, 120, 180 days
Example: If Usance Days = 60:
- Documents presented: 01-Jan-2024
- Payment due: 02-Mar-2024 (60 days later)
```

---

#### Step 8: Required Documents

**Click "Add Row" in Documents table**

For each document, specify:

**Document Type:** *(Required)*
```
Select from dropdown:
- Commercial Invoice: Seller's bill
- Packing List: Contents of shipment
- Bill of Lading: Shipping document (for sea freight)
- Airway Bill: Shipping document (for air freight)
- Certificate of Origin: Proof of manufacturing country
- Inspection Certificate: Quality inspection report
- Insurance Certificate: Cargo insurance
- Phytosanitary Certificate: Plant health certificate
- Health Certificate: For food/medical products
- Weight Certificate: Certified weight statement
- Quality Certificate: Quality assurance document
- Beneficiary Certificate: Supplier's declaration
- Other: Any other document

Banks are strict - ensure all required documents are listed
```

**Document Name:** *(Optional)*
```
Specific name or reference for this document
Example: "Certificate of Origin - Form A"
Helps in tracking specific document versions
```

**Required Copies:** *(Default: 1)*
```
Number of original copies needed
Common: 1, 2, 3
Example: Commercial Invoice - 3 copies
Banks need originals for negotiation
```

**Status:** *(Default: Pending)*
```
Track document submission status:
- Pending: Not yet submitted
- Submitted: Given to bank
- Accepted: Bank has accepted
- Rejected: Bank has rejected (discrepancies found)

Update this as documents are processed
```

**Submitted Date:** *(Optional)*
```
Date when document was submitted to bank
Important for tracking presentation timeline
Example: 15-Mar-2024
```

**Attached File:** *(Optional)*
```
Upload digital copy of the document
Click "Attach" button
Supports: PDF, JPG, PNG
Creates digital archive
```

**Remarks:** *(Optional)*
```
Any notes about this document
Example: "Awaiting courier tracking number"
          "Resubmitted after correction"
```

---

#### Step 9: Shipments (Add as goods are shipped)

**Click "Add Row" in Shipments table**

**Shipment Date:** *(Required)*
```
Date when goods were shipped
Must be on or before Latest Shipment Date
Example: 10-Mar-2024
Used for compliance checking
```

**B/L or AWB Number:** *(Required)*
```
Bill of Lading (sea) or Airway Bill (air) number
Official shipping document reference
Example: MAEU1234567890 (for sea freight)
         157-12345678 (for air freight)
This is the key document for claiming goods
```

**Delivery Note:** *(Optional but Recommended)*
```
Link to ERPNext Delivery Note
Auto-fills: Shipment Date, Value, Quantity
Click "..." to search and select
Ensures consistency with shipping records
```

**Shipped Quantity:** *(Optional)*
```
Total quantity of goods in this shipment
Units depend on your product (pcs, kg, boxes, etc.)
Example: 1000 pieces
Used for tracking against order quantity
```

**Shipped Value:** *(Required)*
```
Total value of goods in this shipment
Must be in LC currency
Example: 25000 (for USD 25,000)
Automatically updates Utilized Amount
```

**Vessel/Flight Name:** *(Optional)*
```
Name of ship or flight carrying goods
Example: MSC MERAVIGLIA (ship name)
         AI 191 (flight number)
Useful for tracking and documentation
```

**Container Number:** *(Optional)*
```
Container reference for sea freight
Example: TCLU1234567
Multiple containers: Separate with commas
Helps in cargo tracking
```

**Remarks:** *(Optional)*
```
Any notes about this shipment
Example: "First partial shipment"
          "Container delayed by 2 days"
```

**Important:** When you add/edit shipments, watch the Utilized Amount and Balance Amount fields update automatically!

---

#### Step 10: LC Charges

**Click "Add Row" in Charges table**

**Charge Type:** *(Required)*
```
Select from dropdown:
- LC Opening Charge: Bank's charge to open LC
- LC Amendment Charge: For modifying LC
- LC Advising Charge: Advising bank's fee
- LC Confirmation Charge: Confirming bank's fee
- Negotiation Charge: For document negotiation
- Acceptance Charge: For accepting drafts
- Discounting Charge: For early payment
- Courier Charge: Sending documents
- SWIFT Charge: Electronic communication
- Document Handling Charge: Processing fees
- Insurance Charge: Cargo insurance
- Port Charge: Port-related fees
- Customs Duty: Import/export duties
- Other: Any other charge
```

**Charge Date:** *(Required)*
```
Date when charge was incurred
Example: 05-Jan-2024
Used for expense reporting
```

**Amount:** *(Required)*
```
Charge amount
Enter numeric value
Example: 500
```

**Currency:** *(Required)*
```
Currency of the charge
Often same as LC currency but can be different
Example: USD, INR, EUR
```

**Payment Entry:** *(Optional)*
```
Link to ERPNext Payment Entry if charge was paid
Click "..." to search and select
Creates accounting link
```

**Journal Entry:** *(Optional)*
```
Link to ERPNext Journal Entry for accounting
Alternative to Payment Entry
For complex accounting entries
```

**Remarks:** *(Optional)*
```
Notes about this charge
Example: "Quarterly bank charges"
          "Rush amendment fee"
```

---

#### Step 11: Additional Information

**Special Instructions:** *(Optional, Text Editor)*
```
Any specific instructions or conditions for this LC
Example:
- "Shipment must be from Indian port only"
- "Invoice should show FOB value separately"
- "Original documents must reach within 21 days"

Use the text editor for formatting
Important for compliance
```

**Terms and Conditions:** *(Optional, Text Editor)*
```
Standard or custom terms for this LC
Example:
- Payment terms details
- Document requirements details
- Inspection procedures
- Dispute resolution clauses

Copy from templates if available
```

---

#### Step 12: Save and Submit

**Save as Draft:**
```
1. Click "Save" button (top right)
2. LC is saved but not active
3. Status: "Draft"
4. You can edit anytime
```

**Submit (Activate) LC:**
```
1. After saving, click "Submit" button
2. LC becomes active
3. Status changes to "Opened"
4. Cannot edit (must amend instead)
5. Available for document submission and shipping

Only submit when bank has actually opened the LC!
```

---

### Quick Tips for Creating LCs

✅ **Always link to Purchase/Sales Order** - Saves time and reduces errors  
✅ **Double-check LC number** - This is your bank reference  
✅ **Set expiry with buffer** - Give time for document preparation  
✅ **Add all required documents** - Prevents delays later  
✅ **Set realistic tolerance** - Usually 5-10% is standard  
✅ **Save frequently** - Don't lose your work  
✅ **Don't submit until bank opens** - Submit only after receiving bank confirmation

---

## Managing LC Amendments

### When to Create an Amendment

- LC amount needs to be increased/decreased
- Expiry date needs extension
- Shipment date needs to be extended
- Payment terms change
- Document requirements change
- Any other modification to LC terms

### Step-by-Step Amendment Process

#### Step 1: Create Amendment

**Method 1:** Open the LC → Click "Actions" button → "Create Amendment"  
**Method 2:** From workspace, click "New LC Amendment" → Select LC

---

#### Step 2: Fill Amendment Details

**Letter of Credit:** *(Auto-filled or Select)*
```
The LC you want to amend
Search and select if not auto-filled
All current LC values will be fetched automatically
```

**Amendment Number:** *(Auto-generated)*
```
System automatically assigns sequential number
Example: If this is 2nd amendment, shows "2"
Read-only field
```

**Amendment Date:** *(Required)*
```
Date of amendment request/approval
Usually the date bank issues amendment
Example: 25-Feb-2024
Must be after LC Opening Date
```

**Amendment Type:** *(Required)*
```
Select primary reason:
- Amount Increase: Raising LC value
- Amount Decrease: Reducing LC value
- Date Extension: Extending expiry or shipment dates
- Terms Change: Modifying payment or other terms
- Document Change: Adding/removing required documents
- Other: Any other modification

Helps in reporting and tracking
```

---

#### Step 3: Amendment Details Section

**Previous LC Amount:** *(Auto-filled, Read-only)*
```
Current LC amount before amendment
Fetched from the LC
Cannot be changed
Reference field for comparison
```

**New LC Amount:** *(Optional)*
```
Updated LC amount
Enter only if amount is changing
Leave blank if amount stays same
Example: If increasing from 50,000 to 60,000
New LC Amount: 60,000
```

**Amount Change:** *(Auto-calculated, Read-only)*
```
Difference between new and previous amount
Formula: New LC Amount - Previous LC Amount
Positive = Increase
Negative = Decrease
Example: 60,000 - 50,000 = +10,000
```

**Previous Expiry Date:** *(Auto-filled, Read-only)*
```
Current expiry date before amendment
Fetched from the LC
Reference field
```

**New Expiry Date:** *(Optional)*
```
Extended/modified expiry date
Enter only if extending expiry
Must be after Amendment Date
Leave blank if not changing
Example: Extending from 31-Mar-2024 to 30-Apr-2024
```

**Previous Shipment Date:** *(Auto-filled, Read-only)*
```
Current latest shipment date
Fetched from LC
Reference field
```

**New Shipment Date:** *(Optional)*
```
Extended/modified shipment date
Enter only if extending shipment date
Must be before or equal to New Expiry Date
Example: Extending from 15-Mar-2024 to 15-Apr-2024
```

---

#### Step 4: Reason & Details

**Reason for Amendment:** *(Optional but Recommended)*
```
Select from dropdown:
- Delay in Shipment: Goods not ready on time
- Increase in Order Quantity: Buyer ordered more
- Decrease in Order Quantity: Buyer ordered less
- Change in Terms: Modification in agreement
- Change in Documents: Updated requirements
- Buyer Request: Customer requested change
- Supplier Request: Vendor requested change
- Other: Any other reason

Helps in audit and analysis
```

**Amendment Details:** *(Optional, Text Editor)*
```
Detailed explanation of changes
Example:
"Due to manufacturing delay, shipment postponed by 30 days.
Original expiry: 31-Mar-2024
New expiry: 30-Apr-2024
New shipment date: 15-Apr-2024
Buyer has agreed to extension."

Provide complete context
```

---

#### Step 5: Charges & References

**Amendment Charge:** *(Optional)*
```
Bank's fee for processing amendment
Numeric value in currency
Example: 250 (for USD 250 amendment fee)
Track all amendment costs
```

**Payment Entry:** *(Optional)*
```
Link to payment for amendment charge
Click "..." to search and select
Creates accounting link
```

**Bank Reference:** *(Optional)*
```
Bank's amendment reference number
Example: AMD/2024/001
Useful for bank correspondence
```

**Status:** *(Auto-managed)*
```
System tracks amendment status:
- Draft: Being created
- Submitted: Amendment request submitted
- Approved: Amendment processed (auto-set on submit)
- Rejected: Amendment declined (manual)
- Cancelled: Amendment cancelled

Usually moves Draft → Submitted → Approved
```

---

#### Step 6: Save and Submit Amendment

**Save as Draft:**
```
1. Click "Save"
2. Amendment saved but not applied
3. LC values unchanged
```

**Submit Amendment:**
```
1. Click "Submit"
2. Amendment is applied
3. LC is automatically updated with new values
4. Original values stored in amendment for history
5. LC status changes to "Amended"
6. Comment added to LC about amendment

Important: Submit only after bank confirms amendment!
```

---

#### Step 7: Verify Amendment Applied

**Check Original LC:**
```
1. Open the original LC
2. Verify updated fields:
   - LC Amount (if changed)
   - Expiry Date (if changed)
   - Shipment Date (if changed)
3. Status should show "Amended"
4. Check comments section for amendment note
```

---

### Amendment Best Practices

✅ **Create amendment before expiry** - Don't wait until last minute  
✅ **Get bank confirmation first** - Then submit amendment  
✅ **Document the reason** - Helps in future reference  
✅ **Track amendment charges** - For cost analysis  
✅ **One amendment = One change type** - Don't mix multiple major changes  
✅ **Verify LC updated** - Always check original LC after submitting amendment

### Cancelling an Amendment

If you need to revert an amendment:

1. Open the amendment document
2. Click "Cancel" button
3. System will restore LC to previous values
4. Amendment status changes to "Cancelled"
5. Comment added to LC about cancellation

**Warning:** Only cancel if bank has not processed the amendment!

---

## Document Management

### Purpose of Document Tracking

LCs are document-based transactions. Banks only pay when ALL required documents are:
- Submitted within expiry date
- Compliant with LC terms
- Free from discrepancies

Proper document management ensures smooth payment.

### Adding Required Documents

(Already covered in LC creation above - see Step 8)

### Updating Document Status

**As documents are prepared and submitted:**

1. **Open the LC**
2. **Scroll to "Required Documents" table**
3. **Click on the document row to edit**
4. **Update fields:**
   - **Submission Status:** Change from "Pending" to "Submitted"
   - **Submitted Date:** Enter submission date
   - **Attached File:** Upload document copy
   - **Remarks:** Add any notes
5. **Save the LC**

### Document Status Workflow

```
Pending (Initial)
   ↓
Submitted (When given to bank)
   ↓
Accepted (Bank approves) OR Rejected (Discrepancies found)
   ↓
If Rejected: Correct and change back to Submitted
```

### Attaching Document Files

**To attach a document:**

1. **In the document row, click "Attach" button**
2. **Choose file from computer**
3. **Supported formats:** PDF, JPG, PNG, DOCX
4. **File size limit:** Usually 5-10 MB
5. **File uploads and attaches to that document row**
6. **Save LC to confirm attachment**

**Benefits:**
- Digital archive of all documents
- Easy access for review
- Quick sharing with team members
- Audit trail

### Common Documents Explained

**Commercial Invoice:**
```
- Seller's bill for goods
- Must match LC description exactly
- Shows price, quantity, terms
- Usually required: 3 copies
- Most important document
```

**Packing List:**
```
- Details of how goods are packed
- Shows number of boxes, weight, dimensions
- Helps in customs clearance
- Usually required: 2-3 copies
```

**Bill of Lading (B/L):**
```
- For sea freight shipments
- Proof of goods loaded on ship
- Title document (negotiable)
- Required: Original(s) + copies
- Must be "clean" (no remarks about damage)
```

**Airway Bill (AWB):**
```
- For air freight shipments
- Non-negotiable (not a title document)
- Faster but more expensive than B/L
- Required: 1 original + copies
```

**Certificate of Origin:**
```
- Proves country where goods manufactured
- Required for customs duty calculation
- Often needs embassy/chamber certification
- Common forms: Form A, Form E, Certificate of Origin
```

**Inspection Certificate:**
```
- Third-party quality inspection report
- Proves goods meet specifications
- Issued by surveyor (SGS, Bureau Veritas, etc.)
- Important for quality assurance
```

### Document Checklist Strategy

**Before shipment:**
☐ List all required documents in LC  
☐ Check if any need special certification  
☐ Plan timeline (some certificates take days)  
☐ Arrange inspection if needed

**After shipment:**
☐ Collect all shipping documents (B/L, Packing List)  
☐ Prepare commercial invoice (exact LC description)  
☐ Get certificates (origin, inspection, etc.)  
☐ Check all documents for discrepancies  
☐ Submit to bank before expiry

**After submission:**
☐ Update status to "Submitted" in system  
☐ Get bank receipt/acknowledgment  
☐ Track acceptance status  
☐ Respond quickly to any discrepancies

---

## Shipment Tracking

### Purpose

Track utilization of LC as goods are shipped. Critical for:
- Monitoring how much LC value is used
- Preventing over-utilization
- Compliance with partial shipment terms
- Financial planning

### Adding a Shipment

(Already covered in LC creation - see Step 9)

### Multiple Shipments (Partial Shipments)

**If LC allows partial shipments:**

**Example Scenario:**
- LC Amount: USD 100,000
- Tolerance: 5%
- Maximum drawable: USD 105,000

**Shipment 1:**
- Date: 10-Mar-2024
- Value: USD 40,000
- Utilized: USD 40,000
- Balance: USD 65,000

**Shipment 2:**
- Date: 25-Mar-2024
- Value: USD 35,000
- Utilized: USD 75,000 (40K + 35K)
- Balance: USD 30,000

**Shipment 3:**
- Date: 05-Apr-2024
- Value: USD 30,000
- Utilized: USD 105,000 (75K + 30K)
- Balance: USD 0

**System automatically:**
- Adds up all shipment values
- Updates Utilized Amount
- Calculates Balance
- Warns if exceeding maximum

### Linking Delivery Notes

**If you use ERPNext Delivery Notes:**

1. **Create Delivery Note first** (in Stock module)
2. **In LC Shipment table, select the Delivery Note**
3. **System auto-fills:**
   - Shipment Date (from DN posting date)
   - Shipped Value (from DN grand total)
   - Shipped Quantity (sum of all items)
4. **Still need to manually enter:**
   - B/L or AWB Number
   - Vessel/Container details
5. **Save LC**

**Benefits:**
- Consistency with shipping records
- Less data entry
- Automatic quantity calculations
- Links to stock movement

### Shipment Compliance Checks

**System validates:**

✅ **Shipment Date ≤ Latest Shipment Date**
```
Error if you ship after allowed date
Example: Latest Shipment Date: 15-Mar-2024
Cannot enter Shipment Date: 20-Mar-2024
```

✅ **Utilized Amount ≤ LC Amount + Tolerance**
```
Warns if total shipments exceed maximum
Example: LC 100,000 + 5% = 105,000 max
Cannot ship more than 105,000
```

✅ **Partial Shipment Allowed (if multiple shipments)**
```
If LC says "Partial Shipment: Not Allowed"
Can only have ONE shipment
System prevents adding second shipment
```

### Editing/Deleting Shipments

**To Edit:**
1. Open LC
2. Click on shipment row
3. Modify values
4. Save
5. Utilized and Balance amounts recalculate

**To Delete:**
1. Open LC
2. Click "X" on shipment row
3. Confirm deletion
4. Save
5. Amounts recalculate

**Important:** Only edit before documents are submitted to bank!

---

## Charges Management

### Purpose

Track all costs associated with LC to understand true cost of transaction.

### Types of Charges Explained

**LC Opening Charge:**
```
Bank's fee to open/issue the LC
Usually: 0.10% - 0.25% of LC amount
Charged: When LC is opened
Example: LC 100,000 × 0.15% = $150
```

**LC Amendment Charge:**
```
Bank's fee for any modification
Usually: Flat fee (USD 50-100) or percentage
Charged: Each time LC is amended
```

**LC Advising Charge:**
```
Advising bank's fee to notify beneficiary
Usually: Flat fee (USD 50-75)
Charged: When LC is received/advised
```

**LC Confirmation Charge:**
```
For confirmed LCs (bank guarantee)
Usually: 0.10% - 0.50% per quarter
Charged: Periodically until payment
Higher risk = higher charge
```

**Negotiation Charge:**
```
Bank's fee to negotiate/buy documents
Usually: 0.10% - 0.25% of invoice value
Charged: When documents presented
```

**Acceptance Charge:**
```
For usance LCs - accepting time draft
Usually: Percentage for credit period
Charged: When accepting draft
```

**Discounting Charge:**
```
For early payment on usance LCs
Interest charge for prepayment
Depends on: Usance period, interest rate
```

**SWIFT Charge:**
```
Electronic communication charges
Usually: USD 10-25 per message
Multiple messages = multiple charges
```

**Document Handling:**
```
Processing and checking documents
Usually: USD 50-100 per presentation
Charged: When submitting documents
```

**Courier Charge:**
```
Sending documents via courier
Actual courier costs
Example: DHL, FedEx charges
```

**Insurance Charge:**
```
Cargo insurance premium
Usually: 0.10% - 0.50% of shipment value
Depends on: Route, cargo type, coverage
```

**Port Charge:**
```
Port fees - loading, unloading, storage
Varies by port and cargo volume
Example: Container handling charges
```

**Customs Duty:**
```
Import/export duties and taxes
Depends on: Product, country, trade agreements
Can be significant portion of total cost
```

### Adding Charges

(Already covered - see LC creation Step 10)

### Linking Charges to Payments

**When you pay a charge:**

1. **Create Payment Entry in ERPNext**
   - Go to Accounts → Payment Entry → New
   - Enter payment details
   - Save and Submit

2. **Link to LC Charge**
   - Open your LC
   - Find the charge row
   - Click in "Payment Entry" field
   - Search and select the payment
   - Save LC

**Benefit:** Creates complete financial trail from LC to payment

### Charge Analysis

**View all charges for an LC:**
1. Open the LC
2. Scroll to "LC Charges" section
3. See all charges with dates and amounts
4. Total is calculated automatically

**For overall charge analysis, use LC Charges Analysis Report** (covered in Reports section)

---

## Using Reports

### Report 1: LC Register

#### Purpose
Master report showing all LCs with complete details. Your "go-to" report for LC overview.

#### When to Use
- **Daily:** Quick status check of all active LCs
- **Weekly:** Management updates
- **Monthly:** Period-end reporting
- **Audit:** Compliance and verification
- **Planning:** Cash flow forecasting

#### How to Access
**Method 1:** Workspace → Click "LC Register" under Reports  
**Method 2:** Search bar → Type "LC Register" → Click  
**Method 3:** LC List → Click "Menu" → "LC Register"

#### Using Filters

**From Date & To Date:**
```
Filter LCs by opening date range
Example: From: 01-Jan-2024, To: 31-Mar-2024
Shows: All LCs opened in Q1 2024
Leave blank: Shows all LCs
```

**Transaction Type:**
```
Filter by Import or Export
Select: Import (to see only import LCs)
Blank: Shows both
```

**LC Type:**
```
Filter by specific LC type
Select: Sight LC, Usance LC, etc.
Useful: "Show me all Sight LCs"
```

**Status:**
```
Filter by current status
Select: Opened, Documents Submitted, Settled, etc.
Example: Status = "Opened" shows active LCs
```

**Currency:**
```
Filter by LC currency
Select: USD, EUR, GBP, etc.
Useful: "Show all USD LCs"
```

**Issuing Bank:**
```
Filter by bank name
Type: Bank name (partial match works)
Example: "HDFC" finds all HDFC Bank LCs
```

**Applicant / Beneficiary:**
```
Filter by party name
Type: Customer or Supplier name
Example: "ABC Corp" shows all LCs with this party
```

#### Understanding the Report

**Key Columns:**

**LC Number:** Click to open LC document  
**Bank LC Number:** Official bank reference  
**Type:** Import/Export  
**LC Type:** Sight, Usance, etc.  
**Dates:** Opening, Expiry dates  
**Parties:** Who applied, who receives payment  
**Financial:** Amount, Utilized, Balance, Utilization %  
**Status:** Current workflow status  
**Bank:** Issuing bank name  
**Reference:** Linked PO or SO  

**Utilization %:**
```
Shows how much of LC is used
Formula: (Utilized / LC Amount) × 100
Example: 75,000 / 100,000 = 75%

Color coding (in some views):
- Green: 0-50% (Low utilization)
- Yellow: 50-75% (Moderate)
- Orange: 75-95% (High)
- Red: 95-100% (Nearly/Fully utilized)
```

**Total Row:**
```
Bottom row shows:
- Count of LCs
- Total LC Amount
- Total Utilized
- Total Balance
- Average Utilization %

Useful for financial summaries
```

#### Report Actions

**Export to Excel:**
1. Click "Menu" (three dots)
2. Select "Download"
3. Choose format: Excel or CSV
4. File downloads to your computer

**Print:**
1. Click "Menu"
2. Select "Print"
3. Choose print settings
4. Print or Save as PDF

**Email Report:**
1. Click "Menu"
2. Select "Email"
3. Enter recipient email
4. Add message
5. Send

#### Common Use Cases

**Scenario 1: Month-End Reporting**
```
Filters:
- From Date: 01-Jan-2024
- To Date: 31-Jan-2024
- Status: (blank - all)

Result: All LCs opened in January
Use: Monthly management report
```

**Scenario 2: Check Active Import LCs**
```
Filters:
- Transaction Type: Import
- Status: Opened, Amended, Documents Submitted

Result: All active import LCs
Use: Daily operations monitoring
```

**Scenario 3: Bank-wise Analysis**
```
Filters:
- Issuing Bank: HDFC Bank
- From Date: 01-Jan-2024
- To Date: 31-Dec-2024

Result: All HDFC LCs for the year
Use: Bank relationship analysis
Export to Excel for further analysis
```

---

### Report 2: LC Expiry Report

#### Purpose
Proactive monitoring of LCs approaching expiry. Your "early warning system" to prevent last-minute rushes.

#### When to Use
- **Daily:** Morning routine check
- **Weekly:** Planning amendments
- **Before holidays:** Ensure coverage
- **Team meetings:** Assign priorities

#### How to Access
**Method 1:** Workspace → Click "LC Expiry Report"  
**Method 2:** Workspace → Click "Expiring LCs" shortcut (quick access)  
**Method 3:** Search "LC Expiry Report"

#### Using Filters

**Transaction Type:**
```
Import or Export
Example: Import (focus on import obligations)
```

**Issuing Bank:**
```
Filter by specific bank
Useful: Check one bank's expiring LCs
```

**Show All:**
```
Checkbox: ☐ (default) Shows LCs expiring within 90 days
         ☑ (checked) Shows ALL LCs regardless of expiry

Recommendation: Keep unchecked for daily use
Check when doing comprehensive review
```

#### Understanding the Report

**Expiry Status Categories:**

**Expired (Red Alert):**
```
Days to Expiry: Negative number (e.g., -5 = 5 days overdue)
Meaning: LC has already expired
Action: URGENT - Check if amendment needed
        Contact bank immediately
        May need to cancel and reopen
```

**Expiring This Week (Critical):**
```
Days to Expiry: 0-7 days
Meaning: Less than a week remaining
Action: URGENT - Priority 1
        Ensure all documents ready
        Submit immediately if not already done
        Consider emergency amendment if needed
```

**Expiring This Month (High Priority):**
```
Days to Expiry: 8-30 days
Meaning: Expires within current month
Action: High priority
        Monitor shipment status
        Prepare documents
        Plan amendment if shipment delayed
```

**Expiring in 60 Days (Plan Ahead):**
```
Days to Expiry: 31-60 days
Meaning: 1-2 months buffer
Action: Normal monitoring
        Track shipment progress
        Start document collection
```

**Active (Comfortable):**
```
Days to Expiry: 61+ days
Meaning: Plenty of time
Action: Routine monitoring
        No immediate action needed
```

#### The Expiry Chart

**Visual representation:**
```
Bar chart showing count of LCs in each category
X-axis: Status categories
Y-axis: Number of LCs
Colors: Red → Orange → Yellow → Green

Quick visual: See where most LCs are concentrated
Management view: Easy to understand at a glance
```

#### Daily Routine with This Report

**Every Morning:**

1. **Open LC Expiry Report**
2. **Check "Expired" section**
   - Any LCs? → URGENT action needed
3. **Check "Expiring This Week"**
   - List all → Assign to team
   - Check document status for each
   - Expedite any pending items
4. **Check "Expiring This Month"**
   - Review shipment status
   - Flag any potential delays
   - Plan amendments if needed
5. **Export list** if needed for team distribution

**Weekly Planning:**

1. **Run report on Monday**
2. **Focus on "This Month" category**
3. **Assign priorities:**
   - Which need amendments?
   - Which are on track?
   - Which need follow-up?
4. **Schedule team meeting** to discuss critical items
5. **Document actions taken**

#### Best Practices

✅ **Set calendar reminders**
```
30 days before expiry: First alert
15 days before expiry: Second alert
7 days before expiry: Final alert
```

✅ **Create action plan**
```
For each LC expiring in 30 days:
- Shipment status?
- Documents ready?
- Amendment needed?
- Who is responsible?
```

✅ **Communicate proactively**
```
Inform:
- Suppliers (if export)
- Customers (if import)
- Banks (for amendments)
- Internal team (for coordination)
```

✅ **Document reasons**
```
If amendment needed, note why:
- Production delay
- Shipping delay
- Quality issues
- Buyer request
Helps in pattern analysis
```

---

### Report 3: LC Utilization Report

#### Purpose
Financial analysis of how effectively LCs are being used. Your "working capital optimization" tool.

#### When to Use
- **Weekly:** Cash flow monitoring
- **Monthly:** Financial planning
- **Quarterly:** Performance review
- **Budget planning:** Future LC requirements
- **Bank negotiations:** Usage patterns for better terms

#### How to Access
**Method 1:** Workspace → "LC Utilization Report"  
**Method 2:** Search bar → Type report name

#### Using Filters

**From Date & To Date:**
```
Filter by LC opening date
Example: Q1 2024 utilization analysis
```

**Transaction Type:**
```
Import vs Export comparison
See: Which has better utilization?
```

**Currency:**
```
Analyze by currency
Example: USD LC utilization
```

**Status:**
```
Filter by status
Example: Only "Opened" LCs (active)
```

#### Understanding the Report

**Utilization Categories:**

**Not Utilized (0%):**
```
Meaning: LC opened but no shipments yet
Typical: New LCs, delayed shipments
Action: Check shipment plans
Risk: LC expiring without use
```

**Low Utilization (<50%):**
```
Meaning: Less than half LC value used
Typical: Partial shipments in progress
Action: Monitor shipment schedule
Opportunity: Potential to ship more
```

**Moderately Utilized (50-75%):**
```
Meaning: Majority utilized, some balance remains
Typical: Active partial shipments
Action: Plan final shipments
Good: On track for full utilization
```

**Highly Utilized (75-95%):**
```
Meaning: Almost fully used
Typical: Final shipments in progress
Action: Use remaining balance carefully
Note: Good utilization level
```

**Fully Utilized (95-100%+):**
```
Meaning: LC fully or nearly fully used
Typical: All shipments completed
Action: Prepare for settlement
Success: Optimal LC usage
```

**Max Amount (With Tolerance):**
```
Shows: LC Amount + Tolerance Amount
Example: 100,000 + 5% = 105,000
Important: This is true maximum drawable
```

**Utilization %:**
```
Formula: (Utilized / LC Amount) × 100
Note: Can exceed 100% if using tolerance
Example: 105,000 / 100,000 = 105%
```

**Shipment Count:**
```
Number of shipments made
Low count: Large shipments
High count: Many partial shipments
Analysis: Shipping pattern
```

#### Summary Cards (Top of Report)

**Card 1: Total LCs**
```
Count of all LCs in filtered view
Quick: How many LCs am I analyzing?
```

**Card 2: Total LC Value**
```
Sum of all LC amounts
Shows: Total LC commitments
Important: Working capital tied up
```

**Card 3: Total Utilized**
```
Sum of all utilized amounts
Shows: How much has been drawn
Analysis: Actual usage vs commitments
```

**Card 4: Total Balance**
```
Sum of all balance amounts
Shows: Remaining LC capacity
Planning: Available for future shipments
```

**Card 5: Avg Utilization %**
```
Average across all LCs
Benchmark: Is utilization efficient?
Target: Usually aim for 95%+ for efficiency
```

#### The Utilization Chart

**Visual breakdown:**
```
Bar chart by utilization category
See: How many LCs in each category
Analysis: Are most LCs being used well?
Ideal: Most in "Highly" or "Fully" categories
```

#### Analysis Scenarios

**Scenario 1: Working Capital Analysis**
```
Goal: How much capital is locked in LCs?

Steps:
1. Run report for current month
2. Check "Total LC Value" card
3. Check "Total Utilized" card
4. Check "Total Balance" card

Analysis:
Balance = Unused working capital
High balance = Opportunity to:
  - Negotiate better LC terms
  - Reduce LC amounts
  - Improve shipment planning
```

**Scenario 2: Efficiency Check**
```
Goal: Are we using LCs efficiently?

Steps:
1. Run report for last quarter
2. Check "Avg Utilization %" card
3. Look at utilization distribution

Benchmarks:
- >90%: Excellent utilization
- 75-90%: Good utilization
- 60-75%: Moderate (room for improvement)
- <60%: Poor (investigate causes)

Actions:
- If low: Why? Shipment delays? Over-opening?
- Adjust future LC amounts accordingly
```

**Scenario 3: Currency-wise Performance**
```
Goal: Which currency LCs are used better?

Steps:
1. Run report with Currency = USD
2. Note average utilization
3. Repeat for EUR, GBP, etc.
4. Compare

Insights:
- Better utilization in some currencies?
- Plan future LCs accordingly
- Negotiate better terms for high-volume currencies
```

**Scenario 4: Not Utilized LCs**
```
Goal: Identify and fix unused LCs

Steps:
1. Run report
2. Sort by Utilization % (ascending)
3. Check all 0% utilized LCs

Questions:
- Why no shipment?
- Is shipment delayed?
- Should we cancel and reopen?
- Is LC about to expire?

Action:
- Follow up on each
- Amend or cancel if needed
- Prevent expiry without use
```

#### Monthly Utilization Review

**Step-by-step monthly review:**

1. **Run report for previous month**
2. **Note key metrics:**
   - Total LCs opened: _____
   - Total value: _____
   - Avg utilization: _____%
3. **Identify issues:**
   - Any 0% utilized? Why?
   - Any unusually low? Causes?
4. **Compare to previous month:**
   - Utilization improving or declining?
   - Trend analysis
5. **Action items:**
   - Which LCs need attention?
   - Process improvements needed?
6. **Report to management:**
   - Export to Excel
   - Add commentary
   - Share insights

---

### Report 4: LC Charges Analysis

#### Purpose
Understand the true cost of LC operations. Your "cost optimization" tool.

#### When to Use
- **Monthly:** Expense tracking
- **Quarterly:** Cost analysis
- **Annually:** Budget planning
- **Bank review:** Compare bank charges
- **Vendor selection:** Factor LC costs in pricing

#### How to Access
**Method 1:** Workspace → "LC Charges Analysis"  
**Method 2:** Search bar → Type report name

#### Using Filters

**From Date & To Date:**
```
Filter by charge date
Example: Q1 2024 charges
```

**LC Number:**
```
Charges for specific LC
Example: See all costs for LC-IMP-2024-001
```

**Transaction Type:**
```
Import vs Export charge comparison
Which type costs more?
```

**Charge Type:**
```
Specific charge analysis
Example: Only "LC Opening Charge"
Compare opening charges across LCs
```

**Currency:**
```
Analyze charges by currency
Example: USD charges vs INR charges
```

**Issuing Bank:**
```
Compare costs across banks
Example: HDFC vs ICICI charges
Use for bank negotiations
```

#### Understanding the Report

**Key Columns:**

**LC Number:** Which LC this charge belongs to  
**Bank LC Number:** Bank's reference  
**Transaction Type:** Import or Export  
**Charge Type:** What kind of charge  
**Charge Date:** When incurred  
**Currency:** Charge currency  
**Amount:** Charge amount  
**Payment Entry:** Link to payment  
**Journal Entry:** Link to accounting  
**Beneficiary:** Who receives LC payment  
**Issuing Bank:** Bank charging the fee  
**Remarks:** Notes about charge  

#### Summary Cards

**Card 1: Total Charge Entries**
```
Count of all charges
Shows: How many charge transactions
More entries ≠ higher cost (depends on amounts)
```

**Card 2: Total Charges Amount**
```
Sum of all charges
Shows: Total LC cost for period
Critical: True cost of LC operations
```

**Card 3: LCs with Charges**
```
Number of unique LCs that have charges
Analysis: Coverage of charge tracking
```

**Card 4: Avg Charge per LC**
```
Total Charges / Number of LCs
Benchmark: Is cost per LC acceptable?
Compare: Against industry standards
```

**Card 5: Most Common Charge**
```
Which charge type appears most frequently
Insight: Where most costs occur
Opportunity: Focus optimization here
```

#### The Charges Chart

**Visual breakdown:**
```
Bar chart showing total amount by charge type
X-axis: Charge types
Y-axis: Total amount
Sorted: Highest to lowest

Quick view: Which charges cost most
Focus: Optimize the big ones first
```

#### Cost Analysis Scenarios

**Scenario 1: Calculate True LC Cost**
```
Goal: What did this LC really cost?

Steps:
1. Use filter: LC Number = [specific LC]
2. View all charges for that LC
3. Check "Total Charges Amount"

Example:
LC Amount: $100,000
Charges:
- Opening: $150
- Amendment: $75
- Negotiation: $200
- SWIFT: $20
- Documents: $100
Total Charges: $545
True Cost: 0.545% of LC value

Use: Compare against supplier pricing
Factor into product costing
```

**Scenario 2: Bank Comparison**
```
Goal: Which bank offers better rates?

Steps:
1. Run report for HDFC Bank
2. Note average charge per LC
3. Repeat for other banks
4. Compare

Example:
HDFC: Avg $450 per LC
ICICI: Avg $520 per LC
Axis: Avg $380 per LC

Insight: Axis Bank most cost-effective
Action: Negotiate with others or switch
```

**Scenario 3: Charge Type Analysis**
```
Goal: Where are we spending most?

Steps:
1. Run report for year
2. Look at charges chart
3. Identify top 3 charge types

Example findings:
1. Negotiation: $5,200 (40%)
2. Opening: $3,800 (29%)
3. Amendment: $2,100 (16%)
Others: $1,900 (15%)

Insights:
- Negotiation charges high
  Why? Multiple presentations?
  Action: Improve document quality
  
- Amendment charges significant
  Why? Frequent amendments?
  Action: Better planning, realistic timelines
```

**Scenario 4: Monthly Cost Trending**
```
Goal: Are LC costs increasing?

Steps:
1. Run report for Jan 2024
2. Note total charges
3. Repeat for Feb, Mar, etc.
4. Plot trend

Example:
Jan: $2,500
Feb: $2,800
Mar: $3,200
Apr: $3,500

Trend: Increasing
Question: Why?
- More LCs?
- Higher bank charges?
- More amendments?

Action: Investigate and control
```

#### Optimization Strategies

**Strategy 1: Reduce Amendment Charges**
```
Problem: High amendment costs

Root causes:
- Unrealistic timelines
- Poor shipment planning
- Production delays
- Communication gaps

Solutions:
- Add buffer to expiry dates
- Improve shipment forecasting
- Better supplier coordination
- Use realistic LC amounts
```

**Strategy 2: Improve Document Quality**
```
Problem: High negotiation/re-presentation charges

Root causes:
- Document discrepancies
- Missing documents
- Incorrect details
- Late submissions

Solutions:
- Document checklist
- Pre-submission review
- Training for doc preparation
- Use document management system
```

**Strategy 3: Consolidate Banking**
```
Problem: High charges due to multiple banks

Solution:
- Concentrate LCs with one/two banks
- Negotiate volume discounts
- Build relationship for better terms
- Standardize processes
```

**Strategy 4: Negotiate Better Rates**
```
Preparation:
1. Run charges analysis for year
2. Calculate total charges paid
3. Count number of LCs
4. Prepare comparison with other banks

Negotiation points:
- "We paid $25,000 in charges last year"
- "That's 50 LCs averaging $500 each"
- "Competitor bank offers $400 average"
- "Can you match or better this?"

Result: 10-20% savings possible
```

#### Monthly Charges Review Process

**Step 1: Run Report**
```
Filters:
- From Date: First day of month
- To Date: Last day of month
```

**Step 2: Calculate Key Metrics**
```
- Total charges for month: $______
- Number of LCs: ______
- Average per LC: $______
- Most expensive charge type: ______
```

**Step 3: Compare to Budget**
```
Budgeted LC charges: $______
Actual charges: $______
Variance: $______ (over/under)
Variance %: ______%
```

**Step 4: Identify Anomalies**
```
- Any unusually high charges?
- Any unexpected charge types?
- Any charges not linked to payments?
```

**Step 5: Take Action**
```
- Follow up on unpaid charges
- Question unusual charges with bank
- Update budget if needed
- Implement cost controls
```

**Step 6: Report**
```
- Export to Excel
- Add analysis comments
- Share with finance team
- Present in management meetings
```

---

## Workspace Navigation

### Understanding the Workspace

The Letter of Credit workspace is your central hub for all LC operations.

#### Workspace Layout

**Top Section: Header**
```
"Letter of Credit Management"
Your main heading
```

**Section 1: Quick Action Shortcuts**
```
Blue button: Letter of Credit
  - Click to create new LC
  - Direct access to LC list

Orange button: LC Amendment
  - Click to create amendment
  - Direct access to amendments list

Red button: LC Expiry Report
  - Quick access to expiring LCs
  - Most frequently used report
```

**Section 2: Reports**
```
Card: LC Reports
- LC Register
- LC Expiry Report
- LC Utilization Report

Card: LC Analysis
- LC Charges Analysis

Click any report name to open
```

**Section 3: Masters**
```
Links to:
- Letter of Credit (DocType list)
- LC Amendment (DocType list)

Access all documents
```

### Daily Workflow Using Workspace

**Morning Routine:**

1. **Click workspace icon** (☰ in sidebar)
2. **Select "Letter of Credit"**
3. **Click red "LC Expiry Report" button**
4. **Check expiring LCs**
5. **Take action on urgent items**
6. **Return to workspace**

**Creating New LC:**

1. **From workspace**
2. **Click blue "Letter of Credit" button**
3. **Or click "Letter of Credit" under Masters**
4. **Fill in details**
5. **Save and Submit**

**Checking Reports:**

1. **From workspace**
2. **Scroll to Reports section**
3. **Click desired report**
4. **Apply filters**
5. **Analyze results**

### Customizing Workspace (Optional)

**If you want to personalize:**

1. **Open workspace**
2. **Click "Edit" button** (top right)
3. **Drag and drop** to reorder
4. **Add/remove** shortcuts
5. **Save when done**

**Note:** Changes apply only to your view unless you're Workspace Manager

---

## Best Practices

### LC Creation Best Practices

✅ **Always start from Purchase/Sales Order**
- Ensures consistency
- Auto-fills most fields
- Reduces errors
- Links for tracking

✅ **Set realistic timelines**
```
Opening to Expiry: Minimum 60-90 days
Shipment to Expiry: Minimum 15-21 days
Allows time for:
- Production
- Shipment
- Document preparation
- Bank processing
```

✅ **Use standard tolerance**
```
5-10% is industry standard
Too low: Risk of discrepancy
Too high: Risk of over-draw
```

✅ **List ALL required documents**
```
Don't assume - explicitly list
Cross-check with:
- Bank's LC opening advice
- Customer requirements
- Country regulations
```

✅ **Add buffer for expiry dates**
```
Don't set expiry = expected shipment date
Add 15-30 days buffer
Accounts for:
- Unexpected delays
- Document preparation time
- Bank processing time
```

✅ **Document as you go**
```
Don't wait until submission
Update document status regularly
Attach files immediately
Prevents last-minute confusion
```

### Amendment Best Practices

✅ **Plan amendments early**
```
Don't wait until 5 days before expiry
Ideal: 30+ days before expiry
Banks need time to process
```

✅ **Communicate proactively**
```
Inform:
- Bank (for processing)
- Supplier/Customer (for acknowledgment)
- Internal team (for coordination)

Early communication prevents delays
```

✅ **Document the reason**
```
Always fill "Reason for Amendment"
Helps in:
- Audit trail
- Pattern identification
- Process improvement
```

✅ **Track amendment charges**
```
Link amendments to charges
Compare banks' amendment fees
Factor into total cost analysis
```

✅ **One amendment at a time**
```
Don't request multiple major changes together
Easier for bank to process
Clearer documentation
```

### Document Management Best Practices

✅ **Create checklist early**
```
As soon as LC is opened:
1. List all required documents
2. Assign responsibility
3. Set internal deadlines
4. Track progress
```

✅ **Use document templates**
```
Standardize:
- Commercial invoice format
- Packing list format
- Beneficiary certificates

Reduces errors
Speeds preparation
```

✅ **Pre-submission review**
```
Before submitting to bank:
1. Check all documents present
2. Verify quantities match
3. Check descriptions match LC
4. Ensure no discrepancies
5. Get second person to review
```

✅ **Keep digital copies**
```
Scan/attach all documents
Benefits:
- Easy access
- Quick reference
- Audit trail
- No physical storage needed
```

✅ **Track submission timeline**
```
Note:
- When documents ready
- When submitted to bank
- When bank acknowledges
- When bank accepts/rejects
- Response time

Helps identify delays
```

### Shipment Best Practices

✅ **Update immediately**
```
As soon as shipment occurs:
1. Enter shipment details in LC
2. Update utilized amount
3. Check balance
4. Monitor tolerance

Real-time visibility
```

✅ **Link Delivery Notes**
```
Use ERPNext Delivery Notes
Auto-fills shipment data
Ensures consistency
Links to inventory
```

✅ **Verify before adding**
```
Before adding shipment:
- Check partial shipment allowed?
- Will it exceed LC amount + tolerance?
- Is it before latest shipment date?

Prevents compliance issues
```

✅ **Track container/vessel details**
```
Record all shipping details
Useful for:
- Cargo tracking
- Insurance claims
- Customs clearance
- Customer communication
```

### Charges Best Practices

✅ **Record immediately**
```
Don't wait for month-end
Add charges as incurred
Ensures accurate costing
```

✅ **Link to payments**
```
Always link charges to Payment Entry
Benefits:
- Complete financial trail
- Easy reconciliation
- Audit compliance
```

✅ **Review monthly**
```
Run LC Charges Analysis monthly
Check for:
- Unusual charges
- Missing payments
- Cost trends
- Optimization opportunities
```

✅ **Budget and forecast**
```
Use historical data
Calculate average charge per LC
Factor into pricing
Budget for future LCs
```

✅ **Negotiate annually**
```
Armed with annual charges data:
- Negotiate better rates
- Seek volume discounts
- Compare banks
- Build relationship
```

### Reporting Best Practices

✅ **Daily: LC Expiry Report**
```
First thing every morning
Check expiring LCs
Assign priorities
Take action
```

✅ **Weekly: LC Register**
```
Review all active LCs
Check status progression
Identify stuck items
Follow up
```

✅ **Monthly: All Reports**
```
- LC Register: Month summary
- Utilization: Efficiency check
- Charges: Cost analysis
- Expiry: Forward planning

Package for management
```

✅ **Quarterly: Deep Analysis**
```
- Trends over 3 months
- Compare quarters
- Identify patterns
- Strategic planning
```

✅ **Export and analyze**
```
Don't just view reports
Export to Excel for:
- Custom analysis
- Charts/graphs
- Sharing
- Archiving
```

### General Best Practices

✅ **Train your team**
```
Everyone should understand:
- What is an LC
- How system works
- Their responsibilities
- Who to escalate to
```

✅ **Document procedures**
```
Create SOPs for:
- Creating LCs
- Managing amendments
- Document submission
- Charge recording

Ensures consistency
```

✅ **Regular audits**
```
Monthly/quarterly:
- Review all open LCs
- Check for stale items
- Verify all charges recorded
- Ensure documents attached
```

✅ **Backup and archive**
```
Regular backups of system
Export critical reports
Store documents off-system too
Disaster recovery planning
```

✅ **Continuous improvement**
```
Quarterly review:
- What went wrong?
- What can be improved?
- Update processes
- Train team on changes
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Cannot Submit LC

**Symptoms:**
- Submit button grayed out
- Error message when submitting

**Possible Causes & Solutions:**

**Cause 1: Mandatory fields missing**
```
Solution:
1. Check for red asterisk (*) fields
2. Fill in all required fields:
   - LC Number
   - LC Type
   - Transaction Type
   - LC Date
   - Expiry Date
   - Applicant
   - Beneficiary
   - Issuing Bank
   - Currency
   - LC Amount
   - Payment Terms
3. Save and try submit again
```

**Cause 2: Date validation error**
```
Solution:
1. Check Expiry Date > LC Date
2. Check Latest Shipment Date ≤ Expiry Date
3. Correct dates
4. Save and submit
```

**Cause 3: Permission issue**
```
Solution:
1. Check your role
2. Only Accounts Manager/User can submit
3. Contact system administrator
4. Request Submit permission
```

#### Issue 2: Utilization Amount Not Updating

**Symptoms:**
- Added shipment but Utilized Amount unchanged
- Balance Amount incorrect

**Solutions:**

**Solution 1: Save the document**
```
After adding/editing shipments:
1. Click Save button
2. System recalculates on save
3. Check Utilized and Balance amounts
```

**Solution 2: Check shipment values**
```
1. Open Shipments table
2. Verify "Shipped Value" filled
3. Numeric values only
4. No text or special characters
5. Save
```

**Solution 3: Refresh the