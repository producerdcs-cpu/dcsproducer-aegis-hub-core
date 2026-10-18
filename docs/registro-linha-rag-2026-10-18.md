# Registro de produção — linha RAG

**Data:** 2026-10-18  
**Skill:** `dcsproducer-aegis-hub-core`  
**Diagnóstico:** Core HTTPS no ar. Hub sync ainda aberto (falta sessão do operador).

## Medição

| Alvo | Resultado |
|------|-----------|
| `GET https://dcs-protocol-core.vercel.app/health` | `status: ok`, `version: 0.1.7`, `supabase: true` |
| `POST /protocol/v1/message` sem JWT | `401` fail-closed |
| Hub sync | Aberto. Não é conflito de Git. Exige **Entrar → Sync Core** em `dcsproducer-hub` |

O README do Protocol Core que mostrava `supabase: false` ficou defasado. A Project URL no Vercel passou a ser válida.

## Onde cada repo mora (AEGIS OS)

| Camada | Repo | Papel |
|--------|------|--------|
| L1 AEGIS / núcleo | `dcs-protocol-core` | API, JWT, RLS, sync de projetos |
| L2 MetaRAG | `dcsproducer-hub` + `Job` | Hub de controle e Capstone NEXUS (corpus, MCP, career gap) |
| L2 pipeline | `dcs-rag-starter` | PDF → chunk → embedding → retrieve |
| L4 agente | `dcs-rag-agent` | LangGraph, tools, memória |
| L3 evidência | `tesseract` | Guia do Desenvolvedor. Superfície pública. Não é o Capstone |
| Ancestral | `RAG` | Mesma linha do guia. Permanece privado (PDF-fonte no histórico) |

`tesseract` entra na lista de repositórios novos. Não substitui o gate ativo (NeuroLeitor) nem o Capstone (`Job`).

## Fora deste registro

Elite de Sistemas e ERP não têm repositório. Não foram criados. Só abrem na ordem seguinte, com decisão explícita.

## Skills irmãs no Tesseract

Superfícies, não cópia de código: `pdf-wordpress-editor` (`/ebook`), `dcs-system-design-master` (`/arquitetura`), `dcs-learning-orchestrator` (`/orquestrador`), `career-gap-analyzer` (`/carreira`). O Arauto recupera o corpus do próprio guia.
