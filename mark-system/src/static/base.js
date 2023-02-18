 /* eslint-disable */ 
// 替换文本前与后的空格
String.prototype.trim = function () {
	return this.replace(/(^\s*)|(\s*$)/g, "");
}

// 数组添加删除操作
Array.prototype.remove = function (val) {
	var index = this.indexOf(val);
	if (index > -1) {
		this.splice(index, 1);
	}
};

// 是否是base64
String.prototype.isBase64 = function () {
	const notBase64 = /[^A-Z0-9+\/=]/i;
	const len = this.length;
	if (!len || len % 4 !== 0 || notBase64.test(this)) {
		return false;
	}
	const firstPaddingChar = this.indexOf('=');
	return firstPaddingChar === -1 ||
		firstPaddingChar === len - 1 ||
		(firstPaddingChar === len - 2 && this[len - 1] === '=');
}