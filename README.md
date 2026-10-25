# CVPR 2026

每次用 VS Code 打开整个 `E:\gaptex` 文件夹，点击 `main.tex`，按 `Ctrl+Alt+V`：左侧写 LaTeX，右侧预览 PDF。
停止输入约 1 秒后自动保存、编译，编译完成后 PDF 自动刷新。
如果快捷键无效，按 `Ctrl+Shift+P`，选择 `LaTeX Workshop: View LaTeX PDF file in VSCode tab`。
也可以展开左侧文件列表里的 `build`，点击 `main.pdf`。若修改后没有更新，按 `Ctrl+Alt+B` 手动编译并查看错误提示。

- `main.tex`：论文正文；`references.bib`：BibTeX 文献，正文用 `\cite{key}` 引用。
- `Ctrl+Alt+B`：手动编译；`Ctrl+Alt+J`：源码跳转 PDF；PDF 中 `Ctrl+单击`：跳回源码。
- 默认是匿名审稿版；定稿时把 `\usepackage[review]{cvpr}` 改为 `\usepackage{cvpr}`，填写作者和论文编号。
- 编译结果在 `build/main.pdf`，可直接在文件列表中找到；编译中间文件和样式文件隐藏，保留在磁盘上。

来源：[CVPR 2026 官方模板](https://github.com/cvpr-org/author-kit/releases/tag/CVPR2026-v1%28latex%29)，提交 `12909ae437f6dbc7435069cfdb4ca44c18e6a02f`。
已去掉示例论文、图片、补充材料、rebuttal 和说明性注释；保留排版定义、必要的 TeX 行末 `%` 和许可证说明。
编译使用本机 MiKTeX（pdfLaTeX + BibTeX），无需 Perl；配置和构建脚本仅保存在本工作区 `.vscode/` 中。

本机 VS Code 1.102.3 的预览兼容修复：LaTeX Workshop 10.14.0 的 PDF.js 5.6.205 已替换为同版本官方 legacy 构建。
原文件备份在 `%LOCALAPPDATA%\gaptex\backups\latex-workshop-10.14.0-pdfjs-5.6.205`。扩展升级可能覆盖此修复；届时可同步升级 VS Code。
