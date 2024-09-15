<script lang="ts">
    import { onMount } from 'svelte';
    import { useQueryClient, createQuery, createMutation } from '@tanstack/svelte-query';
    import { settingsQuery } from "$lib/queries";

    export let name: string;
    export let img: string;
    export let description: string;
    export let signup_link: string;
    export let options: { name: string, value: string }[] = [];
    export let show_extra_data_list: boolean = false;
    export let extra_data_propperty: string | null = null;

    const client = useQueryClient();

    let settings = [];

    // Fetch settings on mount
    onMount(async () => {
        const response = await fetch('/api/earners/settings/');
        settings = await response.json();
        const earnerSettings = settings.find(setting => setting.id === name);
        if (earnerSettings) {
            options = earnerSettings.settings.options;
        }
    });

    const updateMutation = createMutation({
        mutationFn: async (data: any) => {
            const response = await fetch(`/api/earners/${name}/settings/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            return response.json();
        },
        onSuccess: () => client.invalidateQueries({ queryKey: 'settings' }),
    });

    function saveConfig() {
        $updateMutation.mutate({ name, options });
    }
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
                <img src={img} alt={name} class="w-auto h-20 object-cover rounded">
            </a>
        </div>
    </div>

    <div class="flex flex-col gap-2">
        {#each options as option (option.name)}
            <div class="grid grid-cols-8 gap-6 w-full">
                <label class="font-medium col-span-2 md:col-span-1 text-right" for="{option.name}">{option.name}:</label>
                <input
                    class="w-full rounded px-1 py-0.5 bg-slate-100 col-span-6 md:col-span-7 border border-slate-300 active:border-blue-300 active:shadow"
                    id="{option.name}" type="text" bind:value={option.value}>
            </div>
        {/each}
        {#if show_extra_data_list}
        {/if}
    </div>
    <button class="bg-blue-500 text-white rounded px-2 py-1 mt-2" on:click={saveConfig}>Save and send to clients</button>
</div>