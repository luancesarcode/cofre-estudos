---
tipo: home
tags: [home]
---

# 🏠 Home

> Requer o plugin **Dataview** ativado.

## 📚 Cadeiras ativas
```dataview
TABLE semestre AS "Semestre", professor AS "Professor", status AS "Status"
FROM "01_Cadeiras"
WHERE tipo = "cadeira" AND status = "ativa"
SORT semestre DESC, file.name ASC
```

## 🔁 Conceitos para revisar / incompletos
```dataview
TABLE area AS "Área", status AS "Status", ultima_revisao AS "Última revisão"
FROM "02_Conceitos"
WHERE contains(tags, "revisar") OR status = "rascunho" OR status = "revisar"
SORT ultima_revisao ASC
```

## 📥 Notas recentes na Inbox
```dataview
TABLE file.mtime AS "Modificada"
FROM "00_Inbox"
SORT file.mtime DESC
LIMIT 15
```

## 🧭 Atalhos
- Templates: [[Template_Cadeira]] · [[Template_Aula]] · [[Template_Conceito]]
- Comandos do tutor: `/extrair` · `/avaliar` · `/simulado` · `/simular`
