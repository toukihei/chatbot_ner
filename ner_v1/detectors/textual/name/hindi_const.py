# coding=utf-8
HINDI_BADWORDS = [u'बकर छोड़',
                  u'बाहें छोड़',
                  u'बाहें के लॉड',
                  u'बाहें के टक्के',
                  u'बकलंड',
                  u'बेटी छोड़',
                  u'भढ़ावा',
                  u'भद्वे का अवलट',
                  u'भाई छोड़',
                  u'भांड ख़ौ',
                  u'भोंसरी वाला',
                  u'भूट्नी का',
                  u'भोसद छोड़',
                  u'भोसदीके',
                  u'बर की चटनी',
                  u'च्छेद',
                  u'छ्होला फुदकना',
                  u'छिनाल',
                  u'छोड़ेला',
                  u'छोद्रा',
                  u'छोड़ू भगत',
                  u'छोड़ू',
                  u'चूछीी',
                  u'छूट का बाल',
                  u'छूट के भूत',
                  u'छूट मारनी का',
                  u'चूतिया',
                  u'चुदाई खाना',
                  u'चुड़ान छुड़ा',
                  u'छूट का पुजारी',
                  u'छूट के ढक्कन',
                  u'छूट के गुलाम',
                  u'छूट मारी के',
                  u'छूट मारीके',
                  u'छूट',
                  u'चूटान',
                  u'कुंटमामा',
                  u'गांद का माखन',
                  u'गांद मैं डंडा',
                  u'गांद मैं कीरा',
                  u'गांद मैं ला**आन',
                  u'गांद मरौ',
                  u'गांद',
                  u'गांड्फाट',
                  u'गांदमास्ती',
                  u'गान्डू',
                  u'हराम ज़ादा',
                  u'हरामी',
                  u'हिजड़े',
                  u'झाँत के पिस्सू',
                  u'झल्ला',
                  u'झांट चातु',
                  u'झांट के बाल',
                  u'कड़क माल',
                  u'कमीना',
                  u'कुत्ते का अवलट',
                  u'कुत्ते का बीज',
                  u'कुट्टिया',
                  u'लॉडा, लंड',
                  u'लवंडर',
                  u'ळव्ड',
                  u'लवदे के बाल',
                  u'लंड',
                  u'लंड चूसू',
                  u'मा चूड़ी',
                  u'फुदधि',
                  u'रांडी बाजेर',
                  u'रुंडी का बचा',
                  u'रुंडी के टट्टी पे बियतने वाला मखी',
                  u'रुंडी खाना',
                  u'रुंडी की बची',
                  u'मदरचोड़',
                  u'भोसदीके',
                  u'भें छोड़',
                  u'बेटी छोड़',
                  u'भढ़ावा',
                  u'छोड़ू',
                  u'चूतिया',
                  u'गांद',
                  u'गान्डू',
                  u'गढ़ा, बकलंड',
                  u'लॉडा, लंड',
                  u'हियिरा',
                  u'कुट्टिया',
                  u'पाद',
                  u'रंडी',
                  u'साला कुत्ता',
                  u'साली कुट्टी',
                  u'टट्टी',
                  u'कमीना',
                  u'छूट के पसीने में तले हुए भजिए',
                  u'छूट के ढक्कन',
                  u'छूट के गुलाम',
                  u'चूतिया का भेजा घास खाने गया है',
                  u'छूट मारनी का',
                  u'छूट का बाल',
                  u'छिपकली के झाट के बाल',
                  u'छिपकली के झाट के पसीने',
                  u'छिपकली के गांद के पसीने',
                  u'छिपकली के छूट के पसीने',
                  u'छिपकली की भीगी छूट',
                  u'छिनाल के गद्दे के निपल के बाल के जून',
                  u'चुल्लू भर मूठ में डूब मार',
                  u'कुंटमामा',
                  u'च्छेद',
                  u'अपनी गांद में मुति डाल',
                  u'अपनी लंड चूस',
                  u'अपनी मा को जा चूस',
                  u'भें के लॉड',
                  u'भें के टक्के: गो आंड सक युवर सिस्टर’स बॉल्',
                  u'अबला नारी तेरा बुबले भारी',
                  u'भोंसरी',
                  u'भद्वे का अवलट',
                  u'भैंस की औलाद',
                  u'बुद्धा खूसट',
                  u'बोल तेरी गंद कैसे मारू',
                  u'बर की चटनी',
                  u'चुननी',
                  u'छिनाल',
                  u'चुदाई खाना',
                  u'चुड़ान छुड़ा',
                  u'छूट का पुजारी',
                  u'छूट का भूत',
                  u'गांद का माखन',
                  u'गांद मैं लाषसन',
                  u'गांद']

HINDI_STOPWORDS = [u'अत',
                   u'अपना',
                   u'अपनी',
                   u'अपने',
                   u'अभी',
                   u'अंदर',
                   u'आदि',
                   u'आप',
                   u'इत्यादि',
                   u'इन ',
                   u'इनका',
                   u'इन्हीं',
                   u'इन्हें',
                   u'इन्हों',
                   u'इस',
                   u'इसका',
                   u'इसकी',
                   u'इसके',
                   u'इसमें',
                   u'इसी',
                   u'इसे',
                   u'उन',
                   u'उनका',
                   u'उनकी',
                   u'उनके',
                   u'उनको',
                   u'उन्हीं',
                   u'उन्हें',
                   u'उन्हों',
                   u'उस',
                   u'उसके',
                   u'उसी',
                   u'उसे',
                   u'एक',
                   u'एवं',
                   u'एस',
                   u'ऐसे',
                   u'और',
                   u'कई',
                   u'कर',
                   u'करता',
                   u'करते',
                   u'करना',
                   u'करने',
                   u'करें',
                   u'कहते',
                   u'कहा',
                   u'का',
                   u'काफ़ी',
                   u'कि',
                   u'कितना',
                   u'किन्हें',
                   u'किन्हों',
                   u'किया',
                   u'किर',
                   u'किस',
                   u'किसी',
                   u'किसे',
                   u'की',
                   u'कुछ',
                   u'कुल',
                   u'के',
                   u'को',
                   u'कोई',
                   u'कौन',
                   u'कौनसा',
                   u'गया',
                   u'घर',
                   u'जब',
                   u'जहाँ',
                   u'जा',
                   u'जितना',
                   u'जिन',
                   u'जिन्हें',
                   u'जिन्हों',
                   u'जिस',
                   u'जिसे',
                   u'जीधर',
                   u'जैसा',
                   u'जैसे',
                   u'जो',
                   u'तक',
                   u'तब',
                   u'तरह',
                   u'तिन',
                   u'तिन्हें',
                   u'तिन्हों',
                   u'तिस',
                   u'तिसे',
                   u'तो',
                   u'था',
                   u'थी',
                   u'थे',
                   u'दबारा',
                   u'दिया',
                   u'दुसरा',
                   u'दूसरे',
                   u'दो',
                   u'द्वारा',
                   u'न',
                   u'नके',
                   u'नहीं',
                   u'ना',
                   u'निहायत',
                   u'नीचे',
                   u'ने',
                   u'पर',
                   u'पहले',
                   u'पूरा',
                   u'पे',
                   u'फिर',
                   u'बनी',
                   u'बही',
                   u'बहुत',
                   u'बाद',
                   u'बाला',
                   u'बिलकुल',
                   u'भी',
                   u'भीतर',
                   u'मगर',
                   u'मानो',
                   u'मे',
                   u'में',
                   u'यदि',
                   u'यह',
                   u'यहाँ',
                   u'यही',
                   u'या',
                   u'यिह',
                   u'ये',
                   u'रखें',
                   u'रहा',
                   u'रहे',
                   u'ऱ्वासा',
                   u'लिए',
                   u'लिये',
                   u'लेकिन',
                   u'व',
                   u'वग़ैरह',
                   u'वर्ग',
                   u'वह',
                   u'वहाँ',
                   u'वहीं',
                   u'वाले',
                   u'वुह',
                   u'वे',
                   u'सकता',
                   u'सकते',
                   u'सबसे',
                   u'सभी',
                   u'साथ',
                   u'साबुत',
                   u'साभ',
                   u'सारा',
                   u'से',
                   u'सो',
                   u'संग',
                   u'ही',
                   u'हुआ',
                   u'हुई',
                   u'हुए',
                   u'है',
                   u'हैं',
                   u'हो',
                   u'होता',
                   u'होती',
                   u'होते',
                   u'होना',
                   u'होन',
                   u'हूँ']

HINDI_QUESTIONWORDS = [u'क्या', u'कब', u'कहा', u'क्यों', u'कौन', u'कौन', u'जिसे', u'जिसका', u'कैसे', u'कितने']

# Variants in "name" to check for previous context flag
NAME_VARIATIONS = ['name', u'नाम']

# Common hindi words occuring in context to a name
COMMON_HINDI_WORDS_OCCURING_WITH_NAME = {u"मुझे",
                                         u"हमें",
                                         u"मुझको",
                                         u"हमको",
                                         u"हमे",
                                         u"लोग",
                                         u"नाम",
                                         u"से",
                                         u"कहते",
                                         u"बुलाते",
                                         u"बुलाओ",
                                         u"नाम",
                                         u"मैं",
                                         u"हम",
                                         u"मै",
                                         u"मुझे",
                                         u"हमें",
                                         u"मुझको",
                                         u"हमको",
                                         u"हमे",
                                         u"कहते",
                                         u"बुलाते",
                                         u"बुलाओ",
                                         u"मुझे",
                                         u"मैं",
                                         u"मै)",
                                         u"कहते",
                                         u"बुलाते",
                                         u"बुलाओ",
                                         u"हमारा",
                                         u"मेरा"}
