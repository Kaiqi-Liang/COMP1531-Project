
import qs from 'querystring';
import Axios from 'axios';

export const post = (url, payload) => {
    return Axios.post(url, qs.stringify(payload), { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }});
};

export const get = (url, payload) => {
    return Axios.get(url, qs.stringify(payload), { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }});
};

export const put = (url, payload) => {
    return Axios.put(url, qs.stringify(payload), { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }});
};

export const del = (url, payload) => {
    return Axios.delete(url, qs.stringify(payload), { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }});
};
