<template>
<div>
<h2>Add Expense</h2>
<form @submit.prevent='addExpense'>
<label for='name'>Name</label>
<select id='category' v-model='expense.category'>
<option value= 'Spotify'>Spotify</option>
<option value='Netflix'>Netflix</option>
<option value='Food'>Food</option>
<option value='Google Play'>Google Play</option>
<option value='UBA Bank'>UBA Bank</option>
<option value='Groceries'>Groceries</option>
</select>
</form>
</div>
</template>

<script>
export default {
       data() {
       	      return {
	      	     expense: {
			amount: null,
			date: null,
			category: 'food'
			}
	};
		},

methods: {
	 addExpense() {
	 if(!this.expense.amount || !this.expense.date) {
	 alert('Please fill in all fields');
	 return;
}
this.$emit('addExpense', this.expense);
this.expense= {
amount: null,
date: null,
category: 'food'
}
}
}
</script>