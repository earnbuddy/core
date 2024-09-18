<script lang="ts">
    import ClientListItem from './MachineListItem.svelte';
    import { useQueryClient, createQuery } from '@tanstack/svelte-query'
    import {getMachines} from "$lib/api";

    const machines = createQuery({
        queryKey: ['machines'],
        queryFn: getMachines,
        refetchInterval: 10000,
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
        {#if $machines.isLoading}
            <tr>
                <td colspan="8">Loading...</td>
            </tr>
        {/if}
        {#if $machines.isError}
            <tr>
                <td colspan="8">Error: {$machines.error.message}</td>
            </tr>
        {/if}
        {#if $machines.isSuccess}
            {#each $machines.data as machine}
                <ClientListItem client={machine}/>
            {/each}
        {/if}
        </tbody>
    </table>
</div>