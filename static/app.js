window.onload = function() {
    axios.get('/api/transactions')
        .then(function (response) {
            const transactionsDiv = document.getElementById('transactions');
            response.data.forEach(function(transaction) {
                const transactionElement = document.createElement('div');
                transactionElement.textContent = `${transaction.date} - ${transaction.type} - ${transaction.category} - ${transaction.amount}`;
                transactionsDiv.appendChild(transactionElement);
            });
        })
        .catch(function (error) {
            console.error(error);
        });
};