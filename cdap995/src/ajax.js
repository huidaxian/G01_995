import axios from 'axios';

const SERVICE_PATH = "http://127.0.0.1:9898/data/"

const service = axios.create({
    // process.env.NODE_ENV === 'development' 来判断是否开发环境
    // easy-mock服务挂了，暂时不使用了
    // baseURL: 'https://www.easy-mock.com/mock/592501a391470c0ac1fab128',
    timeout: 5000
});

// query一般是查询条件，对post就是body，对get就是querystring
export const fetchData = (meth, url, query) => {
    return service({
        url: SERVICE_PATH + url,
        method: meth,
        data: query
    });
};
