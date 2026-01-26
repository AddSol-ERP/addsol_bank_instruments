// Copyright (c) 2024, Addition Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('Letter of Credit', {
	refresh: function(frm) {
		// Set naming series
		set_naming_series(frm);
		// Add custom buttons
		if (frm.doc.docstatus === 1) {
			// Add Amendment button
			frm.add_custom_button(__('Create Amendment'), function() {
				frappe.new_doc('LC Amendment', {
					letter_of_credit: frm.doc.name
				});
			}, __('Actions'));
			
			// Add Document Submission button
			if (frm.doc.status === 'Opened' || frm.doc.status === 'Amended') {
				frm.add_custom_button(__('Submit Documents'), function() {
					frm.set_value('status', 'Documents Submitted');
					frm.save();
				}, __('Actions'));
			}
			
			// Add Payment button
			if (frm.doc.status === 'Documents Accepted') {
				frm.add_custom_button(__('Make Payment'), function() {
					make_payment_entry(frm);
				}, __('Actions'));
			}
		}
		
		// Set color indicators based on status
		set_status_indicator(frm);
		
		// Add alerts for expiring LCs
		check_expiry_alert(frm);
	},
	
	transaction_type: function(frm) {
		set_naming_series(frm);
		// Auto-set applicant and beneficiary types based on transaction type
		if (frm.doc.transaction_type === 'Import') {
			frm.set_value('applicant_type', 'Company');
			frm.set_value('beneficiary_type', 'Supplier');
		} else if (frm.doc.transaction_type === 'Export') {
			frm.set_value('applicant_type', 'Customer');
			frm.set_value('beneficiary_type', 'Company');
		}
	},
	
	applicant: function(frm) {
		// Fetch applicant name
		if (frm.doc.applicant && frm.doc.applicant_type) {
			// If company set Applicant Name as Company Name
			if (frm.doc.applicant_type === 'Company') {
				// Get Company name
				frm.set_value('applicant_name', frappe.defaults.get_global_default("company"));
			}
			else {
				frappe.db.get_value(frm.doc.applicant_type, frm.doc.applicant, 'name', (r) => {
					if (r) {
						frm.set_value('applicant_name', r.name);
					}
				});
			}
		}
	},
	
	beneficiary: function(frm) {
		// Fetch beneficiary name
		if (frm.doc.beneficiary && frm.doc.beneficiary_type) {
			// If Beneficiery is Company then set Benificiery Name as Company
			if (frm.doc.beneficiary_type === 'Company') {
				// Get Company name
				frm.set_value('beneficiary_name', frappe.defaults.get_global_default("company"));
			}
			else {
				frappe.db.get_value(frm.doc.beneficiary_type, frm.doc.beneficiary, 'name', (r) => {
					if (r) {
						frm.set_value('beneficiary_name', r.name);
				}
			});
		}
	}
	},
	
	purchase_order: function(frm) {
		// Auto-populate fields from Purchase Order
		if (frm.doc.purchase_order) {
			frappe.call({
				method: 'frappe.client.get',
				args: {
					doctype: 'Purchase Order',
					name: frm.doc.purchase_order
				},
				callback: function(r) {
					if (r.message) {
						let po = r.message;
						
						// Set supplier as beneficiary
						if (frm.doc.transaction_type === 'Import') {
							frm.set_value('beneficiary_type', 'Supplier');
							frm.set_value('beneficiary', po.supplier);
						}
						
						// Set currency and amount
						if (!frm.doc.currency) {
							frm.set_value('currency', po.currency);
						}
						if (!frm.doc.lc_amount) {
							frm.set_value('lc_amount', po.grand_total);
						}
						
						// Set incoterm
						if (po.incoterm && !frm.doc.incoterms) {
							frm.set_value('incoterms', po.incoterm);
						}
					}
				}
			});
		}
	},
	
	sales_order: function(frm) {
		// Auto-populate fields from Sales Order
		if (frm.doc.sales_order) {
			frappe.call({
				method: 'frappe.client.get',
				args: {
					doctype: 'Sales Order',
					name: frm.doc.sales_order
				},
				callback: function(r) {
					if (r.message) {
						let so = r.message;
						
						// Set customer as applicant
						if (frm.doc.transaction_type === 'Export') {
							frm.set_value('applicant_type', 'Customer');
							frm.set_value('applicant', so.customer);
						}
						
						// Set currency and amount
						if (!frm.doc.currency) {
							frm.set_value('currency', so.currency);
						}
						if (!frm.doc.lc_amount) {
							frm.set_value('lc_amount', so.grand_total);
						}
						
						// Set incoterm
						if (so.incoterm && !frm.doc.incoterms) {
							frm.set_value('incoterms', so.incoterm);
						}
					}
				}
			});
		}
	},
	
	lc_amount: function(frm) {
		calculate_balance_amount(frm);
	},
	
	tolerance_percentage: function(frm) {
		calculate_balance_amount(frm);
	},
	
	utilized_amount: function(frm) {
		calculate_balance_amount(frm);
	},
	
	lc_type: function(frm) {
		// Set default payment terms based on LC type
		if (frm.doc.lc_type === 'Sight LC') {
			frm.set_value('payment_terms', 'At Sight');
		} else if (frm.doc.lc_type === 'Usance LC') {
			frm.set_value('payment_terms', 'Usance');
		} else if (frm.doc.lc_type === 'Deferred Payment LC') {
			frm.set_value('payment_terms', 'Deferred Payment');
		}
	},
	
	payment_terms: function(frm) {
		// Show/hide usance days field
		if (frm.doc.payment_terms === 'Usance') {
			frm.set_df_property('usance_days', 'reqd', 1);
		} else {
			frm.set_df_property('usance_days', 'reqd', 0);
		}
	}
});

// Child table: LC Shipment
frappe.ui.form.on('LC Shipment', {
	shipments_add: function(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		// Set default shipment date to today
		frappe.model.set_value(cdt, cdn, 'shipment_date', frappe.datetime.get_today());
	},
	
	shipped_value: function(frm, cdt, cdn) {
		calculate_total_shipped(frm);
		calculate_balance_amount(frm);
	},
	
	shipments_remove: function(frm) {
		calculate_total_shipped(frm);
		calculate_balance_amount(frm);
	},
	
	delivery_note: function(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		
		// Fetch details from Delivery Note
		if (row.delivery_note) {
			frappe.call({
				method: 'frappe.client.get',
				args: {
					doctype: 'Delivery Note',
					name: row.delivery_note
				},
				callback: function(r) {
					if (r.message) {
						let dn = r.message;
						
						// Set values from DN
						frappe.model.set_value(cdt, cdn, 'shipment_date', dn.posting_date);
						frappe.model.set_value(cdt, cdn, 'shipped_value', dn.grand_total);
						
						// Set BL/AWB if available
						if (dn.lr_no) {
							frappe.model.set_value(cdt, cdn, 'bl_awb_number', dn.lr_no);
						}
						
						// Calculate total quantity
						let total_qty = 0;
						if (dn.items) {
							dn.items.forEach(item => {
								total_qty += item.qty;
							});
						}
						frappe.model.set_value(cdt, cdn, 'shipped_quantity', total_qty);
					}
				}
			});
		}
	}
});

// Child table: LC Charges
frappe.ui.form.on('LC Charges', {
	charges_add: function(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		// Set default charge date and currency
		frappe.model.set_value(cdt, cdn, 'charge_date', frappe.datetime.get_today());
		frappe.model.set_value(cdt, cdn, 'currency', frm.doc.currency);
	}
});

// Helper Functions

function set_naming_series(frm) {
    if (!frm.doc.transaction_type) return;

    let series_map = {
        "Import": ["LC-IMP-.YYYY.-"],
        "Export": ["LC-EXP-.YYYY.-"]
    };

    let options = series_map[frm.doc.transaction_type] || [];

    // Set options dynamically
    frm.set_df_property(
        "naming_series",
        "options",
        options.join("\n")
    );

    // Auto-select if only one option
    if (options.length === 1) {
        frm.set_value("naming_series", options[0]);
    }
}

function calculate_balance_amount(frm) {
	let lc_amount = frm.doc.lc_amount || 0;
	let tolerance = frm.doc.tolerance_percentage || 0;
	let utilized = frm.doc.utilized_amount || 0;
	
	let tolerance_amount = lc_amount * tolerance / 100;
	let max_lc_amount = lc_amount + tolerance_amount;
	let balance = max_lc_amount - utilized;
	
	frm.set_value('balance_amount', balance);
	
	// Show warning if over-utilized
	if (utilized > max_lc_amount) {
		frappe.msgprint({
			title: __('Warning'),
			indicator: 'red',
			message: __('Utilized amount exceeds LC amount including tolerance!')
		});
	}
}

function calculate_total_shipped(frm) {
	let total_shipped = 0;
	
	if (frm.doc.shipments) {
		frm.doc.shipments.forEach(row => {
			total_shipped += row.shipped_value || 0;
		});
	}
	
	frm.set_value('utilized_amount', total_shipped);
}

function set_status_indicator(frm) {
	let status_colors = {
		'Draft': 'grey',
		'Opened': 'blue',
		'Amended': 'orange',
		'Documents Submitted': 'purple',
		'Documents Accepted': 'green',
		'Payment Made': 'cyan',
		'Settled': 'green',
		'Cancelled': 'red',
		'Expired': 'darkgrey'
	};
	
	if (frm.doc.status) {
		frm.page.set_indicator(__(frm.doc.status), status_colors[frm.doc.status] || 'blue');
	}
}

function check_expiry_alert(frm) {
	if (frm.doc.expiry_date && frm.doc.docstatus === 1) {
		let today = frappe.datetime.get_today();
		let expiry = frm.doc.expiry_date;
		let days_to_expiry = frappe.datetime.get_day_diff(expiry, today);
		
		// Alert if expiring within 30 days
		if (days_to_expiry > 0 && days_to_expiry <= 30) {
			frm.dashboard.add_comment(
				__('LC expiring in {0} days!', [days_to_expiry]), 
				'yellow', 
				true
			);
		}
		
		// Alert if expired
		if (days_to_expiry < 0) {
			frm.dashboard.add_comment(
				__('LC has expired!'), 
				'red', 
				true
			);
		}
	}
}

function make_payment_entry(frm) {
	frappe.call({
		method: 'erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry',
		args: {
			dt: 'Purchase Order',
			dn: frm.doc.purchase_order || ''
		},
		callback: function(r) {
			if (r.message) {
				let payment_entry = frappe.model.sync(r.message);
				frappe.set_route('Form', 'Payment Entry', payment_entry[0].name);
			} else {
				// Create new payment entry
				frappe.new_doc('Payment Entry', {
					party_type: frm.doc.beneficiary_type,
					party: frm.doc.beneficiary,
					paid_amount: frm.doc.lc_amount,
					paid_to_account_currency: frm.doc.currency
				});
			}
		}
	});
}