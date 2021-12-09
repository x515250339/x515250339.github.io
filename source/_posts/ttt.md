---
title: test2
date: 2021-12-08 20:59:25
tags: 嘎嘎嘎
---
文章
#内容卡片
opacity: 自定义展示的文章卡片透明度，默认为 0.8
## 文章

### [#](https://hexo-theme-yun.vercel.app/guide/config.html#内容卡片)内容卡片

- `opacity`: 自定义展示的文章卡片透明度，默认为 `0.8`

```yaml
post_card:
  opacity: 0.8
```

#### [#](https://hexo-them:qe-yun.vercel.app/guide/config.html#type)type

为文章设置 `type` 属性，即可将其转为其他类型卡片，并跳转 `url` 设置的链接。

譬如：

```markdown
---
title: xxx
type: bilibili
url: https://www.bilibili.com/video/av8153395/
---
```

在文章标题前将会出现 bilibili 的图标，点击标题会跳转至对应的链接。

目前默认支持以下类型（哔哩哔哩、豆瓣、GitHub、网易云音乐、推特、微信公众号、微博、语雀、知乎、Notion、外链）：

```yaml
types:
  link:
    color: blue
    icon: icon-external-link-line
  bilibili:
    color: "#FF8EB3"
    icon: icon-bilibili-line
  douban:
    color: "#007722"
    icon: icon-douban-line
  github:
    color: black
    icon: icon-github-line
  netease-cloud-music:
    color: "#C10D0C"
    icon: icon-netease-cloud-music-line
  notion:
    color: black
    icon: icon-notion
  twitter:
    color: "#1da1f2"
    icon: icon-twitter-line
  wechat:
    color: "#1AAD19"
    icon: icon-wechat-2-line
  weibo:
    color: "#E6162D"
    icon: icon-weibo-line
  yuque:
    color: "#25b864"
    icon: icon-yuque
  zhihu:
    color: "#0084FF"
    icon: icon-zhihu-line
```

你也可以自己在 `yun.yml` 设置你跳转不同链接专属的图标和颜色。

```yaml
types:
  google:
    color: xxx
    icon: xxx
```

1
2
3
4

当你指定的 `type` 不存在于默认支持中，也没有进行自定义，将默认使用蓝色的额外链接图标。

如果你想在你的外链卡片上显示一些信息，你可以写在 `<!-- more -->` 前，它会被当作摘要显示。

譬如：

```markdown
---
title: hexo-theme-yun
type: github
url: https://github.com/YunYouJun/hexo-theme-yun
---

Hexo 主题 Yun

<!-- more -->
```

#### [#](https://hexo-theme-yun.vercel.app/guide/config.html#hide)hide

你可以在文章头部添加 `hide` 属性，来临时隐藏某篇文章。

- ```
  hide
  ```

  :

  - `index`: 设置为 `index` 时，将只在首页隐藏，归档中仍然展示。（譬如放一些没有必要放在首页的笔记，并在归档中方便自己查看。）
  - `true`: 当设置为 `true` 时，该文章仍然会被渲染，你自己可以直接访问链接进行查看。但不会被显示在展示的文章卡片与归档中。

> 什么？你想完全不渲染不显示？那你为何不将其放在 `_drafts` 文件夹下，或干脆不提交这篇文章。

```yaml
---
title: xxx
hide: true
# hide: index
sitemap: false
indexing: false
---
```



TIP

如果你开启了站点地图，那它还会出现在 `sitemap.xml` 中，你还需要在 front matter 处设置 `sitemap: false` 来排除它。

> [excluding-posts | hexo-generator-sitemapopen in new window](https://github.com/hexojs/hexo-generator-sitemap#excluding-posts)

如果你开启了本地搜索，那它还会出现在 `search.xml` 中，你还需要设置 `indexing: false` 来排除它。

> [exclude-indexing | hexo-generator-searchopen in new window](https://github.com/wzpan/hexo-generator-search#exclude-indexing)

> 题外话，这个功能是我当初应付备案临时加的。 我更改备案信息时，客服通知我首页不能用跳转其他页面链接的内容（有一个和文章混在一起直接跳转 bilibili 的卡片），所以我就加了这个功能临时隐藏掉了。 也许还挺实用的，你可以放一些只是自己看看，暂时还不打算发到主页显示的页面。

### [#](https://hexo-theme-yun.vercel.app/guide/config.html#信息)信息

- `item_text`: 是否显示文字（如：发表于、更新于，若关闭则只显示图标与时间信息）
- `created_at`: 是否显示创建时间
- `updated_at`: 是否显示更新时间
- `categories`: 是否显示种类
- `tags`: 是否显示标签

```yaml
post_meta:
  item_text: false
  created_at: true
  updated_at: true
  categories: true
  tags: true
```

### [#](https://hexo-theme-yun.vercel.app/guide/config.html#目录)目录

你只要遵循 [Markdown 语法open in new window](https://segmentfault.com/markdown)，就会自动生成目录！

TIP

具有良好 SEO 的 HTML 页面，有且应当只有一个 `h1` 作为一级标题。 本主题默认采用您设置的 `title` 作为一级标题。 在接下来的文章内容中，您应当只从二级标题开始使用。

```markdown
---
title: 一级标题
---

## 二级标题
```



> 没什么人会要关这个功能的吧，hhh（所以我根本没加关闭的功能）

当你开启显示编号，并切换到目录时，再次点击目录按钮，可切换隐藏目录编号。

- `list_number`: 显示编号
- `max_depth`: 生成 TOC 的最大深度
- `min_depth`: 生成 TOC 的最小深度
- `placeholder`: 当目录不存在时，显示的话。
- `collapse`: 是否折叠目录（默认折叠，即隐藏次级目录，滚到到相关位置时才展开）

```yaml
toc:
  list_number: true
  max_depth: 6
  min_depth: 1
  placeholder: 很遗憾，咱没写啥目录
  collapse: false
```



> [辅助函数 ｜ Hexoopen in new window](https://hexo.io/zh-cn/docs/helpers#toc)

### [#](https://hexo-theme-yun.vercel.app/guide/config.html#编辑链接)编辑链接

若开启，则会在文章页面标题旁显示一个编辑图标。 点击后跳转到编辑页面。

- `url`: 文章所在地址（您可以参照默认链接设置您的仓库跳转链接）

如我使用 `GitHub` 作为博客的托管仓库，仓库名为 `yunyoujun.github.io`，在 `hexo` 分支下，`source` 文件夹中， 则链接为 [https://github.com/YunYouJun/yunyoujun.github.io/tree/hexo/source/open in new window](https://github.com/YunYouJun/yunyoujun.github.io/tree/hexo/source/)。

```yaml
post_edit:
  enable: true
  url: https://github.com/YunYouJun/yunyoujun.github.io/tree/hexo/source/
```



### [#](https://hexo-theme-yun.vercel.app/guide/config.html#代码高亮)代码高亮

设置代码高亮

由于性能及定位问题，且 [Hexo 5.0open in new window](https://blog.skk.moe/post/hexo-5/) 已原生支持 prism，本主题更推荐使用 [prismjsopen in new window](https://github.com/PrismJS/prism) 而非 `highlight.js`。

> 请升级 Hexo 至 5.0。`npm install hexo@latest`

PrismJS 是一个轻量级的代码高亮库，相比 highlight.js，prismjs 可以在 Node.js 环境执行（即：可在 Hexo 生成页面时进行代码高亮）。

我们可以通过 CDN 快速切换主题，本主题也支持为亮暗模式设置不同的代码高亮主题。

> 当前 Prism 支持的语言：[https://prismjs.com/#supported-languagesopen in new window](https://prismjs.com/#supported-languages) 你应当使用更通用的 `cpp` 替代 `c++` 以高亮 C++ 代码

在 Hexo （须升级至 5.0 以上版本）工作目录下的 `_config.yml` 中配置：

```yaml
# 关闭 highlight
highlight:
  enable: false
# 启用 prism
prismjs:
  enable: true
  preprocess: true
  line_number: false
  tab_replace: ""
```



在 `yun.yml` 中：

- `copy_btn`: 开启一键复制按钮

- ```
  prismjs
  ```

  - `light`: 亮模式下，代码高亮主题
  - `dark`: 暗模式下，代码高亮主题

（可以为亮暗模式分别设置对应适合的高亮样式。）

> 代码高亮主题可参见 [https://cdn.jsdelivr.net/npm/prismjs@latest/themes/open in new window](https://cdn.jsdelivr.net/npm/prismjs@latest/themes/)。

```yaml
codeblock:
  copy_btn: true
  prismjs:
    light: default
    dark: tomorrow
```

> 建议关闭行号，[这里open in new window](https://highlightjs.readthedocs.io/en/latest/line-numbers.html)是 highlight 作者写的为什么 highlight 不支持行号。 行号是否存在影响不大，当去掉时可以节约出一部分空间，譬如一些原先需要滚动条的代码，去掉后，就可以完全显示出来。

### [#](https://hexo-theme-yun.vercel.app/guide/config.html#版权)版权

设置您的文章的分享版权

> [关于许可协议open in new window](https://creativecommons.org/licenses/) 默认使用 署名-非商业性使用-相同方式共享 4.0，即 [CC BY-NC-SA 4.0open in new window](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)。

- `license`: 设置证书 (by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero)
- `language`: 设置语言 (deed.zh | deed.en | deed.ja ｜ ...)
- `post`: 在每篇文章末尾显示
- `clipboard`: 是否在复制文章时，在剪贴板中追加版权信息（默认关闭）

```yaml
creative_commons:
  license: by-nc-sa
  post: true
  language: deed.zh
  clipboard: false
```



> 你的 `url` 请在 Hexo 工作目录下的 `_config.yml` 中设置。 [配置｜ Hexoopen in new window](https://hexo.io/zh-cn/docs/configuration#网址)

```yaml
# URL
## If your site is put in a subdirectory, set url as 'https://yoursite.com/child' and root as '/child/'
url: https://www.yunyoujun.cn
```



### [#](https://hexo-theme-yun.vercel.app/guide/config.html#图片懒加载)图片懒加载

默认开启，将会为 Markdown 的图片 `img` 加上 `loading="lazy"` 属性。

> [![img]() loadingopen in new window](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img#attr-loading) 当前仍有许多浏览器不支持该特性 [Can I use loading?open in new window](https://caniuse.com/#search=loading)

```yaml
lazyload:
  enable: true
```