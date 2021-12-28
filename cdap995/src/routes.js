import index from "./pages/index.vue"
import login from "./pages/login.vue"
import home from "./pages/home.vue"
import salesTrend from "./pages/salesTrend.vue"
import salesComparison from "./pages/salesComparison.vue"
import hotSalesArea from "./pages/hotSalesArea.vue"
import priceComparison from "./pages/priceComparison.vue"
import carPurpose from "./pages/carPurpose.vue"
import scoreAnalysis from "./pages/scoreAnalysis.vue"
import fuelAnalysis from "./pages/fuelAnalysis.vue"
import message from "./pages/message.vue"
import user from "./pages/user.vue"
import admin from "./pages/admin.vue"

var routes =[
    {
        path: '/',
        redirect: '/login'
    },
    {
        path:'/admin.html',
        name:"admin",
        component:admin,

    },
    {
        path:"/index",
        name:"index",
        component:index,
        redirect: '/index/home.html',
        children: [
            {
                path: "home.html",
                name: "home",
                meta: {
                    title: '系统首页'
                },
                component: home,
            }, {
                path: "salesTrend.html",
                name: "salesTrend",
                meta: {
                    title: '销售趋势'
                },
                component: salesTrend,
            },
            {
                path: "salesComparison.html",
                name: "salesComparison",
                meta: {
                    title: '销量对比'
                },
                component: salesComparison,
            }, {
                path: "hotSalesArea.html",
                name: "hotSalesArea",
                meta: {
                    title: '销售热点区域'
                },
                component: hotSalesArea,
            },
            {
                path: "priceComparison.html",
                name: "priceComparison",
                meta: {
                    title: '价格对比'
                },
                component: priceComparison,
            }, {
                path: "carPurpose.html",
                name: "carPurpose",
                meta: {
                    title: '购车目的'
                },
                component: carPurpose,
            },
            {
                path: "scoreAnalysis.html",
                name: "scoreAnalysis",
                meta: {
                    title: '指标分析'
                },
                component: scoreAnalysis,
            }, {
                path: "fuelAnalysis.html",
                name: "fuelAnalysis",
                meta: {
                    title: '油耗分析'
                },
                component: fuelAnalysis,
            },
            {
                path: "message.html",
                name: "message",
                meta: {
                    title: '消息通知'
                },
                component: message,
            },
            {
                path: "user.html",
                name: "user",
                meta: {
                    title: '个人中心'
                },
                component: user,
            }
        ]
    },
    {
        path:"/login",
        name:"login",
        component:login
    },
];

export {routes}