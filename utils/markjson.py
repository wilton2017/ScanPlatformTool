# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     markjson
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

test = {
    "log": {
        "version": "1.2",
        "creator": {
            "name": "WebInspector",
            "version": "537.36"
        },
        "pages": [
            {
                "startedDateTime": "2019-03-15T01:25:52.150Z",
                "id": "page_1",
                "title": "https://stg1-mark.yingxiang.pingan.com/",
                "pageTimings": {
                    "onContentLoad": 1555.1519999862649,
                    "onLoad": 1812.513000011677
                }
            }
        ],
        "entries": [
            {
                "startedDateTime": "2019-03-15T01:25:52.699Z",
                "time": 534.0980000114068,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "Upgrade-Insecure-Requests",
                            "value": "1"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-d37\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 476,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-d37\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 3383,
                        "mimeType": "text/html"
                    },
                    "redirectURL": "",
                    "headersSize": 212,
                    "bodySize": 0,
                    "_transferSize": 3595
                },
                "cache": {},
                "timings": {
                    "blocked": 11.4779999896418,
                    "dns": -1,
                    "ssl": 222.87200001301304,
                    "connect": 353.58700001961523,
                    "send": 0.9149999823420103,
                    "wait": 169.11800001980782,
                    "receive": 0,
                    "_blocked_queueing": -1,
                    "_blocked_proxy": 11.37299998663363
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "267",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.706Z",
                "time": 179.1203389938164,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/app.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-62a855\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 423,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-62a855\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 6465621,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 215,
                    "bodySize": 0,
                    "_transferSize": 215
                },
                "cache": {},
                "timings": {
                    "blocked": 4.3873389935761224,
                    "dns": -1,
                    "ssl": -1,
                    "connect": -1,
                    "send": 0.8190000080503497,
                    "wait": 155.57299999636598,
                    "receive": 20.34099999582395,
                    "_blocked_queueing": 0.3389999910723418,
                    "_blocked_proxy": 3.2169999903999296
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "261",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.706Z",
                "time": 215.35154499931377,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/js/agent.min.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-46f9\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 430,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-46f9\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 18169,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 6.457545010402101,
                    "dns": -1,
                    "ssl": -1,
                    "connect": -1,
                    "send": 0.7540000078734002,
                    "wait": 208.3099999872502,
                    "receive": 1.8299999937880784,
                    "_blocked_queueing": 0.5449999880511314,
                    "_blocked_proxy": 5.772999982582402
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "282",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.929Z",
                "time": 726.6134619954682,
                "request": {
                    "method": "GET",
                    "url": "https://wiseapm.yun.pingan.com/browser_upload/config/v1.7.0/87.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "Host",
                            "value": "wiseapm.yun.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 359,
                    "bodySize": 0
                },
                "response": {
                    "status": 200,
                    "statusText": "OK",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "content-encoding",
                            "value": "gzip"
                        },
                        {
                            "name": "Server",
                            "value": "nginx"
                        },
                        {
                            "name": "Transfer-Encoding",
                            "value": "chunked"
                        },
                        {
                            "name": "Content-Type",
                            "value": "text/json;charset=utf-8"
                        },
                        {
                            "name": "access-control-allow-origin",
                            "value": "*"
                        },
                        {
                            "name": "Access-Control-Allow-Credentials",
                            "value": "true"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Access-Control-Allow-Headers",
                            "value": "Content-Type,Accept"
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 103,
                        "mimeType": "text/json",
                        "compression": -23
                    },
                    "redirectURL": "",
                    "headersSize": 304,
                    "bodySize": 126,
                    "_transferSize": 430
                },
                "cache": {},
                "timings": {
                    "blocked": 10.018462000851333,
                    "dns": -1,
                    "ssl": 227.310999995098,
                    "connect": 341.713000001619,
                    "send": 0.8889999880919959,
                    "wait": 147.53300001029828,
                    "receive": 227.45999999460764,
                    "_blocked_queueing": 0.4619999963324517,
                    "_blocked_proxy": 9.407000005012378
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "377",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 725.2252219898801,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/0.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-7011\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 438,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-7011\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 28689,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 25.66822201522886,
                    "dns": -1,
                    "ssl": 89.89399997517398,
                    "connect": 185.2789999975358,
                    "send": 1.079999987268991,
                    "wait": 180.82000000867964,
                    "receive": 333.3779999811668,
                    "_blocked_queueing": 4.221999988658354,
                    "_blocked_proxy": 22.93900001677687
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "386",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 724.1691949816304,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/1.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-1e229\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-1e229\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 123433,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 32.056194995006095,
                    "dns": -1,
                    "ssl": 91.044999979203,
                    "connect": 179.2880000139117,
                    "send": 1.0639999818529873,
                    "wait": 112.35000001033731,
                    "receive": 400.4109999805223,
                    "_blocked_queueing": 4.194999986793846,
                    "_blocked_proxy": 26.31999997538519
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "398",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 722.6181840061035,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/10.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-14ad5\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 440,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "1"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-14ad5\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 84693,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 11.830184001737546,
                    "dns": -1,
                    "ssl": -1,
                    "connect": -1,
                    "send": 0.8859999943523995,
                    "wait": 303.3830000204034,
                    "receive": 408.51899998961017,
                    "_blocked_queueing": 4.18399999034591,
                    "_blocked_proxy": 9.90500001353213
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "272",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 721.19918299868,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/11.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-1e09e\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 440,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "1"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-1e09e\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 123038,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 14.990182994690235,
                    "dns": -1,
                    "ssl": -1,
                    "connect": -1,
                    "send": 0.9469999931753001,
                    "wait": 248.2200000085868,
                    "receive": 459.0420000022277,
                    "_blocked_queueing": 4.183000011835247,
                    "_blocked_proxy": 12.96400002320299
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "287",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 724.3461850197345,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/12.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-d785\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-d785\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 55173,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 31.65418501899696,
                    "dns": -1,
                    "ssl": 79.490000003716,
                    "connect": 184.375999990152,
                    "send": 0.6669999856970037,
                    "wait": 115.51600001985199,
                    "receive": 393.1330000050366,
                    "_blocked_queueing": 4.184999997960404,
                    "_blocked_proxy": 29.077000013785458
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "392",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 721.5392029973736,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/13.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-db9f\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:52 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "1"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-db9f\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 56223,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 20.084202987520307,
                    "dns": -1,
                    "ssl": -1,
                    "connect": -1,
                    "send": 1.0060000058728988,
                    "wait": 254.6889999939594,
                    "receive": 447.76000001002103,
                    "_blocked_queueing": 4.203000018605962,
                    "_blocked_proxy": 17.985000013140912
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "277",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.930Z",
                "time": 773.8414859948098,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/14.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-9e2a\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-9e2a\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 40490,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 13.87748597929019,
                    "dns": -1,
                    "ssl": 101.09199999715199,
                    "connect": 213.5100000014065,
                    "send": 1.6720000130590051,
                    "wait": 165.78099998878298,
                    "receive": 380.0010000122711,
                    "_blocked_queueing": 269.48600000469014,
                    "_blocked_proxy": 3.179999999702
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "409",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 766.3451169851178,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/15.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-ad0f\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-ad0f\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 44303,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 53.79711698539901,
                    "dns": -1,
                    "ssl": 83.65600000252002,
                    "connect": 177.9169999936129,
                    "send": 0.6740000098949963,
                    "wait": 118.61199999111653,
                    "receive": 416.34500000509433,
                    "_blocked_queueing": 281.11700000590645,
                    "_blocked_proxy": 4.924999986542393
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "431",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 766.8213880163094,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/16.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-af3b\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-af3b\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 44859,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 4.130387987097491,
                    "dns": -1,
                    "ssl": 110.3040000016334,
                    "connect": 202.9090000141877,
                    "send": 0.8680000028110157,
                    "wait": 116.49299997952744,
                    "receive": 443.4210000326857,
                    "_blocked_queueing": 321.38800001121126,
                    "_blocked_proxy": 2.917000005254524
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "423",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 774.0840269836481,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/17.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-ae4c\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-ae4c\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 44620,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 4.647027013532349,
                    "dns": -1,
                    "ssl": 135.861999995541,
                    "connect": 220.28199999476772,
                    "send": 0.9689999860709975,
                    "wait": 154.62700001080546,
                    "receive": 394.55899997847155,
                    "_blocked_queueing": 330.0269999890588,
                    "_blocked_proxy": 3.6790000158362064
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "415",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 779.4254409995337,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/18.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-988e\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-988e\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 39054,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 64.26544098867448,
                    "dns": -1,
                    "ssl": 76.12700000754597,
                    "connect": 171.24799999874108,
                    "send": 0.8329999982379945,
                    "wait": 173.6820000223813,
                    "receive": 370.3969999914989,
                    "_blocked_queueing": 337.4410000105854,
                    "_blocked_proxy": 3.009000007295979
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "448",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 780.3291749942,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/19.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-5d05\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-5d05\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 23813,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 4.422175001993306,
                    "dns": -1,
                    "ssl": 144.2380000080453,
                    "connect": 196.69800001429365,
                    "send": 0.6789999897590064,
                    "wait": 152.96800000942358,
                    "receive": 426.56199997873046,
                    "_blocked_queueing": 397.17499999096617,
                    "_blocked_proxy": 3.157999977702271
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "440",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 972.095939983672,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/2.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-8a2d\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 438,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-8a2d\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 35373,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 5.604940024262758,
                    "dns": -1,
                    "ssl": 84.763000020757,
                    "connect": 217.14699998847254,
                    "send": 0.865000009071025,
                    "wait": 114.84399999608246,
                    "receive": 634.6349999657832,
                    "_blocked_queueing": 632.9399999813177,
                    "_blocked_proxy": 4.267999989679085
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "474",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 1045.2364459942619,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/3.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-7098c\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-7098c\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 461196,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 109.08044599430283,
                    "dns": -1,
                    "ssl": 82.912000012584,
                    "connect": 176.17500000051197,
                    "send": 0.6160000048110419,
                    "wait": 107.38199998741084,
                    "receive": 652.9830000072252,
                    "_blocked_queueing": 646.4459999988321,
                    "_blocked_proxy": 4.776999994646762
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "512",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 1077.8834439888305,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/4.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-5de31\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-5de31\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 384561,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 13.289444003690708,
                    "dns": -1,
                    "ssl": 82.27600000100202,
                    "connect": 197.7970000007194,
                    "send": 0.629999994998002,
                    "wait": 115.51000000326934,
                    "receive": 751.6569999861531,
                    "_blocked_queueing": 748.4439999971073,
                    "_blocked_proxy": 5.567000014707443
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "518",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.931Z",
                "time": 1088.9846339984506,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/5.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-2951a\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-2951a\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 169242,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 8.854633992508756,
                    "dns": -1,
                    "ssl": 139.9039999814706,
                    "connect": 221.5150000120043,
                    "send": 0.7269999769060007,
                    "wait": 103.83100001490627,
                    "receive": 755.0570000021253,
                    "_blocked_queueing": 752.6340000040364,
                    "_blocked_proxy": 7.320000004256148
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "502",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.932Z",
                "time": 1341.4784479970112,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/6.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-1ff67\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-1ff67\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 130919,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 63.326447994215386,
                    "dns": -1,
                    "ssl": 84.89700002246599,
                    "connect": 204.1700000117995,
                    "send": 0.6850000063429889,
                    "wait": 100.20499999518478,
                    "receive": 974.0919999894686,
                    "_blocked_queueing": 972.4479999858886,
                    "_blocked_proxy": 3.1290000188165
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "545",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.932Z",
                "time": 1334.7987219765782,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/7.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-1cafb\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-1cafb\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 117499,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 74.72072202432898,
                    "dns": -1,
                    "ssl": 94.55700000398801,
                    "connect": 198.91899998765481,
                    "send": 1.7240000015589771,
                    "wait": 86.37400000588934,
                    "receive": 974.0609999571461,
                    "_blocked_queueing": 972.721999976784,
                    "_blocked_proxy": 5.8019999996759
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "564",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.932Z",
                "time": 1405.8026090058556,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/8.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-252a5\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-252a5\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 152229,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 5.946609012928089,
                    "dns": -1,
                    "ssl": 149.927999998908,
                    "connect": 247.21000000136007,
                    "send": 0.6489999941549911,
                    "wait": 121.63199999486065,
                    "receive": 1031.3650000025518,
                    "_blocked_queueing": 1029.6089999901596,
                    "_blocked_proxy": 4.099000012502071
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "537",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:52.932Z",
                "time": 1475.10283499246,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/9.js",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Purpose",
                            "value": "prefetch"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-2280f\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 439,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-2280f\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 141327,
                        "mimeType": "application/javascript"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 5.232835002359938,
                    "dns": -1,
                    "ssl": 87.013000011211,
                    "connect": 211.45199998863976,
                    "send": 0.5100000125819975,
                    "wait": 179.37999998684987,
                    "receive": 1079.5280000020284,
                    "_blocked_queueing": 1077.835000003688,
                    "_blocked_proxy": 3.3559999719727824
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "572",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:53.583Z",
                "time": 377.0888870227209,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/static/img/Group.ddfd681f.png",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "image/webp,image/apng,image/*,*/*;q=0.8"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-16dd0\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 481,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-16dd0\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 93648,
                        "mimeType": "image/png"
                    },
                    "redirectURL": "",
                    "headersSize": 214,
                    "bodySize": 0,
                    "_transferSize": 214
                },
                "cache": {},
                "timings": {
                    "blocked": 3.6838869840430535,
                    "dns": -1,
                    "ssl": 83.65200000116639,
                    "connect": 171.0000000020959,
                    "send": 1.3449999969450062,
                    "wait": 187.50299999373948,
                    "receive": 14.55700004589744,
                    "_blocked_queueing": 12.88700001896359,
                    "_blocked_proxy": 2.814999985275792
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "494",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:53.585Z",
                "time": 318.2904630165431,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/static/img/logo@3x.304777c0.png",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Accept",
                            "value": "image/webp,image/apng,image/*,*/*;q=0.8"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "If-None-Match",
                            "value": "\"5c870e10-1558\""
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "If-Modified-Since",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 482,
                    "bodySize": 0
                },
                "response": {
                    "status": 304,
                    "statusText": "Not Modified",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:53 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Last-Modified",
                            "value": "Tue, 12 Mar 2019 01:40:32 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "ETag",
                            "value": "\"5c870e10-1558\""
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 5464,
                        "mimeType": "image/png"
                    },
                    "redirectURL": "",
                    "headersSize": 213,
                    "bodySize": 0,
                    "_transferSize": 213
                },
                "cache": {},
                "timings": {
                    "blocked": 3.7094630139763454,
                    "dns": -1,
                    "ssl": 83.90600001439469,
                    "connect": 127.5159999786413,
                    "send": 1.6790000081529968,
                    "wait": 128.30400001257613,
                    "receive": 58.0820000031963,
                    "_blocked_queueing": 57.46300000464544,
                    "_blocked_proxy": 3.114000021014361
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "482",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:53.967Z",
                "time": 517.6604920015379,
                "request": {
                    "method": "POST",
                    "url": "https://wiseapm.yun.pingan.com/browser_upload/pf?av=1.7.0&v=1.9.3&key=iRiIZP9b7eQ&ref=https%3A%2F%2Fstg1-mark.yingxiang.pingan.com%2F%23%2F&referer=&base=&rand=1552613153967&pvid=e6aead00-94cc-406e-b038-8cf703ba8c94&aid=87&if=0&ns=1552613152145&f=4&ds=4&de=4&cs=17&ce=371&sl=148&qs=371&rs=541&re=555&ol=555&oi=1554&os=1554&oe=1554&oc=1817&ls=1817&le=1817&je=0&gid=&bl=0&sh=1080&sw=1920&fs=1517&sp=0",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Origin",
                            "value": "https://stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Host",
                            "value": "wiseapm.yun.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        },
                        {
                            "name": "Content-Type",
                            "value": "text/plain;charset=UTF-8"
                        },
                        {
                            "name": "Accept",
                            "value": "*/*"
                        },
                        {
                            "name": "Cache-Control",
                            "value": "max-age=0"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "Content-Length",
                            "value": "59"
                        }
                    ],
                    "queryString": [
                        {
                            "name": "av",
                            "value": "1.7.0"
                        },
                        {
                            "name": "v",
                            "value": "1.9.3"
                        },
                        {
                            "name": "key",
                            "value": "iRiIZP9b7eQ"
                        },
                        {
                            "name": "ref",
                            "value": "https%3A%2F%2Fstg1-mark.yingxiang.pingan.com%2F%23%2F"
                        },
                        {
                            "name": "referer",
                            "value": ""
                        },
                        {
                            "name": "base",
                            "value": ""
                        },
                        {
                            "name": "rand",
                            "value": "1552613153967"
                        },
                        {
                            "name": "pvid",
                            "value": "e6aead00-94cc-406e-b038-8cf703ba8c94"
                        },
                        {
                            "name": "aid",
                            "value": "87"
                        },
                        {
                            "name": "if",
                            "value": "0"
                        },
                        {
                            "name": "ns",
                            "value": "1552613152145"
                        },
                        {
                            "name": "f",
                            "value": "4"
                        },
                        {
                            "name": "ds",
                            "value": "4"
                        },
                        {
                            "name": "de",
                            "value": "4"
                        },
                        {
                            "name": "cs",
                            "value": "17"
                        },
                        {
                            "name": "ce",
                            "value": "371"
                        },
                        {
                            "name": "sl",
                            "value": "148"
                        },
                        {
                            "name": "qs",
                            "value": "371"
                        },
                        {
                            "name": "rs",
                            "value": "541"
                        },
                        {
                            "name": "re",
                            "value": "555"
                        },
                        {
                            "name": "ol",
                            "value": "555"
                        },
                        {
                            "name": "oi",
                            "value": "1554"
                        },
                        {
                            "name": "os",
                            "value": "1554"
                        },
                        {
                            "name": "oe",
                            "value": "1554"
                        },
                        {
                            "name": "oc",
                            "value": "1817"
                        },
                        {
                            "name": "ls",
                            "value": "1817"
                        },
                        {
                            "name": "le",
                            "value": "1817"
                        },
                        {
                            "name": "je",
                            "value": "0"
                        },
                        {
                            "name": "gid",
                            "value": ""
                        },
                        {
                            "name": "bl",
                            "value": "0"
                        },
                        {
                            "name": "sh",
                            "value": "1080"
                        },
                        {
                            "name": "sw",
                            "value": "1920"
                        },
                        {
                            "name": "fs",
                            "value": "1517"
                        },
                        {
                            "name": "sp",
                            "value": "0"
                        }
                    ],
                    "cookies": [],
                    "headersSize": 827,
                    "bodySize": 59,
                    "postData": {
                        "mimeType": "text/plain;charset=UTF-8",
                        "text": "{\"tr\":true,\"tt\":\"mark-platform\",\"charset\":\"UTF-8\",\"res\":[]}"
                    }
                },
                "response": {
                    "status": 200,
                    "statusText": "OK",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Server",
                            "value": "nginx"
                        },
                        {
                            "name": "Content-Type",
                            "value": "text/json;charset=utf-8"
                        },
                        {
                            "name": "access-control-allow-origin",
                            "value": "*"
                        },
                        {
                            "name": "Access-Control-Allow-Credentials",
                            "value": "true"
                        },
                        {
                            "name": "Connection",
                            "value": "close"
                        },
                        {
                            "name": "Access-Control-Allow-Headers",
                            "value": "Content-Type,Accept"
                        },
                        {
                            "name": "Content-Length",
                            "value": "0"
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 0,
                        "mimeType": "text/json",
                        "compression": 0
                    },
                    "redirectURL": "",
                    "headersSize": 271,
                    "bodySize": 0,
                    "_transferSize": 271
                },
                "cache": {},
                "timings": {
                    "blocked": 6.663492007384777,
                    "dns": -1,
                    "ssl": 164.905999990879,
                    "connect": 287.45699999854014,
                    "send": 2.6519999955780236,
                    "wait": 220.78800000599546,
                    "receive": 1.0999999940395355,
                    "_blocked_queueing": 0.49199999193660915,
                    "_blocked_proxy": 6.437000003643333
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "558",
                "pageref": "page_1"
            },
            {
                "startedDateTime": "2019-03-15T01:25:53.968Z",
                "time": 301.3061159901554,
                "request": {
                    "method": "GET",
                    "url": "https://stg1-mark.yingxiang.pingan.com/favicon.ico",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Accept",
                            "value": "image/webp,image/apng,image/*,*/*;q=0.8"
                        },
                        {
                            "name": "Connection",
                            "value": "keep-alive"
                        },
                        {
                            "name": "Accept-Encoding",
                            "value": "gzip, deflate, br"
                        },
                        {
                            "name": "Referer",
                            "value": "https://stg1-mark.yingxiang.pingan.com/"
                        },
                        {
                            "name": "Host",
                            "value": "stg1-mark.yingxiang.pingan.com"
                        },
                        {
                            "name": "Accept-Language",
                            "value": "zh-CN,zh;q=0.9"
                        },
                        {
                            "name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
                        }
                    ],
                    "queryString": [],
                    "cookies": [],
                    "headersSize": 380,
                    "bodySize": 0
                },
                "response": {
                    "status": 404,
                    "statusText": "Not Found",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {
                            "name": "Date",
                            "value": "Fri, 15 Mar 2019 01:25:54 GMT"
                        },
                        {
                            "name": "Via",
                            "value": "HTTPS/1.1 PINGAN-WCG01"
                        },
                        {
                            "name": "Server",
                            "value": "nginx/1.12.1"
                        },
                        {
                            "name": "Age",
                            "value": "0"
                        },
                        {
                            "name": "Content-Length",
                            "value": "571"
                        },
                        {
                            "name": "Content-Type",
                            "value": "text/html"
                        }
                    ],
                    "cookies": [],
                    "content": {
                        "size": 571,
                        "mimeType": "text/html",
                        "compression": 0
                    },
                    "redirectURL": "",
                    "headersSize": 168,
                    "bodySize": 571,
                    "_transferSize": 739
                },
                "cache": {},
                "timings": {
                    "blocked": 8.774116008658897,
                    "dns": -1,
                    "ssl": 127.43199997930739,
                    "connect": 177.04599999706255,
                    "send": 0.5470000032800044,
                    "wait": 114.08199998550134,
                    "receive": 1.8569999956525862,
                    "_blocked_queueing": 1.1159999994561076,
                    "_blocked_proxy": 7.938000024296347
                },
                "serverIPAddress": "10.37.84.36",
                "connection": "531",
                "pageref": "page_1"
            }
        ]
    }
}
