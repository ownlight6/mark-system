<template>
  <el-container class="bodyContainer">
    <el-header class="headerContainer">
      <div class="title">{{ doc }}</div>
      <el-row>
        <el-button type="primary" @click="loadFunc">加载ann</el-button>
        <el-button type="primary" @click="loadFunc">导出ann</el-button>
        <el-button type="primary" @click="selectDoc()">选择文件</el-button>
        <el-button type="primary">保存标注</el-button>
      </el-row>
    </el-header>
    <el-container class="mainContainer">
      <el-aside class="menuBox" v-if="0">目录 </el-aside>
      <el-main class="articleContainer" @click="selectText">
        <p class="line" v-for="(ele, index) in article" :key="index">
          {{ ele.isBase64() ? "" : ele }}
          <img v-if="ele.isBase64()" :src="getBase64(ele)" alt="" />
        </p>
      </el-main>
      <el-aside class="markContainer">
        <div class="title">标注信息</div>
        <el-row>
          <el-button
            plain
            size="small"
            type="primary"
            @click="filterAnn('实体')"
            >实体</el-button
          >
          <el-button
            plain
            size="small"
            type="primary"
            @click="filterAnn('属性')"
            >属性</el-button
          >
        </el-row>
        <div
          class="markLine"
          v-for="(ele, index) in annTable"
          :key="index"
          @click="scrollView(ele.id)"
        >
          <div class="cate line">
            <el-tag>类型</el-tag>{{ ele.cate }} {{ ele.name }}
          </div>
          <div class="quote line"><el-tag>标注文本</el-tag>{{ ele.quote }}</div>
          <div class="text line">
            <el-tag>标注内容</el-tag>
            <el-input v-model="ele.text" autosize type="textarea" />
          </div>
          <el-row class="line">
            <el-button size="small" type="success" @click="loadFunc"
              >审核</el-button
            >
            <el-popconfirm title="确定删除?" @confirm="deleteAnn(ele)">
              <template #reference>
                <el-button size="small" type="danger">删除</el-button>
              </template>
            </el-popconfirm>
          </el-row>
        </div>
      </el-aside>
    </el-container>
  </el-container>

  <!-- 提交对话框 -->
  <el-dialog v-model="dialogFormVisible" title="标注">
    <el-form :model="form">
      <el-form-item label="标注文本">
        <el-input v-model="form.quote" autosize type="textarea" disabled />
      </el-form-item>
      <el-form-item label="标注类型">
        <el-select v-model="form.cate">
          <el-option label="实体" value="实体" />
          <el-option label="属性" value="属性" />
        </el-select>
        <el-input
          v-model="form.name"
          autocomplete="off"
          placeholder="请输入类型名称"
        />
      </el-form-item>
    </el-form>
    <el-form-item label="标注内容">
      <el-input v-model="form.text" autosize type="textarea" />
    </el-form-item>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="cancelDialog()">取消</el-button>
        <el-button type="primary" @click="confirmDialog()"> 确定 </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
/* eslint-disable */
import $ from "jquery";
export default {
  data() {
    return {
      // 当前打开的文件
      doc: "",
      // 当前打开的标注
      ann: "",
      // 文章内容
      article: "",
      // 标准内容
      annContent: [],
      // 修改绑定
      editArr: [],
      // 对话框显示
      dialogFormVisible: false,
      // 标注表单
      form: {
        quote: "",
        text: "",
        cate: "",
        name: "",
        start: "",
        end: "",
        startOffset: 0,
        endOffset: 0,
        id: "",
      },
      // 当前最大id
      maxAnnId: 0,
      // 标注列表
      annTable: [],
    };
  },
  mounted() {
    this.doc = JSON.parse(this.$route.query.doc);
    this.ann = JSON.parse(this.$route.query.ann);
    window.document.title = this.doc.split("/")[1];
    this.getDocText();
    this.createAnn();
  },
  methods: {
    // 获取base64
    getBase64(ele) {
      return "data:image/png;base64," + ele;
    },
    // 创建标注文件
    createAnn() {
      this.$api
        .createAnn({
          txt_path: this.doc,
          ann_name: this.ann,
        })
        .then((res) => {
          // console.log(res)
          this.getAnnContent();
        });
    },
    // 获取标注列表
    filterAnn(flag) {
      this.annTable = [];
      this.annContent.forEach((ele) => {
        if (ele.type.indexOf(flag) >= 0) this.annTable.push(ele);
      });
    },
    // 确定标注
    confirmDialog() {
      this.dialogFormVisible = false;
      this.form.id = `ann${this.maxAnnId + 1}`;
      let ann = {
        quote: this.form.quote,
        text: this.form.text,
        type: `${this.form.cate}#${this.form.name}#${this.form.id}`,
        ranges: [
          {
            start: this.form.start,
            end: this.form.end,
            startOffset: this.form.startOffset,
            endOffset: this.form.endOffset,
          },
        ],
      };
      console.log(ann);
      this.annContent.unshift(ann);
      this.randerAnn(ann);
      this.editAnnContent(ann);
      this.updateAnn(ann);
      this.filterAnn("实体");
      this.form = {
        quote: "",
        text: "",
        cate: "",
        name: "",
        start: "",
        end: "",
        startOffset: 0,
        endOffset: 0,
        id: "",
      };
    },
    // 更新标注文件
    updateAnn(ann) {
      this.$api
        .updateAnn({ json: JSON.stringify(ann), _method: "post" })
        .then((res) => {
          console.log(res);
        });
    },
    // 取消标注
    cancelDialog() {
      this.dialogFormVisible = false;
      this.form = {
        quote: "",
        text: "",
        cate: "",
        name: "",
        start: "",
        end: "",
        startOffset: 0,
        endOffset: 0,
        id: "",
      };
    },
    // 选择文本
    selectText() {
      let that = this;
      window.onclick = function (e) {
        var element = document.elementFromPoint(e.clientX, e.clientY);
        if (element.nodeName == "IMG") {
          that.dialogFormVisible = true;
          that.form.quote = "图片";
          that.form.startOffset = 0;
          that.form.endOffset = 0;
          let index = $(element.parentNode).index();
          that.form.start = `/p[${index + 1}]`;
          that.form.end = `/p[${index + 1}]`;
        }
      };

      let selecter = window.getSelection();
      console.log(selecter);
      let range = selecter.getRangeAt(0);
      let selectText = selecter.toString();
      console.log(range);
      if (selectText != null && selectText.trim() != "") {
        // console.log(selecter);
        this.dialogFormVisible = true;
        this.form.quote = selectText;
        this.form.startOffset = range.startOffset;
        this.form.endOffset = range.endOffset;
        if (
          $(range.commonAncestorContainer.parentNode)
            .html()
            .split(range.commonAncestorContainer.textContent)[0]
            .indexOf("span") >= 0
        ) {
          let otherOffset = $(range.commonAncestorContainer.parentNode)
            .text()
            .indexOf(range.commonAncestorContainer.textContent);
          this.form.startOffset += otherOffset;
          this.form.endOffset += otherOffset;
        }
        let index = $(range.commonAncestorContainer.parentNode).index();
        this.form.start = `/p[${index + 1}]`;
        this.form.end = `/p[${index + 1}]`;
      }
    },
    // 修改当前标注
    editAnn(ele, index) {
      ele.text = this.editArr[index];
    },
    // 删除当前标注
    deleteAnn(ele) {
      this.annContent.remove(ele);
      $(`span#${ele.id}`).before(ele.quote);
      $(`span#${ele.id}`).remove();
      this.filterAnn("实体");
    },
    // 滚动到标注位置
    scrollView(id) {
      $(".articleContainer").animate(
        { scrollTop: $(`span#${id}`).offset().top },
        500
      );
    },
    // 获取文章内容
    getDocText() {
      const formData = new FormData();
      formData.append("pathname", this.doc);
      formData.append("lastAnnName", this.ann);
      this.$api.docText(formData).then((res) => {
        this.article = res.data.text;
      });
    },
    // 获取标注内容
    getAnnContent() {
      const formData = new FormData();
      formData.append("ann_path", this.ann);
      this.$api.annContent(formData).then((res) => {
        if (res.data.annotations) {
          this.annContent = JSON.parse(res.data.annotations);
        }
        console.log(this.annContent);
        this.annContent.forEach((ele) => {
          this.editAnnContent(ele);
        });
        this.initAnnotation();
      });
    },
    // 编辑ann数据
    editAnnContent(ele) {
      ele.id = ele.type.split("#")[2];
      ele.name = ele.type.split("#")[1];
      ele.cate = ele.type.split("#")[0];
      this.editArr.push("");
      if (parseInt(ele.id.split("ann")[1]) > this.maxAnnId)
        this.maxAnnId = parseInt(ele.id.split("ann")[1]);
    },
    // 初始化标注数据
    initAnnotation() {
      this.annContent.forEach((ele) => {
        this.randerAnn(ele);
      });
      this.filterAnn("实体");
    },
    // 渲染标注  有bug
    randerAnn(ele) {
      let element = ele.ranges[0].start.split("/")[1].split("[")[0];
      let nodeNum =
        parseInt(ele.ranges[0].start.split("[")[1].split("]")[0]) - 1;
      let node = $(`.articleContainer ${element}:eq(${nodeNum})`);
      let startIndex = ele.ranges[0].startOffset;
      let endIndex = ele.ranges[0].endOffset;
      let middle = node.text().slice(startIndex, endIndex);
      let start = node.html().slice(0, node.html().indexOf(middle));
      let end = node
        .html()
        .slice(node.html().indexOf(middle) + middle.length, node.html().length);
      node.html(
        `${start}<span style="color:red;" id="${
          ele.type.split("#")[2]
        }">${middle}</span>${end}`
      );
      // console.log(middle);
    },
    // 选择文件
    selectDoc() {
      this.$router.push("/");
    },
    // loading
    loadFunc() {
      this.$message("功能开发中");
    },
  },
};
</script>

<style lang="scss">
.bodyContainer {
  height: 100vh;
  padding: 0 20px 20px;
  box-sizing: border-box;
  overflow: hidden;
  .headerContainer {
    border-bottom: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .title {
      font-size: 22px;
    }
  }
  .mainContainer {
    padding-top: 20px;
    height: inherit;
    .menuBox {
      width: 150px;
      max-width: 200px;
      border-right: 1px solid #ddd;
      padding-right: 20px;
    }
    .articleContainer {
      padding-top: 0;
      height: inherit;
      font-size: 20px;
      overflow-y: auto;
      padding-bottom: 150px;
      .line {
        margin-bottom: 10px;
      }
    }
    .markContainer {
      width: 230px;
      border-left: 1px solid #ddd;
      padding-left: 20px;
      padding-bottom: 150px;
      .title {
        font-size: 18px;
        font-weight: bold;
      }
      .el-row {
        margin-top: 10px;
      }
      .markLine {
        box-sizing: border-box;
        padding: 10px;
        font-size: 14px;
        margin-top: 10px;
        width: 100%;
        border: 2px solid #eee;
        border-radius: 10px;
        color: #000;
        cursor: pointer;
        .el-tag {
          margin-right: 10px;
        }
        textarea {
          margin-top: 10px;
        }
        .line {
          margin-top: 8px;
        }
      }
    }
  }
}
</style>