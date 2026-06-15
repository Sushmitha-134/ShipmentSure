import pandas as pd

def create_features(
    warehouse,
    shipment,
    importance,
    gender,
    customer_care_calls,
    customer_rating,
    cost,
    prior_purchases,
    discount,
    weight
):

    data = {

        'Customer_care_calls': [customer_care_calls],

        'Customer_rating': [customer_rating],

        'Cost_of_the_Product': [cost],

        'Prior_purchases': [prior_purchases],

        'Discount_offered': [discount],

        'Weight_in_gms': [weight],

        'Cost_Weight_Ratio': [
            cost / weight if weight != 0 else 0
        ],

        'Discount_Cost_Ratio': [
            discount / cost if cost != 0 else 0
        ],

        'Calls_Per_Purchase': [
            customer_care_calls / (prior_purchases + 1)
        ],

        'Warehouse_block_B': [
            1 if warehouse == "B" else 0
        ],

        'Warehouse_block_C': [
            1 if warehouse == "C" else 0
        ],

        'Warehouse_block_D': [
            1 if warehouse == "D" else 0
        ],

        'Warehouse_block_F': [
            1 if warehouse == "F" else 0
        ],

        'Mode_of_Shipment_Road': [
            1 if shipment == "Road" else 0
        ],

        'Mode_of_Shipment_Ship': [
            1 if shipment == "Ship" else 0
        ],

        'Product_importance_low': [
            1 if importance == "low" else 0
        ],

        'Product_importance_medium': [
            1 if importance == "medium" else 0
        ],

        'Gender_M': [
            1 if gender == "M" else 0
        ]
    }

    return pd.DataFrame(data)