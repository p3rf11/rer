class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t.id != transaction_id]

    def filter_transactions_by_date(self, start_date, end_date):
        return [t.serialize() for t in self.transactions if start_date <= t.date <= end_date]

    def filter_transactions_by_type(self, transaction_type):
        return [t.serialize() for t in self.transactions if t.type == transaction_type]

    def get_total_amount_by_type(self, transaction_type):
        return sum(t.amount for t in self.transactions if t.type == transaction_type)

    def serialize_transactions(self):
        return [t.serialize() for t in self.transactions]

if __name__ == "__main__":
    transaction1 = Transaction(1, "2024-04-01", "expense", "groceries", 100, "Buying groceries")
    transaction2 = Transaction(2, "2024-04-02", "income", "salary", 2000, "Monthly salary")
    
    manager = TransactionManager()
    manager.add_transaction(transaction1)
    manager.add_transaction(transaction2)
    
    print(manager.filter_transactions_by_type("expense"))
    print(manager.get_total_amount_by_type("income"))
    print(manager.serialize_transactions())

    manager.remove_transaction(1)
    print(manager.serialize_transactions())
