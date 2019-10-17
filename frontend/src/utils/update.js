let isPolling = false;
export const getIsPolling = () => isPolling;
export const setIsPolling = bool => isPolling = !!bool; // force boolean type
export const pollingInterval = 1000;
export const stepSubscribers = [];
export const subscribeToStep = (subscriber) => stepSubscribers.push(subscriber);
export const unsubscribeToStep = (unsubscriber) => stepSubscribers = stepSubscribers.filter(subscriber => subscriber !== unsubscriber);
export const step = () => stepSubscribers.forEach(subscriber => subscriber());
