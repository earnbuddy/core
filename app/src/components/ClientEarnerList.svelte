<script lang="ts">
	import { onMount } from 'svelte';

	export let client;
	let earners = [];

</script>

<div class="flex gap-1 flex-wrap">
	{#each earners as earner}
		<div class="bg-gray-400 rounded flex gap-1 items-center px-1 py-0.5 w-fit text-xs">
			<h2>{earner.from_earner}</h2>

				<span class="bg-green-700 rounded-full p-1"></span>

		</div>
	{/each}
</div>