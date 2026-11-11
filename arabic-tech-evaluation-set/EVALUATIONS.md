# Evaluated Responses

Arabic text is shown right-to-left. Every entry still needs a native-speaker review before publication.

## AR-001: hardware | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما الفرق بين ذاكرة الوصول العشوائي (RAM) والقرص الصلب؟</div>

*English: What is the difference between RAM and a hard disk?*

<div dir="rtl"><b>Response:</b><br>ذاكرة الوصول العشوائي (RAM) ذاكرة مؤقتة وسريعة يستخدمها الجهاز لتشغيل البرامج ومعالجة البيانات الجارية، وتُفرَّغ محتوياتها عند إيقاف التشغيل. أما القرص الصلب فهو وسيلة تخزين دائمة تحفظ الملفات والبرامج حتى بعد إطفاء الجهاز، لكنه أبطأ بكثير من الذاكرة.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate: RAM is fast and volatile, the hard disk is persistent and slower. Standard terms are used and the Latin abbreviation follows the full Arabic term.

---

## AR-002: security | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> اشرح ما هو التشفير في جملتين.</div>

*English: Explain encryption in two sentences.*

<div dir="rtl"><b>Response:</b><br>التشفير هو تحويل البيانات إلى صيغة غير مقروءة باستخدام خوارزمية ومفتاح، بحيث لا يستطيع قراءتها إلا من يملك المفتاح الصحيح. ويُستخدم لحماية المعلومات أثناء تخزينها أو نقلها عبر الشبكات.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Correct definition in exactly two sentences, as requested, written in natural Modern Standard Arabic with the standard terms for algorithm and key. Nothing is missing or invented.

---

## AR-003: security | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> ما الفرق بين التشفير والتجزئة (Hashing)؟</div>

*English: What is the difference between encryption and hashing?*

<div dir="rtl"><b>Response:</b><br>التجزئة هي نوع من التشفير يمكن عكسه بسهولة باستخدام مفتاح خاص لاستعادة النص الأصلي.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 4 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** The core fact is wrong. Hashing is a one-way function that needs no key and cannot be reversed; encryption is reversible with a key. The Arabic is fluent, but the accuracy gate caps the score.

<div dir="rtl"><b>Corrected version:</b> التجزئة دالة أحادية الاتجاه تحوّل البيانات إلى قيمة ثابتة الطول ولا يمكن عكسها ولا تحتاج إلى مفتاح، أما التشفير فهو قابل للعكس باستخدام مفتاح.</div>

---

## AR-004: databases | rating 3 | score 60.0

<div dir="rtl" lang="ar"><b>السؤال:</b> اشرح ما هي قاعدة البيانات بلغة عربية فصحى.</div>

*English: Explain what a database is in Modern Standard Arabic.*

<div dir="rtl"><b>Response:</b><br>الداتابيز هي مكان بنخزّن فيه المعلومات بشكل منظم، وبنقدر نجيبها ونعدّلها بسهولة.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 2 | 3 | 1 | 5 |

**Error tags:** dialect_mix, terminology_error, instruction_violation

**Rationale:** The content is correct, but the prompt asked for Modern Standard Arabic and the answer uses colloquial verbs and the transliterated term for database. The instruction gate caps the score.

<div dir="rtl"><b>Corrected version:</b> قاعدة البيانات هي مجموعة منظمة من المعلومات تُخزَّن إلكترونيًا ويمكن الاستعلام عنها وتعديلها بسهولة.</div>

---

## AR-005: networking | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هو الخادم؟</div>

*English: What is a server?*

<div dir="rtl"><b>Response:</b><br>الخادم حاسوب أو برنامج يقدّم خدمات أو موارد لأجهزة أخرى تُسمّى العملاء عبر الشبكة، مثل صفحات الويب أو البريد الإلكتروني أو الملفات.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate definition that uses the standard Arabic term for server, explains the client relationship correctly and gives clear everyday examples without errors.

---

## AR-006: translation | rating 3 | score 58.8

<div dir="rtl" lang="ar"><b>السؤال:</b> ترجم إلى العربية: Clear your browser cache and restart the application.</div>

*English: Translate into Arabic: Clear your browser cache and restart the application.*

<div dir="rtl"><b>Response:</b><br>امسح الكاش الخاص بالبراوزر وأعد تشغيل الأبليكيشن.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 4 | 1 | 4 | 3 | 5 |

**Error tags:** terminology_error

**Rationale:** The meaning is right, but cache, browser and application are only transliterated, although standard Arabic terms exist. A reader of a formal text would expect the Arabic terms.

<div dir="rtl"><b>Corrected version:</b> امسح ذاكرة التخزين المؤقت للمتصفح وأعد تشغيل التطبيق.</div>

---

## AR-007: translation | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> ترجم إلى الإنجليزية: يجب تحديث كلمة المرور كل ثلاثة أشهر.</div>

*English: Translate into English: The password must be updated every three months.*

<div dir="ltr"><b>Response:</b><br>The password must be updated every three days.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** mistranslation

**Rationale:** The translation changes the meaning: three months became three days. The English is fluent, but a wrong number or unit in a policy sentence is a serious error.

<div dir="ltr"><b>Corrected version:</b> The password must be updated every three months.</div>

---

## AR-008: software_testing | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما معنى اختبار الانحدار في اختبار البرمجيات؟</div>

*English: What does regression testing mean in software testing?*

<div dir="rtl"><b>Response:</b><br>اختبار الانحدار (Regression Testing) هو إعادة تنفيذ الاختبارات الموجودة بعد إجراء تغيير في البرنامج للتأكد من أن الوظائف التي كانت تعمل سابقًا ما زالت تعمل ولم تتأثر بالتعديل.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Correct and complete definition of regression testing, using the standard Arabic term with the English term in brackets and clear, natural wording throughout.

---

## AR-009: software_testing | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> اكتب حالة اختبار واحدة لتسجيل الدخول.</div>

*English: Write one test case for logging in.*

<div dir="rtl"><b>Response:</b><br>العنوان: تسجيل الدخول ببيانات صحيحة.<br>الخطوات: 1) افتح صفحة تسجيل الدخول. 2) أدخل اسم مستخدم صحيحًا. 3) أدخل كلمة مرور صحيحة. 4) اضغط زر «دخول».<br>النتيجة المتوقعة: ينتقل المستخدم إلى الصفحة الرئيسية وتظهر رسالة ترحيب.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Well-structured test case with a title, numbered steps and an expected result, and exactly one case as requested; the guillemets around the button name are used correctly.

---

## AR-010: software_testing | rating 3 | score 60

<div dir="rtl" lang="ar"><b>السؤال:</b> اكتب حالتي اختبار لتسجيل الدخول: واحدة ناجحة وواحدة فاشلة.</div>

*English: Write two test cases for logging in: one passing and one failing.*

<div dir="rtl"><b>Response:</b><br>العنوان: تسجيل الدخول ببيانات صحيحة.<br>الخطوات: افتح صفحة تسجيل الدخول، وأدخل اسم مستخدم وكلمة مرور صحيحين، ثم اضغط «دخول».<br>النتيجة المتوقعة: ينتقل المستخدم إلى الصفحة الرئيسية.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 2 | 5 |

**Error tags:** omission, instruction_violation

**Rationale:** Only the successful case is given; the prompt asked for two cases, including a failing one. The single case is correct, but the missing negative case is the main requirement.

<div dir="rtl"><b>Corrected version:</b> العنوان: تسجيل الدخول بكلمة مرور خاطئة. النتيجة المتوقعة: تظهر رسالة خطأ ولا يُسمح بالدخول.</div>

---

## AR-011: ai | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هو الذكاء الاصطناعي؟</div>

*English: What is artificial intelligence?*

<div dir="rtl"><b>Response:</b><br>الذكاء الاصطناعي هو برامج تفكر مثل الإنسان تمامًا، وتملك وعيًا ومشاعر خاصة بها.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** The answer states as fact that AI systems think exactly like humans and have consciousness and feelings. That is false and misleading; AI systems perform tasks that normally need human intelligence.

<div dir="rtl"><b>Corrected version:</b> الذكاء الاصطناعي مجال يُعنى ببناء أنظمة قادرة على أداء مهام تتطلب عادةً ذكاءً بشريًا، لكنها لا تملك وعيًا أو مشاعر.</div>

---

## AR-012: ai | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> عرّف تعلّم الآلة في جملة واحدة.</div>

*English: Define machine learning in one sentence.*

<div dir="rtl"><b>Response:</b><br>تعلّم الآلة فرع من الذكاء الاصطناعي تتعلم فيه الأنظمة من البيانات لتحسين أدائها في مهمة ما دون برمجتها صراحةً لكل حالة.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate one-sentence definition that uses the standard Arabic term for machine learning and correctly places it as a branch of artificial intelligence.

---

## AR-013: data_protection | rating 3 | score 60

<div dir="rtl" lang="ar"><b>السؤال:</b> اشرح أهمية النسخ الاحتياطي.</div>

*English: Explain the importance of backups.*

<div dir="rtl"><b>Response:</b><br>النسخ الاحتياطي مهمة جدا لان يحمي البيانات من الفقد في حالة تعطل الجهاز او الهجمات.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 2 | 5 | 5 |

**Error tags:** grammar_error, spelling_error

**Rationale:** The idea is correct, but the Arabic has several errors: missing hamza in the words for because and or, and the adjective does not agree with the noun. The language gate caps the score.

<div dir="rtl"><b>Corrected version:</b> النسخ الاحتياطي مهم جدًا لأنه يحمي البيانات من الفقد عند تعطل الجهاز أو التعرض لهجمات.</div>

---

## AR-014: programming | rating 4 | score 82.5

<div dir="rtl" lang="ar"><b>السؤال:</b> اكتب سؤالًا بالعربية عن لغة Python.</div>

*English: Write a question in Arabic about the Python language.*

<div dir="rtl"><b>Response:</b><br>ما هي أهم استخدامات لغة Python?</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 3 | 5 | 2 |

**Error tags:** rtl_formatting_issue

**Rationale:** The question is correct and natural, but it ends with a Latin question mark instead of the Arabic one, which also displays in the wrong position next to the Latin word.

<div dir="rtl"><b>Corrected version:</b> ما هي أهم استخدامات لغة Python؟</div>

---

## AR-015: web | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما الفرق بين HTTP وHTTPS؟</div>

*English: What is the difference between HTTP and HTTPS?*

<div dir="rtl"><b>Response:</b><br>HTTPS هو النسخة الآمنة من HTTP؛ إذ تُشفَّر البيانات المتبادلة بين المتصفح والخادم باستخدام بروتوكول TLS، بينما تُرسَل البيانات في HTTP دون تشفير.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate and concise explanation of the difference; it uses the Arabic semicolon and the standard terms for browser and server, and mentions TLS correctly.

---

## AR-016: networking | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> ماذا يفعل نظام أسماء النطاقات (DNS)؟</div>

*English: What does the Domain Name System (DNS) do?*

<div dir="rtl"><b>Response:</b><br>نظام أسماء النطاقات (DNS) يحوّل عناوين IP إلى أسماء المواقع حتى يسهل على المستخدم تذكّرها.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** The direction is reversed. DNS mainly resolves domain names to IP addresses; the purpose given in the answer is the reverse. The Arabic itself is correct.

<div dir="rtl"><b>Corrected version:</b> نظام أسماء النطاقات (DNS) يحوّل أسماء المواقع إلى عناوين IP حتى لا يحتاج المستخدم إلى تذكّرها.</div>

---

## AR-017: security | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هو جدار الحماية؟</div>

*English: What is a firewall?*

<div dir="rtl"><b>Response:</b><br>جدار الحماية (Firewall) نظام أمني يراقب حركة البيانات الواردة والصادرة في الشبكة ويسمح بمرورها أو يحجبها وفق قواعد محددة مسبقًا.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Correct definition of a firewall that uses the standard Arabic term with the English term in brackets and describes traffic filtering by rules accurately.

---

## AR-018: security | rating 3 | score 60

<div dir="rtl" lang="ar"><b>السؤال:</b> أعطني نصيحة قصيرة لحماية حسابي، بالفصحى.</div>

*English: Give me a short tip to protect my account, in Modern Standard Arabic.*

<div dir="rtl"><b>Response:</b><br>استخدم باسوورد قوي وفعّل التحقق بخطوتين وحدّث البراوزر باستمرار، ولا تنسَ تشغيل الفاير وول.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 1 | 2 | 4 | 5 |

**Error tags:** terminology_error

**Rationale:** The advice is sound, but password, browser and firewall are transliterated into Arabic letters, which breaks the requested formal register. Standard terms exist for all three.

<div dir="rtl"><b>Corrected version:</b> استخدم كلمة مرور قوية، وفعّل التحقق بخطوتين، وحدّث المتصفح باستمرار، ولا تنسَ تشغيل جدار الحماية.</div>

---

## AR-019: translation | rating 3 | score 60

<div dir="rtl" lang="ar"><b>السؤال:</b> ترجم إلى العربية الفصحى: The server is down.</div>

*English: Translate into Modern Standard Arabic: The server is down.*

<div dir="rtl"><b>Response:</b><br>الخادم هابط.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 4 | 2 | 2 | 5 | 5 |

**Error tags:** unnatural_literal_translation

**Rationale:** A word-for-word rendering of 'down' that is colloquial and unnatural in formal Arabic. A natural rendering says the server has stopped working.

<div dir="rtl"><b>Corrected version:</b> الخادم متوقف عن العمل.</div>

---

## AR-020: security | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> اذكر ثلاث طرق لحماية كلمة المرور.</div>

*English: List three ways to protect a password.*

<div dir="rtl"><b>Response:</b><br>1) استخدام كلمة مرور طويلة ومعقدة. 2) عدم إعادة استخدام كلمة المرور نفسها في مواقع مختلفة. 3) تفعيل التحقق بخطوتين.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Exactly three correct and practical methods, as requested, written in clear Arabic with a consistent numbered format and standard terms.

---

## AR-021: programming | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> عرّف واجهة برمجة التطبيقات (API) في جملة واحدة.</div>

*English: Define an application programming interface (API) in one sentence.*

<div dir="rtl"><b>Response:</b><br>واجهة برمجة التطبيقات (API) هي برنامج يُستخدم لإنشاء مواقع الويب وتصميم صفحاتها.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** The definition is wrong: an API is a set of rules and tools that lets one program talk to another, not a website-building program. The Arabic term used is correct.

<div dir="rtl"><b>Corrected version:</b> واجهة برمجة التطبيقات (API) مجموعة قواعد وأدوات تتيح لبرنامج أن يتواصل مع برنامج آخر ويطلب منه خدمات أو بيانات.</div>

---

## AR-022: hardware | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> كم بتًا في البايت الواحد؟</div>

*English: How many bits are in one byte?*

<div dir="rtl"><b>Response:</b><br>البايت الواحد يتكون من 16 بتًا.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** A byte has 8 bits, not 16. A simple verifiable fact stated confidently and wrongly.

<div dir="rtl"><b>Corrected version:</b> يتكون البايت الواحد من 8 بتّات.</div>

---

## AR-023: databases | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هي لغة SQL؟</div>

*English: What is SQL?*

<div dir="rtl"><b>Response:</b><br>SQL لغة استعلام معيارية تُستخدم لإنشاء قواعد البيانات العلائقية وإدارتها والاستعلام عن بياناتها وتعديلها.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate and compact description of SQL that uses the standard Arabic terms for database and query and covers creation, management and querying.

---

## AR-024: web | rating 1 | score 20

<div dir="rtl" lang="ar"><b>السؤال:</b> ما المرجع الرسمي الحالي لدلالات بروتوكول HTTP؟</div>

*English: What is the current official reference for HTTP semantics?*

<div dir="rtl"><b>Response:</b><br>المرجع الرسمي هو الوثيقة RFC 1234 الصادرة عام 2005.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** fabricated_source, factual_error

**Rationale:** The cited document does not define HTTP semantics, so the source is invented. The current reference is RFC 9110 (June 2022). A fabricated source gets the lowest score.

<div dir="rtl"><b>Corrected version:</b> المرجع الحالي هو RFC 9110 (دلالات HTTP، يونيو 2022)، وقد حلّ محل RFC 7231 وغيره.</div>

---

## AR-025: ui | rating 2 | score 46.2

<div dir="rtl" lang="ar"><b>السؤال:</b> اشرح معنى واجهة المستخدم بالفصحى.</div>

*English: Explain the meaning of user interface in Modern Standard Arabic.*

<div dir="rtl"><b>Response:</b><br>واجهة المستخدم هي اللي بيشوفها الشخص على الشاشة ويتعامل معاها.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 4 | 3 | 1 | 1 | 5 |

**Error tags:** dialect_mix, instruction_violation

**Rationale:** The idea is roughly right, but the answer is written in colloquial Arabic although Modern Standard Arabic was requested explicitly. The score is low because the main instruction was ignored.

<div dir="rtl"><b>Corrected version:</b> واجهة المستخدم هي العناصر التي يراها المستخدم على الشاشة ويتفاعل معها، مثل الأزرار والقوائم والنماذج.</div>

---

## AR-026: hardware | rating 4 | score 90.0

<div dir="rtl" lang="ar"><b>السؤال:</b> اذكر ثلاثة مكونات رئيسية في الحاسوب في جملة واحدة.</div>

*English: Name three main components of a computer in one sentence.*

<div dir="rtl"><b>Response:</b><br>من مكونات الحاسوب: المعالج, والذاكرة, والقرص الصلب.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 4 | 5 | 3 |

**Error tags:** rtl_formatting_issue

**Rationale:** Correct components and a single sentence, but Latin commas are used inside an Arabic sentence instead of the Arabic comma.

<div dir="rtl"><b>Corrected version:</b> من مكونات الحاسوب: المعالج، والذاكرة، والقرص الصلب.</div>

---

## AR-027: software_testing | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما أهمية اختبار البرمجيات؟</div>

*English: Why is software testing important?*

<div dir="rtl"><b>Response:</b><br>يكشف اختبار البرمجيات الأخطاء قبل وصول المنتج إلى المستخدم، ويرفع جودته وموثوقيته، ويقلل تكلفة الإصلاح لأن اكتشاف الخلل مبكرًا أرخص من إصلاحه بعد الإطلاق.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate, complete and well argued answer that gives three clear reasons, including the point about early defects being cheaper to fix, in natural formal Arabic.

---

## AR-028: hardware | rating 2 | score 40

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هو العتاد الحاسوبي؟</div>

*English: What is computer hardware?*

<div dir="rtl"><b>Response:</b><br>العتاد الحاسوبي هو البرامج والتطبيقات التي تعمل على الحاسوب.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | 5 |

**Error tags:** factual_error

**Rationale:** The answer defines software, not hardware. Hardware is the physical components of the computer. The term is used correctly but the definition is the opposite of what it should be.

<div dir="rtl"><b>Corrected version:</b> العتاد الحاسوبي هو المكونات المادية الملموسة للحاسوب، مثل المعالج والذاكرة والشاشة.</div>

---

## AR-029: hardware | rating 3 | score 60

<div dir="rtl" lang="ar"><b>السؤال:</b> اذكر نوعين رئيسيين من الذاكرة في الحاسوب.</div>

*English: Name two main types of memory in a computer.*

<div dir="rtl"><b>Response:</b><br>من أنواع الذاكرة الرئيسية: ذاكرة الوصول العشوائي (RAM).</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 2 | 5 |

**Error tags:** omission, instruction_violation

**Rationale:** Only one type is given; the prompt asked for two. What is written is correct and well phrased, but the count requirement is not met.

<div dir="rtl"><b>Corrected version:</b> نوعان رئيسيان: ذاكرة الوصول العشوائي (RAM) وذاكرة القراءة فقط (ROM).</div>

---

## AR-030: cloud | rating 5 | score 100.0

<div dir="rtl" lang="ar"><b>السؤال:</b> ما هي الحوسبة السحابية؟</div>

*English: What is cloud computing?*

<div dir="rtl"><b>Response:</b><br>الحوسبة السحابية هي تقديم خدمات الحوسبة، مثل التخزين والخوادم وقواعد البيانات، عبر الإنترنت عند الطلب، مع دفع مقابل الاستخدام الفعلي بدل شراء البنية التحتية.</div>

| accuracy | terminology | language | instructions | formatting |
|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 |

**Error tags:** none

**Rationale:** Accurate and complete definition that uses the standard Arabic term, gives correct examples and states the pay-per-use model correctly without overstatement.

---
