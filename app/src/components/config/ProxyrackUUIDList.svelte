<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { clients, uuids } from '$lib/api';

	export let name: string;
	export let img: string;
	export let description: string;
	export let signup_link: string;

</script>

<div class="bg-slate-50 rounded p-2">
	<div class="grid grid-cols-2 mb-6">
		<div>
			<h3 class="font-medium text-xl">{name}</h3>
			<p>{description}</p>
			<button class="bg-blue-500 text-white rounded px-2 py-1">Sign up -></button>
		</div>
		<div>
			<a href="{signup_link}">
				<img src={img} alt={name} class="w-full h-14 object-cover">
			</a>
		</div>
	</div>
	<div>
		<h4 class="font-medium">UUID List:</h4>
		<ul>
			{#each $uuids as item (item.uuid)}
				<li>{item.device_name} - {item.uuid}</li>
			{/each}
		</ul>
		<p class="font-medium text-red-500">You need to manually add these to your account</p>
	</div>
</div>
