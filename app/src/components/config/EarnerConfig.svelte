<script lang="ts">
    import {onMount} from 'svelte';
    import {useQueryClient, createQuery, createMutation} from '@tanstack/svelte-query';
    import {getEarnersHeartBeat, getMachines, getSettings} from "$lib/api";

    export let name: string;
    export let img: string;
    export let description: string;
    export let signup_link: string;
    export let options: { name: string, value: string }[] = [];
    export let show_extra_data_list: boolean = false;
    export let extra_data_propperty: string | null = null;

    const client = useQueryClient();

    const settings = createQuery({
        queryKey: ['settings'],
        queryFn: getSettings
    });

    onMount(async () => {
        const data = await client.fetchQuery({
            queryKey: ['settings'],
            queryFn: getSettings
        });
        const eanerSetting = data.find((s: any) => s.name === name);
        if (eanerSetting) {
            options = options.map(option => ({
                name: option.name,
                value: eanerSetting.settings[option.name] || ''
            }));
        }

    });

    const earnerHeartbeat = createQuery({
        queryKey: ['earnerHeartbeat', name],
        queryFn: () => getEarnersHeartBeat(name)
    });

    const settingsMutation = createMutation({
        mutationFn: () => {
            const payload = options.reduce((acc, option) => {
                acc[option.name] = option.value;
                return acc;
            }, {});

            return fetch(`/api/earners/${name}/settings/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({"settings": payload}),
            });
        },
        onMutate: async (data) => {
            await client.cancelQueries('settings');
            const previousValue = client.getQueryData('settings');
            client.setQueryData('settings', data);
            return {previousValue};
        },
        onError: (err, data, context) => {
            client.setQueryData('settings', context.previousValue);
        },
        onSettled: () => {
            client.invalidateQueries('settings');
        },
    });

</script>

<div class="bg-slate-50 rounded p-2">
    <div class="grid grid-cols-2 mb-6">
        <div>
            <h3 class="font-medium text-xl">{name}</h3>
            <p>{@html description}</p>
            <a href={signup_link} class="bg-blue-500 text-white rounded px-2 py-1">Sign up -&gt;</a>
        </div>
        <div class="flex justify-center items-center">
            <a href="{signup_link}">
                <img src="static{img}" alt={name} class="w-auto h-20 object-cover rounded">
            </a>
        </div>
    </div>

    <div class="flex flex-col gap-2">
        {#each options as option (option.name)}
            <div class="grid grid-cols-8 gap-6 w-full">
                <label class="font-medium col-span-2 md:col-span-1 text-right" for="{option.name}">{option.name}
                    :</label>
                <input
                        class="w-full rounded px-1 py-0.5 bg-slate-100 col-span-6 md:col-span-7 border border-slate-300 active:border-blue-300 active:shadow"
                        id="{option.name}" type="text" bind:value={option.value}>
            </div>
        {/each}
        {#if show_extra_data_list}
            {#if $earnerHeartbeat.isFetching}
                <div>Loading...</div>
            {:else}
                {#if $earnerHeartbeat.isError}
                    <div>Error: {$earnerHeartbeat.error.message}</div>
                {/if}
                {#if $earnerHeartbeat.isSuccess}
                    {#each $earnerHeartbeat.data as entry}
                        <div>{entry.from_client_id} : {entry.extra_data[extra_data_propperty]}</div>
                    {/each}
                {/if}
            {/if}
        {/if}
    </div>
    <button class="bg-blue-500 text-white rounded px-2 py-1 mt-2" on:click={$settingsMutation.mutate()}>Save and
        send to
        clients
    </button>
</div>