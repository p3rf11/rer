window.onload = function() {
    axios.get('/api/transactions')
        .then(function (response) {
            const transactionsDiv = document.getElementById('transactions');
            if (response.data.length === 0) {
                transactionsDiv.textContent = 'No transactions to display.';
                return;
            }
            const sortedTransactions = response.data.sort((a, b) => new Date(a.date) - new Date(b.date));
            sortedTransactions.forEach(function(transaction) {
                const transactionElement = document.createElement('div');
                const amountFormatted = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(transaction.amount);
                transactionElement.textContent = `${transaction.date} - ${transaction.type} - ${transaction.category} - ${amountFormatted}`;
                transactionsDiv.appendChild(transactionElement);
            });
        })
        .catch(function (error) {
            console.error(error);
        });
};
