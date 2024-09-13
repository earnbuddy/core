<script lang="ts">
    import ClientList from '../components/ClientList.svelte';
    import Config from '../components/config/Config.svelte';
    import { useQueryClient } from '@tanstack/svelte-query';
    import { machinesQuery } from "$lib/queries";

    const client = useQueryClient();

    $: machines = machinesQuery();
</script>
<div class="flex flex-col gap-2 pt-6 px-2">
    <h1 class="text-white font-medium text-center text-4xl">Earn Buddy</h1>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2">

        <div class="bg-slate-50 rounded p-2 text-center">
            <span class="font-medium text-3xl">{#if $machines.isSuccess}{$machines.data.length}{/if}</span>
            <h3 class="mx-auto">Online clients</h3>
        </div>

        <div class="bg-slate-50 rounded p-2 text-center">
            <span class="font-medium text-3xl">100</span>
            <h3 class="mx-auto">Online clients</h3>
        </div>

        <div class="bg-slate-50 rounded p-2 text-center">
            <span class="font-medium text-3xl">100</span>
            <h3 class="mx-auto">Online clients</h3>
        </div>

        <div class="bg-slate-50 rounded p-2 text-center">
            <span class="font-medium text-3xl">100</span>
            <h3 class="mx-auto">Online clients</h3>
        </div>

    </div>

    <ClientList/>

    <Config/>
</div>
