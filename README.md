# RAG feladat

## Feladat

Implementálj egy Retrieval-Augmented Generation (RAG) alapú alkalmazást, amely különböző forrásokból származó adatokból tud kérdésekre válaszolni. A feladat egy Q&A pipeline megvalósítása, amelyet tetszőlegesen összetett komponensekből építhetsz fel.

## Adatok

Bármilyen szöveges tartalmat felhasználhatsz adatbázis létrehozásához, legyen az egy vagy több PDF, vagy akár egy Kaggle dataset. Az adatfeldolgozás mennyisége nem elsődleges szempont; a minőség és skálázhatóság fontosabb.

## Példák

https://huggingface.co/datasets/legacy-datasets/wikipedia
https://arxiv.org/pdf/1706.03762

## Technikai részletek

- Programozási nyelv: Python

- Kód: Ügyelj a kód reprodukálhatóságára és minőségére.

- Megjelenítés: Nem szükséges vizuális felület fejlesztése; egy jól felépített notebook is elegendő, amely érthetővé teszi az alkalmazás működését a bemutató során.

- Modellek és API-k: Ne használj fizetős API-kat. Külön értékeljük, ha a lehetőségeidhez mérten választasz modellt. Ha nem áll rendelkezésre megfelelő modell, imitálhatsz nagy nyelvi modell (LLM) válaszokat, de a megoldás legyen könnyen cserélhető.

- Framework: Szabadon használhatsz bármilyen framework-öt, de tudnod kell indokolni, miért azt választottad.

## Eredmények bemutatása

- Notebook: A bemutatáshoz nincs szükség külön prezentációra; a notebook-ot úgy kell elkészíteni, hogy könnyen érthető legyen.

- Részegységek bemutatása: Mutasd be a pipeline különböző részegységeit és a felhasznált technológiák indoklását.

- Teljesítmény és tesztelés: Ismertesd, hogy mik a jelenlegi megoldás bottleneck-jei, hogyan mérnéd és tesztelnéd az alkalmazás teljesítményét, illetve milyen javaslataid vannak a további fejlesztésekre.

## Értékelési szempontok

- Kód minősége

- Alkalmazás reprodukálhatósága

- A pipeline-ban felhasznált elemek és koncepció indokoltsága


---------


ES indoklás
Docker indoklás
TGI indoklás
Model indkolás: open-source, low memory, speed, context length
Backend indoklás:

Backend & llm különböző service



Javaslatok
- Konténerek feltöltése egy közös registry-be.

