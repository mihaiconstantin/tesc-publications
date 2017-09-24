<template>
	<div class="app-paper shadow">	
		
		<div class="row paper-title">
			<div class="col-md-12">
				<h5>Paper title: <a v-bind:href="paper.url" target="_blank">{{ paper.title }}</a><small> - </small><small class="text-muted">{{ paper.doi }}</small></h5>
			</div>
		</div>

		<div class="row">
			<div class="col-md-3">
				<strong>TESC authors:</strong>
				<ul class="">
					<li v-for="tescAuthor in paper.tesc_authors">{{ tescAuthor }}</li>
				</ul>
			</div>

			<div class="col-md-3">
				<strong>External authors:</strong>
				<ul class="">
					<li v-for="externalAuthor in paper.external_authors">{{ externalAuthor }}</li>
				</ul>
			</div>

			<div class="col-md-6">
				<p><strong>Abstract: </strong>{{ paper.abstract }}</p>
			</div>
		</div>

	</div>
</template>


<script>
	export default {
		props: ['paper']
	}
</script>


<style lang="scss" scoped>
	
	.app-paper {
		padding: 1rem;
		border-radius: 1rem;
		margin-bottom: 1.5rem;
	}

	.paper-title {
		margin-bottom: 1rem;
	}

	ul li {
		font-size: .95rem;
	}

	.shadow {
	  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
	  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
	}

	.shadow:hover {
	  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
	}
</style>