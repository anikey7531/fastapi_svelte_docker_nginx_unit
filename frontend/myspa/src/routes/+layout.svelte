<script>
	import "../app.css";
    import Aside from './Aside.svelte';
</script>

<div class="app">
	<div class="text-blueGray-700 antialiased">


			  <Aside/>

		<!-- Основное содержимое страницы -->
		<main class="md:ml-64 bg-blueGray-100">

			<slot />
			
		</main>

	  </div>
	


</div>

<style>

</style>
