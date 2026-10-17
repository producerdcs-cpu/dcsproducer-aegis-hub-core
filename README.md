# DcsProducer® AEGIS Hub Core

![DcsProducer AEGIS Hub Core](docs/aegis-ecosystem-diagram.png)

> **Sistema operacional de produção com GenAI + MetaRAG**  
> Governança AEGIS · 9 Pilares · Labs · Skills  
> **Titular:** DcsProducer®

---

## Visão

O **DcsProducer AEGIS Hub Core** é a camada de governança e orquestração de todo o ecossistema DcsProducer.  
Ele une Hub Core MetaRAG, AEGIS Layer, 9 Pilares de Engenharia de Software, laboratórios práticos e skills irmãs sob uma única diretriz de produção.

```bash
python scripts/aegis_orchestrator.py --init
```

---

## Estrutura do Repositório

```
├── architecture/          ← Arquitetura de alto nível (AEGIS OS)
├── licensing/             ← Modelo de licenciamento
├── skills/
│   ├── dcsproducer-aegis-hub-core/
│   └── six-pillars-engineer/
├── labs/                  ← Labs 01–04 (dentro do ZIP)
├── scripts/               ← aegis_orchestrator.py
├── docs/                  ← PDFs, HTML e diagrama
├── brand/                 ← Guidelines da marca
└── dcsproducer-aegis-export-20261016.zip  ← Pacote completo
```

---

## Componentes Principais

| Camada | Conteúdo |
|--------|----------|
| **AEGIS Layer** | Governança · Proteção · Inteligência |
| **9 Pilares** | DevOps · Microsserviços · Serverless · Containers · Arquitetura Limpa · DDD · Observability · DevSecOps · Event-Driven |
| **Skills** | dcsproducer-aegis-hub-core + six-pillars-engineer (+ irmãs) |
| **Labs** | 01 Observability+RAG · 02 DevSecOps+Agentic · 03 Event-Driven · 04 Clean Arch+Containers |
| **Hub Core** | MetaRAG — https://dcsproducer-hub-pqj9.vercel.app |

---

## Como iniciar

```bash
# 1. Extrair o pacote completo (se necessário)
unzip dcsproducer-aegis-export-20261016.zip

# 2. Inicializar governança AEGIS
python scripts/aegis_orchestrator.py --init

# 3. Ver status de alinhamento
python scripts/aegis_orchestrator.py --status

# 4. Preparar um lab
python scripts/aegis_orchestrator.py --lab 01
```

---

## Propriedade Intelectual

Todo o conteúdo deste repositório é de propriedade de **DcsProducer®**.  
Uso comercial, redistribuição ou white-label requer licença formal.  
Consulte [`licensing/modelo-licenciamento-dcsproducer-aegis.md`](licensing/modelo-licenciamento-dcsproducer-aegis.md).

---

## Documentação

- [Arquitetura de Alto Nível](architecture/dcsproducer-aegis-os-high-level.md)
- [Modelo de Licenciamento](licensing/modelo-licenciamento-dcsproducer-aegis.md)
- [Skill Principal](skills/dcsproducer-aegis-hub-core/SKILL.md)
- [Six Pillars Engineer](skills/six-pillars-engineer/SKILL.md)

---

**DcsProducer® Creative Studio**  
Governança AEGIS · Produção com GenAI + MetaRAG
