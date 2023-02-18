import axios from "axios"

const service = axios.create({
    baseURL: "http://127.0.0.1:8000",
    // baseURL: `${window.location.origin}/label`,
    timeout: 6000
})

export default service;