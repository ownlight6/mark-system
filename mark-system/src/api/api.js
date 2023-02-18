import request from "../utils/request"

export default {
    // 文件目录
    documentMenu(data) {
        return request({
            url: "/initWeb/get_txtcatalog/",
            method: "post",
            data
        })
    },
    // 上传文件
    docUpload(data) {
        return request({
            url: "/initWeb/upload/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    },
    // 文章内容
    docText(data) {
        return request({
            url: "/initWeb/get_text/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    },
    // 标注文件目录
    annMenu(data) {
        return request({
            url: "/initWeb/get_annCatalog/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    },
    // 新建标注文件
    createAnn(data) {
        return request({
            url: "/other/makeFilename/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    },
    // 获取标注文件
    annContent(data) {
        return request({
            url: "/other/readAll/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    },
    // 更新标注文件
    updateAnn(data) {
        return request({
            url: "/createAnn/create/",
            method: "post",
            headers: {
                'Content-type' : 'multipart/form-data'
            },
            data
        })
    }
}