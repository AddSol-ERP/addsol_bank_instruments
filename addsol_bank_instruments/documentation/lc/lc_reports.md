# LC Reports Guide

## Overview

The Bank Instruments Management app provides four comprehensive reports for Letters of Credit (LC) that offer detailed insights into LC operations, utilization, expiry monitoring, and cost analysis. These reports help businesses make informed decisions, maintain compliance, and optimize their LC management processes.

## Available LC Reports

### 1. LC Register

**Purpose**: Provides a complete register of all Letters of Credit with their current status and key details.

**Key Features**:
- Complete listing of all submitted LCs
- Real-time status tracking
- Utilization and balance information
- Multi-dimensional filtering capabilities
- Export functionality for external reporting

**Report Columns**:
- **LC Number**: Internal system reference (Link to LC document)
- **Bank LC Number**: Bank-assigned LC reference number
- **Type**: Import or Export transaction type
- **LC Type**: LC category (Sight, Usance, Deferred, etc.)
- **LC Date**: Date of LC issuance
- **Expiry Date**: LC expiry date
- **Applicant**: LC applicant (Dynamic Link)
- **Beneficiary**: LC beneficiary (Dynamic Link)
- **Currency**: LC currency
- **LC Amount**: Original LC amount
- **Utilized Amount**: Amount currently utilized
- **Balance Amount**: Remaining available balance
- **Utilization %**: Percentage of LC utilized
- **Status**: Current LC status
- **Issuing Bank**: Name of issuing bank
- **Purchase Order**: Linked Purchase Order (if applicable)
- **Sales Order**: Linked Sales Order (if applicable)

**Available Filters**:
- **From Date/To Date**: Filter by LC creation date range
- **Transaction Type**: Import/Export filter
- **LC Type**: Filter by LC category
- **Status**: Filter by current status
- **Currency**: Filter by currency
- **Issuing Bank**: Filter by bank name
- **Applicant**: Filter by applicant
- **Beneficiary**: Filter by beneficiary

**Use Cases**:
- Complete LC portfolio overview
- Status tracking across all LCs
- Compliance reporting
- Audit trail generation
- Performance analysis by bank or type

---

### 2. LC Utilization Report

**Purpose**: Analyzes LC utilization patterns, balances, and shipment activity with visual charts and summary metrics.

**Key Features**:
- Utilization percentage analysis
- Tolerance-based calculations
- Shipment tracking integration
- Visual utilization distribution chart
- Summary cards with key metrics
- Utilization status categorization

**Report Columns**:
- **LC Number**: Internal system reference
- **Bank LC Number**: Bank-assigned reference
- **Type**: Import/Export transaction type
- **Beneficiary**: LC beneficiary name
- **Currency**: LC currency
- **LC Amount**: Original LC amount
- **Tolerance %**: Allowed tolerance percentage
- **Max Amount (With Tolerance)**: Maximum utilizable amount including tolerance
- **Utilized Amount**: Current utilized amount
- **Balance Amount**: Remaining balance
- **Utilization %**: Current utilization percentage
- **Utilization Status**: Categorized utilization level
- **Shipments**: Number of shipments linked to LC
- **Status**: Current LC status

**Utilization Status Categories**:
- **Not Utilized**: 0% utilization
- **Low Utilization**: < 50% utilization
- **Moderately Utilized**: 50-74% utilization
- **Highly Utilized**: 75-99% utilization
- **Fully Utilized**: 100%+ utilization (including tolerance)

**Available Filters**:
- **From Date/To Date**: Filter by LC date range
- **Transaction Type**: Import/Export filter
- **Currency**: Filter by currency
- **Utilization Status**: Filter by utilization category
- **Status**: Filter by LC status

**Visual Elements**:
- **Bar Chart**: Distribution of LCs by utilization status
- **Summary Cards**: Total LCs, amounts, utilization metrics

**Use Cases**:
- Monitor LC efficiency and utilization
- Identify underutilized LCs for optimization
- Cash flow planning based on available balances
- Performance analysis by transaction type
- Tolerance compliance monitoring

---

### 3. LC Expiry Report

**Purpose**: Monitors LC expiry dates and provides early warnings for upcoming expirations to prevent lapses.

**Key Features**:
- Days-to-expiry calculation
- Expiry status categorization
- Early warning system
- Visual expiry distribution
- Default 90-day expiry horizon
- Balance amount tracking for expiring LCs

**Report Columns**:
- **LC Number**: Internal system reference
- **Bank LC Number**: Bank-assigned reference
- **Type**: Import/Export transaction type
- **Applicant**: LC applicant name
- **Beneficiary**: LC beneficiary name
- **LC Date**: Date of LC issuance
- **Expiry Date**: LC expiry date
- **Days to Expiry**: Calculated days remaining
- **Expiry Status**: Categorized expiry urgency
- **LC Amount**: Original LC amount
- **Balance Amount**: Remaining unutilized amount
- **Status**: Current LC status
- **Issuing Bank**: Name of issuing bank

**Expiry Status Categories**:
- **Expired**: Already expired (negative days)
- **Expiring This Week**: 7 days or less
- **Expiring This Month**: 30 days or less
- **Expiring in 60 Days**: 60 days or less
- **Active**: More than 60 days remaining

**Available Filters**:
- **Expiry Status**: Filter by expiry category
- **Transaction Type**: Import/Export filter
- **Issuing Bank**: Filter by bank name
- **Show All**: Include all LCs regardless of expiry date

**Visual Elements**:
- **Bar Chart**: Distribution of LCs by expiry status
- **Color Coding**: Red (expired) to Green (active)

**Use Cases**:
- Proactive expiry management
- Renewal planning and scheduling
- Risk mitigation for expired LCs
- Cash flow impact assessment
- Compliance with LC terms

---

### 4. LC Charges Analysis

**Purpose**: Tracks and analyzes all charges associated with LCs including commissions, processing fees, and other costs.

**Key Features**:
- Comprehensive charge tracking
- Charge type categorization
- Payment entry integration
- Visual charge distribution
- Cost analysis by charge type
- Average charge calculations

**Report Columns**:
- **LC Number**: Internal system reference
- **Bank LC Number**: Bank-assigned reference
- **Type**: Import/Export transaction type
- **Charge Type**: Category of charge (Commission, Processing, etc.)
- **Charge Date**: Date charge was incurred
- **Currency**: Charge currency
- **Amount**: Charge amount
- **Payment Entry**: Linked payment entry
- **Journal Entry**: Linked journal entry
- **Beneficiary**: LC beneficiary name
- **Issuing Bank**: Name of issuing bank
- **Remarks**: Additional charge details

**Available Filters**:
- **From Date/To Date**: Filter by charge date range
- **Transaction Type**: Import/Export filter
- **Charge Type**: Filter by charge category
- **Currency**: Filter by currency
- **Issuing Bank**: Filter by bank name
- **LC Number**: Filter by specific LC

**Visual Elements**:
- **Bar Chart**: Charge distribution by type
- **Summary Cards**: Total charges, averages, most common charges

**Use Cases**:
- Cost analysis and budgeting
- Bank charge comparison
- Expense tracking and allocation
- Profitability analysis
- Negotiation support with banks

## Report Access and Permissions

### Required Roles
- **Accounts Manager**: Full access to all LC reports
- **Accounts User**: Read access to LC reports
- **Purchase Manager**: Access to Import LC reports
- **Sales Manager**: Access to Export LC reports

### Navigation
1. Go to **Bank Instruments** workspace
2. Click on **Reports** section
3. Select desired LC report from the list
4. Apply filters as needed
5. View, export, or print the report

## Export and Integration

### Export Options
- **Excel**: Full data export with formatting
- **PDF**: Formatted report for printing/sharing
- **CSV**: Raw data export for analysis

### Integration Features
- **Real-time Data**: Reports show current data from LC documents
- **Drill-down**: Click on LC numbers to view full document
- **Linked Documents**: Access related orders and shipments
- **Email Reports**: Schedule and email automated reports

## Best Practices

### Regular Report Review
1. **LC Register**: Weekly review for status updates
2. **Utilization Report**: Monthly analysis for efficiency
3. **Expiry Report**: Weekly check for upcoming expiries
4. **Charges Analysis**: Monthly cost review

### Filter Optimization
- Use date ranges to focus on relevant periods
- Combine filters for targeted analysis
- Save frequently used filter combinations

### Performance Tips
- Limit date ranges for large datasets
- Use specific filters to reduce processing time
- Export during off-peak hours for large reports

## Troubleshooting

### Common Issues
- **No Data Display**: Check filter settings and date ranges
- **Slow Loading**: Reduce date range or add specific filters
- **Missing LCs**: Verify LC submission status (docstatus = 1)
- **Incorrect Calculations**: Refresh report or check LC document data

### Data Validation
- Cross-check totals with LC documents
- Verify currency conversions
- Validate tolerance calculations
- Confirm charge allocations

## Report Customization

### Custom Filters
Add custom filters through report builder:
1. Open report in Edit mode
2. Add new filter fields
3. Update SQL conditions
4. Test and save changes

### Custom Columns
Modify report columns as needed:
1. Edit report columns array
2. Update SQL query
3. Adjust formatting and calculations
4. Test display and functionality

### Custom Charts
Create custom visualizations:
1. Modify chart data functions
2. Update chart types and colors
3. Add new chart datasets
4. Test chart rendering

## Support and Training

### Additional Resources
- [LC User Manual](lc_user_manual.md) - Detailed LC management guide
- [LC Features](lc_app_features.md) - Complete feature documentation
- [Quick Start Guide](lc_quick_start.md) - Getting started with LCs

### Training Recommendations
- Basic report navigation for all users
- Advanced filtering for power users
- Export and integration training for administrators
- Custom report development for technical users

---

*For technical support or feature requests, please refer to the main app documentation or contact your system administrator.*
