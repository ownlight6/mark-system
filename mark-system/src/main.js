import { createApp } from 'vue'
import App from './App.vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import annotator from "annotator"

import router from "./router/index.js"
import api from './api/api'

import "./static/base.js"
import './static/base.css'

const app = createApp(App)
app.config.globalProperties.$api = api

app.use(ElementPlus)
    .use(router)
    .use(annotator)
    .mount('#app')