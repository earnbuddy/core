<script lang="ts">
    import {onMount} from 'svelte';
    import {configs} from '$lib/api';
    import {updateConfig} from '$lib/api';

    export let name: string;
    export let img: string;
    export let description: string;
    export let signup_link: string;
    export let options: { name: string, value: string }[] = [];

    onMount(() => {
        const unsubscribe = configs.subscribe(config => {
            // Convert config object to an array and find the config based on the name from the api
            const configData = Object.values(config).find((c: any) => c.id === name);
            if (configData) {
                const settings = configData.settings;
                // Merge the options with the settings from the API
                options = options.map(option => ({
                    name: option.name,
                    value: settings[option.name] || option.value
                }));
            }
        });
        return unsubscribe;
    });

    function saveConfig() {
        const config = options.reduce((acc, option) => {
            acc[option.name] = option.value;
            return acc;
        }, {});
        updateConfig(name, config);
    }

</script>

<div class="bg-slate-50 rounded p-2">
    <div class="grid grid-cols-2 mb-6">
        <div>
            <h3 class="font-medium text-xl">{name}</h3>
            <p>{description}</p>
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
                <label class="font-medium col-span-2 md:col-span-1 text-right" for="{option.name}">{option.name}
                    :</label>
                <input
                        class="w-full rounded px-1 py-0.5 bg-slate-100 col-span-6 md:col-span-7 border border-slate-300 active:border-blue-300 active:shadow"
                        id="{option.name}" type="text" bind:value={option.value}>
            </div>
        {/each}
    </div>
    <button class="bg-blue-500 text-white rounded px-2 py-1 mt-2" on:click={saveConfig}>Save and send to clients
    </button>
</div>
