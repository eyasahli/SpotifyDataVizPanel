import panel as pn

def create_accuracy_card(accuracy):
    accuracy_card = pn.Card(
        pn.indicators.Number(
            value=int(accuracy * 100),  # Multiply by 100 to display as a percentage
            default_color='white',
            name='Model Accuracy',
            format='{value}%',  # Format as a percentage with 2 decimal places
        ),
        styles={'background': '#72EB8E'},
        hide_header=True,
        width=200,
        margin=(20, 20, 20, 20)
    )
    return accuracy_card


def create_recall_card(recall):
    recall_card = pn.Card(
        pn.indicators.Number(
            value=int(recall * 100),  # Multiply by 100 to display as a percentage
            default_color='white',
            name='Class Recall',
            format='{value}%',  # Format as a percentage with 2 decimal places
        ),
        styles={'background': '#72EB8E'},
        hide_header=True,
        width=200,
        margin=(20, 20, 20, 20)
    )
    return recall_card

def create_precision_card(precision):
    precision_card = pn.Card(
        pn.indicators.Number(
            value=int(precision * 100),  # Multiply by 100 to display as a percentage
            default_color='white',
            name='Class Precision',
            format='{value}%',  # Format as a percentage with 2 decimal places
        ),
        styles={'background': '#72EB8E'},
        hide_header=True,
        width=200,
        margin=(20, 20, 20, 20)
    )
    return precision_card

def create_f1_score_card(f1_score):
    f1_score_card = pn.Card(
        pn.indicators.Number(
            value=int(f1_score * 100),  # Multiply by 100 to display as a percentage
            default_color='white',
            name='Class F1 Score',
            format='{value}%',  # Format as a percentage with 2 decimal places
        ),
        styles={'background': '#72EB8E'},
        hide_header=True,
        width=200,
        margin=(20, 20, 20, 20)
    )
    return f1_score_card