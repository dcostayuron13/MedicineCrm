<<<<<<< HEAD
USER_ROLES = (
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('team_manager', 'Team Manager'),
        ('team_lead', 'Team Lead'),
        ('agent', 'Agent'),
        ('customer_care', 'Customer Care'),
        ('customer', 'Customer'),
        ('escalator', 'Escalator'),
        ('verifier', 'Verifier'),
    )

LEAD_SOURCE = (
        ('outbound', 'Outbound'),
        ('inbound', 'Inbound'),
        ('website', 'Website'),
        ('email', 'Email'),
    )

ORDER_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
=======
USER_ROLES = (
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('team_manager', 'Team Manager'),
        ('team_lead', 'Team Lead'),
        ('agent', 'Agent'),
        ('customer_care', 'Customer Care'),
        ('customer', 'Customer'),
        ('escalator', 'Escalator'),
('verifier', 'Verifier'),
    )

LEAD_SOURCE = (
        ('outbound', 'Outbound'),
        ('inbound', 'Inbound'),
        ('website', 'Website'),
        ('email', 'Email'),
    )

TICKET_STATUS = (
        ('pending', 'Pending'),
('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('review', 'Review'),
        ('resolved', 'Resolved'),
('cancelled', 'Cancelled'),
    )

PRIORITY = (
        ('low', 'Low'),
('medium', 'Medium'),
        ('high', 'High'),
    )

PAYMENT_METHOD = (
        ('card', 'Card'),
('link', 'Link'),
        ('bank_transfer', 'Bank Transfer'),
('check_po', 'Check/ Postal Order'),
    )

PAYMENT_STATUS = (
        ('pending', 'Pending'),
('processing', 'Processing'),
        ('authorized', 'Authorized'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
('cancelled', 'Cancelled'),
('cancelled', 'Cancelled'),
('refunded', 'Refunded'),
('on_hold', 'On Hold'),
# ('payment_gateway', 'Payment Gateway'),

>>>>>>> development
    )