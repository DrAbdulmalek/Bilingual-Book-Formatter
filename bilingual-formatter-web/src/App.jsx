import { useState, useRef } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Alert, AlertDescription } from '@/components/ui/alert.jsx'
import { Upload, FileText, Download, Settings, Eye, BookOpen, Languages, Zap } from 'lucide-react'
import './App.css'

function App() {
  const [lang1File, setLang1File] = useState(null)
  const [lang2File, setLang2File] = useState(null)
  const [outputFormat, setOutputFormat] = useState('docx')
  const [processing, setProcessing] = useState(false)
  const [progress, setProgress] = useState(0)
  const [preview, setPreview] = useState('')
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')
  
  const lang1InputRef = useRef(null)
  const lang2InputRef = useRef(null)

  const handleFileSelect = (fileInputRef, setFile, fileType) => {
    fileInputRef.current?.click()
  }

  const handleFileChange = (event, setFile, fileType) => {
    const file = event.target.files[0]
    if (file) {
      const allowedTypes = ['.docx', '.pdf', '.epub', '.txt', '.md']
      const fileExtension = '.' + file.name.split('.').pop().toLowerCase()
      
      if (allowedTypes.includes(fileExtension)) {
        setFile(file)
        setError('')
      } else {
        setError(`نوع الملف غير مدعوم. الأنواع المدعومة: ${allowedTypes.join(', ')}`)
      }
    }
  }

  const handlePreview = async () => {
    if (!lang1File || !lang2File) {
      setError('يرجى اختيار كلا الملفين أولاً')
      return
    }

    setPreview('جاري تحميل المعاينة...')
    
    // محاكاة معاينة المحتوى
    setTimeout(() => {
      const samplePreview = `
معاينة المحتوى:

--- الفقرة 1 ---
الملف الأول (${lang1File.name}): This is a sample paragraph from the first document...
الملف الثاني (${lang2File.name}): هذه فقرة نموذجية من المستند الثاني...

--- الفقرة 2 ---
الملف الأول: Another paragraph with different content structure...
الملف الثاني: فقرة أخرى بهيكل محتوى مختلف...

--- الفقرة 3 ---
الملف الأول: The third paragraph demonstrates alignment...
الملف الثاني: الفقرة الثالثة تُظهر المحاذاة...
      `
      setPreview(samplePreview)
    }, 1500)
  }

  const handleProcess = async () => {
    if (!lang1File || !lang2File) {
      setError('يرجى اختيار كلا الملفين أولاً')
      return
    }

    setProcessing(true)
    setProgress(0)
    setError('')

    // محاكاة عملية المعالجة
    const progressSteps = [
      { step: 20, message: 'استخراج المحتوى من الملف الأول...' },
      { step: 40, message: 'استخراج المحتوى من الملف الثاني...' },
      { step: 60, message: 'محاذاة المحتوى...' },
      { step: 80, message: 'معالجة الصور...' },
      { step: 100, message: 'إنشاء الملف النهائي...' }
    ]

    for (const { step, message } of progressSteps) {
      await new Promise(resolve => setTimeout(resolve, 1000))
      setProgress(step)
      console.log(message)
    }

    // محاكاة النتيجة
    setResult({
      filename: `bilingual_output.${outputFormat}`,
      size: '2.5 MB',
      pages: 45,
      downloadUrl: '#'
    })

    setProcessing(false)
  }

  const handleDownload = () => {
    // في التطبيق الحقيقي، هذا سيقوم بتحميل الملف الفعلي
    alert('سيتم تحميل الملف قريباً...')
  }

  const clearAll = () => {
    setLang1File(null)
    setLang2File(null)
    setPreview('')
    setResult(null)
    setError('')
    setProgress(0)
    if (lang1InputRef.current) lang1InputRef.current.value = ''
    if (lang2InputRef.current) lang2InputRef.current.value = ''
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <BookOpen className="h-10 w-10 text-blue-600" />
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white">
              Bilingual Book Formatter
            </h1>
            <Languages className="h-10 w-10 text-blue-600" />
          </div>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            أداة متطورة لمعالجة الكتب والمستندات ثنائية اللغة مع دعم صيغ متعددة وميزات متقدمة
          </p>
          <div className="flex justify-center gap-2 mt-4">
            <Badge variant="secondary">DOCX</Badge>
            <Badge variant="secondary">PDF</Badge>
            <Badge variant="secondary">EPUB</Badge>
            <Badge variant="secondary">HTML</Badge>
          </div>
        </div>

        {/* Error Alert */}
        {error && (
          <Alert className="mb-6 border-red-200 bg-red-50 text-red-800">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        <Tabs defaultValue="process" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="process" className="flex items-center gap-2">
              <Zap className="h-4 w-4" />
              معالجة الملفات
            </TabsTrigger>
            <TabsTrigger value="preview" className="flex items-center gap-2">
              <Eye className="h-4 w-4" />
              معاينة المحتوى
            </TabsTrigger>
            <TabsTrigger value="settings" className="flex items-center gap-2">
              <Settings className="h-4 w-4" />
              الإعدادات
            </TabsTrigger>
          </TabsList>

          <TabsContent value="process" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* File Selection */}
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Upload className="h-5 w-5" />
                    اختيار الملفات
                  </CardTitle>
                  <CardDescription>
                    اختر الملفين اللذين تريد دمجهما في مستند ثنائي اللغة
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  {/* First File */}
                  <div className="space-y-2">
                    <Label htmlFor="lang1">الملف الأول</Label>
                    <div className="flex items-center gap-2">
                      <Button
                        variant="outline"
                        onClick={() => handleFileSelect(lang1InputRef, setLang1File, 'lang1')}
                        className="flex-1"
                      >
                        <FileText className="h-4 w-4 mr-2" />
                        {lang1File ? lang1File.name : 'اختيار ملف'}
                      </Button>
                      <input
                        ref={lang1InputRef}
                        type="file"
                        className="hidden"
                        accept=".docx,.pdf,.epub,.txt,.md"
                        onChange={(e) => handleFileChange(e, setLang1File, 'lang1')}
                      />
                    </div>
                  </div>

                  {/* Second File */}
                  <div className="space-y-2">
                    <Label htmlFor="lang2">الملف الثاني</Label>
                    <div className="flex items-center gap-2">
                      <Button
                        variant="outline"
                        onClick={() => handleFileSelect(lang2InputRef, setLang2File, 'lang2')}
                        className="flex-1"
                      >
                        <FileText className="h-4 w-4 mr-2" />
                        {lang2File ? lang2File.name : 'اختيار ملف'}
                      </Button>
                      <input
                        ref={lang2InputRef}
                        type="file"
                        className="hidden"
                        accept=".docx,.pdf,.epub,.txt,.md"
                        onChange={(e) => handleFileChange(e, setLang2File, 'lang2')}
                      />
                    </div>
                  </div>

                  {/* Output Format */}
                  <div className="space-y-2">
                    <Label>تنسيق الإخراج</Label>
                    <Select value={outputFormat} onValueChange={setOutputFormat}>
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="docx">DOCX (Word Document)</SelectItem>
                        <SelectItem value="epub">EPUB (E-Book)</SelectItem>
                        <SelectItem value="pdf">PDF (Portable Document)</SelectItem>
                        <SelectItem value="html">HTML (Web Page)</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </CardContent>
              </Card>

              {/* Processing & Results */}
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Zap className="h-5 w-5" />
                    المعالجة والنتائج
                  </CardTitle>
                  <CardDescription>
                    ابدأ معالجة الملفات وتحميل النتيجة
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  {/* Progress Bar */}
                  {processing && (
                    <div className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span>جاري المعالجة...</span>
                        <span>{progress}%</span>
                      </div>
                      <Progress value={progress} className="w-full" />
                    </div>
                  )}

                  {/* Action Buttons */}
                  <div className="flex flex-col gap-2">
                    <Button
                      onClick={handlePreview}
                      variant="outline"
                      disabled={!lang1File || !lang2File || processing}
                      className="w-full"
                    >
                      <Eye className="h-4 w-4 mr-2" />
                      معاينة المحتوى
                    </Button>
                    
                    <Button
                      onClick={handleProcess}
                      disabled={!lang1File || !lang2File || processing}
                      className="w-full"
                    >
                      <Zap className="h-4 w-4 mr-2" />
                      {processing ? 'جاري المعالجة...' : 'بدء المعالجة'}
                    </Button>

                    {result && (
                      <Button
                        onClick={handleDownload}
                        variant="default"
                        className="w-full bg-green-600 hover:bg-green-700"
                      >
                        <Download className="h-4 w-4 mr-2" />
                        تحميل النتيجة ({result.size})
                      </Button>
                    )}

                    <Button
                      onClick={clearAll}
                      variant="outline"
                      className="w-full"
                    >
                      مسح الكل
                    </Button>
                  </div>

                  {/* Result Info */}
                  {result && (
                    <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-800">
                      <h4 className="font-semibold text-green-800 dark:text-green-200 mb-2">
                        تمت المعالجة بنجاح!
                      </h4>
                      <div className="text-sm text-green-700 dark:text-green-300 space-y-1">
                        <p>اسم الملف: {result.filename}</p>
                        <p>حجم الملف: {result.size}</p>
                        <p>عدد الصفحات: {result.pages}</p>
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="preview" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Eye className="h-5 w-5" />
                  معاينة المحتوى
                </CardTitle>
                <CardDescription>
                  اعرض عينة من المحتوى المحاذي قبل المعالجة النهائية
                </CardDescription>
              </CardHeader>
              <CardContent>
                {preview ? (
                  <Textarea
                    value={preview}
                    readOnly
                    className="min-h-[400px] font-mono text-sm"
                    placeholder="ستظهر معاينة المحتوى هنا..."
                  />
                ) : (
                  <div className="text-center py-12 text-gray-500">
                    <Eye className="h-12 w-12 mx-auto mb-4 opacity-50" />
                    <p>اختر الملفين واضغط على "معاينة المحتوى" لعرض النتيجة</p>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="settings" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle>إعدادات التنسيق</CardTitle>
                  <CardDescription>
                    تخصيص شكل وتنسيق المستند النهائي
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-2">
                    <Label>خط اللغة الإنجليزية</Label>
                    <Select defaultValue="times">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="times">Times New Roman</SelectItem>
                        <SelectItem value="arial">Arial</SelectItem>
                        <SelectItem value="calibri">Calibri</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label>خط اللغة العربية</Label>
                    <Select defaultValue="traditional">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="traditional">Traditional Arabic</SelectItem>
                        <SelectItem value="amiri">Amiri</SelectItem>
                        <SelectItem value="noto">Noto Sans Arabic</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label>حجم الخط</Label>
                    <Select defaultValue="12">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="10">10pt</SelectItem>
                        <SelectItem value="11">11pt</SelectItem>
                        <SelectItem value="12">12pt</SelectItem>
                        <SelectItem value="14">14pt</SelectItem>
                        <SelectItem value="16">16pt</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>إعدادات متقدمة</CardTitle>
                  <CardDescription>
                    خيارات إضافية لتحسين النتيجة
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-2">
                    <Label>موضع الصور</Label>
                    <Select defaultValue="center">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="center">وسط الصفحة</SelectItem>
                        <SelectItem value="left">يسار الصفحة</SelectItem>
                        <SelectItem value="right">يمين الصفحة</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label>جودة الصور</Label>
                    <Select defaultValue="high">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="low">منخفضة (سريع)</SelectItem>
                        <SelectItem value="medium">متوسطة</SelectItem>
                        <SelectItem value="high">عالية (بطيء)</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label>هوامش الصفحة (سم)</Label>
                    <div className="grid grid-cols-2 gap-2">
                      <Input placeholder="أعلى" defaultValue="2.5" />
                      <Input placeholder="أسفل" defaultValue="2.5" />
                      <Input placeholder="يسار" defaultValue="2.0" />
                      <Input placeholder="يمين" defaultValue="2.0" />
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>

        {/* Footer */}
        <div className="text-center mt-12 text-gray-600 dark:text-gray-400">
          <p className="text-sm">
            Bilingual Book Formatter v2.3 - تم التطوير بواسطة د. عبدالمالك تامر الحسيني
          </p>
          <p className="text-xs mt-1">
            يدعم DOCX، PDF، EPUB، HTML مع معالجة متقدمة للصور والنصوص
          </p>
        </div>
      </div>
    </div>
  )
}

export default App

