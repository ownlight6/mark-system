(function () {
    var t = {
        3054: function (t, e, n) {
            "use strict";
            var r = n(8222);
            const o = {id: "app"};

            function i(t, e, n, i, a, u) {
                const s = (0, r.up)("router-view");
                return (0, r.wg)(), (0, r.iD)("div", o, [a.isRouterAlive ? ((0, r.wg)(), (0, r.j4)(s, {key: 0})) : (0, r.kq)("", !0)])
            }

            var a = {
                name: "App", provide() {
                    return {reload: this.reload}
                }, data() {
                    return {isRouterAlive: !0}
                }, methods: {
                    reload() {
                        this.isRouterAlive = !1, this.$nextTick((function () {
                            this.isRouterAlive = !0
                        }))
                    }
                }
            }, u = n(3744);
            const s = (0, u.Z)(a, [["render", i]]);
            var c = s, f = n(5455), l = (n(4415), n(5641)), d = n(2201);
            const p = [{
                path: "/",
                component: () => Promise.all([n.e(658), n.e(652)]).then(n.bind(n, 2652)),
                meta: {name: "打开文件"}
            }, {
                path: "/mark",
                component: () => Promise.all([n.e(658), n.e(773)]).then(n.bind(n, 4773)),
                meta: {name: "标注系统"}
            }], m = (0, d.p7)({history: (0, d.PO)(), routes: p});
            var h = m, v = n(8433);
            const g = v.Z.create({baseURL: "http://127.0.0.1:8000", timeout: 6e3});
            var y = g, b = {
                documentMenu(t) {
                    return y({url: "/initWeb/get_txtcatalog/", method: "post", data: t})
                }, docUpload(t) {
                    return y({
                        url: "/initWeb/upload/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }, docText(t) {
                    return y({
                        url: "/initWeb/get_text/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }, annMenu(t) {
                    return y({
                        url: "/initWeb/get_annCatalog/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }, createAnn(t) {
                    return y({
                        url: "/other/makeFilename/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }, annContent(t) {
                    return y({
                        url: "/other/readAll/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }, updateAnn(t) {
                    return y({
                        url: "/createAnn/create/",
                        method: "post",
                        headers: {"Content-type": "multipart/form-data"},
                        data: t
                    })
                }
            };
            n(753);
            const k = (0, r.ri)(c);
            k.config.globalProperties.$api = b, k.use(f.Z).use(h).use(l).mount("#app")
        }, 753: function () {
            String.prototype.trim = function () {
                return this.replace(/(^\s*)|(\s*$)/g, "")
            }, Array.prototype.remove = function (t) {
                var e = this.indexOf(t);
                e > -1 && this.splice(e, 1)
            }, String.prototype.isBase64 = function () {
                const t = /[^A-Z0-9+\/=]/i, e = this.length;
                if (!e || e % 4 !== 0 || t.test(this)) return !1;
                const n = this.indexOf("=");
                return -1 === n || n === e - 1 || n === e - 2 && "=" === this[e - 1]
            }
        }
    }, e = {};

    function n(r) {
        var o = e[r];
        if (void 0 !== o) return o.exports;
        var i = e[r] = {exports: {}};
        return t[r].call(i.exports, i, i.exports, n), i.exports
    }

    n.m = t, function () {
        var t = [];
        n.O = function (e, r, o, i) {
            if (!r) {
                var a = 1 / 0;
                for (f = 0; f < t.length; f++) {
                    r = t[f][0], o = t[f][1], i = t[f][2];
                    for (var u = !0, s = 0; s < r.length; s++) (!1 & i || a >= i) && Object.keys(n.O).every((function (t) {
                        return n.O[t](r[s])
                    })) ? r.splice(s--, 1) : (u = !1, i < a && (a = i));
                    if (u) {
                        t.splice(f--, 1);
                        var c = o();
                        void 0 !== c && (e = c)
                    }
                }
                return e
            }
            i = i || 0;
            for (var f = t.length; f > 0 && t[f - 1][2] > i; f--) t[f] = t[f - 1];
            t[f] = [r, o, i]
        }
    }(), function () {
        n.n = function (t) {
            var e = t && t.__esModule ? function () {
                return t["default"]
            } : function () {
                return t
            };
            return n.d(e, {a: e}), e
        }
    }(), function () {
        n.d = function (t, e) {
            for (var r in e) n.o(e, r) && !n.o(t, r) && Object.defineProperty(t, r, {enumerable: !0, get: e[r]})
        }
    }(), function () {
        n.f = {}, n.e = function (t) {
            return Promise.all(Object.keys(n.f).reduce((function (e, r) {
                return n.f[r](t, e), e
            }), []))
        }
    }(), function () {
        n.u = function (t) {
            return "js/" + t + ".js"
        }
    }(), function () {
        n.miniCssF = function (t) {
            return "css/" + t + ".css"
        }
    }(), function () {
        n.g = function () {
            if ("object" === typeof globalThis) return globalThis;
            try {
                return this || new Function("return this")()
            } catch (t) {
                if ("object" === typeof window) return window
            }
        }()
    }(), function () {
        n.o = function (t, e) {
            return Object.prototype.hasOwnProperty.call(t, e)
        }
    }(), function () {
        var t = {}, e = "mark-system:";
        n.l = function (r, o, i, a) {
            if (t[r]) t[r].push(o); else {
                var u, s;
                if (void 0 !== i) for (var c = document.getElementsByTagName("script"), f = 0; f < c.length; f++) {
                    var l = c[f];
                    if (l.getAttribute("src") == r || l.getAttribute("data-webpack") == e + i) {
                        u = l;
                        break
                    }
                }
                u || (s = !0, u = document.createElement("script"), u.charset = "utf-8", u.timeout = 120, n.nc && u.setAttribute("nonce", n.nc), u.setAttribute("data-webpack", e + i), u.src = r), t[r] = [o];
                var d = function (e, n) {
                    u.onerror = u.onload = null, clearTimeout(p);
                    var o = t[r];
                    if (delete t[r], u.parentNode && u.parentNode.removeChild(u), o && o.forEach((function (t) {
                        return t(n)
                    })), e) return e(n)
                }, p = setTimeout(d.bind(null, void 0, {type: "timeout", target: u}), 12e4);
                u.onerror = d.bind(null, u.onerror), u.onload = d.bind(null, u.onload), s && document.head.appendChild(u)
            }
        }
    }(), function () {
        n.r = function (t) {
            "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {value: "Module"}), Object.defineProperty(t, "__esModule", {value: !0})
        }
    }(), function () {
        n.p = ""
    }(), function () {
        if ("undefined" !== typeof document) {
            var t = function (t, e, n, r, o) {
                var i = document.createElement("link");
                i.rel = "stylesheet", i.type = "text/css";
                var a = function (n) {
                    if (i.onerror = i.onload = null, "load" === n.type) r(); else {
                        var a = n && ("load" === n.type ? "missing" : n.type), u = n && n.target && n.target.href || e,
                            s = new Error("Loading CSS chunk " + t + " failed.\n(" + u + ")");
                        s.code = "CSS_CHUNK_LOAD_FAILED", s.type = a, s.request = u, i.parentNode.removeChild(i), o(s)
                    }
                };
                return i.onerror = i.onload = a, i.href = e, n ? n.parentNode.insertBefore(i, n.nextSibling) : document.head.appendChild(i), i
            }, e = function (t, e) {
                for (var n = document.getElementsByTagName("link"), r = 0; r < n.length; r++) {
                    var o = n[r], i = o.getAttribute("data-href") || o.getAttribute("href");
                    if ("stylesheet" === o.rel && (i === t || i === e)) return o
                }
                var a = document.getElementsByTagName("style");
                for (r = 0; r < a.length; r++) {
                    o = a[r], i = o.getAttribute("data-href");
                    if (i === t || i === e) return o
                }
            }, r = function (r) {
                return new Promise((function (o, i) {
                    var a = n.miniCssF(r), u = n.p + a;
                    if (e(a, u)) return o();
                    t(r, u, null, o, i)
                }))
            }, o = {143: 0};
            n.f.miniCss = function (t, e) {
                var n = {652: 1, 773: 1};
                o[t] ? e.push(o[t]) : 0 !== o[t] && n[t] && e.push(o[t] = r(t).then((function () {
                    o[t] = 0
                }), (function (e) {
                    throw delete o[t], e
                })))
            }
        }
    }(), function () {
        var t = {143: 0};
        n.f.j = function (e, r) {
            var o = n.o(t, e) ? t[e] : void 0;
            if (0 !== o) if (o) r.push(o[2]); else {
                var i = new Promise((function (n, r) {
                    o = t[e] = [n, r]
                }));
                r.push(o[2] = i);
                var a = n.p + n.u(e), u = new Error, s = function (r) {
                    if (n.o(t, e) && (o = t[e], 0 !== o && (t[e] = void 0), o)) {
                        var i = r && ("load" === r.type ? "missing" : r.type), a = r && r.target && r.target.src;
                        u.message = "Loading chunk " + e + " failed.\n(" + i + ": " + a + ")", u.name = "ChunkLoadError", u.type = i, u.request = a, o[1](u)
                    }
                };
                n.l(a, s, "chunk-" + e, e)
            }
        }, n.O.j = function (e) {
            return 0 === t[e]
        };
        var e = function (e, r) {
            var o, i, a = r[0], u = r[1], s = r[2], c = 0;
            if (a.some((function (e) {
                return 0 !== t[e]
            }))) {
                for (o in u) n.o(u, o) && (n.m[o] = u[o]);
                if (s) var f = s(n)
            }
            for (e && e(r); c < a.length; c++) i = a[c], n.o(t, i) && t[i] && t[i][0](), t[i] = 0;
            return n.O(f)
        }, r = self["webpackChunkmark_system"] = self["webpackChunkmark_system"] || [];
        r.forEach(e.bind(null, 0)), r.push = e.bind(null, r.push.bind(r))
    }();
    var r = n.O(void 0, [998], (function () {
        return n(3054)
    }));
    r = n.O(r)
})();