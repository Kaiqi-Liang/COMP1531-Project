import axios from 'axios';
import qs from 'qs';

import { url } from './utils/constants';

axios.defaults.baseURL = url;
axios.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.delete['Content-Type'] = 'application/x-www-form-urlencoded';

axios.interceptors.request.use((request) => {
    if (request.method === 'put' || request.method === 'post' || request.method === 'delete') {
        request.data = qs.stringify(request.data);
    }
    return request;
});