from flask import Blueprint, request, jsonify, render_template
from .models import Transaction

app_views = Blueprint('app_views', __name__)

transactions = []

@app_views.route('/')
def index():
    return render_template('transactions.html')

@app_views.route('/api/transactions', methods=['POST', 'GET'])
def handle_transactions():
    if request.method == 'POST':
        data = request.json
        new_transaction = Transaction(len(transactions) + 1, **data)
        transactions.append(new_transaction)
        return jsonify(new_transaction.serialize()), 201
    
    elif request.method == 'GET':
        return jsonify([transaction.serialize() for transaction in transactions]), 200
