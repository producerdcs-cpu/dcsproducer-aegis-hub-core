# DcsProducer® AEGIS Hub Core — Pacote de Exportação

**Titular:** DcsProducer®  
**Data de geração:** 2026-10-16  
**Sessão AEGIS:** aegis-20261016-233741  
**Governança:** AEGIS Layer  

---

## Conteúdo do Pacote

```
dcsproducer-aegis-export/
├── skills/
│   ├── dcsproducer-aegis-hub-core/     ← Skill principal + orchestrator
│   └── six-pillars-engineer/           ← Skill irmã prioritária
├── labs/
│   ├── lab-01-observability-rag/
│   ├── lab-02-devsecops-agentic/
│   ├── lab-03-event-driven-agents/
│   └── lab-04-clean-arch-containers/
├── scripts/
│   └── aegis_orchestrator.py           ← Kernel de governança
├── docs/
│   ├── dcsproducer-aegis-hub-core-completo-20261016.pdf
│   ├── dcsproducer-9-pilares-aegis-20261016.pdf
│   └── dcsproducer-9-pilares-aegis-20261016.html
├── architecture/
│   └── dcsproducer-aegis-os-high-level.md
├── licensing/
│   └── modelo-licenciamento-dcsproducer-aegis.md
├── brand/
│   └── dcsproducer-brand.md
└── README.md                           ← este arquivo
```

---

## Como usar o Orchestrator

```bash
python scripts/aegis_orchestrator.py --init      # inicia sessão + alinhamento
python scripts/aegis_orchestrator.py --status    # snapshot
python scripts/aegis_orchestrator.py --lab 01    # prepara lab
```

---

## Propriedade Intelectual

Todo o conteúdo deste pacote é de propriedade de **DcsProducer®**.  
Uso comercial, redistribuição ou white-label requer licença formal.  
Consulte `licensing/modelo-licenciamento-dcsproducer-aegis.md`.

---

## Arquitetura de Alto Nível

Consulte `architecture/dcsproducer-aegis-os-high-level.md` para a visão do **DcsProducer AEGIS OS**.

---

**Gerado sob governança AEGIS · Skill dcsproducer-aegis-hub-core**
