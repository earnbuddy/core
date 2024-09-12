<script lang="ts">
	import { onMount } from 'svelte';
	import ClientListItem from './ClientListItem.svelte';

	let clientsData = [];

	onMount(async () => {
		try {
			const response = await fetch('/api/clients/');
			clientsData = await response.json();
		} catch (error) {
			console.error('Error fetching client data:', error);
		}
	});
</script>

<div class="bg-slate-50 rounded p-2">
	<table class="w-full">
		<thead class="font-medium">
		<tr>
			<td>Name</td>
			<td>Public ip</td>
			<td>Status</td>
			<td>Earners</td>
			<td>Client version</td>
			<td>Docker version</td>
			<td>OS type</td>
			<td>actions</td>
		</tr>
		</thead>
		<tbody>
		{#each clientsData as client}
			<ClientListItem {client} />
		{/each}
		</tbody>
	</table>
</div>
