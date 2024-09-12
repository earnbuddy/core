<script lang="ts">
	import ClientEarnerList from './ClientEarnerList.svelte';

	let isOnline = true;
	export let client: any;

</script>

<tr class="hover:bg-slate-200">
	<td>{client.device_name}</td>
	<td>{client.public_ip}</td>
	<td>
		{client.last_ping ? new Date(client.last_ping).toLocaleString() : 'never'}
		<!--{#if isOnline}-->
		<!--	<span class="bg-green-700 text-white rounded px-1 py-0.5">online</span>-->
		<!--{:else}-->
		<!--	<span class="bg-red-700 text-white rounded px-1 py-0.5">offline</span>-->
		<!--{/if}-->
	</td>
	<td>
		<ClientEarnerList client={client.device_name}/>
	</td>
	<td>{client.client_version}</td>
	<td>{client.docker_version ? client.docker_version : '-'}</td>
	<td>{client.system_platform}</td>
	<td><button class="bg-blue-300 rounded px-1 py-0.5">Do</button></td>
</tr>
