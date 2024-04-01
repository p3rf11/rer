class Transaction:
    def __init__(self, id, date, type, category, amount, description):
        self.id = id
        self.date = date
        self.type = type  
        self.category = category
        self.amount = amount
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'type': self.type,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }
