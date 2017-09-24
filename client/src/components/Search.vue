<template>
	<div id="app-search">
		<h3>Quick search tool</h3>
		
		<form v-on:submit.prevent="onSubmit">
			<div class="form-group row">
				<label for="start-year" class="col-sm-2 col-form-label">Start year:</label>
				<div class="col-sm-10">
					<input v-model="start" type="text" class="form-control" id="start-year" placeholder="Enter the year start searching from... Default: 2016">
				</div>
			</div>

			<div class="form-group row">
				<label for="end-year" class="col-sm-2 col-form-label">End year:</label>
				<div class="col-sm-10">
					<input v-model="end" type="text" class="form-control" id="end-year" placeholder="Enter the year to stop searching at... Default: 2017">
				</div>
			</div>

			<div class="form-group row">
				<label for="query" class="col-sm-2 col-form-label">Query:</label>
				<div class="col-sm-10">
					<input v-model="search" type="text" class="form-control" id="query" placeholder='Default: ^title:"experience sampling" OR abstract:"experience sampling"'>
				</div>
			</div>

			<div class="form-group row">
				<div class="col-sm-10">
					<button type="submit" class="btn btn-primary">Find papers</button>
				</div>
			</div>
		</form>

		<hr>

		<app-results v-bind:sts="status" v-bind:set="results"></app-results>
	</div>
</template>


<script>
	import Results from './Results.vue'

	export default {
		components: {
			'app-results': Results
		},

		data: function() {
			return {
				start: '2016',
				end: '2017',
				search: '^title:"experience sampling" OR abstract:"experience sampling"',
				results: [],
				status: 'no results.'
			}
		},

		methods: {
			onSubmit: function() {
				let timepoint1 = performance.now();
				var that = this;
				
				console.log('Fetching data...');

				this.status = 'collecting papers...';

				jQuery.ajax({
					url: '/tesc',
					data: { 
						start: 	this.start, 
						end: 	this.end, 
						search: this.search
					},
					type: 'POST',
					success: function(response) {
						console.log(`Response collected.`);

						that.results = JSON.parse(response);
						that.status = `Found ${that.results.length} papers in ${((performance.now() - timepoint1) / 1000).toFixed(2)} seconds.`;
					}
				});
			}
		}
	}
</script>


<style lang="scss" scoped>
</style>