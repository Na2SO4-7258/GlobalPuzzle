# CVPR 2027

每次用 VS Code 打开整个 `E:\gaptex` 文件夹，点击 `main.tex`，按 `Ctrl+Alt+V`：左侧写 LaTeX，右侧预览 PDF。
停止输入约 1 秒后自动保存、编译，编译完成后 PDF 自动刷新。
如果快捷键无效，按 `Ctrl+Shift+P`，选择 `LaTeX Workshop: View LaTeX PDF file in VSCode tab`。
也可以展开左侧文件列表里的 `build`，点击 `main.pdf`。若修改后没有更新，按 `Ctrl+Alt+B` 手动编译并查看错误提示。

- `main.tex`：论文正文；`references.bib`：BibTeX 文献，正文用 `\cite{key}` 引用。
- `Ctrl+Alt+B`：手动编译；`Ctrl+Alt+J`：源码跳转 PDF；PDF 中 `Ctrl+单击`：跳回源码。
- 默认是匿名审稿版；定稿时把 `\usepackage[review]{cvpr}` 改为 `\usepackage{cvpr}`，填写作者。2027 官方模板已移除论文编号显示。
- 编译结果在 `build/main.pdf`，可直接在文件列表中找到；编译中间文件和样式文件隐藏，保留在磁盘上。
- `preamble.tex`：官方导言区及额外宏包；`cvpr.sty` 和 `ieeenat_fullname.bst` 使用 2027 官方原文件。
- `main.tex` 的参考文献前新增 `LLM Usage Statement` 待填写占位；投稿前请按实际使用情况填写工具名称、涉及部分和使用程度。
- `old/`：迁移前的完整项目备份（含正文、图片、中文草稿、参考文献、旧模板、编辑器配置和当时的编译结果，不含 Git 历史）；`old/main.tex` 为原稿。
- `templates/CVPR2027/`：下载的官方 ZIP 和完整解压模板，保留示例及 rebuttal，供查阅。

来源：[CVPR 2027 作者指南](https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines)链接的[官方 LaTeX 模板包 v1](https://media.eventhosts.cc/Conferences/CVPR2027/author-kit-CVPR2027-v1-latex.zip)，下载日期为 2026-10-27。
ZIP 的 SHA-256：`7271bdbb0d2f20043b101c3bb10cba67a8c7f2711f0067b395f9f27451c43121`。
论文标题、作者占位、摘要、正文、公式、图片、表格和参考文献路径沿用原稿；正文继续集中在 `main.tex` 中编辑。
编译使用本机 MiKTeX（pdfLaTeX + BibTeX），无需 Perl；配置和构建脚本仅保存在本工作区 `.vscode/` 中。

本机 VS Code 1.102.3 的预览兼容修复：LaTeX Workshop 10.14.0 的 PDF.js 5.6.205 已替换为同版本官方 legacy 构建。
原文件备份在 `%LOCALAPPDATA%\gaptex\backups\latex-workshop-10.14.0-pdfjs-5.6.205`。扩展升级可能覆盖此修复；届时可同步升级 VS Code。
