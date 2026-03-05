# BG Reports Guide

## Overview

The Bank Instruments Management app provides four comprehensive reports for Bank Guarantees (BG) that deliver detailed insights into BG operations, utilization, expiry monitoring, and charges analysis. These reports help businesses effectively manage their guarantee portfolio, maintain compliance, and optimize financial planning.

## Available BG Reports

### 1. BG Register

**Purpose**: Provides a complete register of all Bank Guarantees with their current status, fixed deposit details, and key information.

**Key Features**:
- Complete listing of all submitted BGs
- Real-time status tracking
- Fixed deposit and maturity amount tracking
- Utilization and availability monitoring
- Multi-dimensional filtering capabilities
- Days-to-expiry calculation
- Integration with projects and orders

**Report Columns**:
- **BG Number**: Internal system reference (Link to BG document)
- **BG Type**: Guarantee category (Performance, Financial, etc.)
- **Applicant**: BG applicant name
- **Beneficiary**: BG beneficiary name
- **Issue Date**: Date of BG issuance
- **Expiry Date**: BG expiry date
- **Days to Expiry**: Calculated days remaining until expiry
- **FD Number**: Fixed Deposit account number
- **FD Amount**: Original Fixed Deposit amount
- **Maturity Amount**: FD maturity amount (including interest)
- **Utilized Amount**: Amount currently utilized against guarantee
- **Available Amount**: Remaining available guarantee amount
- **Status**: Current BG status
- **Issuing Bank**: Name of issuing bank
- **Project**: Linked Project (if applicable)
- **Sales Order**: Linked Sales Order (if applicable)
- **Purchase Order**: Linked Purchase Order (if applicable)

**Available Filters**:
- **From Date/To Date**: Filter by BG issue date range
- **BG Type**: Filter by guarantee category
- **Status**: Filter by current status
- **Bank**: Filter by issuing bank name

**Use Cases**:
- Complete BG portfolio overview
- Status tracking across all guarantees
- Fixed deposit utilization monitoring
- Compliance and audit reporting
- Performance analysis by guarantee type
- Bank relationship management

---

### 2. BG Utilization Report

**Purpose**: Analyzes BG utilization patterns, available amounts, and guarantee performance with visual charts and comprehensive metrics.

**Key Features**:
- Utilization percentage analysis based on maturity amounts
- Available guarantee tracking
- Extension history consideration
- Visual utilization distribution chart
- Summary cards with key performance indicators
- Utilization status categorization
- Claim tracking integration

**Report Columns**:
- **BG Number**: Internal system reference
- **BG Type**: Guarantee category
- **Beneficiary**: BG beneficiary name
- **Issue Date**: Date of BG issuance
- **Expiry Date**: BG expiry date
- **FD Amount**: Original Fixed Deposit amount
- **Maturity Amount**: Total maturity amount including interest
- **Utilized Amount**: Current utilized amount
- **Available Amount**: Remaining available guarantee amount
- **Utilization %**: Percentage of guarantee utilized
- **Utilization Status**: Categorized utilization level
- **Claims**: Number of claims against the BG
- **Status**: Current BG status
- **Issuing Bank**: Name of issuing bank

**Utilization Status Categories**:
- **Not Utilized**: 0% utilization
- **Low Utilization**: < 50% utilization
- **Moderately Utilized**: 50-74% utilization
- **Highly Utilized**: 75-99% utilization
- **Fully Utilized**: 100% utilization

**Available Filters**:
- **From Date/To Date**: Filter by BG issue date range
- **BG Type**: Filter by guarantee category
- **Currency**: Filter by currency (if applicable)
- **Utilization Status**: Filter by utilization category
- **Status**: Filter by BG status

**Visual Elements**:
- **Bar Chart**: Distribution of BGs by utilization status
- **Summary Cards**: Total BGs, amounts, utilization metrics

**Key Metrics**:
- **Total BGs**: Number of guarantees in report
- **Total Maturity Amount**: Sum of all maturity amounts
- **Total Utilized**: Sum of utilized amounts
- **Total Available**: Sum of available amounts
- **Avg Utilization %**: Average utilization across all BGs

**Use Cases**:
- Monitor guarantee efficiency and utilization
- Identify underutilized guarantees for optimization
- Cash flow and collateral planning
- Performance analysis by guarantee type
- Risk assessment and management
- Bank facility optimization

---

### 3. BG Expiry Report

**Purpose**: Monitors BG expiry dates including extensions and provides early warnings for upcoming expirations to prevent guarantee lapses.

**Key Features**:
- Days-to-expiry calculation with extension consideration
- Effective expiry date tracking
- Expiry status categorization
- Early warning system for renewals
- Visual expiry distribution
- Default 90-day expiry horizon
- Utilized and available amount tracking

**Report Columns**:
- **BG Number**: Internal system reference
- **BG Type**: Guarantee category
- **Applicant**: BG applicant name
- **Beneficiary**: BG beneficiary name
- **Issue Date**: Date of BG issuance
- **Expiry Date**: Original BG expiry date
- **Days to Expiry**: Calculated days remaining (considering extensions)
- **Expiry Status**: Categorized expiry urgency
- **FD Amount**: Original Fixed Deposit amount
- **Maturity Amount**: Total maturity amount
- **Utilized Amount**: Current utilized amount
- **Available Amount**: Remaining available amount
- **Status**: Current BG status
- **Issuing Bank**: Name of issuing bank

**Expiry Status Categories**:
- **Expired**: Already expired (negative days)
- **Expiring This Week**: 7 days or less
- **Expiring This Month**: 30 days or less
- **Expiring in 60 Days**: 60 days or less
- **Active**: More than 60 days remaining

**Extension Handling**:
- Considers BG extensions for effective expiry calculation
- Uses latest extension expiry date when status is 'Extended'
- Provides accurate days-to-expiry based on effective dates

**Available Filters**:
- **Expiry Status**: Filter by expiry category
- **BG Type**: Filter by guarantee category
- **Issuing Bank**: Filter by bank name
- **Show All**: Include all BGs regardless of expiry date

**Visual Elements**:
- **Bar Chart**: Distribution of BGs by expiry status
- **Color Coding**: Red (expired) to Green (active) status indicators

**Use Cases**:
- Proactive expiry management and renewal planning
- Risk mitigation for expired guarantees
- Cash flow impact assessment
- Compliance with guarantee terms
- Bank relationship coordination
- Project continuity planning

---

### 4. BG Charges Analysis

**Purpose**: Tracks and analyzes all charges associated with Bank Guarantees including commissions, processing fees, and total cost analysis.

**Key Features**:
- Comprehensive charge tracking by guarantee type
- Commission rate and amount analysis
- Processing charges monitoring
- Total charges calculation
- Charges as percentage of FD amount
- Visual charge distribution by BG type
- Cost analysis across different guarantee categories

**Report Columns**:
- **BG Number**: Internal system reference
- **BG Type**: Guarantee category
- **Beneficiary**: BG beneficiary name
- **FD Amount**: Original Fixed Deposit amount
- **Commission Rate %**: Bank commission percentage
- **Commission Amount**: Calculated commission amount
- **Processing Charges**: Additional processing fees
- **Total Charges**: Sum of all charges
- **Charges % of FD**: Total charges as percentage of FD amount
- **Issuing Bank**: Name of issuing bank
- **Issue Date**: Date of BG issuance

**Charge Calculations**:
- **Commission Amount**: FD Amount × Commission Rate
- **Total Charges**: Commission Amount + Processing Charges
- **Charges %**: (Total Charges / FD Amount) × 100

**Available Filters**:
- **From Date/To Date**: Filter by BG issue date range
- **BG Type**: Filter by guarantee category
- **Bank**: Filter by issuing bank name

**Visual Elements**:
- **Pie Chart**: Charges distribution by BG type
- **Summary Cards**: Key financial metrics and averages

**Key Metrics**:
- **Total BGs**: Number of guarantees with charges
- **Total FD Amount**: Sum of all Fixed Deposit amounts
- **Total Commission**: Sum of all commission charges
- **Total Processing Charges**: Sum of processing fees
- **Total Charges**: Sum of all charges
- **Avg Charges %**: Average charges as percentage of FD

**Use Cases**:
- Cost analysis and budget planning
- Bank charge comparison and negotiation
- Expense tracking and allocation
- Profitability analysis by project
- Guarantee pricing optimization
- Financial reporting and compliance

## Report Access and Permissions

### Required Roles
- **Accounts Manager**: Full access to all BG reports
- **Accounts User**: Read access to BG reports
- **Projects Manager**: Access to project-linked BG reports
- **Sales Manager**: Access to sales order-linked BG reports

### Navigation
1. Go to **Bank Instruments** workspace
2. Click on **Reports** section
3. Select desired BG report from the list
4. Apply filters as needed
5. View, export, or print the report

## Export and Integration

### Export Options
- **Excel**: Full data export with formatting and formulas
- **PDF**: Formatted report for printing and sharing
- **CSV**: Raw data export for further analysis

### Integration Features
- **Real-time Data**: Reports reflect current BG document status
- **Drill-down Capability**: Click on BG numbers to view complete documents
- **Linked Document Access**: Navigate to related projects and orders
- **Scheduled Reports**: Set up automated email delivery

## Advanced Features

### Extension Tracking
- BG Expiry Report automatically considers extensions
- Effective expiry date calculations
- Extension history impact on reporting

### Fixed Deposit Integration
- FD amount tracking across all reports
- Maturity amount calculations
- Charge analysis based on FD amounts

### Multi-dimensional Analysis
- Cross-analysis by BG type, bank, and status
- Time-based trend analysis
- Utilization vs. cost correlation

## Best Practices

### Regular Report Review Schedule
1. **BG Register**: Weekly review for status updates and new guarantees
2. **Utilization Report**: Monthly analysis for efficiency and optimization
3. **Expiry Report**: Weekly check for upcoming expirations and renewals
4. **Charges Analysis**: Monthly cost review and bank comparison

### Filter Optimization Strategies
- Use date ranges to focus on relevant periods
- Combine BG type and bank filters for targeted analysis
- Save frequently used filter combinations for quick access

### Performance Optimization
- Limit date ranges for large datasets
- Use specific filters to reduce processing time
- Export large reports during off-peak hours
- Consider data archiving for historical periods

## Troubleshooting

### Common Issues and Solutions
- **No Data Display**: Check filter settings and verify BG submission status
- **Slow Loading**: Reduce date range or add more specific filters
- **Missing BGs**: Ensure BG documents are submitted (docstatus = 1)
- **Incorrect Calculations**: Refresh report or verify source document data
- **Extension Issues**: Check extension document status and dates

### Data Validation Procedures
- Cross-check report totals with individual BG documents
- Verify currency conversions and exchange rates
- Validate FD and maturity amount calculations
- Confirm charge allocations and percentages

## Report Customization

### Custom Filter Implementation
1. Open report in Edit mode
2. Add new filter fields to filter array
3. Update SQL conditions in get_conditions function
4. Test filter functionality
5. Save and document changes

### Custom Column Addition
1. Modify columns array in get_columns function
2. Update SQL query to include new fields
3. Add any required calculations or formatting
4. Test column display and functionality
5. Update documentation

### Custom Chart Development
1. Modify get_chart_data function
2. Update chart type, colors, and datasets
3. Add new chart calculations if needed
4. Test chart rendering and interactivity
5. Document chart functionality

## Integration with Other Modules

### Project Management
- Link BGs to specific projects
- Track guarantee utilization by project
- Monitor project-related expiry dates

### Sales and Purchase Orders
- Connect BGs to order documents
- Analyze guarantee requirements by transaction
- Track order fulfillment against guarantees

### Accounting Integration
- Automatic charge posting to accounts
- Commission and processing fee tracking
- Financial statement integration

## Compliance and Audit

### Regulatory Compliance
- Complete audit trail for all BG operations
- Expiry monitoring for regulatory requirements
- Document retention and archival

### Internal Controls
- Role-based access control
- Approval workflow integration
- Segregation of duties support

## Support and Training

### Additional Resources
- [BG User Manual](bg_user_manual.md) - Comprehensive BG management guide
- [BG Features](bg_features_doc.md) - Complete feature documentation
- [Quick Start Guide](bg_quickstart_doc.md) - Getting started with BGs

### Training Recommendations
- **Basic Users**: Report navigation and filtering
- **Power Users**: Advanced filtering and export features
- **Administrators**: Custom report development and integration
- **Finance Teams**: Cost analysis and financial reporting

### Ongoing Support
- Regular report usage reviews
- Performance optimization assistance
- Custom development support
- User feedback incorporation

---

*For technical support, feature requests, or customization assistance, please refer to the main app documentation or contact your system administrator.*
