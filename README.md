# Twitter Card 落地页 — 六大交易所邀请码

> 把 `twitter-cards/` 里的内容上传到 GitHub Pages，就能让推特发链接时自动生成大卡片预览。

## 📦 文件结构

```
twitter-cards/
├── .nojekyll              # 禁用 GitHub Jekyll 处理
├── configure.py           # 配置脚本：填入你的 GitHub Pages 地址
├── index.html             # 六大交易所合集首页
├── binance/
│   ├── card.png           # 1200×628 推特卡片图片
│   └── index.html         # 落地页：Twitter Card meta + 自动跳转注册
├── okx/
├── bybit/
├── bitget/
├── bit/
└── msx/
```

## 🚀 部署到 GitHub Pages

### 1. 创建 GitHub 仓库
- 打开 https://github.com/new
- Repository name 填 `twitter-cards`（可改）
- 选择 **Public**
- 点 **Create repository**

### 2. 上传文件
把 `twitter-cards/` 文件夹里的**所有文件和子文件夹**上传到仓库根目录。方式二选一：

**方式 A：网页上传（最简单）**
- 仓库页面点 `Add file` → `Upload files`
- 拖入 `twitter-cards/` 内全部内容
- 点 `Commit changes`

**方式 B：命令行（Git）**
```bash
cd 你本地路径/twitter-cards
git init
git add .
git commit -m "init twitter cards"
git branch -M main
git remote add origin https://github.com/你的用户名/twitter-cards.git
git push -u origin main
```

### 3. 配置 GitHub Pages 地址
仓库上传后，运行配置脚本，把 `{{BASE_URL}}` 换成你的真实地址：

```bash
# Windows 双击运行，或在 PowerShell 里：
python configure.py
# 提示输入时填：
# https://你的用户名.github.io/twitter-cards/
```

**修改完成后记得重新提交上传一次！**

### 4. 开启 GitHub Pages
- 仓库 Settings（设置）→ 左侧 Pages
- Source 选择 **Deploy from a branch**
- Branch 选 **main**，文件夹选 **/(root)**
- 点 **Save**
- 等待 1-2 分钟，直到页面上方显示绿色 ✅ `Your site is live at https://...`

### 5. 测试
打开链接确认能正常跳转：
- `https://你的用户名.github.io/twitter-cards/binance/`
- `https://你的用户名.github.io/twitter-cards/okx/`
- ...以此类推

## 🐦 在推特使用

发推时，写完正文后**粘贴你的中转页链接**，推特会自动抓取 meta 标签并显示大卡片：

```
🟡 币安注册邀请码：BTC9149
✅ 20% 手续费返佣 + 新人奖励最高 $100
👉 https://你的用户名.github.io/twitter-cards/binance/
```

### 各交易所链接

| 交易所 | 邀请码 | 中转页 URL |
|---|---|---|
| 币安 Binance | BTC9149 | `https://你的用户名.github.io/twitter-cards/binance/` |
| 欧易 OKX | BTC9149 | `https://你的用户名.github.io/twitter-cards/okx/` |
| Bybit | BTC9149 | `https://你的用户名.github.io/twitter-cards/bybit/` |
| Bitget | BTC9149 | `https://你的用户名.github.io/twitter-cards/bitget/` |
| BIT | F7DC7Z | `https://你的用户名.github.io/twitter-cards/bit/` |
| MSX | jUTs61 | `https://你的用户名.github.io/twitter-cards/msx/` |

### 验证推特卡片
- 访问 https://cards-dev.twitter.com/validator
- 输入任一落地页链接，可预览卡片效果

## ⚠️ 注意事项

1. **图片 URL 必须是绝对地址**：推特读不到相对路径，所以 `configure.py` 必须运行，把 `{{BASE_URL}}` 改成真实地址。
2. **GitHub Pages 首次部署有缓存**：上传后等 2-5 分钟再用推特验证器测试。
3. **不要改图片文件名**：`card.png` 这个名字在 index.html 里写死了。
4. **中转页会自动跳转到交易所注册页**：访客点击卡片或链接后 1 秒自动跳转。

## ✅ 完整检查清单

- [ ] GitHub 仓库已创建
- [ ] `twitter-cards/` 内所有文件已上传到仓库根目录
- [ ] `configure.py` 已运行并替换 `{{BASE_URL}}`
- [ ] GitHub Pages 已开启
- [ ] 浏览器访问落地页能正常跳转
- [ ] Twitter Card Validator 能正常显示卡片
- [ ] 发推测试能看到大卡片预览
