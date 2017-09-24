<template>
	<div class="container">
		<div class="row">
  			<div class="col-md-12">
  				<h1 class="text-center display-4">Tilburg Experience Sampling<br>Center</h1>
  			</div>
		</div>

		<hr>

		<app-search></app-search>

		<hr>

		<footer class="text-center">
			<span><small class="text-muted">Copyright &copy; 2017 TESC - Tilburg University</small></span>
		</footer>
	</div>
</template>


<script>
import Search from './components/Search.vue';

export default {
	components: {
		'app-search': Search
	}
}
</script>


<style lang="scss">
	body {
		margin-top: 2rem;
	}

	.container, .row {
		border: 0px solid red;
	}

	h3 {
		margin-bottom: 1.5rem;
	}

	hr {
		margin-top: 2rem; 
		margin-bottom: 2rem; 
	}

	footer {
		margin-bottom: 1rem;
	}
</style>
