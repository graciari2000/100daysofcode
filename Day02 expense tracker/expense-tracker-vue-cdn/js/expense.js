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
            this.expenses.push({ ...this.newExpense });
            this.newExpense = { expense: '', amount: 0, category: 'Food' };
            this.updateExpenseChart();
        },
        removeExpense(index) {
            this.expenses.splice(index, 1);
            this.updateExpenseChart();
        },
        updateExpenseChart() {
            // Update the chart data here
        },
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
