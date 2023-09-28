from rest_framework import serializers
from .models import Notes
from utils.dynamicfields import DynamicFieldsModelSerializer


class NotesSerializer(DynamicFieldsModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    # agent_name = serializers.CharField(source='agent.name', read_only=True)

    class Meta:
        model = Notes
        fields = [
            # 'id',
            'customer',
            'description',  # Include the customer's name from the related Customer model
            'agent',
            'agent_name',  # Include the agent's name from the related Employee model
            'inventory',
            'order_quantity',
            'status',
            'total_amount',
            'remarks',
        ]

