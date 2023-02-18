<template>
  <div class="initContainer">
    <div class="header">
      <div class="title">标注系统</div>
      <el-button type="primary" @click="clickUpload()">上传文件</el-button>
      <input ref="file" type="file" style="display: none" @change="onChange" />
    </div>
    <div class="selectContainer">
      <div class="docBox">
        <div class="title">选择文件</div>
        <div class="docSelect">
          <el-tree
            class="docTree"
            :data="docMenu"
            :props="docProp"
            @node-click="docNodeClick"
          ></el-tree>
        </div>
      </div>
      <div class="docBox" v-if="annMenu.length">
        <div class="title">选择标注</div>
        <div class="docSelect">
          <el-tree
            class="docTree"
            :data="annMenu"
            :props="docProp"
            @node-click="annNodeClick"
          ></el-tree>
        </div>
      </div>
    </div>
    <div class="backImg"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 文件目录数据
      docMenu: {},
      // 文件目录prop
      docProp: {
        label: "name",
        children: "children",
      },
      // 标注目录
      annMenu: {},
      // 当前选择的文件
      docName: "",
    };
  },
  created() {
    this.getDocumentMenu();
  },
  methods: {
    // 点击上传
    clickUpload() {
      this.$refs.file.click();
    },
    // 上传文件
    onChange() {
      const file = this.$refs.file?.files[0];
      const formData = new FormData();
      formData.append("file", file);
      this.$api.docUpload(formData).then((res) => {
        this.$message.success(res.data.msg);
        this.getDocumentMenu();
      });
    },
    // 获取文件目录
    getDocumentMenu() {
      this.$api
        .documentMenu({
          getWhat: "catalog",
        })
        .then((res) => {
          this.docMenu = JSON.parse(res.data.catalog);
        });
    },
    // 点击文件
    docNodeClick(data, node) {
      if (data.type == "leaf") {
        let doc = node.parent.data.name + "/" + data.name;
        console.log(doc);
        this.docName = doc;
        this.getAnnMenu(doc);
      }
    },
    // 获取标注
    getAnnMenu(doc) {
      const formData = new FormData();
      formData.append("pathname", doc);
      this.$api.annMenu(formData).then((res) => {
        this.annMenu = JSON.parse(res.data.annCatalog);
      });
    },
    // 点击标注
    annNodeClick(data) {
      let ann = this.docName.split("/")[0] + "/" + data.name;
      this.$router.push({
        path: "mark",
        query: {
          doc: JSON.stringify(this.docName),
          ann: JSON.stringify(ann),
        },
      });
    },
  },
};
</script>

<style lang="scss">
.initContainer {
  width: 100%;
  height: 100vh;
  position: relative;
  padding: 40px;
  box-sizing: border-box;
  overflow: hidden;
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    .title {
      font-size: 40px;
    }
  }
  .selectContainer {
    display: flex;
    .docBox {
      position: relative;
      z-index: 2;
      margin-top: 40px;
      width: 50%;
      .title {
        font-size: 22px;
        color: #999;
        font-weight: 100;
      }
      .docSelect {
        margin-top: 10px;
        width: 100%;
        height: 500px;
        overflow-y: auto;
        .docTree {
          background-color: transparent;
        }
      }
    }
  }
  .backImg {
    position: absolute;
    right: 0px;
    bottom: -50px;
    width: 600px;
    height: 600px;
    background-image: url("../static/img/doc.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    z-index: 0;
  }
}
</style>