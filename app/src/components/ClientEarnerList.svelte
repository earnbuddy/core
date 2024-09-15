<script lang="ts">
    import {createQuery, useQueryClient} from "@tanstack/svelte-query";
    import {getMachineHeartBeat} from "$lib/api";

    export let machine_name;

    const client = useQueryClient();

    const earners = createQuery({
        queryKey: ['earners', machine_name],
        queryFn: () => getMachineHeartBeat(machine_name),
        refetchInterval: 10000,
    });

</script>

<div class="flex gap-1 flex-wrap">
    {#if $earners.isLoading}
        <span>Loading...</span>
    {/if}
    {#if $earners.isSuccess }
        {#each $earners.data as earner}
            <div class="bg-gray-400 rounded flex gap-1 items-center px-1 py-0.5 w-fit text-xs">
                <h2>{earner.from_earner}</h2>
                <span class="bg-green-700 rounded-full p-1"></span>
            </div>
        {/each}
    {/if}
</div>