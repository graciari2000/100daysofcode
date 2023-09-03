<template>
    <h2>Expense Tracker App</h2>
    <p>Welcome to the Expense Tracker App</p>
  <div class="expense-item">
    <h3>{{ expense.name }}</h3>
    <p>Amount: ${{ expense.amount }}</p>
    <p>Date: {{ expense.date }}</p>
    <p>Category: {{ expense.category }}</p>
  </div>
</template>

<script>
export default {
  props: {
    expense: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.expense-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  background-color: red;
}
</style>