import { createQuery } from "@tanstack/svelte-query";

export const machinesQuery = () => {
    return createQuery({
        queryKey: ['machines'],
        queryFn: async () => await fetch('/api/clients/').then((r) => r.json()),
        refetchInterval: 5000,
    });
};

export const settingsQuery = () => {
    return createQuery({
        queryKey: ['settings'],
        queryFn: async () => await fetch('/api/earners/settings/').then((r) => r.json()),

    });
};