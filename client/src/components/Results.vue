<template>
	<div id="app-results">
		<h3>Results</h3>
		
		<div class="status row">
			<div class="col-md-12 text-center"><h4><span class="text-muted">Status: </span><span class="badge badge-pill badge-success">{{ sts }}</span></h4></div>
		</div>

		<div class="papers">
			<app-paper v-for="paper in set" v-bind:paper="paper" v-bind:key="paper.id"></app-paper>
		</div>
	</div>
</template>


<script>
	import Paper from './Paper.vue';

	export default {
		props: ['sts', 'set'],
		components: {
			'app-paper': Paper
		}
	}

</script>


<style lang="scss" scoped>
	.status {
		margin-bottom: 1.5rem;
	}
</style>