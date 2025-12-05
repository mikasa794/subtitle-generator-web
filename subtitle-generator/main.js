const fileInput = document.getElementById('fileInput')
const fileNameEl = document.getElementById('fileName')
const lineHeightEl = document.getElementById('lineHeight')
const fontSizeEl = document.getElementById('fontSize')
const fillColorEl = document.getElementById('fillColor')
const strokeColorEl = document.getElementById('strokeColor')
const barColorEl = document.getElementById('barColor')
const barAlphaEl = document.getElementById('barAlpha')
const barRadiusEl = document.getElementById('barRadius')
const gapEl = document.getElementById('gap')
const paddingXEl = document.getElementById('paddingX')
const bottomMarginEl = document.getElementById('bottomMargin')
const fontFamilyEl = document.getElementById('fontFamily')
const fontWeightEl = document.getElementById('fontWeight')
const letterSpacingEl = document.getElementById('letterSpacing')
const langSelectEl = document.getElementById('langSelect')
const textFileInputEl = document.getElementById('textFileInput')
const textInput = document.getElementById('textInput')
const generateBtn = document.getElementById('generateBtn')
const saveBtn = document.getElementById('saveBtn')
const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')

let img = null
let imgURL = null
let currentLang = 'zh'

function resetCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  canvas.width = 0
  canvas.height = 0
}

function loadImageFromFile(file) {
  return new Promise((resolve, reject) => {
    const valid = ['image/png', 'image/jpeg', 'image/jpg', 'image/webp']
    if (!valid.includes(file.type)) {
      reject(new Error('不支持的文件类型'))
      return
    }
    const reader = new FileReader()
    reader.onload = () => {
      if (imgURL) URL.revokeObjectURL(imgURL)
      imgURL = reader.result
      const image = new Image()
      image.onload = () => resolve(image)
      image.onerror = () => reject(new Error('图片加载失败'))
      image.src = imgURL
    }
    reader.onerror = () => reject(new Error('文件读取失败'))
    reader.readAsDataURL(file)
  })
}

fileInput.addEventListener('change', async () => {
  const file = fileInput.files && fileInput.files[0]
  if (!file) return
  fileNameEl.textContent = file.name
  try {
    img = await loadImageFromFile(file)
    resetCanvas()
  } catch (e) {
    alert(e.message)
  }
})

const i18n = {
  zh: {
    title: '图片字幕生成器',
    chooseFile: '选择文件',
    lang: '语言',
    importText: '导入文本文件',
    lineHeightLabel: '字幕高度(px)',
    fontSizeLabel: '字体大小(px)',
    fillColorLabel: '字体颜色',
    strokeColorLabel: '轮廓颜色',
    barColorLabel: '背景颜色',
    barAlphaLabel: '背景透明度(0-1)',
    barRadiusLabel: '背景圆角(px)',
    gapLabel: '行间隙(px)',
    paddingXLabel: '左右内边距(px)',
    bottomMarginLabel: '底部边距(px)',
    fontFamilyLabel: '字体',
    fontWeightLabel: '字重',
    letterSpacingLabel: '字间距(px)',
    textareaPlaceholder: '在此输入多行字幕，回车换行',
    generateBtn: '生成字幕图片',
    saveBtn: '保存图片',
    needImage: '请先选择图片',
    tooHigh: '字幕区域过高，请调整行数或参数',
    needGenerate: '请先生成字幕图片'
  },
  en: {
    title: 'Subtitle Image Generator',
    chooseFile: 'Choose File',
    lang: 'Language',
    importText: 'Import Text File',
    lineHeightLabel: 'Line Height(px)',
    fontSizeLabel: 'Font Size(px)',
    fillColorLabel: 'Fill Color',
    strokeColorLabel: 'Stroke Color',
    barColorLabel: 'Bar Color',
    barAlphaLabel: 'Bar Alpha(0-1)',
    barRadiusLabel: 'Bar Radius(px)',
    gapLabel: 'Line Gap(px)',
    paddingXLabel: 'Side Padding(px)',
    bottomMarginLabel: 'Bottom Margin(px)',
    fontFamilyLabel: 'Font Family',
    fontWeightLabel: 'Font Weight',
    letterSpacingLabel: 'Letter Spacing(px)',
    textareaPlaceholder: 'Enter multi-line subtitles, press Enter to break lines',
    generateBtn: 'Generate',
    saveBtn: 'Save Image',
    needImage: 'Please choose an image first',
    tooHigh: 'Subtitle area is too tall, adjust lines or params',
    needGenerate: 'Generate the subtitle image first'
  }
}

function applyLang(lang){
  currentLang = lang
  const dict = i18n[lang]
  document.querySelectorAll('[data-i18n]').forEach(el=>{
    const key = el.getAttribute('data-i18n')
    if (dict[key]) el.textContent = dict[key]
  })
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el=>{
    const key = el.getAttribute('data-i18n-placeholder')
    if (dict[key]) el.setAttribute('placeholder', dict[key])
  })
}

applyLang(currentLang)
langSelectEl.addEventListener('change',()=>{
  applyLang(langSelectEl.value)
})

function parseTextFileContent(text, mime){
  const t = text.replace(/^\ufeff/,'')
  if (mime && mime.includes('json')){
    try{
      const arr = JSON.parse(t)
      if (Array.isArray(arr)) return arr.map(v=>String(v))
    }catch{}
  }
  const lines = t.split(/\r?\n/).map(s=>s.trimEnd())
  if (mime && mime.includes('csv')){
    return lines.map(line=>line.split(',').map(s=>s.trim()).join(' '))
  }
  return lines
}

textFileInputEl && textFileInputEl.addEventListener('change',()=>{
  const f = textFileInputEl.files && textFileInputEl.files[0]
  if (!f) return
  const reader = new FileReader()
  reader.onload = ()=>{
    const lines = parseTextFileContent(String(reader.result||''), f.type||'')
    textInput.value = (lines||['']).join('\n')
  }
  reader.readAsText(f, 'utf-8')
})

function getLines() {
  const raw = textInput.value || ''
  const lines = raw.split(/\r?\n/)
  if (lines.length === 1 && lines[0].trim() === '') return ['']
  return lines
}

function hexToRgb(hex) {
  const s = hex.replace('#','')
  const r = parseInt(s.substring(0,2),16)
  const g = parseInt(s.substring(2,4),16)
  const b = parseInt(s.substring(4,6),16)
  return [r,g,b]
}

function drawRoundedRect(x,y,w,h,r,color) {
  ctx.fillStyle = color
  if (!r) {
    ctx.fillRect(x,y,w,h)
    return
  }
  const rr = Math.min(r, h/2, w/2)
  ctx.beginPath()
  ctx.moveTo(x+rr,y)
  ctx.lineTo(x+w-rr,y)
  ctx.arcTo(x+w,y,x+w,y+rr,rr)
  ctx.lineTo(x+w,y+h-rr)
  ctx.arcTo(x+w,y+h,x+w-rr,y+h,rr)
  ctx.lineTo(x+rr,y+h)
  ctx.arcTo(x,y+h,x,y+h-rr,rr)
  ctx.lineTo(x,y+rr)
  ctx.arcTo(x,y,x+rr,y,rr)
  ctx.closePath()
  ctx.fill()
}

function measureTextWidth(text, font) {
  ctx.font = font
  let w = 0
  for (let i = 0; i < text.length; i++) {
    w += ctx.measureText(text[i]).width
  }
  return w
}

function drawTextWithSpacing(text, centerX, y, spacing, font, strokeStyle, fillStyle) {
  if (!text || text.trim() === '') return
  const baseWidth = measureTextWidth(text, font)
  const totalWidth = baseWidth + Math.max(0, spacing) * (text.length - 1)
  let x = centerX - totalWidth / 2
  ctx.font = font
  ctx.textAlign = 'left'
  ctx.textBaseline = 'middle'
  ctx.strokeStyle = strokeStyle
  ctx.fillStyle = fillStyle
  ctx.lineWidth = 2
  for (let i = 0; i < text.length; i++) {
    const ch = text[i]
    ctx.strokeText(ch, x, y)
    ctx.fillText(ch, x, y)
    x += ctx.measureText(ch).width + Math.max(0, spacing)
  }
}

function generate() {
  if (!img) {
    alert(i18n[currentLang].needImage)
    return
  }
  const dpr = window.devicePixelRatio || 1
  const margin = Math.max(0, Number(bottomMarginEl.value || 20))
  const gap = Math.max(0, Number(gapEl.value || 8))
  const paddingX = Math.max(0, Number(paddingXEl.value || 24))

  const lineHeight = Math.max(10, Number(lineHeightEl.value || 0))
  const fontSize = Math.max(10, Number(fontSizeEl.value || 0))
  const fillColor = fillColorEl.value || '#ffffff'
  const strokeColor = strokeColorEl.value || '#000000'
  const barColorHex = barColorEl.value || '#000000'
  const barAlpha = Math.min(1, Math.max(0, Number(barAlphaEl.value || 0.5)))
  const barRadius = Math.max(0, Number(barRadiusEl.value || 0))
  const fontFamily = fontFamilyEl.value || 'Microsoft YaHei'
  const fontWeight = fontWeightEl.value || '700'
  const letterSpacing = Math.max(0, Number(letterSpacingEl.value || 0))
  const lines = getLines()

  const totalH = lines.length * lineHeight + (lines.length - 1) * gap
  if (totalH > img.height * 0.4) {
    alert(i18n[currentLang].tooHigh)
    return
  }

  canvas.width = Math.floor(img.width * dpr)
  canvas.height = Math.floor(img.height * dpr)
  canvas.style.width = img.width + 'px'
  canvas.style.height = img.height + 'px'
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)

  ctx.drawImage(img, 0, 0, img.width, img.height)

  const startY = img.height - margin - totalH
  const barLeft = paddingX
  const barWidth = img.width - paddingX * 2
  const [r,g,b] = hexToRgb(barColorHex)
  const barColor = `rgba(${r},${g},${b},${barAlpha})`

  const fontStr = `${fontWeight} ${fontSize}px ${fontFamily}, Arial, sans-serif`

  for (let i = 0; i < lines.length; i++) {
    const barTop = startY + i * (lineHeight + gap)
    drawRoundedRect(barLeft, barTop, barWidth, lineHeight, barRadius, barColor)
    ctx.fillStyle = fillColor
    const textY = barTop + lineHeight / 2
    const textX = img.width / 2
    const text = lines[i]
    drawTextWithSpacing(text, textX, textY, letterSpacing, fontStr, strokeColor, fillColor)
  }
}

function save() {
  if (!canvas.width || !canvas.height) {
    alert(i18n[currentLang].needGenerate)
    return
  }
  canvas.toBlob(blob => {
    if (!blob) return
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'subtitle.png'
    document.body.appendChild(a)
    a.click()
    a.remove()
    URL.revokeObjectURL(url)
  }, 'image/png')
}

generateBtn.addEventListener('click', generate)
saveBtn.addEventListener('click', save)
