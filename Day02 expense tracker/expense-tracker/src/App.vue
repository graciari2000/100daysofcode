<template>
  <div id="app">
    <h1>Expense Tracker</h1>
    <div>
      <h2>Expense List</h2>
      <!-- Use the ExpenseItem component here -->
      <expense-item :expense="expenseData" />
    </div>
  </div>
</template>

<script>
import ExpenseItem from './components/ExpenseItem.vue'; // Adjust the import path as needed

export default {
  components: {
    ExpenseItem, // Register the ExpenseItem component
  },
  data() {
    return {
      expenseData: {
        name: 'Groceries',
        amount: 50.00,
        date: '2023-09-02',
        category: 'Food',
      },
    };
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
