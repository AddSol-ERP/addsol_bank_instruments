# BG Management - Features Documentation

**Version:** 1.0  
**Module:** BG Management  
**App:** addsol_lc  
**Compatible with:** ERPNext 15.x  
**Date:** January 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Core Features](#core-features)
3. [Financial Management Features](#financial-management-features)
4. [Extension & Renewal Features](#extension--renewal-features)
5. [Document Management Features](#document-management-features)
6. [Automation Features](#automation-features)
7. [Reporting & Analytics Features](#reporting--analytics-features)
8. [Integration Features](#integration-features)
9. [Security & Compliance Features](#security--compliance-features)
10. [User Interface Features](#user-interface-features)

---

## Overview

BG Management is a comprehensive Bank Guarantee management module for ERPNext 15 that provides end-to-end lifecycle management of bank guarantees. Built as a custom DocType to complement ERPNext's standard Bank Guarantee functionality, it offers advanced features for tracking FDs, extensions, claims, and comprehensive reporting.

**Key Differentiators:**
- Named "BG Management" to avoid conflicts with ERPNext's standard Bank Guarantee DocType
- Professional-grade FD tracking with full financial visibility
- Automated expiry notifications and status management
- Complete audit trail with extension history
- Multi-document attachment capability

---

## Core Features

### 1. Comprehensive Bank Guarantee Tracking

**BG Information Management**
- **Unique BG Number**: Auto-naming based on BG number field
- **Multiple BG Types**: 
  - Performance Bank Guarantee
  - Bid Bond Guarantee
  - Advance Payment Guarantee
  - Retention Money Guarantee
  - Financial Guarantee
  - Payment Guarantee
  - Warranty Guarantee
- **Custom BG Types**: Easily add more types as needed

**Party Information**
- **Beneficiary Management**: Link to Customer, Supplier, or other party types
- **Dynamic Linking**: Automatic beneficiary name fetching
- **Applicant Tracking**: Company-wise segregation
- **Project Linking**: Associate BGs with specific projects
- **Reference Linking**: Connect to Purchase Orders or Sales Orders

**Status Lifecycle Management**
- **Active**: Currently valid and enforceable
- **Extended**: BG has been extended with new expiry date
- **Expired**: Past expiry date
- **Claimed**: Beneficiary has invoked the guarantee
- **Closed**: Normally completed without claim
- **Cancelled**: Cancelled before expiry
- **Auto Status Updates**: System automatically updates status based on dates

### 2. Comprehensive Date Tracking

**Primary Dates**
- **Issue Date**: When BG was issued
- **Expiry Date**: Original expiry date
- **Claim Date**: Date when BG was claimed (if applicable)
- **FD Maturity Date**: When underlying FD matures

**Extension Dates**
- **Extension Expiry Date**: New expiry after extension
- **Extension Claim Date**: Claim date for extended period
- **Multiple Extensions**: Track unlimited extensions with history

**Calculated Fields**
- **Days to Expiry**: Auto-calculated remaining days
- **Extension Days**: Calculated for each extension

---

## Financial Management Features

### 3. Fixed Deposit (FD) Tracking

**Complete FD Information**
- **FD Number**: Unique FD reference
- **FD Amount**: Original fixed deposit amount
- **Maturity Amount**: Expected amount at maturity
- **Maturity Date**: When FD matures

**Utilization Tracking**
- **Utilized Amount**: Amount already claimed/used
- **Available Amount**: Auto-calculated (Maturity Amount - Utilized Amount)
- **Real-time Calculations**: Updates automatically

**Validation**
- Ensures utilized amount doesn't exceed maturity amount
- Validates FD maturity date is on/after BG expiry date
- Prevents invalid data entry

### 4. Charges & Commission Management

**Commission Calculation**
- **Commission Rate**: Percentage-based commission
- **Commission Amount**: Auto-calculated based on FD amount × rate
- **Real-time Updates**: Recalculates on any change

**Other Charges**
- **Processing Charges**: One-time or recurring charges
- **Extension Charges**: Tracked separately for each extension
- **Total Charges**: Automatically summed

**Financial Visibility**
- Complete cost breakdown
- Historical charge tracking
- Extension-specific charges in child table

### 5. Bank Information

**Bank Details**
- **Issuing Bank**: Link to Bank master
- **Bank Account**: Specific account used
- **Filtered Selection**: Bank account dropdown filtered by selected bank

---

## Extension & Renewal Features

### 6. Extension Management

**Extension Tracking**
- **Unlimited Extensions**: No limit on number of extensions
- **Extension History Child Table**: Complete audit trail
- **Extension Number**: Auto-numbered sequentially
- **Previous Expiry Date**: Records original expiry
- **New Expiry Date**: Updated expiry date
- **Extension Days**: Auto-calculated duration

**Extension Details**
- **Extension Date**: When extension was processed
- **Extension Charges**: Cost of extension
- **Approved By**: User who approved extension
- **Remarks**: Notes for each extension

**Extension Process**
- **Custom Button**: "Extend BG" in Actions menu
- **Interactive Dialog**: User-friendly extension form
- **Validation**: Ensures new date is after current expiry
- **Auto-Update**: Updates main document fields
- **Status Change**: Automatically sets status to "Extended"

### 7. Extension History

**Child Table Features**
- **Complete Audit Trail**: All extensions recorded
- **Sequential Numbering**: Extension #1, #2, #3, etc.
- **Date Tracking**: Previous and new expiry dates
- **Financial Record**: Extension charges for each
- **Approval Tracking**: Who approved each extension
- **Remarks**: Context for each extension

**Benefits**
- Full transparency
- Historical reference
- Compliance documentation
- Easy auditing

---

## Document Management Features

### 8. Multi-Document Attachment System

**Primary Documents**
- **BG Document**: Main bank guarantee document
- **FD Receipt**: Fixed deposit receipt
- **Direct Upload**: Attach files directly to main form

**Supporting Documents Child Table**
- **Multiple Documents**: Unlimited supporting files
- **Document Types**:
  - BG Application
  - BG Approval Letter
  - FD Certificate
  - Renewal Letter
  - Closure Letter
  - Claim Letter
  - Other
- **Document Name**: Custom naming for each file
- **Upload Date**: Automatic date tracking
- **Remarks**: Notes for each document

**Document Features**
- Organized storage
- Easy retrieval
- Type-based categorization
- Complete documentation history

---

## Automation Features

### 9. Automatic Status Management

**Rule-Based Status Updates**
- **On Document Save**: Status recalculates automatically
- **Expiry Check**: Sets to "Expired" when past expiry date
- **Extension Detection**: Sets to "Extended" when extension added
- **Claim Detection**: Sets to "Claimed" when claim date entered
- **Utilization Check**: Sets to "Closed" when fully utilized

**Manual Status Control**
- Close BG via custom button
- Cancel via standard ERPNext workflow
- Override when necessary

### 10. Automated Notifications

**Daily Scheduler**
- **Runs Daily**: Automated background job
- **Multi-Level Alerts**: Notifications at different thresholds
- **Configurable**: Easy to modify notification days

**Notification Thresholds**
- 30 days before expiry
- 15 days before expiry
- 7 days before expiry
- 3 days before expiry
- 1 day before expiry

**Email Features**
- **Recipients**: All users with "Accounts Manager" role
- **Email Content**:
  - BG Number
  - BG Type
  - Beneficiary name
  - Expiry date
  - Days remaining
  - FD amount
- **Professional Format**: HTML formatted emails
- **Reference Link**: Links back to BG document

**Additional Notifications**
- On BG submission
- On BG cancellation
- On claim
- On closure

### 11. Auto-Calculations

**Real-Time Calculations**
- **Days to Expiry**: 
  - Based on current date vs expiry/extension date
  - Updates on form load
  - Considers extended dates
  
- **Available Amount**:
  - Maturity Amount - Utilized Amount
  - Updates when either field changes
  - Displayed prominently
  
- **Commission Amount**:
  - FD Amount × Commission Rate / 100
  - Recalculates instantly
  
- **Total Charges**:
  - Commission Amount + Processing Charges
  - Auto-sums all charges

**Extension Calculations**
- Extension days automatically calculated
- Extension number auto-incremented
- Previous expiry captured automatically

---

## Reporting & Analytics Features

### 12. Active BG Management Report

**Comprehensive Filtering**
- **Company**: Filter by organization
- **Date Range**: From date and to date
- **Bank**: Specific bank filter
- **BG Type**: Filter by guarantee type
- **Status**: Active, Extended, Expired, etc.
- **Beneficiary**: Party-wise filtering
- **Project**: Project-specific view
- **Expiring in Days**: Special filter for urgent BGs

**Report Columns**
- BG Number (clickable link)
- Type of BG
- Beneficiary name
- Status
- Issue Date
- Expiry Date
- Days to Expiry
- FD Amount
- Maturity Amount
- Utilized Amount
- Available Amount
- Bank
- Project

**Visual Analytics**
- **Donut Chart**: BG distribution by status
- **Color Coding**: Visual status indicators
- **Report Summary**: Key metrics at top

**Summary Metrics**
- Total number of BGs
- Total FD Amount
- Total Maturity Amount
- Total Utilized Amount
- Total Available Amount
- Number of BGs expiring in 30 days

**Export Options**
- PDF export
- Excel export
- Print view
- CSV download

### 13. Dashboard Indicators

**Form-Level Indicators**
- **Status Badge**: Color-coded status display
  - Green: Active
  - Blue: Extended
  - Red: Expired
  - Orange: Claimed
  - Gray: Closed
  - Dark Gray: Cancelled

**Alert Messages**
- Red alert: Expired
- Red alert: Expiring in 7 days or less
- Orange alert: Expiring in 8-15 days
- Yellow alert: Expiring in 16-30 days

**Visual Feedback**
- Dashboard comments
- Color-coded warnings
- Days remaining display

---

## Integration Features

### 14. ERPNext Module Integration

**Sales Module**
- Link to Sales Order
- Track customer BGs
- Order-wise BG view

**Buying Module**
- Link to Purchase Order
- Track supplier BGs
- PO-wise BG view

**Projects Module**
- Link to Project
- Project-wise BG tracking
- Multi-BG per project

**Accounts Module**
- Bank master integration
- Bank Account linking
- Journal Entry creation (optional)
- Commission accounting

**CRM Module**
- Customer/Supplier linking
- Party-wise BG history
- Relationship tracking

### 15. Custom App Integration

**Letter of Credit Module**
- Easy linking to existing LC module
- Add LC reference field
- Cross-reference capabilities
- Unified financial instrument tracking

**Extensibility**
- Custom field support
- Server script hooks
- Client script customization
- Workflow integration

---

## Security & Compliance Features

### 16. Permission Management

**Role-Based Access**
- **Accounts Manager**: Full control
  - Create, Read, Write, Delete
  - Submit, Cancel, Amend
  
- **Accounts User**: Limited access
  - Create, Read, Write
  - Submit only

**Customizable Permissions**
- Add more roles as needed
- Field-level permissions possible
- Document-level restrictions

### 17. Audit Trail

**Change Tracking**
- **Track Changes**: Enabled by default
- **Version History**: All changes logged
- **User Tracking**: Who made what change
- **Timestamp**: When changes occurred

**Extension History**
- Complete extension audit trail
- Approved by tracking
- Date and amount tracking
- Remarks for context

**Submission Workflow**
- **Submittable**: Cannot edit after submit
- **Amendment**: Version control via amend
- **Cancellation**: Proper cancellation workflow
- **Status History**: Status change tracking

### 18. Data Validation

**Mandatory Field Validation**
- BG Number required
- BG Type required
- Bank required
- FD Amount required
- Maturity Amount required
- Issue Date required
- Expiry Date required
- FD Maturity Date required

**Business Logic Validation**
- Expiry date must be after issue date
- FD maturity must be on/after BG expiry
- Extension date must be after current expiry
- Utilized amount cannot exceed maturity amount
- BG document required before submission
- FD number required before submission

**Data Integrity**
- Unique BG numbers
- Referential integrity with linked documents
- Proper date sequencing
- Financial validation

---

## User Interface Features

### 19. Form Layout

**Organized Sections**
- **Basic Details**: BG Number, Type, Status
- **Party Details**: Beneficiary, Applicant, References
- **Financial Details**: Bank, FD, Amounts
- **Date Details**: All date fields
- **Extension Details**: Extension information (collapsible)
- **Charges & Commission**: Financial charges
- **Documents & Attachments**: File management
- **Remarks**: Notes and internal comments

**Smart Field Arrangement**
- **Column Breaks**: Efficient use of screen space
- **Grouped Fields**: Related fields together
- **Collapsible Sections**: Extension details hidden when not used
- **Conditional Display**: Extension fields show only when extended

### 20. Custom Buttons

**Action Buttons (When Submitted)**
- **Extend BG**: Launch extension dialog
- **Mark as Claimed**: Record claim
- **Close BG**: Normal closure
- **Create Journal Entry**: Accounting integration

**Button Visibility**
- Context-aware display
- Only shown when applicable
- Status-based availability

**Interactive Dialogs**
- User-friendly forms
- Field validation
- Help text
- Default values

### 21. Smart Field Behaviors

**Auto-Fetch**
- Beneficiary name from party
- Bank account filtered by bank
- Default issue date (Today)
- Default status (Active)

**Dependent Fields**
- Extension fields depend on "Is Extended"
- Bank account depends on bank
- Dynamic link beneficiary depends on type

**Read-Only Fields**
- Status (system managed)
- Available Amount (calculated)
- Days to Expiry (calculated)
- Commission Amount (calculated)
- Total Charges (calculated)
- Extension Number (auto-generated)
- Extension Days (calculated)

**Conditional Formatting**
- Currency fields
- Date fields
- Percentage fields
- Link fields with auto-complete

---

## Advanced Features

### 22. Multi-Company Support

**Company-Wise Segregation**
- Default company from user settings
- Filter BGs by company
- Company-wise reporting
- Multi-company installations supported

### 23. Search & Filter

**Quick Search**
- BG Number
- Beneficiary
- BG Type
- Status

**Standard Filters**
- Pre-defined filter fields
- Quick access filters
- List view filtering

**Advanced Filters**
- Custom filter creation
- Multiple condition filters
- Save custom filters
- Share filters with team

### 24. List View Features

**Customized List View**
- **Visible Columns**:
  - BG Number
  - BG Type
  - Status
  - FD Number
  
**List Features**
- Color-coded status indicators
- Quick edit
- Bulk actions
- Sort by any field
- Filter on any field

### 25. Print Formats

**Standard Print**
- Professional BG print format
- Company letterhead
- All relevant details
- Signature blocks

**Customizable**
- Create custom print formats
- Jinja template support
- Add company branding
- Multiple print formats

---

## Performance Features

### 26. Optimization

**Database Indexing**
- Indexed on BG Number
- Indexed on Status
- Indexed on Expiry Date
- Fast search performance

**Efficient Queries**
- Optimized SQL queries
- Minimal database calls
- Cached lookups where applicable

### 27. Scalability

**Large Dataset Handling**
- Efficient for 1000+ BGs
- Pagination in list view
- Filtered reports
- Archive old records

**Background Jobs**
- Scheduler for notifications
- Non-blocking operations
- Queue management

---

## Mobile Features

### 28. Mobile Compatibility

**Responsive Design**
- Mobile-friendly forms
- Touch-optimized
- Responsive tables
- Mobile navigation

**ERPNext Mobile App**
- Full functionality in mobile app
- Create/edit BGs on mobile
- View reports on mobile
- Receive notifications

---

## Customization Features

### 29. Extensibility

**Custom Fields**
- Add fields via Customize Form
- No code modification needed
- Preserve on updates

**Custom Scripts**
- Client Script support
- Server Script support
- Custom API methods
- Webhook integration

**Custom Reports**
- Create derivative reports
- Script Report framework
- Query Report option
- Report Builder compatibility

### 30. Configuration

**System Configuration**
- Notification day thresholds (configurable in code)
- BG Types (easily add more)
- Document types (expandable list)
- Email templates (customizable)

**Workflow Configuration**
- Optional workflow states
- Approval routing
- Email actions
- Auto-assignments

---

## Support Features

### 31. Documentation

**In-App Help**
- Field descriptions
- Help text
- User manual reference
- Context-sensitive help

**External Documentation**
- Features document (this file)
- Quick Start Guide
- User Manual
- Implementation Guide

### 32. Error Handling

**User-Friendly Messages**
- Clear validation messages
- Helpful error descriptions
- Actionable suggestions

**Error Logging**
- System errors logged
- Email errors logged
- Scheduler errors logged
- Debug information available

---

## Compliance Features

### 33. Regulatory Compliance

**Audit Requirements**
- Complete change history
- User action tracking
- Document versioning
- Timestamp all changes

**Financial Compliance**
- Accurate financial tracking
- Commission transparency
- Charge documentation
- FD reconciliation support

### 34. Data Retention

**Archive Support**
- Closed BGs can be archived
- Historical data preserved
- Compliance with retention policies
- Easy retrieval when needed

---

## Comparison with ERPNext Standard Bank Guarantee

| Feature | ERPNext Standard | BG Management (Custom) |
|---------|-----------------|----------------------|
| **Naming** | Bank Guarantee | BG Management |
| **FD Tracking** | Basic (FD Number only) | Complete (Number, Amount, Maturity, Utilization) |
| **Extension Management** | Not available | Full extension history with child table |
| **Auto Notifications** | Manual email alert setup | Built-in automated alerts (30/15/7/3/1 days) |
| **Document Management** | Single attachment | Multiple documents with child table |
| **Status Tracking** | Basic status | 6 detailed statuses with auto-updates |
| **Commission Calculation** | Not available | Auto-calculated with rates |
| **Days to Expiry** | Not tracked | Auto-calculated and displayed |
| **Project Linking** | Not available | Full project integration |
| **Available Amount** | Not calculated | Real-time calculation |
| **Extension History** | Not tracked | Complete audit trail |
| **Custom Actions** | Standard | Extend/Claim/Close buttons |
| **Reports** | Basic | Advanced with charts and analytics |
| **Utilized Amount** | Not tracked | Fully tracked and validated |

---

## Future Enhancement Possibilities

### Potential Future Features
1. **SMS Notifications** - Twilio integration for SMS alerts
2. **Document OCR** - Auto-extract BG data from scanned documents
3. **Bank API Integration** - Fetch FD rates and status automatically
4. **Multi-level Approvals** - Workflow for high-value BGs
5. **Advanced Analytics** - Trend analysis and predictive alerts
6. **Mobile Push Notifications** - Real-time mobile alerts
7. **Automatic Renewal Requests** - 60/90 day advance renewal reminders
8. **Integration with Treasury Management** - Cash flow planning
9. **Risk Assessment** - Automatic risk scoring
10. **Blockchain Integration** - Immutable audit trail

---

## Technical Specifications

**Platform Requirements**
- ERPNext: Version 15.x
- Frappe Framework: Version 15.x
- Python: 3.10+
- MariaDB/PostgreSQL: As per ERPNext requirements

**Browser Support**
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

**Server Requirements**
- As per ERPNext standard requirements
- Additional storage for documents
- Email server for notifications

---

## Summary

BG Management provides a complete, professional-grade Bank Guarantee management solution with:

✅ **31 Major Features** across 10 categories  
✅ **Automated workflows** and notifications  
✅ **Complete audit trail** and compliance  
✅ **Advanced reporting** with visual analytics  
✅ **Seamless integration** with ERPNext modules  
✅ **User-friendly interface** with smart behaviors  
✅ **Scalable architecture** for growing businesses  
✅ **Customizable** and extensible framework  

Perfect for organizations managing multiple bank guarantees with complex requirements for tracking, reporting, and compliance.

---

**Document Version:** 1.0  
**Last Updated:** January 2025  
**Maintained By:** Implementation Team  
**Contact:** support@yourcompany.com