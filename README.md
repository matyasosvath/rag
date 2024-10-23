
Az alkalmazás három részből áll:
- Generatív nyelvi modell (LLM)
- Kereső motor és adatbázis (Elasticsearch)
- Backend service, ami a kettőt összeköti és a leendő front-end-et kiszolgálja

Ennek a megoldásnak szerintem az architektúra a legnagyobb előnye. Habár a hugginface könyvtáraknak van már beépített funkcionalitása RAG pipeline-okra (https://huggingface.co/learn/cookbook/en/advanced_rag), nekem az az eddigi tapasztalatom, hogy minél nagyobb és komplexebb rendszert építünk, annál fontosabb, hogy nagy kontrollunk legyen a különböző - jól szeparált - komponensekre.

Jelenleg egy egyszerű BM25-n alapuló hasonlóságot nézünk a kotnextus kereséséhez, ami nem a leghatékonyabb (lásd javaslatok).

Egy példa lekérdezést csatoltam.

Előnyök
- Elasticsearch egy keresési és analitikai motor, amely teljes szöveges keresést, log elemzést, strukturálatlan adatok indexelését és gyors lekérdezést biztosít.
- Docker konténerek használata. Lehetővé teszi a skálázhatóságot és robosztusságot stb.
- Text Generation Inference (TGI) használata, ami egy optimalizált inference rendszer nagy nyelvi modellekhez. Erőforráshatékony.
- Horizontális skálázás és load balancing könnyen megoldható
- Szeparált felelősségi körrel rendelkező komponensek, LLM vagy Elasticserach cseréje könnyű
- Backend egy egyszerű python konténer FastAPI-val -> könnyű, gyors fejlesztés és tesztelés

Javaslatok:
- vektor adatbázis és BERT modellek használata a beágyazásokhoz (Elasticsearch vektoradatbázis is, azt nem kellene cserélni)
- nagy, "releváns" adatbázis használata: a wikipédia első 1000 szövegét töltöttem be csak az egyszerűség kedvéért (lásd scripts/upload_to_es.py)
- szkriptek és más service-k kialakítása az adatok folyamatos növekedéséhez (node-k, shard-ok és replikák hozzáadása szükség szerint)
- llm cseréje: egy kicsi gpt modellt használtam a tesztelés miatt, llama vagy saját modellre cserélendő


A kódban sok helyre írtam "recommendation"-t vagy "suggestion"-t, amit javítani kellene egy minőségi kódhoz és production környezethez. Ezeket idő hiányában nem csináltam meg, illetve nem tudom mennyire "részletes" megoldást szeretnétek.





