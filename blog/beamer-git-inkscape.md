---
date_created: 2026-07-13T10:44:49+0200
date_modified: 2026-07-13T10:52:10+0200
type: article 
tags: #presentation #git #beamer #latex #inkscape
---

# Beamer、Git 與 Inkscape：研究簡報的可重現工作流

## Beamer 最大的優點是什麼？
它不只是公式排版，對生物研究簡報，Beamer 的核心價值在於把**投影片、分析程式、圖表、文獻引用與版本歷史**放入同一個可編譯的專案中。

論文與簡報不應直接共用正文。
論文需要完整論證；投影片用於口頭敘述。
真正能共用的是研究元件：

- 分析流程產生的圖表
- 縮寫、統計符號、單位與術語定義
- 參考文獻資料庫與 citation key
- 圖表路徑與命名規則
- 版本控制紀錄

例如，同一張 UMAP 或火山圖可同時被論文與簡報引用；
同一個 `\padj`、`\logFC` 或 `\THPone` 巨集也可在不同文件中保持一致。

公式是 Beamer 明顯的強項，但對以實驗結果、顯微影像、UMAP、差異分析、富集分析或網路圖為主的生物研究簡報，它通常不是主要理由。

## 什麼是專案資料夾中的 `shared/` 資料夾？

`shared/` 指放置同一研究計畫中、多種輸出文件共同使用的來源檔。

```text
project/
├── analysis/
├── figures/
├── manuscript/
│   └── main.tex
├── slides/
│   └── lab_meeting.tex
└── shared/
    ├── macros.tex
    ├── bibliography.bib
    ├── colors.tex
    └── notation.tex
```

適合放入 `shared/` 的內容包括：

- `macros.tex`：常用術語、基因或蛋白質名稱、統計符號與單位格式
- `bibliography.bib`：引用條目與 citation key
- `notation.tex`：模型、方法與數學符號
- `colors.tex`：實驗組別、細胞類型或專案配色定義

不應強行共用文件類別、頁面尺寸、Beamer 主題、論文期刊格式與投影片動畫邏輯。
這些是呈現層設定，論文與投影片的需求不同。

```latex
% shared/macros.tex
\newcommand{\THPone}{THP-1}
\newcommand{\LPS}{lipopolysaccharide}
\newcommand{\padj}{\ensuremath{p_{\mathrm{adj}}}}
\newcommand{\logFC}{\ensuremath{\log_2\mathrm{FC}}}
```

```latex
% manuscript/main.tex 或 slides/lab_meeting.tex
\input{../shared/macros.tex}
\addbibresource{../shared/bibliography.bib}
```

## 重複性的文章應該每次複製一份日期化 `.tex` 檔嗎？
例如每週或每月或定期性的報告，該 `.tex` 檔不建議有日期標記，它是用來編輯「進行中」的資料。
所以保留單一 `slides/lab_meeting.tex` 作為正在演化的簡報來源，
使用 Git 保存歷史，並以日期標記正式報告的版本。

```text
project/
├── analysis/
├── slides/
│   └── lab_meeting.tex
├── shared/
├── build/
└── archive/
```

每次有可辨識的研究進度時提交 commit：

```bash
git add analysis/ slides/ shared/ .gitignore
git commit -m "lab meeting: update LPS phosphoproteomics interpretation"
```

在實際報告後，建立 tag：

```bash
git tag -a lab-meeting-2026-07-13 \
  -m "Presented at lab meeting on 2026-07-13"
git push origin main --tags
```

日期化檔名應留給最終展示 PDF，而不是 `.tex` 原始碼：

```text
archive/lab-meeting-2026-07-13.pdf
```

這樣可以回到某次報告所用的完整原始碼狀態，而不需要維護大量幾乎相同的 `lab-meeting-YYYY-MM-DD.tex` 副本。

## 分析圖、PDF 與二進位檔應該全部放進 Git 嗎？
不應作為預設。Git 最適合追蹤文字化來源，例如 R、Python、Nextflow、LaTeX、YAML、TSV、設定檔與 Makefile。

持續更新的 PNG、TIFF、PDF、顯微影像或高解析圖表屬於二進位檔。一般 Git 無法提供有意義的逐行差異比較，每次修改都可能顯著增加儲存庫體積。

建議結構：

```text
project/
├── analysis/                 # Git 追蹤
├── slides/                   # Git 追蹤
├── shared/                   # Git 追蹤
├── figures/
│   ├── source/               # 視情況追蹤或使用 Git LFS
│   └── rendered/             # 分析產物，通常不追蹤
├── build/                    # 編譯產物，不追蹤
└── archive/
    └── lab-meeting-2026-07-13.pdf
```

`.gitignore` 可採取以下規則：

```gitignore
# LaTeX 暫存檔
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.log
*.nav
*.out
*.run.xml
*.snm
*.synctex.gz
*.toc
*.vrb

# 建置與分析產物
figures/rendered/
build/

# PDF 預設不追蹤
*.pdf

# 只保留正式封存版本
!archive/*.pdf
```

若正式報告 PDF 很小且數量有限，可直接存入 Git。若含高解析影像、單檔達數十 MB 以上，應使用 Git LFS 或機構儲存空間。

## 只保存日期化 PDF，不保存每張圖的快照，是否足夠？
對一般 lab meeting，足夠。封存 PDF 是當天實際展示內容的不可變紀錄；分析圖可以持續被新結果覆寫。

```bash
mkdir -p archive
cp build/lab_meeting.pdf archive/lab-meeting-2026-07-13.pdf

git add archive/lab-meeting-2026-07-13.pdf
git commit -m "archive: lab meeting 2026-07-13 PDF"
git tag -a lab-meeting-2026-07-13 \
  -m "Presented at lab meeting on 2026-07-13"
git push origin main --tags
```

tag 應指向同時包含投影片來源與該次封存 PDF 的 commit。這樣 checkout 該 tag 後，能直接取得展示版本，也能檢查當時的分析與 LaTeX 原始碼。

例外是無法重建的原始實驗影像、手動標註圖、投稿定稿圖或必須長期引用的關鍵結果圖。
這些應放在明確的 `assets/manual/` 或 `figures/final/` 目錄，並視大小採用 Git LFS。

## 問：Beamer 沒有 WYSIWYG 畫布，如何精準控制一頁的視覺設計？
不要用 TikZ 取代所有視覺設計。TikZ 適合少量箭頭、標籤、流程圖、節點與資料圖上的註記；若整張投影片充滿 `xshift`、`yshift` 與絕對座標，維護成本很高。

對需要精確構圖的頁面，使用 Inkscape 作為視覺畫布；Beamer 負責整合該頁與其他原生投影片。

```latex
\begin{frame}[plain]
  \centering
  \includegraphics[
    width=\paperwidth,
    height=\paperheight,
    keepaspectratio
  ]{build/results-overview.pdf}
\end{frame}
```

這不會把整頁轉成可維護的 Beamer 元件；但它保留 Inkscape 的完整視覺構圖，並使最終簡報仍由 Beamer 統一編譯。

## 有工具能把視覺化畫布完整轉成 TikZ 嗎？
最接近的是 Inkscape 搭配 `svg2tikz`。可在 Inkscape 中以拖拉方式設計整頁 SVG，再輸出 TikZ 程式碼並以 `\input{...}` 納入 Beamer。

```latex
\begin{frame}[plain]
  \centering
  \resizebox{\paperwidth}{!}{%
    \input{assets/mechanism-overview.tikz}%
  }
\end{frame}
```

但這不應視為通用投影片製作方案。
SVG-to-TikZ 對基本向量路徑、線條、填色與簡單形狀可行；對文字字距、折行、遮罩、漸層、濾鏡、複雜裁切與嵌入影像，結果不一定與 Inkscape 原稿完全一致。

若目標是穩定重現視覺外觀，Inkscape 輸出 PDF 比輸出 TikZ 更合理。若目標是讓輸出頁中的文字套用 LaTeX 字型與數學模式，可用 PDF + LaTeX 匯出：

```latex
\begin{frame}[plain]
  \centering
  \def\svgwidth{\paperwidth}
  \input{build/results-overview.pdf_tex}
\end{frame}
```

## Inkscape 內含分析圖後，不是又破壞可重現性嗎？
若在 Inkscape 中以 **Embed** 匯入圖片，確實如此。SVG 會保存圖片當時的內容；分析程式更新圖檔後，流程圖不會同步更新。

應改用 **Link** 匯入模式。SVG 只保存外部圖片的路徑、位置、縮放與裁切框，而不保存圖片本身。

```text
slides/design/results-overview.svg
  └── ../../figures/rendered/umap.png
```

建議專案結構：

```text
project/
├── analysis/
├── figures/
│   └── rendered/
│       ├── umap.png
│       ├── volcano.png
│       └── pathway-network.png
├── slides/
│   ├── lab_meeting.tex
│   └── design/
│       └── results-overview.svg
└── build/
```

Inkscape 裡圖片的框架、座標、縮放與裁切設定仍由模板控制；只有同一路徑的圖片內容被分析流程更新。

這要求分析程式建立固定輸出模式：

- 檔案路徑固定
- 畫布寬高固定
- 長寬比固定
- 外邊界固定
- 字級、圖例位置與軸標籤預留空間固定
- 避免輸出大小隨內容改變的自動裁切

資料變動不等於版面變動。只有新圖改變面板數量、長寬比、圖例結構或需要新的註記時，才需要回到 Inkscape 修改模板。

## Inkscape 能從終端機重新產生投影片頁面嗎？
可以。Inkscape 支援 headless 命令列匯出，不需開啟 GUI。

```bash
inkscape slides/design/results-overview.svg \
  --export-area-page \
  --export-filename=build/results-overview.pdf
```

該命令會讀取 SVG 及其 linked images，輸出新的 PDF。分析程式只要覆寫 `figures/rendered/umap.png`，重新執行 Inkscape 匯出就能取得含有新版 UMAP 的頁面。

可用 Makefile 管理依賴：

```make
DESIGN_SVG := slides/design/results-overview.svg
DESIGN_PDF := build/results-overview.pdf
SLIDES_TEX := slides/lab_meeting.tex
SLIDES_PDF := build/lab_meeting.pdf

$(DESIGN_PDF): $(DESIGN_SVG) figures/rendered/umap.png figures/rendered/volcano.png
	mkdir -p build
	inkscape $< --export-area-page --export-filename=$@

$(SLIDES_PDF): $(SLIDES_TEX) $(DESIGN_PDF)
	mkdir -p build
	latexmk -pdf -output-directory=build $(SLIDES_TEX)
```

執行：

```bash
make build/lab_meeting.pdf
```

建置關係如下：

```text
analysis/
  -> figures/rendered/umap.png
  -> slides/design/results-overview.svg
  -> build/results-overview.pdf
  -> build/lab_meeting.pdf
  -> archive/lab-meeting-YYYY-MM-DD.pdf
```

這個架構把工作分為兩層：

- **分析與資料圖層**：程式產生固定規格的圖檔。
- **視覺模板層**：Inkscape 管理一次性的版面設計，連結外部圖檔。
- **文件整合層**：Beamer 統一編譯原生投影片與 Inkscape 匯出的頁面。
- **封存層**：日期化 PDF 保存實際展示結果。

其目標不是讓所有投影片都變成 LaTeX，而是讓可重現的內容維持可重現，讓需要畫布式編排的頁面仍能以可自動重建的方式納入同一份簡報。
