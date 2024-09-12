import { writable } from 'svelte/store';

// Create stores
export const clients = writable({});
export const configs = writable({});
export const earners = writable({})
export const uuids = writable([]);

// Fetch initial config data
fetch('/api/earners/settings')
	.then(response => response.json())
	.then(data => {
		configs.set(data);
	})
	.catch(error => console.error('Error fetching config data:', error));

// Fetch initial client data
fetch('/api/clients/')
	.then(response => response.json())
	.then(data => {
		clients.set(data);
	})
	.catch(error => console.error('Error fetching client data:', error));

export function updateConfig(topic, data) {
	configs.update(config => ({ ...config, [topic]: data }));
	fetch(`/api/earners/${topic}/settings`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	}).catch(error => console.error('Error updating config:', error));
}

export function updateClient(device_name: string, client_name: string, data: object) {
	clients.update(clients => {
		if (!clients[device_name]) {
			clients[device_name] = {};
		}
		clients[device_name][client_name] = data;
		return clients;
	});
	fetch(`/api/clients/${device_name}/${client_name}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	}).catch(error => console.error('Error updating client:', error));
}