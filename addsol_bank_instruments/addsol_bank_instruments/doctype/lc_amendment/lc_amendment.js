// Copyright (c) 2024, Addition Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('LC Amendment', {
	refresh: function(frm) {
		// Set status color indicator
		set_amendment_status_indicator(frm);
		
		// Add custom button to view original LC
		if (frm.doc.letter_of_credit) {
			frm.add_custom_button(__('View LC'), function() {
				frappe.set_route('Form', 'Letter of Credit', frm.doc.letter_of_credit);
			});
		}
		
		// Disable fields after submit
		if (frm.doc.docstatus === 1) {
			frm.set_df_property('new_lc_amount', 'read_only', 1);
			frm.set_df_property('new_expiry_date', 'read_only', 1);
			frm.set_df_property('new_shipment_date', 'read_only', 1);
		}
	},
	
	letter_of_credit: function(frm) {
		// Fetch LC details when LC is selected
		if (frm.doc.letter_of_credit) {
			frappe.call({
				method: 'frappe.client.get',
				args: {
					doctype: 'Letter of Credit',
					name: frm.doc.letter_of_credit
				},
				callback: function(r) {
					if (r.message) {
						let lc = r.message;
						
						// Set previous values
						frm.set_value('previous_lc_amount', lc.lc_amount);
						frm.set_value('previous_expiry_date', lc.expiry_date);
						frm.set_value('previous_shipment_date', lc.latest_shipment_date);
						
						// Pre-fill new values with current values
						if (!frm.doc.new_lc_amount) {
							frm.set_value('new_lc_amount', lc.lc_amount);
						}
						if (!frm.doc.new_expiry_date) {
							frm.set_value('new_expiry_date', lc.expiry_date);
						}
						if (!frm.doc.new_shipment_date) {
							frm.set_value('new_shipment_date', lc.latest_shipment_date);
						}
					}
				}
			});
		}
	},
	
	amendment_type: function(frm) {
		// Show relevant fields based on amendment type
		if (frm.doc.amendment_type === 'Amount Increase' || 
		    frm.doc.amendment_type === 'Amount Decrease') {
			frm.set_df_property('new_lc_amount', 'reqd', 1);
		}
		
		if (frm.doc.amendment_type === 'Date Extension') {
			frm.set_df_property('new_expiry_date', 'reqd', 1);
			frm.set_df_property('new_shipment_date', 'reqd', 1);
		}
	},
	
	new_lc_amount: function(frm) {
		calculate_amount_change(frm);
		validate_amount_change(frm);
	},
	
	new_expiry_date: function(frm) {
		validate_dates(frm);
	},
	
	new_shipment_date: function(frm) {
		validate_dates(frm);
	}
});

// Helper Functions

function calculate_amount_change(frm) {
	if (frm.doc.new_lc_amount && frm.doc.previous_lc_amount) {
		let change = frm.doc.new_lc_amount - frm.doc.previous_lc_amount;
		frm.set_value('amount_change', change);
		
		// Show indicator for increase/decrease
		if (change > 0) {
			frm.set_df_property('amount_change', 'description', 
				'<span style="color: green;">▲ Increase</span>');
		} else if (change < 0) {
			frm.set_df_property('amount_change', 'description', 
				'<span style="color: red;">▼ Decrease</span>');
		}
	}
}

function validate_amount_change(frm) {
	if (frm.doc.amendment_type === 'Amount Increase' && frm.doc.amount_change < 0) {
		frappe.msgprint({
			title: __('Warning'),
			indicator: 'orange',
			message: __('Amendment type is "Amount Increase" but the new amount is less than previous amount.')
		});
	}
	
	if (frm.doc.amendment_type === 'Amount Decrease' && frm.doc.amount_change > 0) {
		frappe.msgprint({
			title: __('Warning'),
			indicator: 'orange',
			message: __('Amendment type is "Amount Decrease" but the new amount is greater than previous amount.')
		});
	}
}

function validate_dates(frm) {
	// Validate new expiry date is after amendment date
	if (frm.doc.new_expiry_date && frm.doc.amendment_date) {
		let amendment_date = frappe.datetime.str_to_obj(frm.doc.amendment_date);
		let expiry_date = frappe.datetime.str_to_obj(frm.doc.new_expiry_date);
		
		if (expiry_date < amendment_date) {
			frappe.msgprint({
				title: __('Date Validation'),
				indicator: 'red',
				message: __('New Expiry Date cannot be before Amendment Date')
			});
			frm.set_value('new_expiry_date', '');
		}
	}
	
	// Validate shipment date is before expiry date
	if (frm.doc.new_shipment_date && frm.doc.new_expiry_date) {
		let shipment_date = frappe.datetime.str_to_obj(frm.doc.new_shipment_date);
		let expiry_date = frappe.datetime.str_to_obj(frm.doc.new_expiry_date);
		
		if (shipment_date > expiry_date) {
			frappe.msgprint({
				title: __('Date Validation'),
				indicator: 'red',
				message: __('New Shipment Date cannot be after New Expiry Date')
			});
			frm.set_value('new_shipment_date', '');
		}
	}
}

function set_amendment_status_indicator(frm) {
	let status_colors = {
		'Draft': 'grey',
		'Submitted': 'blue',
		'Approved': 'green',
		'Rejected': 'red',
		'Cancelled': 'darkgrey'
	};
	
	if (frm.doc.status) {
		frm.page.set_indicator(__(frm.doc.status), status_colors[frm.doc.status] || 'blue');
	}
}