#!/usr/bin/env python3
"""Generate reference.docx untuk pandoc --reference-doc.

Memodifikasi reference.docx bawaan pandoc agar gaya dokumen Word
mengikuti pedoman laporan akademik:

  - Ukuran halaman A4, margin atas 2cm / bawah 3cm / kiri-kanan 2.5cm
  - Normal (teks isi): Times New Roman 12pt, justify, spasi 1.5
  - Heading 1 (judul BAB): Times New Roman 14pt bold, rata tengah, hitam
  - Heading 2/3 (sub-bab): Times New Roman 12pt bold, rata kiri, hitam
  - Title/Subtitle/Author/Date: Times New Roman, rata tengah, hitam

Usage:
  python3 scripts/make-reference-docx.py [input.docx] [output.docx]

  input.docx  - hasil `pandoc --print-default-data-file reference.docx`
  output.docx - reference.docx hasil styling (default: reference.docx)
"""

import re
import sys
import zipfile

TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'

STYLES = {
    "Normal": f"""<w:style w:type="paragraph" w:styleId="Normal">
  <w:name w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0" w:line="360" w:lineRule="auto"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "BodyText": f"""<w:style w:type="paragraph" w:styleId="BodyText">
  <w:name w:val="Body Text"/>
  <w:basedOn w:val="Normal"/>
  <w:link w:val="BodyTextChar"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0" w:line="360" w:lineRule="auto"/>
    <w:ind w:firstLine="709"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "FirstParagraph": f"""<w:style w:type="paragraph" w:styleId="FirstParagraph">
  <w:name w:val="First Paragraph"/>
  <w:basedOn w:val="BodyText"/>
  <w:link w:val="BodyTextChar"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0" w:line="360" w:lineRule="auto"/>
    <w:ind w:firstLine="709"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "Heading1": f"""<w:style w:type="paragraph" w:styleId="Heading1">
  <w:name w:val="heading 1"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="BodyText"/>
  <w:link w:val="Heading1Char"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:spacing w:before="360" w:after="720"/>
    <w:jc w:val="center"/>
    <w:outlineLvl w:val="0"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Heading2": f"""<w:style w:type="paragraph" w:styleId="Heading2">
  <w:name w:val="heading 2"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="BodyText"/>
  <w:link w:val="Heading2Char"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:spacing w:before="160" w:after="80"/>
    <w:outlineLvl w:val="1"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Heading3": f"""<w:style w:type="paragraph" w:styleId="Heading3">
  <w:name w:val="heading 3"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="BodyText"/>
  <w:link w:val="Heading3Char"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:spacing w:before="160" w:after="80"/>
    <w:outlineLvl w:val="2"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Title": f"""<w:style w:type="paragraph" w:styleId="Title">
  <w:name w:val="Title"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="BodyText"/>
  <w:link w:val="TitleChar"/>
  <w:uiPriority w:val="10"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="80" w:line="240" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Subtitle": f"""<w:style w:type="paragraph" w:styleId="Subtitle">
  <w:name w:val="Subtitle"/>
  <w:basedOn w:val="Title"/>
  <w:next w:val="BodyText"/>
  <w:link w:val="SubtitleChar"/>
  <w:uiPriority w:val="11"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="80" w:line="240" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Author": f"""<w:style w:type="paragraph" w:styleId="Author">
  <w:name w:val="Author"/>
  <w:basedOn w:val="Title"/>
  <w:next w:val="BodyText"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "Date": f"""<w:style w:type="paragraph" w:styleId="Date">
  <w:name w:val="Date"/>
  <w:basedOn w:val="Title"/>
  <w:next w:val="BodyText"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "AbstractTitle": f"""<w:style w:type="paragraph" w:styleId="AbstractTitle">
  <w:name w:val="Abstract Title"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Abstract"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:spacing w:before="300" w:after="0"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Abstract": f"""<w:style w:type="paragraph" w:styleId="Abstract">
  <w:name w:val="Abstract"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="BodyText"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:keepLines/>
    <w:spacing w:before="100" w:after="300"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "Compact": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="Compact">
  <w:name w:val="Compact"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="60" w:after="60" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="0" w:right="0" w:firstLine="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "SourceCode": f"""<w:style w:type="paragraph" w:styleId="SourceCode">
  <w:name w:val="Source Code"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="120" w:after="120" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="0" w:right="0" w:firstLine="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    <w:rFonts w:ascii="DejaVu Sans Mono" w:hAnsi="DejaVu Sans Mono" w:cs="DejaVu Sans Mono"/>
    <w:sz w:val="18"/>
    <w:szCs w:val="18"/>
  </w:rPr>
</w:style>""",
    "ImageCaption": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="ImageCaption">
  <w:name w:val="Image Caption"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="120" w:after="240" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="0" w:right="0" w:firstLine="0"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:i/>
  </w:rPr>
</w:style>""",
    "TableCaption": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="TableCaption">
  <w:name w:val="Table Caption"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:keepNext/>
    <w:spacing w:before="240" w:after="120" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="0" w:right="0" w:firstLine="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:i/>
  </w:rPr>
</w:style>""",
    "BlockText": f"""<w:style w:type="paragraph" w:styleId="BlockText">
  <w:name w:val="Block Text"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="120" w:after="120" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="720" w:right="720" w:firstLine="0"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:i/>
  </w:rPr>
</w:style>""",
    "TOCHeading": f"""<w:style w:type="paragraph" w:styleId="TOCHeading">
  <w:name w:val="TOC Heading"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="39"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="360" w:after="360" w:line="240" w:lineRule="auto"/>
    <w:jc w:val="center"/>
    <w:outlineLvl w:val="9"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "TOC1": f"""<w:style w:type="paragraph" w:styleId="TOC1">
  <w:name w:val="toc 1"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:tabs>
      <w:tab w:val="right" w:leader="dot" w:pos="9072"/>
    </w:tabs>
    <w:spacing w:before="120" w:after="40" w:line="260" w:lineRule="auto"/>
    <w:ind w:left="0" w:right="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "TOC2": f"""<w:style w:type="paragraph" w:styleId="TOC2">
  <w:name w:val="toc 2"/>
  <w:basedOn w:val="TOC1"/>
  <w:next w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:tabs>
      <w:tab w:val="right" w:leader="dot" w:pos="9072"/>
    </w:tabs>
    <w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="360" w:right="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b w:val="0"/>
    <w:bCs w:val="0"/>
  </w:rPr>
</w:style>""",
    "TOC3": f"""<w:style w:type="paragraph" w:styleId="TOC3">
  <w:name w:val="toc 3"/>
  <w:basedOn w:val="TOC2"/>
  <w:next w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:tabs>
      <w:tab w:val="right" w:leader="dot" w:pos="9072"/>
    </w:tabs>
    <w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="720" w:right="0"/>
    <w:jc w:val="left"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
    <w:b w:val="0"/>
    <w:bCs w:val="0"/>
  </w:rPr>
</w:style>""",
    "CoverImage": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverImage">
  <w:name w:val="CoverImage"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0"/>
    <w:jc w:val="center"/>
  </w:pPr>
</w:style>""",
    "CoverTitle": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverTitle">
  <w:name w:val="CoverTitle"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="567" w:after="0" w:line="300" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "CoverSubtitle": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverSubtitle">
  <w:name w:val="CoverSubtitle"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="170" w:after="0" w:line="300" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "CoverCourse": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverCourse">
  <w:name w:val="CoverCourse"/>
  <w:basedOn w:val="CoverLine"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="454" w:after="0" w:line="300" w:lineRule="auto"/>
  </w:pPr>
</w:style>""",
    "CoverLecturer": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverLecturer">
  <w:name w:val="CoverLecturer"/>
  <w:basedOn w:val="CoverLine"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="227" w:after="0" w:line="300" w:lineRule="auto"/>
  </w:pPr>
</w:style>""",
    "CoverName": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverName">
  <w:name w:val="CoverName"/>
  <w:basedOn w:val="CoverLine"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:before="170" w:after="0" w:line="300" w:lineRule="auto"/>
  </w:pPr>
</w:style>""",
    "CoverLine": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverLine">
  <w:name w:val="CoverLine"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0" w:line="300" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "CoverInstitution": f"""<w:style w:type="paragraph" w:customStyle="1" w:styleId="CoverInstitution">
  <w:name w:val="CoverInstitution"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="0" w:line="300" w:lineRule="auto"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:color w:val="000000"/>
    <w:sz w:val="28"/>
    <w:szCs w:val="28"/>
    <w:b/>
    <w:bCs/>
  </w:rPr>
</w:style>""",
    "Bibliography": f"""<w:style w:type="paragraph" w:styleId="Bibliography">
  <w:name w:val="Bibliography"/>
  <w:basedOn w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:spacing w:after="120" w:line="360" w:lineRule="auto"/>
    <w:ind w:left="709" w:hanging="709"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:rPr>
    {TNR}
    <w:sz w:val="24"/>
    <w:szCs w:val="24"/>
  </w:rPr>
</w:style>""",
    "Table": f"""<w:style w:type="table" w:styleId="Table">
  <w:name w:val="Table"/>
  <w:basedOn w:val="TableNormal"/>
  <w:uiPriority w:val="59"/>
  <w:qFormat/>
  <w:tblPr>
    <w:tblInd w:type="dxa" w:w="0"/>
    <w:tblBorders>
      <w:top w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
      <w:left w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
      <w:bottom w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
      <w:right w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
      <w:insideH w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
      <w:insideV w:val="single" w:sz="4" w:space="0" w:color="8C8C8C"/>
    </w:tblBorders>
    <w:tblCellMar>
      <w:top w:type="dxa" w:w="80"/>
      <w:left w:type="dxa" w:w="120"/>
      <w:bottom w:type="dxa" w:w="80"/>
      <w:right w:type="dxa" w:w="120"/>
    </w:tblCellMar>
  </w:tblPr>
  <w:tblStylePr w:type="firstRow">
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:before="60" w:after="60" w:line="240" w:lineRule="auto"/>
      <w:ind w:left="0" w:right="0" w:firstLine="0"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:bCs/>
    </w:rPr>
    <w:tcPr>
      <w:vAlign w:val="center"/>
    </w:tcPr>
  </w:tblStylePr>
  <w:tblStylePr w:type="lastRow"/>
  <w:tblStylePr w:type="firstCol"/>
  <w:tblStylePr w:type="lastCol"/>
  <w:tblStylePr w:type="band1Vert"/>
  <w:tblStylePr w:type="band2Vert"/>
  <w:tblStylePr w:type="band1Horz"/>
  <w:tblStylePr w:type="band2Horz"/>
</w:style>""",
}

SECTPR = """<w:sectPr>
  <w:footerReference r:id="rIdF1" w:type="default"/>
  <w:footnotePr>
    <w:numRestart w:val="eachSect"/>
  </w:footnotePr>
  <w:pgSz w:w="11906" w:h="16838"/>
  <w:pgMar w:top="1134" w:right="1417" w:bottom="1701" w:left="1417" w:header="720" w:footer="720" w:gutter="0"/>
</w:sectPr>"""

FOOTER1 = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>"""


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ref-default.docx"
    dst = sys.argv[2] if len(sys.argv) > 2 else "reference.docx"

    with zipfile.ZipFile(src, "r") as zin:
        names = zin.namelist()
        items = {n: zin.read(n) for n in names}

    styles = items["word/styles.xml"].decode("utf-8")
    missing = []
    for style_id, block in STYLES.items():
        pattern = re.compile(
            rf'<w:style\b[^>]*w:styleId="{style_id}"[^>]*>.*?</w:style>',
            re.S,
        )
        if pattern.search(styles):
            styles = pattern.sub(block, styles)
        else:
            missing.append(style_id)
    if missing:
        styles = styles.replace("</w:styles>", "".join(STYLES[s] for s in missing) + "</w:styles>")
        print(f"[add] style baru ditambahkan: {', '.join(missing)}")
    items["word/styles.xml"] = styles.encode("utf-8")

    doc = items["word/document.xml"].decode("utf-8")
    if re.search(r"<w:sectPr>.*?</w:sectPr>", doc, re.S):
        doc = re.sub(r"<w:sectPr>.*?</w:sectPr>", SECTPR, doc, flags=re.S)
    else:
        print("[warn] sectPr tidak ditemukan di document.xml")
    items["word/document.xml"] = doc.encode("utf-8")

    settings = items["word/settings.xml"].decode("utf-8")
    if "<w:updateFields" not in settings:
        settings = settings.replace(
            "</w:settings>", '<w:updateFields w:val="true"/></w:settings>'
        )
        print("[add] updateFields diaktifkan di settings.xml")
    items["word/settings.xml"] = settings.encode("utf-8")

    if "word/footer1.xml" not in items:
        items["word/footer1.xml"] = FOOTER1.encode("utf-8")
        ct = items["[Content_Types].xml"].decode("utf-8")
        if "footer1.xml" not in ct:
            ct = ct.replace(
                "</Types>",
                '<Override PartName="/word/footer1.xml" '
                'ContentType="application/vnd.openxmlformats-officedocument.'
                'wordprocessingml.footer+xml"/></Types>',
            )
            items["[Content_Types].xml"] = ct.encode("utf-8")
        rels = items["word/_rels/document.xml.rels"].decode("utf-8")
        if 'Id="rIdF1"' not in rels:
            rels = rels.replace(
                "</Relationships>",
                '<Relationship Id="rIdF1" '
                'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" '
                'Target="footer1.xml"/></Relationships>',
            )
            items["word/_rels/document.xml.rels"] = rels.encode("utf-8")
        print("[add] footer1.xml (nomor halaman PAGE) + rels + content-types")

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for n, content in items.items():
            zout.writestr(n, content)

    print(f"[OK] reference.docx dibuat: {dst}")


if __name__ == "__main__":
    main()