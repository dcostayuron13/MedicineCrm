USER_ROLES = (
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('team_manager', 'Team Manager'),
        ('team_lead', 'Team Lead'),
        ('agent', 'Agent'),
        ('customer_care', 'Customer Care'),
        ('escalator', 'Escalator'),
('verifier', 'Verifier'),
    )

ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
('cancelled', 'Cancelled'),
    ('returned', 'Returned'),
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

    )