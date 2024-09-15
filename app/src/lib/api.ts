
export const getMachines = async () => {
    const response = await fetch('/api/clients/');
    return await response.json();
}

export const getSettings = async () => {
    const response = await fetch('/api/earners/settings/');
    return await response.json();
}

export const getMachineHeartBeat = async (machineId: string) => {
    const response = await fetch(`/api/clients/${machineId}/earners/`);
    return await response.json();
}

export const getEarnersHeartBeat = async (earner_id: string) => {
    const response = await fetch(`/api/earners/${earner_id}/heartbeats/`);
    return await response.json();
}