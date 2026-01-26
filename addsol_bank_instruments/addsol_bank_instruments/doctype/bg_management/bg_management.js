// Copyright (c) 2025, Addition Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('BG Management', {
    refresh: function(frm) {
        // Add custom buttons
        if (frm.doc.docstatus === 1) {
            add_custom_buttons(frm);
        }
        
        // Set color indicators
        set_status_indicator(frm);
        
        // Show alerts for expiring BGs
        show_expiry_alerts(frm);
    },
    
    onload: function(frm) {
        // Set default values
        if (frm.is_new()) {
            frm.set_value('issue_date', frappe.datetime.get_today());
            frm.set_value('status', 'Active');
        }
        
        // Set queries for dynamic links
        set_field_queries(frm);
    },
    
    fd_amount: function(frm) {
        calculate_commission(frm);
    },
    
    commission_rate: function(frm) {
        calculate_commission(frm);
    },
    
    processing_charges: function(frm) {
        calculate_total_charges(frm);
    },
    
    commission_amount: function(frm) {
        calculate_total_charges(frm);
    },
    
    maturity_amount: function(frm) {
        calculate_available_amount(frm);
    },
    
    utilized_amount: function(frm) {
        calculate_available_amount(frm);
    },
    
    expiry_date: function(frm) {
        calculate_days_to_expiry(frm);
    },
    
    extension_expiry_date: function(frm) {
        calculate_days_to_expiry(frm);
    },
    
    is_extended: function(frm) {
        calculate_days_to_expiry(frm);
    },
    
    beneficiary_type: function(frm) {
        frm.set_value('beneficiary', '');
        // Clear both order fields when beneficiary type changes
        frm.set_value('sales_order', '');
        frm.set_value('purchase_order', '');
        frm.set_value('beneficiary_name', '');
        frm.set_value('project', '');
        // Reset order filters
        reset_order_filters(frm);
    },
    
    beneficiary: function(frm) {
        // Reset all dependent fields when beneficiary changes
        frm.set_value('sales_order', '');
        frm.set_value('purchase_order', '');
        frm.set_value('project', '');
        
        if (frm.doc.beneficiary && frm.doc.beneficiary_type) {
            if (frm.doc.beneficiary_type === 'Customer') {
                frappe.db.get_value('Customer', frm.doc.beneficiary, 'customer_name', (r) => {
                    frm.set_value('beneficiary_name', r.customer_name);
                });
            } else if (frm.doc.beneficiary_type === 'Supplier') {
                frappe.db.get_value('Supplier', frm.doc.beneficiary, 'supplier_name', (r) => {
                    frm.set_value('beneficiary_name', r.supplier_name);
                });
            } else if (frm.doc.beneficiary_type === 'Company') {
                frappe.db.get_value('Company', frm.doc.beneficiary, 'company_name', (r) => {
                    frm.set_value('beneficiary_name', r.company_name);
                });
            }
            // Set filters for Sales Order and Purchase Order based on beneficiary
            set_order_filters(frm);
        }
    },
    
    sales_order: function(frm) {
        if (frm.doc.sales_order) {
            frm.set_value('purchase_order', '');
            // Auto-populate project from Sales Order
            frappe.db.get_value('Sales Order', frm.doc.sales_order, 'project', (r) => {
                if (r.project) {
                    frm.set_value('project', r.project);
                }
            });
            // Auto-populate FD Amount and Maturity Amount from Sales Order
            frappe.db.get_value('Sales Order', frm.doc.sales_order, ['grand_total', 'rounded_total'], (r) => {
                if (r.grand_total) {
                    frm.set_value('fd_amount', r.grand_total);
                    frm.set_value('maturity_amount', r.grand_total);
                } else if (r.rounded_total) {
                    frm.set_value('fd_amount', r.rounded_total);
                    frm.set_value('maturity_amount', r.rounded_total);
                }
            });
        }
    },
    
    purchase_order: function(frm) {
        if (frm.doc.purchase_order) {
            frm.set_value('sales_order', '');
            // Auto-populate project from Purchase Order
            frappe.db.get_value('Purchase Order', frm.doc.purchase_order, 'project', (r) => {
                if (r.project) {
                    frm.set_value('project', r.project);
                }
            });
            // Auto-populate FD Amount and Maturity Amount from Purchase Order
            frappe.db.get_value('Purchase Order', frm.doc.purchase_order, ['grand_total', 'rounded_total'], (r) => {
                if (r.grand_total) {
                    frm.set_value('fd_amount', r.grand_total);
                    frm.set_value('maturity_amount', r.grand_total);
                } else if (r.rounded_total) {
                    frm.set_value('fd_amount', r.rounded_total);
                    frm.set_value('maturity_amount', r.rounded_total);
                }
            });
        }
    }
});

// Helper Functions

function set_order_filters(frm) {
    if (!frm.doc.beneficiary || !frm.doc.beneficiary_type) {
        return;
    }
    
    // Set Sales Order filter based on beneficiary type
    if (frm.doc.beneficiary_type === 'Customer') {
        frm.set_query('sales_order', function() {
            return {
                filters: {
                    'customer': frm.doc.beneficiary
                }
            };
        });
    } else if (frm.doc.beneficiary_type === 'Company') {
        frm.set_query('sales_order', function() {
            return {
                filters: {
                    'customer': frm.doc.beneficiary
                }
            };
        });
    }
    
    // Set Purchase Order filter based on beneficiary type
    if (frm.doc.beneficiary_type === 'Supplier') {
        frm.set_query('purchase_order', function() {
            return {
                filters: {
                    'supplier': frm.doc.beneficiary
                }
            };
        });
    } else if (frm.doc.beneficiary_type === 'Company') {
        frm.set_query('purchase_order', function() {
            return {
                filters: {
                    'supplier': frm.doc.beneficiary
                }
            };
        });
    }
}

function reset_order_filters(frm) {
    // Reset Sales Order filter
    frm.set_query('sales_order', function() {
        return {};
    });
    
    // Reset Purchase Order filter
    frm.set_query('purchase_order', function() {
        return {};
    });
}

// Child table: BG Management Extension
frappe.ui.form.on('BG Management Extension', {
    extension_history_add: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        row.extension_number = frm.doc.extension_history.length;
        row.extension_date = frappe.datetime.get_today();
        row.approved_by = frappe.session.user;
        
        // Set previous expiry date
        if (frm.doc.is_extended && frm.doc.extension_expiry_date) {
            row.previous_expiry_date = frm.doc.extension_expiry_date;
        } else {
            row.previous_expiry_date = frm.doc.expiry_date;
        }
        
        frm.refresh_field('extension_history');
    },
    
    new_expiry_date: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.previous_expiry_date && row.new_expiry_date) {
            row.extension_days = frappe.datetime.get_day_diff(
                row.new_expiry_date, 
                row.previous_expiry_date
            );
            frm.refresh_field('extension_history');
        }
    }
});

// Helper Functions

function add_custom_buttons(frm) {
    // Extend BG button
    if (frm.doc.status !== 'Claimed' && frm.doc.status !== 'Cancelled' && frm.doc.status !== 'Closed') {
        frm.add_custom_button(__('Extend BG'), function() {
            show_extend_dialog(frm);
        }, __('Actions'));
    }
    
    // Mark as Claimed button
    if (frm.doc.status !== 'Claimed' && frm.doc.status !== 'Cancelled' && frm.doc.status !== 'Closed') {
        frm.add_custom_button(__('Mark as Claimed'), function() {
            show_claim_dialog(frm);
        }, __('Actions'));
    }
    
    // Close BG button
    if (frm.doc.status !== 'Claimed' && frm.doc.status !== 'Cancelled' && frm.doc.status !== 'Closed') {
        frm.add_custom_button(__('Close BG'), function() {
            show_close_dialog(frm);
        }, __('Actions'));
    }
    
    // Create Journal Entry button (if needed)
    frm.add_custom_button(__('Create Journal Entry'), function() {
        create_journal_entry(frm);
    }, __('Create'));
}

function show_extend_dialog(frm) {
    let current_expiry = frm.doc.is_extended ? 
        frm.doc.extension_expiry_date : frm.doc.expiry_date;
    
    let d = new frappe.ui.Dialog({
        title: __('Extend Bank Guarantee'),
        fields: [
            {
                label: __('Current Expiry Date'),
                fieldname: 'current_expiry',
                fieldtype: 'Date',
                read_only: 1,
                default: current_expiry
            },
            {
                label: __('New Expiry Date'),
                fieldname: 'new_expiry_date',
                fieldtype: 'Date',
                reqd: 1
            },
            {
                label: __('Extension Charges'),
                fieldname: 'extension_charges',
                fieldtype: 'Currency',
                default: 0
            },
            {
                label: __('Remarks'),
                fieldname: 'remarks',
                fieldtype: 'Small Text'
            }
        ],
        primary_action_label: __('Extend'),
        primary_action(values) {
            frappe.call({
                method: 'addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.extend_bg_management',
                args: {
                    bg_management_name: frm.doc.name,
                    new_expiry_date: values.new_expiry_date,
                    extension_charges: values.extension_charges,
                    remarks: values.remarks
                },
                callback: function(r) {
                    if (!r.exc) {
                        frm.reload_doc();
                        d.hide();
                    }
                }
            });
        }
    });
    
    d.show();
}

function show_claim_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: __('Mark as Claimed'),
        fields: [
            {
                label: __('Claim Date'),
                fieldname: 'claim_date',
                fieldtype: 'Date',
                default: frappe.datetime.get_today(),
                reqd: 1
            },
            {
                label: __('Claim Amount'),
                fieldname: 'claim_amount',
                fieldtype: 'Currency',
                default: 0
            },
            {
                label: __('Remarks'),
                fieldname: 'remarks',
                fieldtype: 'Small Text'
            }
        ],
        primary_action_label: __('Mark as Claimed'),
        primary_action(values) {
            frappe.call({
                method: 'addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.mark_as_claimed',
                args: {
                    bg_management_name: frm.doc.name,
                    claim_date: values.claim_date,
                    claim_amount: values.claim_amount
                },
                callback: function(r) {
                    if (!r.exc) {
                        frm.reload_doc();
                        d.hide();
                    }
                }
            });
        }
    });
    
    d.show();
}

function show_close_dialog(frm) {
    frappe.confirm(
        __('Are you sure you want to close this Bank Guarantee?'),
        function() {
            let remarks = '';
            frappe.prompt({
                label: __('Closure Remarks'),
                fieldname: 'remarks',
                fieldtype: 'Small Text'
            }, function(values) {
                frappe.call({
                    method: 'addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.close_bg_management',
                    args: {
                        bg_management_name: frm.doc.name,
                        remarks: values.remarks
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            frm.reload_doc();
                        }
                    }
                });
            }, __('Close Bank Guarantee'), __('Close'));
        }
    );
}

function calculate_commission(frm) {
    if (frm.doc.commission_rate && frm.doc.fd_amount) {
        let commission = (frm.doc.fd_amount * frm.doc.commission_rate) / 100;
        frm.set_value('commission_amount', commission);
    }
}

function calculate_total_charges(frm) {
    let total = (frm.doc.commission_amount || 0) + (frm.doc.processing_charges || 0);
    frm.set_value('total_charges', total);
}

function calculate_available_amount(frm) {
    if (frm.doc.maturity_amount) {
        let available = frm.doc.maturity_amount - (frm.doc.utilized_amount || 0);
        frm.set_value('available_amount', available);
    }
}

function calculate_days_to_expiry(frm) {
    let expiry_date = frm.doc.is_extended && frm.doc.extension_expiry_date ? 
        frm.doc.extension_expiry_date : frm.doc.expiry_date;
    
    if (expiry_date) {
        let days = frappe.datetime.get_day_diff(expiry_date, frappe.datetime.get_today());
        frm.set_value('days_to_expiry', days);
    }
}

function set_status_indicator(frm) {
    if (!frm.doc.status) return;
    
    let indicator_map = {
        'Active': 'green',
        'Extended': 'blue',
        'Expired': 'red',
        'Claimed': 'orange',
        'Closed': 'gray',
        'Cancelled': 'darkgray'
    };
    
    frm.page.set_indicator(frm.doc.status, indicator_map[frm.doc.status] || 'gray');
}

function show_expiry_alerts(frm) {
    if (frm.doc.days_to_expiry <= 0) {
        frm.dashboard.add_comment(__('This Bank Guarantee has expired'), 'red', true);
    } else if (frm.doc.days_to_expiry <= 7) {
        frm.dashboard.add_comment(
            __('This Bank Guarantee is expiring in {0} days', [frm.doc.days_to_expiry]), 
            'red', 
            true
        );
    } else if (frm.doc.days_to_expiry <= 15) {
        frm.dashboard.add_comment(
            __('This Bank Guarantee is expiring in {0} days', [frm.doc.days_to_expiry]), 
            'orange', 
            true
        );
    } else if (frm.doc.days_to_expiry <= 30) {
        frm.dashboard.add_comment(
            __('This Bank Guarantee is expiring in {0} days', [frm.doc.days_to_expiry]), 
            'yellow', 
            true
        );
    }
}

function set_field_queries(frm) {
    // Filter bank accounts based on selected bank
    frm.set_query('bank_account', function() {
        return {
            filters: {
                'bank': frm.doc.bank
            }
        };
    });
}

function create_journal_entry(frm) {
    frappe.model.open_mapped_doc({
        method: "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.make_journal_entry",
        frm: frm
    });
}