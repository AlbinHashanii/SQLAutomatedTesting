# SQLAutomatedTesting


Testimi i injektimit SQL kontrollon nëse është e mundur të injektohen të dhëna në aplikacion në mënyrë që ai të ekzekutojë SQL Queries të kontrolluar nga përdoruesi në bazën e të dhënave. Testuesit gjejnë një cenueshmëri të injektimit SQL nëse aplikacioni përdor hyrjen e përdoruesit për të krijuar SQL queries pa vërtetimin e duhur të hyrjes. Një shfrytëzim i suksesshëm i kësaj klase cenueshmërie lejon një përdorues të paautorizuar të aksesojë ose manipulojë të dhënat në bazën e të dhënave.

Kjo është e mundur duke dhënë një URL të caktuar në një fushë teksti. Pastaj skripti në një gjuhë të caktuar, teston URL-në në një mënyrë të automatizuar.

Fajlli 'penetrationTesting.py' fillimisht teston për dobësitë e injektimit SQL duke shtuar thonjëza të vetme dhe të dyfishta në URL dhe duke analizuar përgjigjen. Nëse përgjigja tregon se URL-ja është e cenueshme, funksioni kthen True. Nëse jo, funksioni më pas kërkon në HTML-në e faqes për forma dhe teston çdo formë për dobësitë e injektimit SQL duke shtuar thonjëza të vetme dhe të dyfishta për të formuar hyrje dhe duke analizuar përgjigjen. Nëse ndonjë formë zbulohet se është e cenueshme, funksioni kthen True. Nëse nuk gjenden dobësi, funksioni kthen False.

Skripti përcakton gjithashtu një funksion ndihmës is_vulnerable(response), i cili merr një përgjigje HTTP si hyrje dhe kthen True nëse përgjigja tregon se URL-ja është e cenueshme ndaj sulmeve të injektimit SQL, dhe False ndryshe. Funksioni kërkon mesazhe specifike gabimi në përmbajtjen e përgjigjes që janë tregues të dobësive të injektimit SQL.

Pastaj fajlli 'automatedTesting' ku edhe ekzekutohet aplikacioni fillimisht importon libraritë dhe modulet e nevojshme, duke përfshirë tkinter për GUI, requests dhe re për trajtimin e kërkesave HTTP dhe shprehjeve të rregullta, përkatësisht, dhe unittest për shkrimin dhe ekzekutimin e testeve të unit.

Aplikacioni më pas përcakton një model shprehjeje të rregullt për të përputhur URL-të e vlefshme dhe një funksion give_result() që përdor funksionin scan_sql_injection() nga moduli penetrationTesting për të testuar një uebsajt të caktuar për dobësitë e injektimit SQL.

Aplikacioni përcakton gjithashtu disa funksione për të trajtuar ndërveprimet e përdoruesit me GUI, duke përfshirë check_injection() i cili thirret kur përdoruesi klikon butonin "TEST" dhe clear_clicked() që thirret kur përdoruesi klikon butonin "CLEAR".

Së fundi, aplikacioni krijon dritaren GUI dhe shton elemente të tilla si etiketat, fushat e hyrjes dhe butonat në të. Më pas hyn në ciklin kryesor të ngjarjeve për të pritur ndërveprimet e përdoruesit.
