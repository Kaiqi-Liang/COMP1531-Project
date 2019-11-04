let isPolling = false;
export const getIsPolling = () => isPolling;
export const setIsPolling = bool => isPolling = !!bool; // force boolean type
export const pollingInterval = 2000;
export let stepSubscribers = [];
export const subscribeToStep = (subscriber) => stepSubscribers.push(subscriber);
export const unsubscribeToStep = (unsubscriber) => stepSubscribers = stepSubscribers.filter(subscriber => subscriber !== unsubscriber);
export const step = () => stepSubscribers.forEach(subscriber => subscriber());
