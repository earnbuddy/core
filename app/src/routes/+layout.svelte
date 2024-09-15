<script>
    import "../app.css";

    import {browser} from '$app/environment'
    import {QueryClient, QueryClientProvider} from '@tanstack/svelte-query'

    const queryClient = new QueryClient({
        defaultOptions: {
            queries: {
                enabled: browser,
            },
        },
    })
</script>

<QueryClientProvider client={queryClient}>
    <div class="bg-slate-500 min-h-screen">
        <div class="container mx-auto">
            <slot/>
        </div>
    </div>
</QueryClientProvider>