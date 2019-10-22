import axios from 'axios';

import { url } from './utils/constants';

axios.defaults.baseURL = url;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
