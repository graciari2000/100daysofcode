const app = Vue.createApp({
    data() {
        return {
            newExpense: { expense: '', amount: 0, category: 'Food' },
            expenses: [],
            chartData: {
                labels: [],
                datasets: [{
                    data: [],
                    backgroundColor: ['#ff5733', '#33ff57', '#3366ff', '#ff33f2', '#33f2ff'],
                }],
            },
        };
    },
    methods: {
    addExpense() {
                // Ensure that the required fields are filled in before adding the expense.
                if (!this.newExpense.expense || this.newExpense.amount <= 0) {
                    alert('Please fill in both the expense description and a valid amount.');
                    return; // Don't proceed if fields are not filled.
                }
                // Add the new expense to the expenses array.
                this.expenses.push({ ...this.newExpense });

                // Reset the newExpense object to clear the input fields.
                this.newExpense = { expense: '', amount: 0, category: 'Food' };

                // Update the chart data to reflect the new expense.
                this.updateExpenseChart();
            },
    removeExpense(index) {
            this.expenses.splice(index, 1);
            this.updateExpenseChart();
        },
    updateExpenseChart() {
        const categories = [...new Set(this.expenses.map(expense => expense.category))];
        const data = categories.map(category => {
            const total = this.expenses
                .filter(expense => expense.category === category)
                .reduce((acc, expense) => acc + expense.amount, 0);

            return { category, total };
        });

        this.chartData.labels = data.map(item => item.category);
        this.chartData.datasets[0].data = data.map(item => item.total);
    },
    mounted() {
        const ctx = document.getElementById('expense-chart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: this.chartData,
            options: { responsive: true },
        });
    },
});

app.mount('#app');
